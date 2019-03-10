# To authorise a new bot
from __future__ import print_function
import random
import praw

# 1. Add user to the CaptainScarletBots app and change the first input below
r = praw.Reddit('CAPTAINBLACK',user_agent="CaptainScarletBots")

# 2. Run this and visit url. You may need to remove +s from url
state = str(random.randint(0, 65000))
url = r.auth.url("identity submit edit", state, 'permanent')
print(url)

# 3. Run this with code taken from teh result of step 2.
r.auth.authorize(code="???")

# 4. Save the output in praw.ini as refresh_token
