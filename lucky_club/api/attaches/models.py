import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship
from lucky_club.database import db


class Attachment(db.Model):
    __tablename__ = 'Attachment'

    id = Column(Integer, primary_key=True)
    description = Column(String(255), nullable=True)
    file_url = Column(String(500), nullable=False)
    lot_id = Column(ForeignKey('Lot.id'))
    lot = relationship('Lot', backref=db.backref('images_of_lot', lazy='select'))
    user_id = Column(ForeignKey('User.id'))
    user = relationship('User')
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'description': self.description,
            'file_url': self.file_url,
            'lot_id': self.lot_id,
            'user_id': self.user_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
