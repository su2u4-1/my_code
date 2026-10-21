import json
import random
import time
from dataclasses import dataclass
from typing import Any
import requests
from dotenv import load_dotenv
from os import getenv

load_dotenv()

BONGO_URL = "http://127.0.0.1:7337/mcp"
LM_STUDIO_URL = "http://127.0.0.1:1234/v1/chat/completions"
MODEL = "qwen2.5-0.5b-instruct"
POLL_INTERVAL = 0.2
EVENT_COOLDOWN = 2.0
LM_TIMEOUT = 120
MCP_TIMEOUT = 30
OUTFIT_RESPONSE_CHANCE = 0.1
system_prompt = getenv("PROMPT")


class MCPError(Exception):
    pass


class BongoWaifuMCP:
    def __init__(self, url: str) -> None:
        self.url = url
        self.session = requests.Session()
        self.session_id: str | None = None
        self.request_id = 0

    def _next_id(self) -> int:
        self.request_id += 1
        return self.request_id

    def _headers(self) -> dict[str, str]:
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
        }
        if self.session_id is not None:
            headers["Mcp-Session-Id"] = self.session_id
        return headers

    @staticmethod
    def _parse_response(
        response: requests.Response,
    ) -> dict[str, Any]:
        content_type = response.headers.get("Content-Type", "")
        if "text/event-stream" not in content_type:
            try:
                data = response.json()
            except ValueError as exc:
                raise MCPError(f"MCP 回應不是有效 JSON：\n{response.text}") from exc
            if isinstance(data, dict):
                return data
            raise MCPError(f"MCP 回應格式錯誤：{data!r}")
        data_lines: list[str] = []
        for line in response.text.splitlines():
            if line.startswith("data:"):
                data_lines.append(line[5:].lstrip())
        for raw_data in reversed(data_lines):
            try:
                parsed = json.loads(raw_data)
            except json.JSONDecodeError:
                continue
            if isinstance(parsed, dict):
                return parsed
        raise MCPError(f"MCP SSE 中找不到有效 JSON-RPC：\n{response.text}")

    def _post(
        self,
        method: str,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        request_id = self._next_id()
        payload: dict[str, Any] = {
            "jsonrpc": "2.0",
            "id": request_id,
            "method": method,
        }
        if params is not None:
            payload["params"] = params
        response = self.session.post(
            self.url,
            headers=self._headers(),
            json=payload,
            timeout=MCP_TIMEOUT,
        )
        if response.status_code >= 400:
            raise MCPError(f"MCP HTTP {response.status_code}：{response.text}")
        result = self._parse_response(response)
        if "error" in result:
            raise MCPError(
                "MCP 錯誤："
                + json.dumps(
                    result["error"],
                    ensure_ascii=False,
                )
            )
        return result

    def connect(self) -> None:
        print("[MCP] 正在建立連線...")
        request_id = self._next_id()
        payload = {
            "jsonrpc": "2.0",
            "id": request_id,
            "method": "initialize",
            "params": {
                "protocolVersion": "2025-03-26",
                "capabilities": {},
                "clientInfo": {
                    "name": "BongoWaifu Auto Trigger",
                    "version": "3.0.0",
                },
            },
        }
        response = self.session.post(
            self.url,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json, text/event-stream",
            },
            json=payload,
            timeout=MCP_TIMEOUT,
        )
        response.raise_for_status()
        session_id = response.headers.get("Mcp-Session-Id")
        if not session_id:
            raise MCPError("MCP initialize 成功，但沒有收到 Mcp-Session-Id。")
        self.session_id = session_id
        data = self._parse_response(response)
        if "error" in data:
            raise MCPError(f"initialize 失敗：{data['error']}")
        self._notification("notifications/initialized")
        print("[MCP] 已連線")
        print(f"[MCP] Session ID: {self.session_id}")

    def _notification(self, method: str) -> None:
        payload = {
            "jsonrpc": "2.0",
            "method": method,
        }
        response = self.session.post(
            self.url,
            headers=self._headers(),
            json=payload,
            timeout=MCP_TIMEOUT,
        )
        if response.status_code >= 400:
            raise MCPError(f"MCP notification 失敗：" f"{response.status_code} {response.text}")

    def list_tools(self) -> list[dict[str, Any]]:
        result = self._post("tools/list", {})
        tools = result.get("result", {}).get("tools", [])
        if not isinstance(tools, list):
            raise MCPError("tools/list 回傳格式錯誤。")
        return tools

    def call_tool(
        self,
        name: str,
        arguments: dict[str, Any],
    ) -> Any:
        response = self._post(
            "tools/call",
            {
                "name": name,
                "arguments": arguments,
            },
        )
        return response.get("result")

    def get_game_state(self) -> dict[str, Any]:
        result = self.call_tool(
            "get_game_state",
            {
                "sections": [
                    "character",
                    "achievements",
                    "inventory",
                    "gauges",
                    "stats",
                ],
                "include_locked": True,
            },
        )
        if not isinstance(result, dict):
            raise MCPError(f"get_game_state 回傳格式錯誤：{result!r}")
        return extract_mcp_content(result)


