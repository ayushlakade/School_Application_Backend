from db.model import models as M
from sqlalchemy.orm import Session


class StaffServiceManager:
    def display_all_staff_details(db: Session):
        q=db.query(M.StaffManager)
        try:
            return q.all()
        except Exception as e:
            return None

    def display_staff_details_by_name(db: Session,staff_name):
        q = db.query(M.StaffManager).filter_by(staff_name=staff_name).first()
        try:
            return q
        except Exception as e:
            return None

    def display_staff_details_by_id(db: Session,staff_id):
        q = db.query(M.StaffManager).filter_by(staff_id=staff_id).first()
        try:
            return q
        except Exception as e:
            return None

    def display_staff_details_by_email(db: Session,staff_email):
        q = db.query(M.StaffManager).filter_by(staff_email=staff_email).first()
        try:
            return q
        except Exception as e:
            return None

    def display_staff_details_by_mobile_number(db: Session,staff_mobile_no):
        q = db.query(M.StaffManager).filter_by(staff_mobile_no=staff_mobile_no).first()
        try:
            return q
        except Exception as e:
            return None


    def insert_staff_details(db:Session,staff_name,staff_email,staff_designation,staff_salary,staff_mobile_no):
        try:
            student=M.StaffManager(staff_name=staff_name,staff_email=staff_email,staff_designation=staff_designation,staff_salary=staff_salary,staff_mobile_no=staff_mobile_no)
            db.add(student)
            db.commit()
            q = db.query(M.StaffManager)
            return q.all()
        except Exception as e:
            return e


    def update_staff_email_by_staff_id(db:Session,staff_id,staff_email):#by name email get updated
        try:
            student=db.query(M.StaffManager).filter_by(staff_id=staff_id).first()
            if student:
                student.staff_email=staff_email
                db.commit()
                q = db.query(M.StaffManager)
                return q.all()
            else:
                return {"message":"staff id not found"}
        except Exception as e:
            return e

    def update_staff_name_by_mobile_number(db:Session,staff_mobile_no,staff_name):#by name email get updated
        try:
            student=db.query(M.StaffManager).filter_by(staff_mobile_no=staff_mobile_no).first()
            if student:
                student.staff_name=staff_name
                db.commit()
                q = db.query(M.StaffManager)
                return q.all()
            else:
                return {"message":"student not found"}
        except Exception as e:
            return e

    def update_staff_details_by_mobile_number(db: Session, staff_name,staff_email,staff_designation,staff_salary,staff_mobile_no):
        try:
            staff = db.query(M.StaffManager).filter_by(staff_mobile_no=staff_mobile_no).first()
            if staff:
                staff.staff_name=staff_name
                staff.staff_email=staff_email
                staff.staff_designation=staff_designation
                staff.staff_salary=staff_salary
                db.commit()
                q = db.query(M.StaffManager)
                return q.all()

            else:
                return {"message": "mobile number not found"}
        except Exception as e:
            return e

    def update_staff_details_by_staff_id(db: Session, staff_id,staff_name, staff_email, staff_designation, staff_salary,staff_mobile_no, ):
        try:
            staff = db.query(M.StaffManager).filter_by(staff_id=staff_id).first()
            if staff:
                staff.staff_name = staff_name
                staff.staff_email = staff_email
                staff.staff_designation = staff_designation
                staff.staff_salary = staff_salary
                staff.staff_mobile_no = staff_mobile_no
                db.commit()
                q = db.query(M.StaffManager)
                return q.all()

            else:
                return {"message": "mobile number not found"}
        except Exception as e:
            return e

    def update_staff_details_by_staff_email(db: Session, staff_name, staff_email, staff_designation, staff_salary,staff_mobile_no ):
        try:
            staff = db.query(M.StaffManager).filter_by(staff_email=staff_email).first()
            if staff:
                staff.staff_name = staff_name
                staff.staff_designation = staff_designation
                staff.staff_salary = staff_salary
                staff.staff_mobile_no = staff_mobile_no
                db.commit()
                q = db.query(M.StaffManager)
                return q.all()

            else:
                return {"message": "mobile number not found"}
        except Exception as e:
            return e

    def delete_staff_record_by_email_id(db: Session, staff_email):
        try:
            student = db.query(M.StaffManager).filter_by(staff_email=staff_email).first()
            if student:
                db.delete(student)
                db.commit()
                q = db.query(M.StaffManager)
                return q.all()
            else:
                return None
        except Exception as e:
            return None

    def delete_staff_record_by_name(db: Session, staff_name):
        try:
            student = db.query(M.StaffManager).filter_by(staff_name=staff_name).first()
            if student:
                db.delete(student)
                db.commit()
                q = db.query(M.StaffManager)
                return q.all()
            else:
                return None
        except Exception as e:
            return None

    def delete_staff_record_by_id(db: Session, staff_id):
        try:
            student = db.query(M.StaffManager).filter_by(staff_id=staff_id).first()
            if student:
                db.delete(student)
                db.commit()
                q = db.query(M.StaffManager)
                return q.all()
            else:
                return None
        except Exception as e:
            return None

    def get_staff_with_salary_less_than(db: Session, minimum_salary: int):
        try:
            staff = db.query(M.StaffManager).filter(M.StaffManager.staff_salary <= minimum_salary).all()
            if staff:
                return staff
            else:
                return []
        except Exception as e:
            return []


    def get_staff_with_salary_greater_than(db: Session, minimum_salary: int):
        try:
            staff = db.query(M.StaffManager).filter(M.StaffManager.staff_salary >= minimum_salary).all()
            if staff:
                return staff
            else:
                return []
        except Exception as e:
            return []






