import random
import math
import numpy as np


from discord.ext.commands import Bot

BOT_PREFIX = ("?","!")
TOKEN = "XXXXXXXXXXXX"

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='random',
                description = "Gives random linear algebra theorem",
                aliases = ['rando'],
                pass_context = True)
async def theorem_list(context):
    possible_responses = [
        'A',
        'b',
        'c',
        'd',
        'e',
        'g'
    ]
    await client.say(context.message.author.mention + ", did you know that..   " + random.choice(possible_responses))

@client.command(name = 'det',
                description = "Calculates the determinant of a square matrice. Matrice is to be provided as a list with each entry seperated by a ',' eg. '1,2,3,4' "
                )
async def find_determinant(m1):
    mat1 = str(m1)
    x = mat1.split(",")
    x = [int(i) for i in x]
    sq = len(x)
    root = math.sqrt(sq)
    if ((root - math.floor(root)) != 0):
        await client.say("Must enter a square matrix")

    elif((root - math.floor(root)) == 0):
        mat1 = [x[u:u+root] for u in range(0, len(x), root)]
        det = np.linalg.det(mat1)
        result = round(det,9)
        await client.say("det is = to " + str(result))





client.run(TOKEN)