def extract_mcp_content(
    result: dict[str, Any],
) -> dict[str, Any]:
    if any(
        key in result
        for key in (
            "character",
            "achievements",
            "inventory",
            "gauges",
            "stats",
        )
    ):
        return result
    content = result.get("content")
    if isinstance(content, list):
        for item in content:
            if not isinstance(item, dict):
                continue
            if item.get("type") != "text":
                continue
            text = item.get("text")
            if not isinstance(text, str):
                continue
            try:
                parsed = json.loads(text)
            except json.JSONDecodeError:
                continue
            if isinstance(parsed, dict):
                return parsed
    raise MCPError(
        "無法解析 get_game_state："
        + json.dumps(
            result,
            ensure_ascii=False,
        )
    )


@dataclass
class GameEvent:
    event_type: str
    description: str
    key: str


def get_character(
    state: dict[str, Any],
) -> dict[str, Any]:
    character = state.get("character")
    if isinstance(character, dict):
        return character
    return {}


def get_stats(
    state: dict[str, Any],
) -> dict[str, Any]:
    stats = state.get("stats")
    if isinstance(stats, dict):
        return stats
    return {}


def get_inventory(
    state: dict[str, Any],
) -> Any:
    return state.get("inventory")


def get_clothes(
    state: dict[str, Any],
) -> Any:
    return get_character(state).get("current_clothes")


def normalize_inventory(
    inventory: Any,
) -> dict[str, Any]:
    if isinstance(inventory, dict):
        return inventory
    if isinstance(inventory, list):
        return {str(index): item for index, item in enumerate(inventory)}
    return {
        "value": inventory,
    }


def inventory_difference(
    old_inventory: Any,
    new_inventory: Any,
) -> list[Any]:
    old_normalized = normalize_inventory(old_inventory)
    new_normalized = normalize_inventory(new_inventory)
    new_items: list[Any] = []
    for key, value in new_normalized.items():
        if key not in old_normalized:
            new_items.append(value)
            continue
        old_value = old_normalized[key]
        if isinstance(value, dict) and isinstance(old_value, dict):
            if value != old_value:
                new_items.append(value)
        elif value != old_value:
            new_items.append(value)
    return new_items


def detect_events(
    old_state: dict[str, Any],
    new_state: dict[str, Any],
) -> list[GameEvent]:
    events: list[GameEvent] = []
    old_stats = get_stats(old_state)
    new_stats = get_stats(new_state)

    old_orgasm = old_stats.get("orgasm_count")
    new_orgasm = new_stats.get("orgasm_count")
    if isinstance(old_orgasm, (int, float)) and isinstance(new_orgasm, (int, float)) and new_orgasm > old_orgasm:
        count = int(new_orgasm - old_orgasm)
        for _ in range(count):
            events.append(
                GameEvent(
                    event_type="orgasm",
                    description=getenv("DESCRIPTION1", "DESCRIPTION1"),
                    key="orgasm",
                )
            )

    old_inventory = get_inventory(old_state)
    new_inventory = get_inventory(new_state)
    added_items = inventory_difference(
        old_inventory,
        new_inventory,
    )
    for item in added_items:
        item_text = json.dumps(
            item,
            ensure_ascii=False,
        )
        events.append(
            GameEvent(
                event_type="new_clothing",
                description=getenv("DESCRIPTION2", "DESCRIPTION2: {}").format(item_text),
                key=f"new_clothing:{item_text}",
            )
        )

    old_clothes = get_clothes(old_state)
    new_clothes = get_clothes(new_state)
    if old_clothes != new_clothes:
        old_text = json.dumps(
            old_clothes,
            ensure_ascii=False,
        )
        new_text = json.dumps(
            new_clothes,
            ensure_ascii=False,
        )
        events.append(
            GameEvent(
                event_type="outfit_change",
                description=getenv("DESCRIPTION3", "DESCRIPTION3: {} -> {}").format(old_text, new_text),
                key="outfit_change",
            )
        )
    return events


