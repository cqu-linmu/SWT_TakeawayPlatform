from fastapi import FastAPI, Depends
import hashlib
from sqlalchemy.orm import Session

from DataBaseEngine import SessionLocal
import ModuleParameter
import ModuleConstruct


app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/sign_in')
def create_user(user: ModuleConstruct.User, db: Session = Depends(get_db)):
    db_user = ModuleParameter.User()
    db_user.hash_pwd = hashlib.new('md5', user.pwd.encode()).hexdigest()
    db_user.account, db_user.screen_name = user.account, user.screen_name
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {
        'error': 0,
        'data': 'success'
    }