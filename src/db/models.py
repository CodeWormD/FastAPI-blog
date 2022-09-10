import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'
    
    id = sa.Column(sa.Integer, primary_key=True, index=True, unique=True)
    group_id = sa.Column(sa.Integer, sa.ForeignKey('groups.id'), nullable=True)
    title = sa.Column(sa.String(100), nullable=False)
    text = sa.Column(sa.Text, nullable=False)
    date = sa.Column(sa.DateTime, default=sa.func.now())
    
    groups = relationship('Group', back_populates = 'posts')


class Group(Base):
    __tablename__ = 'groups'
    
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(20), nullable=False)
    
    posts = relationship('Post', back_populates = 'groups', lazy='select')