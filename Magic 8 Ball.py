import random

# ask the user to give a question
question = input("What do you wish to know? ")

# randomise response: good, meh, or bad?
cat = random.randint(1,3)

# dictionaries for responses; identical keys per category
green = {
    1:"It is certain",
    2:"It is decidedly so",
    3:"Without a doubt",
    4:"Yes, you may rely on it",
    5:"Outlook good"
    }
yellow = {
    1:"Reply hazy, try again",
    2:"Ask again later",
    3:"Better not tell you now",
    4:"Cannot predict now",
    5:"Concentrate and ask again"
    }
red = {
    1:"Don't count on it",
    2:"My reply is no",
    3:"My sources say no",
    4:"Outlook not so good",
    5:"Very doubtful"
    }

if cat == 1:
    roll = random.randint(1,5)
    fortune = green.get(roll)
elif cat == 2:
    roll = random.randint(1,5)
    fortune = yellow.get(roll)
elif cat == 3:
    roll = random.randint(1,5)
    fortune = red.get(roll)

    # print results
print(f"You have asked me: {question}")
print(f"I say: {fortune}")
