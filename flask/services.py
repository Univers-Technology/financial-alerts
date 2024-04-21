from flask_sqlalchemy import SQLAlchemy

import models


def get_user(db: SQLAlchemy, user_id: int):
    """Get a user by id"""
    return db.session.execute(
        db.select(models.User).filter(models.User.id == user_id)
    ).scalar()


def get_user_by_email(db: SQLAlchemy, email: str):
    """Get a user by email"""
    return db.session.execute(
        db.select(models.User).filter(models.User.email == email)
    ).scalar()


def get_users(db: SQLAlchemy, skip: int = 0, limit: int = 100):
    """Get all users, with pagination"""
    return db.session.execute(
        db.select(models.User).offset(skip).limit(limit)
    ).scalars()


def create_user(db: SQLAlchemy, email: str, password: str):
    """Create a user"""
    fake_hashed_password = password + "notreallyhashed"
    db_user = models.User(email=email, hashed_password=fake_hashed_password)
    db.session.add(db_user)
    db.session.commit()
    db.session.refresh(db_user)
    return db_user
