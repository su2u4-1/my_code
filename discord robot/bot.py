import math, os, random, discord, modules, time
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
player = {}
equip = []
bag = {}

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(">>bot is online<<")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    nt = time.localtime(time.time())
    uid = message.author.id
    m = message.content
    m2 = m.split()
    print(
        f"{nt.tm_year}-{nt.tm_mon}-{nt.tm_mday} {nt.tm_hour}:{nt.tm_min}:{nt.tm_sec} id:",
        uid,
        m,
        m2,
        end=" -> ",
    )
    if uid not in player:
        player[uid] = modules.CreateAccount(uid)
    if uid not in bag:
        modules.bag(uid)


client = commands.Bot(command_prefix="/", intents=intents)


@client.command()
async def Hi(ctx):
    uid = ctx.author.id
    await ctx.send(f"<@{uid}> Hi!")


@client.command()
async def Hello(ctx):
    uid = ctx.author.id
    await ctx.send(f"<@{uid}> Hello!")


@client.command()
async def 抽籤(ctx):
    uid = ctx.author.id
    a = ["大吉", "小吉", "吉", "凶", "小凶", "大凶"]
    c = 0
    for _ in range(10):
        c += random.randint(0, 5)
    await ctx.send(f"<@{uid}>抽到{a[round(c/10)]}")


@client.command()
async def 占卜(ctx, *m2):
    uid = ctx.author.id
    if len(m2) == 1:
        t = modules.divination()
    else:
        t = modules.divination(m2[1])
    await ctx.send(f"<@{uid}>{t}")


@client.command()
async def 賭(ctx, *m2):
    uid = ctx.author.id
    if len(m2) == 1:
        pass  # /help 賭
    elif len(m2) == 2:
        try:
            m2[1] = int(m2[1])
        except:
            await ctx.send(f"<@{uid}>輸入錯誤")
        if player[uid].m >= m2[1] and player[uid].m >= 0:
            player[uid].m -= m2[1]
            if random.randint(1, 10) <= 4:
                await ctx.send(f"<@{uid}>花掉{m2[1]}塊錢，結果血本無歸")
            else:
                b = round(random.uniform(0, 2) * m2[1])
                player[uid].m += b
                await ctx.send(f"<@{uid}>花掉{m2[1]}塊錢，最後贏得{b}塊錢")
        else:
            await ctx.send(f"<@{uid}>錢不夠了")


@client.command()
async def 升級(ctx, *m2):
    uid = ctx.author.id
    if len(m2) == 1:
        await ctx.send(
            f"<@{uid}>目前屬性為:\n攻擊:{player[uid].at}\n防禦:{player[uid].de}\n速度:{player[uid].ag}\n血量:{player[uid].hp}\n剩餘點數:{player[uid].po}"
        )
    elif len(m2) == 2:
        pass  # help 升級
    elif len(m2) == 3:
        try:
            add = int(m2[2])
        except:
            await ctx.send(f"<@{uid}>輸入錯誤")
        if player[uid].po >= add:
            if m2[1] == "1" or m2[1] == "攻擊" or m2[1] == "att":
                a = random.randint(1, 2)
                await ctx.send(
                    f"<@{uid}>\n攻擊:{player[uid].at} -> {player[uid].at+add*a}\n升級點:{player[uid].po} -> {player[uid].po-add}"
                )
                player[uid].at += add * a
            elif m2[1] == "2" or m2[1] == "防禦" or m2[1] == "def":
                await ctx.send(f"<@{uid}>\n防禦:{player[uid].de} -> {player[uid].de+add}\n升級點:{player[uid].po} -> {player[uid].po-add}")
                player[uid].de += add
            elif m2[1] == "3" or m2[1] == "速度" or m2[1] == "agi":
                await ctx.send(f"<@{uid}>\n速度:{player[uid].ag} -> {player[uid].ag+add}\n升級點:{player[uid].po} -> {player[uid].po-add}")
                player[uid].ag += add
            elif m2[1] == "4" or m2[1] == "血量" or m2[1] == "Hp" or m2[1] == "hp":
                a = random.randint(5, 20)
                await ctx.send(
                    f"<@{uid}>\n血量:{player[uid].hp} -> {player[uid].hp+add*a}\n升級點:{player[uid].po} -> {player[uid].po-add}"
                )
                player[uid].hp += add * a
            player[uid].po -= add
        else:
            await ctx.send(f"<@{uid}>輸入錯誤")


