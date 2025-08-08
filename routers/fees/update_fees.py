from fastapi import APIRouter,HTTPException,Depends
from fastapi.params import Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from db.schemas.schemas import FeePayment,FeePayment2
from app.logger import setup_logging
import logging
from db.services.Fees_Services import FeesServiceManager
from db import get_db
setup_logging()
logger=logging.getLogger(__name__)
router=APIRouter()



@router.patch("/update_student_balance")
def update_balance_by_id(payment: FeePayment, db: Session = Depends(get_db)):
    fee_record = FeesServiceManager.update_student_balance_fee(db, payment.student_id, payment.amount_paid)
    if not fee_record:
        raise HTTPException(status_code=404, detail="Fee record not found")
    return {
        "student_id": fee_record.student_id,
        "student_total_fees": fee_record.student_total_fees,
        "student_balance_fees": fee_record.student_balance_fees,
    }

@router.patch("/update_student_balance_by_name")
def update_balance_by_name(payment: FeePayment2, db: Session = Depends(get_db)):
    fee_record = FeesServiceManager.update_student_balance_fee_by_name(db, payment.student_name, payment.amount_paid)
    if not fee_record:
        raise HTTPException(status_code=404, detail="Fee record not found")
    return {
        "student_id": fee_record.student_id,
        "student_total_fees": fee_record.student_total_fees,
        "student_balance_fees": fee_record.student_balance_fees,
    }
