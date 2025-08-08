from fastapi import APIRouter,HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from app.logger import setup_logging
import logging
from db.services.Staff_Services import StaffServiceManager
from db import get_db
setup_logging()
logger=logging.getLogger(__name__)
router=APIRouter()

@router.get("/get_all_staff_detail")
def get_all_students(db:Session=Depends(get_db)):
    logger.info("Request Received to get all staff info")
    staff_info=StaffServiceManager.display_all_staff_details(db)
    return_list=[]

    for staff in staff_info:
        staff_data = {}
        staff_data['staff_id']=staff.staff_id
        staff_data['staff_name']=staff.staff_name
        staff_data['staff_email']=staff.staff_email
        staff_data['staff_designation'] = staff.staff_designation
        staff_data['staff_salary'] = staff.staff_salary
        staff_data['staff_mobile_no'] = staff.staff_mobile_no

        return_list.append(staff_data)


    return JSONResponse(
        status_code=200,
        content={"message":return_list}
    )

@router.get("/get_staff_details_by_name/{staff_name}")
def get_students_by_id(staff_name:str,db:Session=Depends(get_db)):
    logger.info("Request Received to get staff by name : {0}".format(staff_name))
    staff_info=StaffServiceManager.display_staff_details_by_name(db,staff_name)

    return_list = []
    # for staff_info in staff_info:

    staff_data = {}
    staff_data['staff_id'] = staff_info.staff_id
    staff_data['staff_name'] = staff_info.staff_name
    staff_data['staff_email'] = staff_info.staff_email
    staff_data['staff_designation'] = staff_info.staff_designation
    staff_data['staff_salary'] = staff_info.staff_salary
    staff_data['staff_mobile_no'] = staff_info.staff_mobile_no
    return_list.append(staff_data)

    return JSONResponse(
        status_code=200,
        content={"message":return_list}
    )

@router.get("/get_staff_details_by_id/{staff_id}")
def get_students_by_id(staff_id:int,db:Session=Depends(get_db)):
    logger.info("Request Received to get staff by id : {0}".format(staff_id))
    staff_info=StaffServiceManager.display_staff_details_by_id(db,staff_id)

    return_list = []
    # for staff_info in staff_info:

    staff_data = {}
    staff_data['staff_id'] = staff_info.staff_id
    staff_data['staff_name'] = staff_info.staff_name
    staff_data['staff_email'] = staff_info.staff_email
    staff_data['staff_designation'] = staff_info.staff_designation
    staff_data['staff_salary'] = staff_info.staff_salary
    staff_data['staff_mobile_no'] = staff_info.staff_mobile_no
    return_list.append(staff_data)

    return JSONResponse(
        status_code=200,
        content={"message":return_list}
    )

@router.get("/get_staffs_salary_greater_than/{staff_salary}")
def get_students_by_id(staff_salary:int,db:Session=Depends(get_db)):
    logger.info("Request Received to get staff by email : {0}".format(staff_salary))
    staff_info=StaffServiceManager.get_staff_with_salary_greater_than(db,staff_salary)

    return_list = []
    for staff_info in staff_info:
        staff_data = {}
        staff_data['staff_id'] = staff_info.staff_id
        staff_data['staff_name'] = staff_info.staff_name
        staff_data['staff_email'] = staff_info.staff_email
        staff_data['staff_designation'] = staff_info.staff_designation
        staff_data['staff_salary'] = staff_info.staff_salary
        staff_data['staff_mobile_no'] = staff_info.staff_mobile_no
        return_list.append(staff_data)

    return JSONResponse(
        status_code=200,
        content={"message":return_list}
    )

@router.get("/get_staffs_salary_less_than/{staff_salary}")
def get_students_by_id(staff_salary:int,db:Session=Depends(get_db)):
    logger.info("Request Received to get staff by email : {0}".format(staff_salary))
    staff_info=StaffServiceManager.get_staff_with_salary_less_than(db,staff_salary)

    return_list = []
    for staff_info in staff_info:
        staff_data = {}
        staff_data['staff_id'] = staff_info.staff_id
        staff_data['staff_name'] = staff_info.staff_name
        staff_data['staff_email'] = staff_info.staff_email
        staff_data['staff_designation'] = staff_info.staff_designation
        staff_data['staff_salary'] = staff_info.staff_salary
        staff_data['staff_mobile_no'] = staff_info.staff_mobile_no
        return_list.append(staff_data)

    return JSONResponse(
        status_code=200,
        content={"message":return_list}
    )