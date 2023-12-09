# from flask_sqlalchemy import SQLAlchemy
#
# db = SQLAlchemy()
#
#
# def init_db(app):
#     db.init_app(app)
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Ivanna2223@localhost/Laba1'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     app.config['SECRET_KEY'] = 'cairocoders-ednalan'
#     app.config['SQLALCHEMY_ECHO'] = True
#
#     with app.app_context():
#         db.create_all()
#
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    db.init_app(app)

    with app.app_context():
        db.create_all()
