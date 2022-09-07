import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Post(Base):
    __tablename__ = 'Posts'
    
    id = sa.Column(sa.Integer, primary_key=True, index=True, unique=True)
    title = sa.Column(sa.String(100))
    text = sa.Column(sa.Text)
    date = sa.Column(sa.DateTime)