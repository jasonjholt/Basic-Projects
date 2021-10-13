"""
takes name and a question from the user
returns a random card from the major arcana
fortune changes if the card is rightside up or upside down
"""


import random

name = input("What is your name? ")
question = input(f"Good day, {name}. What do you wish to ask the cards? ")
print("Let's see what they say.")


cards = {
    1:"The Fool",
    2:"The Magician",
    3:"The High Priestess",
    4:"The Empress",
    5:"The Emperor",
    6:"The Hierophant",
    7:"The Lovers",
    8:"The Chariot",
    9:"Strength",
    10:"The Hermit",
    11:"The Wheel of Fortune",
    12:"Justice",
    13:"The Hanged Man",
    14:"Death",
    15:"Temperance",
    16:"The Devil",
    17:"The Tower",
    18:"The Star",
    19:"The Moon",
    20:"The Sun",
    21:"Judgement",
    22:"The World",
    }



cards_up = {
    1:"You face new beginnings. Keep a fresh spirit and a spontaneous innocence always.",
    2:"Take inspired action. Stay resourceful.",
    3:"There is a great, divine knowledge within you. Follow your intuition.",
    4:"You are nurturing, and in your beauty, there lies abundance in your future. Take care.",
    5:"You are an authority, your power established. Take control.",
    6:"Your morals are strict, and uphold tradition and conformity.",
    7:"Your future is full of love, harmony, but full of polarising choices also. Choose love.",
    8:"You have great willpower and determination. Focus and move ahead.",
    9:"You have great strength, but that strength is found also in compassion and leadership. Be brave.",
    10:"You are in a period of introspection, of soul-searching. Take your time.",
    11:"You have reached a turning point in your life. Roll with the changes.",
    12:"Justice, fairness, and the truth are of great importance to you. Keep it that way.",
    13:"You may need to pause and think over your life and what you need to let go of.",
    14:"It is a time when the old die and a new life is found. Embrace change.",
    15:"You value peace, and search for a purpose in all you do.",
    16:"You feel as though you are restricted by your own hidden feelings. Confront your fears.",
    17:"Your life is in upheaval, and large changes are on the horizon.",
    18:"Your future holds hope and renewal.",
    19:"Your subconscious holds an illusion of fear over you.",
    20:"Your future will be filled with celebration and warmth.",
    21:"You are going to find your inner calling, and feel reborn.",
    22:"You are on a journey which is on the verge of being completed."
    }

cards_down = {
    1:"You are holding back, and fear the risk that you have to take.",
    2:"There is untapped talent in you that you have been forced to hide.",
    3:"You are ignoring your intuition and keeping secrets. Trust your instincts.",
    4:"You find that your creativity is lacking, or that you depend too much on others.",
    5:"You are far too controlling and dominating, and need to learn flexibility.",
    6:"Your beliefs do not line up with the majority. Explore them, and challenge the status quo.",
    7:"Your life is out of balance, and your values may feel like they are not your own.",
    8:"You lack self-discipline, and feel as though you are lacking direction.",
    9:"There is a strength within you, but you doubt it and don't have the energy to use it.",
    10:"You are in a period of isolation and withdrawal.",
    11:"You may be in a bit of bad luck, resulting from your unwillingness to change.",
    12:"You may have been dishonest, or failed to take accountability for a mistake. Do the right thing.",
    13:"You are resisting change and delaying the inevitable.",
    14:"You will not find change in your life until you have changed yourself. Heal.",
    15:"You may have found excess or deficiency in yourself, and must heal and re-align yourself.",
    16:"Your beliefs limit you. Detach from them, and explore your darker thoughts.",
    17:"You have escaped a disaster, and now may have changed due to it.",
    18:"You are despairing and feel disconnected from the world. Trust yourself.",
    19:"There is fear, confusion, and repressed imotion in you. Let it out.",
    20:"You may be feeling down and overcompensating for it by being too optimistic.",
    21:"You have a calling that you doubt you can reach. You are too critical of yourself.",
    22:"You seek closure, but are rushing to get there. Slow down, and complete the cycle."
    }

orientation = random.randint(1,2)
draw = random.randint(1,22)
card = cards.get(draw)

if orientation == 1:
    face = "right side up"
    fortune = cards_up.get(draw)
elif orientation == 2:
    face = "upside down"
    fortune = cards_down.get(draw)
    
print(f"Your card is {card}. It is {face}.")
print(fortune)
