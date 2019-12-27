import praw
from urllib.request import urlopen

# common image extensions
image_extensions = ('.png', '.jpeg', '.jpg', 'gif')

# returns true if url exists
def url_exists(url):
    return urlopen(url).code < 400

def main():
    # 'link_check_bot' is taken from praw.ini
    reddit = praw.Reddit('link_check_bot')

    # looking at this particular subreddit just for testing purposes
    subreddit = reddit.subreddit('danielguo')

    # check all recent and incoming submissions for link
    for submission in subreddit.stream.submissions():
        #if this if statement is triggered, then submission is either a link or an image
        if(not submission.is_self):
            url = submission.url
            #if this is statement is triggered, then submission is not an image and we want to check it
            if(not url.endswith(image_extensions)):
                if(url_exists(url)):
                    message = f"I have checked the url {url}, and it DOES exist."
                else:
                    message = f"I have checked the url {url}, and it DOES NOT exist."
                submission.reply(message)

if(__name__ == "__main__"):
    main()