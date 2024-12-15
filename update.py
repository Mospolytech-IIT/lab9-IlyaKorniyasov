"""importing sqlalcheny and stuff"""
from sqlalchemy.orm import sessionmaker
from database import User, Post, engine

Session = sessionmaker(bind=engine)
session = Session()

def update_user_email(user_id, new_email):
    """updating user email"""
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        user.email = new_email
        session.commit()
        return {"message": f"User {user.username} email updated to {new_email}"}
    return {"error": "User not found"}

def update_post_content(post_id, new_content):
    """upodating post content"""
    post = session.query(Post).filter_by(id=post_id).first()
    if post:
        post.content = new_content
        session.commit()
        return {"message": f"Post content updated for post ID {post_id}"}
    return {"error": "Post not found"}
