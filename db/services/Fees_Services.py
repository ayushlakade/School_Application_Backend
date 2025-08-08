from db.model import models as M
from sqlalchemy.orm import Session
from db.schemas.schemas import StudentBase
from db.services.base_Service import BaseSerVice

class FeesServiceManager:
    def display_all_student_fees_details(db: Session):
        q=db.query(M.FeesManager)
        try:
            return q.all()
        except Exception as e:
            return None

    def display_student_pending_fees_details_by_name(db: Session,student_name):
        q = db.query(M.FeesManager).filter_by(student_name=student_name).first()
        try:
            return q
        except Exception as e:
            return None

    def display_student_details_by_id(db: Session,student_id:int):
        q = db.query(M.FeesManager).filter_by(student_id=student_id).first()
        try:
            return q
        except Exception as e:
            return None

    def insert_student_details(db:Session,student_id,student_name,student_total_fees,student_balance_fees):
        try:
            student=M.FeesManager(student_id=student_id,student_name=student_name,student_total_fees=student_total_fees,student_balance_fees=student_balance_fees)
            db.add(student)
            db.commit()
            q = db.query(M.FeesManager)
            return q.all()
        except Exception as e:
            return None

    def update_student_balance_fee_by_name(db: Session, student_name: str, amount_paid: int):
        try:
            fee_record = db.query(M.FeesManager).filter_by(student_name=student_name).first()
            if not fee_record:
                return None

            # Reduce balance fees by amount_paid, prevent negative balance
            new_balance = fee_record.student_balance_fees - amount_paid
            fee_record.student_balance_fees = max(new_balance, 0)

            db.commit()
            db.refresh(fee_record)
            return fee_record

        except Exception:
            db.rollback()
            raise

    def update_student_balance_fee(db: Session, student_id: int, amount_paid: int):
        try:
            fee_record = db.query(M.FeesManager).filter_by(student_id=student_id).first()
            if not fee_record:
                return None

            # Reduce balance fees by amount_paid, prevent negative balance
            new_balance = fee_record.student_balance_fees - amount_paid
            fee_record.student_balance_fees = max(new_balance, 0)

            db.commit()
            db.refresh(fee_record)
            return fee_record

        except Exception:
            db.rollback()
            raise

    def delete_student_details_by_id(db:Session,student_id):
        try:
            student=db.query(M.FeesManager).filter_by(student_id=student_id).first()
            if student:
                db.delete(student)
                db.commit()
                q = db.query(M.FeesManager)
                return q.all()
            else:
                return None
        except Exception as e:
            return None

    def delete_student_details_by_name(db:Session,student_name):
        try:
            student=db.query(M.FeesManager).filter_by(student_name=student_name).first()
            if student:
                db.delete(student)
                db.commit()
                q = db.query(M.FeesManager)
                return q.all()
            else:
                return None
        except Exception as e:
            return None


    def get_student_with_balance_fees_less_than(db: Session, minimum_fees: int):
        try:
            student = db.query(M.FeesManager).filter(M.FeesManager.student_balance_fees <= minimum_fees).all()
            if student:
                return student
            else:
                return []
        except Exception as e:
            return []


    def get_student_with_balance_fees_greater_than(db: Session, minimum_fees: int):
        try:
            student = db.query(M.FeesManager).filter(M.FeesManager.student_balance_fees >= minimum_fees).all()
            if student:
                return student
            else:
                return []
        except Exception as e:
            return []


