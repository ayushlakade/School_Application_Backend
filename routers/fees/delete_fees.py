from fastapi import APIRouter,HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from db.schemas.schemas import DeleteStudentBase2,DeleteStudentBase3
from app.logger import setup_logging
import logging
from db.services.Fees_Services import FeesServiceManager
from db import get_db
setup_logging()
logger=logging.getLogger(__name__)
router=APIRouter()



@router.delete("/delete_student_record_by_name")
def delete_student_record_name(student:DeleteStudentBase2,db:Session=Depends(get_db)):
    logger.info("Request Received to delete student record")
    records=FeesServiceManager.delete_student_details_by_name(db,student.student_name)
    if records:
        return_list = []
        for student in records:
            student_data = {}
            student_data['student_id'] = student.student_id
            student_data['student_name'] = student.student_name
            student_data['student_total_fees'] = student.student_total_fees
            student_data['student_balance_fees'] = student.student_balance_fees
            return_list.append(student_data)

        return JSONResponse(
            status_code=201,
            content={"message": return_list}
        )
    else:
        raise HTTPException(status_code=500,detail="Error in Deleting Student Record")



@router.delete("/delete_student_record_by_id")
def delete_student_record_name(student:DeleteStudentBase3,db:Session=Depends(get_db)):
    logger.info("Request Received to update student record")
    records=FeesServiceManager.delete_student_details_by_id(db,student.student_id)
    if records:
        return_list = []
        for student in records:
            student_data = {}
            student_data['student_id'] = student.student_id
            student_data['student_name'] = student.student_name
            student_data['student_total_fees'] = student.student_total_fees
            student_data['student_balance_fees'] = student.student_balance_fees
            return_list.append(student_data)

        return JSONResponse(
            status_code=201,
            content={"message": return_list}
        )
    else:
        raise HTTPException(status_code=500,detail="Error in Deleting Student Record")