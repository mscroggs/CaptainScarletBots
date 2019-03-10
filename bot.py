from __future__ import print_function
import random
import praw

options = [
           ("CAPTAINBLACK","This is Captain Black, relaying instructions from the Mysterons on Mars. You know what you must do."),
           ("MYSTERONS","This is the voice of the Mysterons. We know you can hear us, Earthmen. We will be avenged."),
           ("NARRATOR","The Mysterons, sworn enemies of Earth, possessing the ability to recreate an exact likeness of an object or person... but first they must destroy.\n\n"
                       "[cat howls, gun fires]\n\n"
                       "Leading the fight, one man fate has made indestructible. His name... {{USER}}.")
          ]

user, comment = random.choice(options)

r = praw.Reddit(user,user_agent="CaptainScarletBots")

subreddit = r.subreddit("CaptainScarletMemes")

for i in subreddit.new():
    if len(i.comments.list()) == 0:
        comment = comment.replace("{{USER}}","/u/"+i.author.name)
        print(r.user.me(), comment)
        i.reply(comment)
        break