class LMStudio:
    def __init__(
        self,
        url: str,
        model: str,
    ) -> None:
        self.url = url
        self.model = model
        self.session = requests.Session()

    def react(
        self,
        event: GameEvent,
        game_state: dict[str, Any],
    ) -> str | None:
        user_prompt = getenv("USER_PROMPT", "USER_PROMPT: {}, {}").format(event.description, json.dumps(game_state, ensure_ascii=False))
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt.strip(),
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
            "temperature": 0.7,
        }
        response = self.session.post(
            self.url,
            headers={
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=LM_TIMEOUT,
        )
        response.raise_for_status()
        data = response.json()
        choices = data.get(
            "choices",
            [],
        )
        if not choices:
            return None
        message = choices[0].get(
            "message",
            {},
        )
        if not isinstance(message, dict):
            return None
        content = message.get("content")
        if not isinstance(content, str):
            return None
        content = content.strip()
        if not content:
            return None
        return content


class AutoTrigger:
    def __init__(self) -> None:
        self.mcp = BongoWaifuMCP(BONGO_URL)
        self.llm = LMStudio(
            LM_STUDIO_URL,
            MODEL,
        )
        self.last_state: dict[str, Any] | None = None
        self.last_event_time: dict[str, float] = {}

    def connect(self) -> None:
        while True:
            try:
                self.mcp = BongoWaifuMCP(BONGO_URL)
                self.mcp.connect()
                tools = self.mcp.list_tools()
                print("[MCP] 可用工具：")
                for tool in tools:
                    if not isinstance(tool, dict):
                        continue
                    name = tool.get("name")
                    if name:
                        print(f"  - {name}")
                return
            except Exception as exc:
                print(f"[MCP] 連線失敗：{exc}")
                print("[MCP] 3 秒後重新連線...")
                time.sleep(3)

    def should_trigger(
        self,
        event: GameEvent,
    ) -> bool:
        now = time.monotonic()
        previous = self.last_event_time.get(event.key)
        if previous is not None and now - previous < EVENT_COOLDOWN:
            return False
        self.last_event_time[event.key] = now
        return True

    def should_respond_to_event(
        self,
        event: GameEvent,
    ) -> bool:
        if event.event_type == "outfit_change":
            result = random.random() < OUTFIT_RESPONSE_CHANCE
            if not result:
                print("[事件] 換裝，但這次不回應。")
            return result
        return True

    def say(
        self,
        text: str,
        duration: float = 5,
    ) -> None:
        text = text.strip()
        if not text:
            return
        duration = max(
            2,
            min(
                30,
                duration,
            ),
        )
        print(f"[BongoWaifu] {text}")
        self.mcp.call_tool(
            "say",
            {
                "text": text,
                "duration_seconds": duration,
            },
        )

    def handle_event(
        self,
        event: GameEvent,
        state: dict[str, Any],
    ) -> None:
        if not self.should_respond_to_event(event):
            return
        if not self.should_trigger(event):
            return
        print()
        print("=" * 60)
        print(f"[事件] {event.event_type}")
        print(f"[事件] {event.description}")
        print("[AI] 正在產生回應...")
        try:
            text = self.llm.react(
                event,
                state,
            )
        except requests.RequestException as exc:
            print(f"[LM Studio] API 請求失敗：{exc}")
            print("=" * 60)
            return
        except Exception as exc:
            print(f"[LM Studio] 發生錯誤：{exc}")
            print("=" * 60)
            return
        if not text:
            print("[錯誤] LM Studio 沒有產生文字。")
            print("=" * 60)
            return
        print(f"[AI] {text}")
        try:
            self.say(text)
        except Exception as exc:
            print(f"[MCP] say 執行失敗：{exc}")
        print("=" * 60)

    def run(self) -> None:
        self.connect()
        print(getenv("LOG", "LOG: {}, {}, {}, {}").format(BONGO_URL, LM_STUDIO_URL, MODEL, POLL_INTERVAL))
        while True:
            try:
                print("[遊戲] 取得初始狀態...")
                self.last_state = self.mcp.get_game_state()
                print("[遊戲] 初始狀態取得成功。")
                break
            except Exception as exc:
                print(f"[遊戲] 取得狀態失敗：{exc}")
                time.sleep(2)
        print()
        print("[監聽] 開始監聽遊戲事件...")
        print()
        while True:
            try:
                time.sleep(POLL_INTERVAL)
                state = self.mcp.get_game_state()
                if self.last_state is None:
                    self.last_state = state
                    continue
                events = detect_events(
                    self.last_state,
                    state,
                )
                self.last_state = state
                for event in events:
                    self.handle_event(
                        event,
                        state,
                    )
            except KeyboardInterrupt:
                print()
                print("[程式] 已停止。")
                break
            except MCPError as exc:
                print(f"[MCP] 發生錯誤：{exc}")
                print("[MCP] 嘗試重新建立連線...")
                time.sleep(1)
                try:
                    self.connect()
                    self.last_state = self.mcp.get_game_state()
                except Exception as reconnect_exc:
                    print("[MCP] 重新連線失敗：" f"{reconnect_exc}")
                    time.sleep(3)
            except requests.RequestException as exc:
                print(f"[網路] 發生錯誤：{exc}")
                time.sleep(2)
            except Exception as exc:
                print(f"[錯誤] {type(exc).__name__}: " f"{exc}")
                time.sleep(1)


def main() -> None:
    trigger = AutoTrigger()
    trigger.run()


if __name__ == "__main__":
    main()
