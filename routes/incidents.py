from fastapi import APIRouter
from database import SessionLocal
from models import Incident

router = APIRouter()

@router.get("/api/incidents")
def get_incidents():
    db = SessionLocal()
    incidents = db.query(Incident).all()

    return [
        {
            "id": i.id,
            "ip": i.source_ip,
            "attack": i.attack_type,
            "pipeline": i.pipeline,
            "confidence": i.confidence,
            "severity": i.severity
        }
        for i in incidents
    ]