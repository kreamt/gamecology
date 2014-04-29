# -*- coding: utf-8 -*-
from gamecology.database import (
    Column,
    db,
    Model,
    ReferenceCol,
    relationship,
    SurrogatePK,
)


class Game(SurrogatePK, Model):
    __tablename__ = 'games'
    name = Column(db.String(80), unique=True, nullable=False)
    description = Column(db.String(80), unique=True, nullable=False)

    def __init__(self, name, **kwargs):
        db.Model.__init__(self, name=name, **kwargs)

    def __repr__(self):
        return '<Game({name})>'.format(name=self.name)
