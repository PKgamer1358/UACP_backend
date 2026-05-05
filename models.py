from sqlalchemy import Column, Integer, String, Float
from database import Base

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    source_ip = Column(String)
    attack_type = Column(String)
    pipeline = Column(String)  # A or B
    confidence = Column(Float)
    severity = Column(String)