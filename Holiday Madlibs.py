""" story taken from  https://dorkdiaries.com/2011/11/holiday-mad-libs/ """

# madlibs: 1


verbing = input("Verb with -ing: ")
place = input("Place: ")
song = input("A holiday song: ")
adj1 = input("Adjective: ")
adj2 = input("Another adjective: ")
friend = input("A friend: ")
past1 = input("Verb with -ed: ")
past2 = input("Another verb with -ed: ")
time = input("Amount of time: ")
verb = input("A verb: ")
plural = input("A plural noun: ")
rel1 = input("A relative: ")
num = input("A number: ")
food = input("Food item: ")
rel2 = input("Another relative: ")
past3 = input("Another verb with -ed: ")
noun = input("A noun:")
sing = input("A singer: ")
adj3 = input("Another adjective: ")
hum = input("A person: ")
mfood = input("A messy food: ")
cloth = input("A piece of clothing: ")
time2 =input("Amount of time: ")
hfood = input("A holiday food: ")

madlib = (f"I was {verbing} at the {place} the other day when I heard {song} come on the radio. \
I was feeling really {adj1} and I'm pretty sure I looked super {adj2} because {friend} \
walked in and almost {past1}. Seriously, she {past2} for close to {time}! \n \
This time every year I {verb} all the time because I get really excited \
thinking about holiday {plural}! That's why I was {verbing} at {place}: \
I was really hoping {rel1} would come by and give me at least {num} pieces \
of holiday {food}! \n \
 \
That didn't happen, but suddenly {rel2} {past3} by in a huge {noun} on wheels \
dressed up as {sing}. I know {adj2} things happen around the holidays, \
but this didn't make any sense! I picked up the phone to call {hum} but the \
phone turned into a big pile of {mfood} and dripped all the way \
down my {cloth}! \n \
 \
Then my alarm went off for about {time2}. It was all a dream! \
I had a ton of {hfood} before I went to sleep. Maybe that's what gave me \
the crazy dream!") 
           

print(madlib)
