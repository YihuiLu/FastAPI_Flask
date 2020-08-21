from sqlalchemy import Column, String, Integer, orm

from app.models.base import Base


class Hello(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    language = Column(String(20), nullable=False)
    color = Column(String(30), default='黑色')

    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'language', 'color']
