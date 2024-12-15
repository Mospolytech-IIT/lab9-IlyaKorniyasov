"""importing funcs"""
from update import update_user_email as update_user_email_db, update_post_content
from delete import delete_post, delete_user_and_posts # pylint: disable=all
from add import add_user, add_post
from extract import get_all_users, get_all_posts_w_users, get_posts_by_user

def create_user(username: str, email: str, password: str):
    """creating user"""
    return add_user(username, email, password)

def create_post(title: str, content: str, user_id: int):
    """creating post"""
    return add_post(title, content, user_id)

def read_all_users():
    """reading users"""
    return get_all_users()

def read_all_posts_w_users():
    """reading all posts w users"""
    return get_all_posts_w_users()

def read_posts_by_user(user_id):
    """reading posts bu user"""
    return get_posts_by_user(user_id)

def update_user_email(user_id, new_email):
    """updating user's email"""
    return update_user_email_db(user_id, new_email)

def update_post_content(post_id, new_content):
    """updating post content"""
    return update_post_content(post_id, new_content)
