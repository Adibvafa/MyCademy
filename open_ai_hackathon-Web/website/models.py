# from . import db      # . refers to the current package (not that we're in the same folder as __init__)
# from flask_login import UserMixin
# from sqlalchemy.sql import func

# class Note(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     data = db.Column(db.String(10000))
#     date = db.Column(db.DateTime(timezone=True), default=func.now())
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # (not capitalized for foreign keys)

# # our class for our database inherits from db.Model, and for specifically the user object, we will also inherit from UserMixin
# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(150), unique=True)     # no user can have the same email as another user
#     password = db.Column(db.String(150))
#     first_name = db.Column(db.String(150))
#     notes = db.relationship('Note')                   # how we can access a users notes (capitalized here)