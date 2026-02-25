from time import time
sessions = {}

def create_session(user_id):
    # Sets login_time to None - improve this to capture the actual login time (current timestamp)
    sessions[user_id] = {'data': {}, 'login_time': int}

def login_user(user_id):
    sessions[user_id]['login_time'] = time()  # This should be replaced with the real current time

def is_session_active(user_id, timeout: int):
    return (timeout + sessions[user_id]['login_time'] > time())


# - Implement a function is_session_active(user_id, timeout) that returns True if the user session is active within the timeout period.
