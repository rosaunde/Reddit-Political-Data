import praw
import pandas
import time

with open('data3.txt', 'w', encoding='utf-8') as f:

    reddit = praw.Reddit(client_id='Jzzy_2GSgfC5Tw',
                         client_secret='7bbxeeAHqtmZAcrE7w3xwDuna64',
                         user_agent='itsamemario',
                         username='rorance',
                         password='firedog25'
                         )


    subreddit = reddit.subreddit('conservative')

    new_posts = subreddit.new(limit = 1000)

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
