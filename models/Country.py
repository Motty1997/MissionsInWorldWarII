from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


from config.base import Base


class Country(Base):
    __tablename__ = 'countries'
    country_id = Column(Integer, primary_key=True, autoincrement=True)
    country_name = Column(String(200), nullable=False)

    cities = relationship("City", lazy="noload", back_populates="country")