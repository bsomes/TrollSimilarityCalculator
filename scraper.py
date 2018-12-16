
user_agent = 'user-comment-scraper /u/bsomes2'

secret = 'YJ6e3QPCYCmP0COCUWc28Ag1nrA'

id = 'LrnNRj0uyfoIrQ'

redirect = 'https://127.0.0.1:65010/authorize_callback'

account_code = 'P-ejFBYnMuxo6nhNfab1wdEpTwc'

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

refresh = '1091926979-s345mlrO57aIwPLzFgrjD1NJP-Y'

def login():
    import praw
    r = praw.Reddit(client_id=id, user_agent=user_agent, client_secret=secret, refresh_token=refresh)
    return r
    