"""importing sqlalchemy and stuff"""
from sqlalchemy.orm import sessionmaker
from database import User, Post, engine

Session = sessionmaker(bind=engine)
session = Session()

def delete_post(post_id):
    """deleting post"""
    post = session.query(Post).filter_by(id=post_id).first()
    if post:
        session.delete(post)
        session.commit()
        return { f"Post ID {post_id} deleted"}
    return {"error": "Post not found"}

def delete_user_and_posts(user_id):
    """deleting user and posts"""
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        posts = session.query(Post).filter_by(user_id=user_id).all()
        for post in posts:
            session.delete(post)
        session.delete(user)
        session.commit()
        return { f"User {user.username} and all posts deleted"}
    return {"error": "User not found"}
