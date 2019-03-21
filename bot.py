from __future__ import print_function
import random
import praw

options = [
           ("CAPTAINBLACK",["This is Captain Black, relaying instructions from the Mysterons on Mars. You know what you must do."]),
           ("MYSTERONS",["This is the voice of the Mysterons. We know you can hear us, Earthmen. We will be avenged.",
                         "This is the voice of the Mysterons. Hear us Earthmen and take heed. You started this war of nerves with your unprovoked attack on our complex..."]),
           ("NARRATOR",["The Mysterons, sworn enemies of Earth, possessing the ability to recreate an exact likeness of an object or person... but first they must destroy.\n\n"
                       "[cat howls, gun fires]\n\n"
                       "Leading the fight, one man fate has made indestructible. His name... {{USER}}."]),
           ("NARRATOR",["{{USER}} ({{USER}}). "
                        "He's the one who knows the Mysteron Game, "
                        "and things that they plan.",
                        "{{USER}} ({{USER}}). "
                        "To his Martian foes a dangerous name, "
                        "a superman.",
                        "They crash {{USER}}, and his body may burn. "
                        "They smash {{USER}}, but they know he'll return, "
                        "to live again.",
                        "{{USER}} ({{USER}}). "
                        "As the Angels are flying wing to wing, "
                        "into the scene, Spectrum Is Green.",
                        "{{USER}} ({{USER}}). "
                        "Though the Mysteron's plan to conquer the earth, "
                        "this indestructible man will show what he's worth."]),
           ("GREEN",["Angels one, two and three. Immediate launch."]),
           ("WHITE",["This is an operational base, not a rest centre!",
                     "What's the meaning of this, {{USER}}? Bursting in here and making demands?",
                     "Captain Scarlet is indestructible. You are not. Remember this. Do not try to imitate him."]),
           ("POLICEMAN",["Some job that driver's got, shipping atomic bombs around.",
                         "It's not a bomb, it's a nuclear device, for civil use.",
                         "What's the difference? It would still make a mess of the city if anything went wrong.",
                         "Oh, relax! What can go wrong?"]),
           ("MAGENTA",["Captain Blue, Captain Scarlet. Is anything wrong?",
                       "Don't worry about that.",
                       "No, sir. Nothing has come within a hundred miles of this base since the Red Alert, except {{USER}} of course."]),
           ("MACEY",["Thirteen... THIRTEEN!?!",
                     "I can't hold it, I just can't hold it! It's out of my control! It's out of my control!"]),
           ("PS2",["Yet again your skills are very impressive. Well done {{USER}}.",
                   "Time and time again you have proven yourself to be the greatest asset Spectrum has against the Mysteron threat. You are truly a hero of our times {{USER}}. I owe you my life.\n\nNow take a well earned rest!",
                   "You are a credit to Spectrum and the world. I owe you my gratitute.\n\nWell done."])
          ]

user, comments = random.choice(options)
comment = random.choice(comments)

r = praw.Reddit(user,user_agent="CaptainScarletBots")

subreddit = r.subreddit("CaptainScarletMemes")

for i in subreddit.new(limit=20):
    if len(i.comments.list()) == 0:
        comment = comment.replace("{{USER}}","/u/"+i.author.name)
        print(r.user.me(), comment)
        i.reply(comment)
        break
