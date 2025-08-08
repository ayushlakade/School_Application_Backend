from fastapi import APIRouter,HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from db.schemas.schemas import DeleteStaff,DeleteStaff2,DeleteStaff3
from app.logger import setup_logging
import logging
from db.services.Staff_Services import StaffServiceManager
from db import get_db
setup_logging()
logger=logging.getLogger(__name__)
router=APIRouter()

@router.delete("/delete_staff_record_by_email_id")
def delete_update_student_record(staff:DeleteStaff,db:Session=Depends(get_db)):
    logger.info("Request Received to update student record")
    staff_info=StaffServiceManager.delete_staff_record_by_email_id(db,staff.staff_email)
    if staff_info:
        return_list = []
        for staff in staff_info:
            staff_data = {}
            staff_data['staff_id'] = staff.staff_id
            staff_data['staff_name'] = staff.staff_name
            staff_data['staff_email'] = staff.staff_email
            staff_data['staff_designation'] = staff.staff_designation
            staff_data['staff_salary'] = staff.staff_salary
            staff_data['staff_mobile_no'] = staff.staff_mobile_no

            return_list.append(staff_data)

        return JSONResponse(
            status_code=200,
            content={"message": return_list}
        )
    else:
        raise HTTPException(status_code=500, detail="Error in Deleting Staff email_id")


@router.delete("/delete_staff_record_by_name")
def delete_update_student_record(staff:DeleteStaff2,db:Session=Depends(get_db)):
    logger.info("Request Received to update student record")
    staff_info=StaffServiceManager.delete_staff_record_by_name(db,staff.staff_name)
    if staff_info:
        return_list = []
        for staff in staff_info:
            staff_data = {}
            staff_data['staff_id'] = staff.staff_id
            staff_data['staff_name'] = staff.staff_name
            staff_data['staff_email'] = staff.staff_email
            staff_data['staff_designation'] = staff.staff_designation
            staff_data['staff_salary'] = staff.staff_salary
            staff_data['staff_mobile_no'] = staff.staff_mobile_no

            return_list.append(staff_data)

        return JSONResponse(
            status_code=200,
            content={"message": return_list}
        )
    else:
        raise HTTPException(status_code=500, detail="Error in Deleting Staff record by name")



@router.delete("/delete_staff_record_by_id")
def delete_update_student_record(staff:DeleteStaff3,db:Session=Depends(get_db)):
    logger.info("Request Received to update student record")
    staff_info=StaffServiceManager.delete_staff_record_by_id(db,staff.staff_id)
    if staff_info:
        return_list = []
        for staff in staff_info:
            staff_data = {}
            staff_data['staff_id'] = staff.staff_id
            staff_data['staff_name'] = staff.staff_name
            staff_data['staff_email'] = staff.staff_email
            staff_data['staff_designation'] = staff.staff_designation
            staff_data['staff_salary'] = staff.staff_salary
            staff_data['staff_mobile_no'] = staff.staff_mobile_no

            return_list.append(staff_data)

        return JSONResponse(
            status_code=200,
            content={"message": return_list}
        )
    else:
        raise HTTPException(status_code=500, detail="Error in Deleting Staff record by id")
