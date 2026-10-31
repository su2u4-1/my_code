from pathlib import Path
from typing import Optional

ROOT_PATH: str = "D:/compiler/test/test_pp"
OUTPUT_PATH: Optional[str] = "D:/compiler/test/test_pp.md"


def iter_files(root: Path, exclude: set[Path]) -> list[Path]:
    """遞迴收集 root 底下所有檔案（排除指定檔案），依相對路徑排序。"""
    files: list[Path] = []
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if p.resolve() in exclude:
            continue
        files.append(p)
    files.sort(key=lambda p: p.relative_to(root).as_posix())
    return files


def build_markdown(root: Path, files: list[Path]) -> str:
    """把所有檔案依照指定的 markdown 格式串接起來。"""
    blocks: list[str] = []
    for file in files:
        rel: str = file.relative_to(root).as_posix()
        display: str = f"./{rel}"
        ext: str = file.suffix.lstrip(".").lower()

        try:
            content: str = file.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            content = f"<error reading file: {exc}>"

        blocks.append(f"{display}:\n```{ext}\n{content}\n```\n")

    return "\n".join(blocks)


def main() -> int:
    root: Path = Path(ROOT_PATH)
    if not root.is_dir():
        print(f"error: {root} 不是資料夾")
        return 1

    excludes: set[Path] = set()
    output: Optional[Path] = Path(OUTPUT_PATH) if OUTPUT_PATH is not None else None
    if output is not None:
        excludes.add(output.resolve())

    files: list[Path] = iter_files(root, excludes)
    markdown: str = build_markdown(root, files)

    if output is None:
        print(markdown)
    else:
        output.write_text(markdown, encoding="utf-8")
        print(f"已寫入 {output}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
