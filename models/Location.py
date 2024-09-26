from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float
from sqlalchemy.orm import relationship


from config.base import Base


class Location(Base):
    __tablename__ = 'locations'
    location_id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float, default=0.0),
    longitude = Column(Float, default=0.0)

    targets = relationship("Target", lazy="noload", back_populates="location")