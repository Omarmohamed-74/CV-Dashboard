import os
from fastapi import APIRouter, UploadFile, File
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import CV

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_cv(file: UploadFile = File(...)):
    filepath = f"{UPLOAD_DIR}/{file.filename}"

    with open(filepath, "wb") as f:
        f.write(await file.read())

    db: Session = SessionLocal()

    cv = CV(filename=file.filename)
    db.add(cv)
    db.commit()
    db.refresh(cv)

    db.close()

    return {
        "message": "uploaded",
        "id": cv.id,
        "filename": file.filename
    }


@router.get("/cvs")
def get_cvs():
    db = SessionLocal()

    cvs = db.query(CV).all()

    db.close()

    return cvs