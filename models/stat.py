from ..database import Base
from sqlalchemy import Column, String, TIME, Integer



class Stat(Base):
    __tablename__ = 'stats'
    id = Column(String, primary_key=True)
    average_run_time = Column(TIME())
    request_count = Column(Integer)
