# Reddit Link_Check_Bot

Checks link posts and comments whether or not that link exists. For example, it would reply to the post with link "thisisafakelink.com" with "I have checked the url "thisisafakelink.com", and it DOES NOT exist."

A user can easily modify this bot to automate deleting the post instead of commenting by editing the the submission.reply(message) line.

To config for your own reddit account, add the praw.ini file to the same directory. This file is formatted according to the praw docs.