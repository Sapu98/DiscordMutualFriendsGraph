import sys

sys.path.insert(0, 'discord.py-self')
sys.path.insert(0, 'discord.py-self_embed')

from discord.ext import commands
import json
import time
import random

from pyvis.network import Network

with open('config.json', 'r') as file:
    config = json.load(file)

TOKEN = config['token']
PREFIX = config['prefix']

bot = commands.Bot(command_prefix=PREFIX, self_bot=True)

clientFriendNames = []
userServer = {}
vertices = []
edges = []


@bot.event
async def on_ready():
    net = Network()
    guilds = list(bot.guilds)
    print(guilds)
    j = 0
    for guild in guilds:
        j = j + 1
        if guild.name != "a𝗞𝗶𝘄𝗶𝗶 🥝":
            i = 0
            for user in guild.members:
                try:
                    time.sleep(1)
                    mutual_friends = (await user.profile()).mutual_friends
                    # not adding the bot to the vertices
                    if user.name == bot.user.name:
                        for mutual_friend in mutual_friends:
                            clientFriendNames.append(mutual_friend.name)
                    else:
                        rand = random.randint(0, 5)
                        time.sleep(1.2 + rand / 10)
                        i = i + 1
                        print(
                            f'**************({i}/{len(guild.members)}) {user.name} - {guild} {j}/{len(guilds)}) **************')
                        for mutual_friend in mutual_friends:
                            if user.name not in vertices:
                                vertices.append(user)
                                userServer[user.name] = guild.name
                            if mutual_friend not in vertices:
                                vertices.append(mutual_friend)
                                userServer[mutual_friend.name] = guild.name
                            if [user, mutual_friend] not in edges and [mutual_friends, user] not in edges:
                                edges.append([user, mutual_friend])
                        print(f"x{len(mutual_friends)} mutuals")
                except Exception as inst:
                    print(f"Error: {user.name} has blocked you! {inst}")
                    net.add_node(user.name, label=user.name, size=10, title="This user has blocked you!", color="red")

    print(f"Analysis finished...")

    for vertex in vertices:
        if vertex.name in clientFriendNames:
            net.add_node(vertex.name, label=vertex.name, size=10, title="")
        else:
            net.add_node(vertex.name, label=vertex.name, size=10, title="", color="green")

    for edge in edges:
        net.add_edge(edge[0].name, edge[1].name)

    neighbor_map = net.get_adj_list()

    for node in net.nodes:
        try:
            node["size"] += len(neighbor_map[node["id"]]) / 2
            node["title"] += userServer[node["id"]]
        except Exception as inst:
            print(inst)

    net.save_graph('graph.html')
    exit(0)


bot.run(TOKEN)
