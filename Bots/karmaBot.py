import praw

user_agent = praw.Reddit('Karma details provided by /u/droolq')

print('\nWelcome!\n\nWhat is the reddit username?')
user_name = input()

reddit_user = user_agent.get_redditor(user_name)

print('\nWhat order do you want karma in ?\n\n1. Ascending order\n2. Descending order')
order = input()

print('\nGetting karma from all the subreddits you have visited. This might take a few seconds\n')
content = reddit_user.get_submitted(limit=None)

karma = {}

for thing in content:
    subreddit = thing.subreddit.display_name
    karma[subreddit] = (karma.get(subreddit, 0) + thing.score)

if '1' in order:
    sorted_karma = sorted(karma, key=lambda x : karma[x], reverse=True)
elif '2' in order:
    sorted_karma = sorted(karma, key=lambda x : karma[x])
else:
    sorted_karma = karma

for subreddit in sorted_karma:
    print('r/{name}: {karma}'.format(name=subreddit, karma=karma[subreddit]))
