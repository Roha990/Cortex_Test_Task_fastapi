from app.database.database import SessionLocal, Position
import re


def add_position(position_name):
    if re.search(r'[0-9\s\W]', position_name):
        return False
    db = SessionLocal()
    new_position = Position(title=position_name)
    db.add(new_position)
    db.commit()
    db.close()
    return True


def get_positions():
    db = SessionLocal()
    query = db.query(Position)
    db.close()
    return db.query(Position)


def get_position(position_id):
    db = SessionLocal()
    position = db.query(Position).filter(Position.id == position_id).first()
    db.close()
    if position is None:
        return False
    return position


def delete_position_db(id):
    db = SessionLocal()
    position = db.query(Position).filter(Position.id == id).first()
    db.delete(position)
    db.commit()
    db.close()
    return True


def update_position(id, name):
    if re.search(r'[0-9\s\W]', name):
        return False
    db = SessionLocal()
    position = db.query(Position).filter(Position.id == id).first()
    position.title = name
    db.commit()
    db.close()
    return True
