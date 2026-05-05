from fastapi import APIRouter
from database import SessionLocal
from models import Incident

router = APIRouter()

@router.post("/api/idps/event")
def idps_event(data: dict):
    db = SessionLocal()

    incident = Incident(
        source_ip=data["ip"],
        attack_type=data["attack"],
        pipeline="A",
        confidence=data["confidence"],
        severity=data["severity"]
    )

    db.add(incident)
    db.commit()
    db.refresh(incident)

    return {"message": "IDPS event stored"}