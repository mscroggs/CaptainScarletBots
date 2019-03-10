from __future__ import print_function
import random
import praw

r = praw.Reddit('CAPTAINBLACK',user_agent="CAPTAINBLACK")

subreddit = r.subreddit("CaptainScarletMemes")
print(subreddit.display_name)

print(r.user.me())


