import praw 
username = "dog posting test"
password = "Arthur@1905"
client_id = "zhyQC5zYNlwyuB-Nd5cMuw"
client_secret = "8gQa6Jn3QIX9B3T2UEQBFsEVN3MFzA"

reddit_instance=praw.Reddit(
    username = username,
    password = password,
    client_id = client_id,
    client_secret = client_secret,
    user_agent = "test_bot"
)
# Getting the top 25 comments in the subreddit cats
print(reddit_instance.user.me())
subreddit = reddit_instance.subreddit("dog")
top_25_submissions = subreddit.hot(limit=25, time_filter = "week")
for submission in top_25_submissions:
    print(submission.title)
# Testing the bot in the testinggrounf4bots subreddit
subreddit = reddit_instance.subreddit("testingground4bots")
subreddit.submit(title="This is my test post from my bot", selftest="Hello how are you doing?")
# Replying to the comments in reddit using bot
submission = reddit_instance.submission("1kwo79")
comments = submission.comments

for comment in comments:
    if "dog" in comment.body:
        comment.reply("I love dogs")