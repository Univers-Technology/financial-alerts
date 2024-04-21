from apiflask import Schema
from apiflask.fields import String, Integer, Boolean


class UserBase(Schema):
    email = String(required=True)


class UserCreate(UserBase):
    password = String(required=True)


class User(UserBase):
    id = Integer(required=True)
    is_active = Boolean(required=True)
    # ... more fields here


class UserReadQuery(Schema):
    skip = Integer(required=False)
    limit = Integer(required=False)
