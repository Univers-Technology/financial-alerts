from apiflask import APIFlask, abort

import schemas
import services
from database import db

app = APIFlask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./db.sqlite3"

db.init_app(app)

with app.app_context():
    db.create_all()


@app.get("/")
def hello_world():
    return {"message": "Hello World"}


@app.post("/users/")
@app.input(schemas.UserCreate)
@app.output(schemas.User)
def create_user(json_data):
    email = json_data.get("email")
    password = json_data.get("password")
    db_user = services.get_user_by_email(db, email)
    if db_user:
        abort(400, "Email already registered")
    return services.create_user(db, email, password)


@app.get("/users/")
@app.input(schemas.UserReadQuery, location="query")
@app.output(schemas.User(many=True))
def read_users(query_data):
    skip: int = query_data.get("skip", 0)
    limit: int = query_data.get("limit", 100)
    return services.get_users(db, skip, limit)


@app.get("/users/<int:user_id>")
@app.output(schemas.User)
def read_user(user_id: int):
    db_user = services.get_user(db, user_id=user_id)
    if db_user is None:
        abort(404, "User not found")
    return db_user
