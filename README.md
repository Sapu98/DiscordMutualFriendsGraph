# DiscordMutualFriendsGraph
Creates a self bot for Discord to create a graph of all your friends and mutual freinds in all the servers you are in.

## How to use
1) Put your discord token in config.json
2) Run the main.py and pip install all the dependencies it asks. 
When it asks for the discord library, do not pip install it (unless the 2.0.1 got realeased by the time).
You will have to install manually the latest version from sources https://github.com/dolfies/discord.py-self
3) Open graph.html
4) Profit

The process may take hours as requesting dicord api too fast will temp ban you. (edit the sleep function at your own risk, it's safe atm, tested on 10000+ requests for about 6 hours working continuously)

## Example output
https://ldflabs.com/graph.html

![raw (1)](https://github.com/Sapu98/DiscordMutualFriendsGraph/assets/13931972/88009b4c-036c-436a-a93d-c761d7eedb57)

Blue nodes are you friends

Green nodes are people that have atleat one of your friends as their friend
