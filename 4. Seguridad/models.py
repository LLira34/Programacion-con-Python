
import datetime
from peewee import *
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash

DATABASE = SqliteDatabase("social.db")

#Start the class
class User(UserMixin, Model):
    #Defining the campos
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length=100)
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin = BooleanField(default = False)

    class Meta:
        database = DATABASE
        #Order the data
        order_by = ("-joined_at",)

    def get_posts(self):
        return Post.seletec().where(Post.user == self)

    def get_stream(self):
        return Post.seletec().where((Post.user == self))

    @classmethod
    def create_user(cls, username, email, password, admin=False):
        try:
            cls.create(
                username = username,
                email = email,
                password = generate_password_hash(password),
                is_admin = admin)
        except IntegrityError:
            raise ValueError("User already exists")


class Post(Model):
    timestamp = DateTimeField(default=datetime.datetime.now)
    user = ForeignKeyField(User, related_name = "posts")
    content = TextField()

    class Meta:
        database = DATABASE
        order_by = ("-timestamp",)

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Post], safe=True)
    DATABASE.close()
