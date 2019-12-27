import praw

# common image extensions
image_extensions = ('.png', '.jpeg', '.jpg', 'gif')

# 'link_check_bot' is taken from praw.ini
reddit = praw.Reddit('link_check_bot')

# looking at this particular subreddit just for testing purposes
subreddit = reddit.subreddit('danielguo')

# check all recent and incoming submissions for link
for submission in subreddit.stream.submissions():
    #if this if statement is triggered, then submission is either a link or an image
    if(not submission.is_self):
        content = submission.url
        #if this is statement is triggered, then submission is not an image and we want to check its safety
        if(not content.endswith(image_extensions)):
            print(content)

