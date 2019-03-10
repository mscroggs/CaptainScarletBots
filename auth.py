# To authorise a new bot
from __future__ import print_function
import random
import praw


# 1. Add user to the CaptainScarletBots app and change the first input below
r = praw.Reddit(input("Who do you want to authorise? "),user_agent="CaptainScarletBots")

# 2. Run this and visit url. You may need to remove +s from url
state = str(random.randint(0, 65000))
scope = "account creddits edit flair history identity livemanage modconfig modcontributors modflair modlog modothers modposts modself modwiki mysubreddits privatemessages read report save submit subscribe vote wikiedit wikiread"
url = r.auth.url(scope, state, 'permanent')
url = url.replace("+".join(i for i in scope.replace(" ","+")),
                  scope.replace(" ","+")
                 )
print("Go to this URL to get token")
print(url)

# 3. Run this with code taken from teh result of step 2.
code = r.auth.authorize(code=input("Paste the token here: "))

# 4. Save the output in praw.ini as refresh_token
print(code)
