from src.db.repository import question_crud
from sqlalchemy.orm import Session

def get_question_list(db: Session)-> List(QuestionEntity):
    _question_list = question_crud.get_question_list(db=db)
    return _question_list

def get_question(db: Session, question_id: int) -> Any | None:
    question: Any | None = question_crud.get_question(db = d)