from fastapi import APIRouter

router = APIRouter()

@router.post("/api/steg/event")
def steg_event():
    return {"message": "Steg working"}