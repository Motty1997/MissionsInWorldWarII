from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from config.base import Base


class Target(Base):
    __tablename__ = "targets"
    target_id = Column(Integer, primary_key=True, autoincrement=True)
    target_industry = Column(String(200))
    target_priority = Column(Integer)
    city_id = Column(Integer, ForeignKey('cities.city_id'))
    target_type_id = Column(Integer, ForeignKey('target_types.target_type_id'))
    location_id = Column(Integer, ForeignKey('locations.location_id'))


    city = relationship("City", back_populates="targets")
    target_type = relationship("TargetType", back_populates="targets")
    location = relationship("Location", back_populates="targets")
