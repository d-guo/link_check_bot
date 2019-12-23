import praw

# 'link_check_bot' is taken from praw.ini
reddit = praw.Reddit('link_check_bot')

# looking at this particular subreddit just for testing purposes
subreddit = reddit.subreddit('cubing')

print(subreddit.description)