@client.command()
async def 冒險(ctx, *m2):
    uid = ctx.author.id
    if len(m2) == 1:
        await ctx.send(f"<@{uid}>目前在({player[uid].x},{player[uid].y})")
        # /help 冒險
    elif len(m2) >= 2:
        event_list = [
            ["殭屍", "骷髏", "蜘蛛", "巨人"],
            ["災難0", "災難1", "災難2", "災難3"],
            ["好事0", "好事1", "好事2", "好事3"],
            ["空曠的草原", "空曠的丘陵", "空曠的山地", "空曠的荒野", "空曠的沙漠", "空曠的森林"],
        ]
        drop = ["金", "水", "木", "火", "土"]
        if m2[1] == "n" or m2[1] == "北":
            player[uid].y -= 1
        elif m2[1] == "s" or m2[1] == "南":
            player[uid].y += 1
        elif m2[1] == "w" or m2[1] == "西":
            player[uid].x -= 1
        elif m2[1] == "e" or m2[1] == "東":
            player[uid].x += 1
        if m2[1] == "e" or m2[1] == "東" or m2[1] == "w" or m2[1] == "西" or m2[1] == "s" or m2[1] == "南" or m2[1] == "n" or m2[1] == "北":
            e = random.choices(event_list, weights=[4, 2, 1, 1])[0]
            event = e[random.randint(0, len(e) - 1)]
            await ctx.send(f"<@{uid}>目前在({player[uid].x},{player[uid].x})，遇到{event}")
            if e == event_list[0]:
                r = random.choices([0, 1, 2], [90, 9, 1])[0]
                if player[uid].lv <= 3:
                    monster = modules.SummonMods(random.randint(1, player[uid].lv + 2), event, r)
                else:
                    monster = modules.SummonMods(random.randint(player[uid].lv - 2, player[uid].lv + 2), event, r)
                if r == 0:
                    s = random.choices(["初", "中", "高"], [9, 1, 0])[0]
                    u = random.choices(["碎片", "結晶", "精華"], [1, 0, 0])[0]
                elif r == 1:
                    s = random.choices(["初", "中", "高"], [1, 8, 1])[0]
                    u = random.choices(["碎片", "結晶", "精華"], [9, 1, 0])[0]
                elif r == 2:
                    s = random.choices(["初", "中", "高"], [0, 1, 9])[0]
                    u = random.choices(["碎片", "結晶", "精華"], [80, 15, 5])[0]
                pl = [player[uid].at, player[uid].de, player[uid].ag, player[uid].hp]
                message_a = modules.fighting(monster, pl, monster[4], player[uid].ar)
                if message_a[-1] == f"你打贏了{monster[4]}":
                    drop_equip = []
                    drop_item = []
                    eq = modules.EquipGenerate(
                        monster[5],
                        random.choices([1, 2, 3, 4, 5, 6, 7], [900000, 90000, 9000, 900, 90, 9, 1])[0],
                        1,
                        1,
                        1,
                    )
                    drop_equip.append(eq)
                    equip.append(eq)
                    for _ in range(random.randint(1, 5)):
                        drop_item.append(f"{s}級{drop[monster[7]]}屬性能量{u}")
                    await ctx.send(f"<@{uid}>")
                    for i in message_a:
                        await ctx.send(i)
                    for i in drop_equip:
                        await ctx.send(f"<@{uid}>你得到了{i.name}")
                        bag[uid].add_equip(i.name, i.id)
                    for i in drop_item:
                        if u == "碎片":
                            u = 1
                        elif u == "結晶":
                            u = 2
                        elif u == "精華":
                            u = 4
                        quantity = random.randint(0, math.ceil(monster[5] / u))
                        await ctx.send(f"<@{uid}>你得到了{quantity}個{i}")
                        bag[uid].add_item(i, quantity)
                    await ctx.send(f"<@{uid}>你得到了{monster[8]}exp\nexp:{player[uid].exp} -> {player[uid].exp+monster[8]}")
                    player[uid].exp += monster[8]
                elif message_a[-1] == f"{monster[4]}打敗你了":
                    await ctx.send(f"<@{uid}>")
                    for i in message_a:
                        await ctx.send(i)
                    await ctx.send(f"<@{uid}>你失去了{monster[8]}exp\nexp:{player[uid].exp} -> {player[uid].exp-monster[8]}")
                    player[uid].exp -= monster[8]
            if e == event_list[1]:
                pass


@client.command()
async def 背包(ctx, *m2):
    uid = ctx.author.id
    f = "物品:"
    for i in bag[uid].item:
        f += f"\n{bag[uid].item[i]}個{i}"
    f += "裝備"
    for i in bag[uid].equip:
        f += str(i)
    await ctx.send(f"<@{uid}>的背包" + f)


@client.command()
async def 刪除(ctx, *m2):
    uid = ctx.author.id
    if len(m2) >= 2:
        try:
            d = int(m2[1])
            await ctx.purge(limit=d)
        except ValueError:
            await ctx.send(f"<@{uid}>輸入錯誤數值")
        except AttributeError:
            await ctx.send(f"<@{uid}>無法刪除訊息，可能是因為權限不足")
    elif len(m2) == 1:
        try:
            await ctx.purge()
        except AttributeError:
            await ctx.send(f"<@{uid}>無法刪除訊息，可能是因為權限不足")


@client.command()
async def exit(ctx):
    uid = ctx.author.id
    if uid == 718652947671810078:
        print(">>bot is offline<<")
        await ctx.send("bot is offline")
        exit()


client.run(os.getenv("TOKEN"))
