import praw
import pandas

with open('data2.txt', 'w') as f:

    reddit = praw.Reddit(client_id='MOxGG3TJPOWdnQ',
                         client_secret='NQTISXFZPGHCcihNWcjSbhyG2Go',
                         user_agent='itsamemario'
                         )


    subreddit = reddit.subreddit('conservative')

    new_posts = subreddit.new(limit = 10000)

    for submission in new_posts:
        if not submission.stickied:
            if submission.score >= 10:
                f.write('Title: {}, score: {}, author: {}, time: {}, selftext: {}'.format(submission.title, submission.score, submission.author, submission.created_utc, submission.selftext) + "\n")
                #print('Title: {}, score: {}, author: {}, time: {}, selftext: {}'.format(submission.title, submission.score, submission.author, submission.created_utc, submission.selftext))
                submission.comments.replace_more(limit = 0)
                comments = submission.comments.list()
                for comment in comments:
                    if comment.score >= 10:
                        f.write('Body: {}, Score: {}, Author: {}'.format(comment.body, comment.score, comment.author) + "\n")
                        #print('Body: {}, Score: {}, Author: {}'.format(comment.body, comment.score, comment.author))
