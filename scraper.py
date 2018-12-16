
user_agent = 'user-comment-scraper /u/bsomes2'

secret = 'Your secret here'

id = 'your app id here'

redirect = 'https://127.0.0.1:65010/authorize_callback'

account_code = 'P-code'

app_scopes = [
    'creddits',
    'modcontributors',
    'modconfig',
    'subscribe',
    'wikiread',
    'wikiedit',
    'vote',
    'mysubreddits',
    'submit',
    'modlog',
    'modposts',
    'modflair',
    'save',
    'modothers',
    'read',
    'privatemessages',
    'report',
    'identity',
    'livemanage',
    'account',
    'modtraffic',
    'edit',
    'modwiki',
    'modself',
    'history',
    'flair'
    ]

refresh = 'your refresh token'

def login():
    import praw
    r = praw.Reddit(client_id=id, user_agent=user_agent, client_secret=secret, refresh_token=refresh)
    return r
    