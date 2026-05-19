from app.database.db import SessionLocal
from app.models.message import Message


def save_message(student_id: str, role: str, content: str):
    db = SessionLocal()

    try:
        msg = Message(
            student_id=student_id,
            role=role,
            content=content
        )

        db.add(msg)
        db.commit()
        print("Saving:", student_id, role, content)

    except Exception as e:
        db.rollback()
        print("DB Error:", e)

    finally:
        db.close()
def get_recent_messages(student_id: str, limit: int = 10):

    db = SessionLocal()

    try:
        messages = (
            db.query(Message)
            .filter(Message.student_id == student_id)
            .order_by(Message.id.desc())
            .limit(limit)
            .all()
        )

        return list(reversed(messages))

    finally:
        db.close()