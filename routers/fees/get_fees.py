from fastapi import APIRouter,HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from app.logger import setup_logging
import logging
from db.services.Fees_Services import FeesServiceManager
from db import get_db
setup_logging()
logger=logging.getLogger(__name__)
router=APIRouter()

@router.get("/get_all_students_fees_details")
def get_all_students(db:Session=Depends(get_db)):
    logger.info("Request Received to get all students fees info")
    student_info=FeesServiceManager.display_all_student_fees_details(db)
    return_list=[]

    for student in student_info:
        student_data = {}
        student_data['student_id']=student.student_id
        student_data['student_name']=student.student_name
        student_data['student_total_fees']=student.student_total_fees
        student_data['student_balance_fees'] = student.student_balance_fees
        return_list.append(student_data)


    return JSONResponse(
        status_code=200,
        content={"message":return_list}
    )

@router.get("/get_students_balance_fees_by_name/{student_name}")
def get_students_by_id(student_name:str,db:Session=Depends(get_db)):
    logger.info("Request Received to get student pending by name : {0}".format(student_name))
    student_info=FeesServiceManager.display_student_pending_fees_details_by_name(db,student_name)

    return_list = []

    student_data = {}
    student_data['student_id'] = student_info.student_id
    # student_data['student_name'] = student_info.student_name
    # student_data['student_total_fees'] = student_info.student_total_fees
    student_data['student_balance_fees'] = student_info.student_balance_fees
    return_list.append(student_data)

    return JSONResponse(
        status_code=200,
        content={"message":return_list}
    )

@router.get("/get_students_by_id/{student_id}")
def get_students_by_id(student_id:int,db:Session=Depends(get_db)):
    logger.info("Request Received to get student by id : {0}".format(student_id))
    student_info=FeesServiceManager.display_student_details_by_id(db,student_id)

    return_list = []
    student_data = {}
    student_data['student_id'] = student_info.student_id
    student_data['student_name'] = student_info.student_name
    student_data['student_total_fees'] = student_info.student_total_fees
    student_data['student_balance_fees'] = student_info.student_balance_fees
    return_list.append(student_data)

    return JSONResponse(
        status_code=200,
        content={"message":return_list}
    )


@router.get("/get_student_balance_fees_greater_than/{minimum_fee}")
def get_courses_by_minimum_fee(minimum_fee: int, db: Session = Depends(get_db)):
    logger.info("Request Received to get course sort by course_fees : {0}".format(minimum_fee))
    student_info = FeesServiceManager.get_student_with_balance_fees_greater_than(db, minimum_fee)
    return_list = []
    for student in student_info:
        student_data = {}
        student_data['student_id'] = student.student_id
        student_data['student_name'] = student.student_name
        student_data['student_total_fees'] = student.student_total_fees
        student_data['student_balance_fees'] = student.student_balance_fees
        return_list.append(student_data)

    return JSONResponse(
        status_code=200,
        content={"message": return_list}
    )


@router.get("/get_student_balance_fees_less_than/{minimum_fee}")
def get_courses_by_minimum_fee(minimum_fee: int, db: Session = Depends(get_db)):
    logger.info("Request Received to get course sort by course_fees : {0}".format(minimum_fee))
    student_info = FeesServiceManager.get_student_with_balance_fees_less_than(db, minimum_fee)
    return_list = []
    for student in student_info:
        student_data = {}
        student_data['student_id'] = student.student_id
        student_data['student_name'] = student.student_name
        student_data['student_total_fees'] = student.student_total_fees
        student_data['student_balance_fees'] = student.student_balance_fees
        return_list.append(student_data)

    return JSONResponse(
        status_code=200,
        content={"message": return_list}
    )