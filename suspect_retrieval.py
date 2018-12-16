import praw

client_secret = '6sMdw_uSx2Gr78AuUSBAAG_IL4A'

client_id = 'ciEjVvc1yUtZJw'

user_agent = 'suspected-user-retrieval /u/bsomes2'

def get_instance():
    return praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

