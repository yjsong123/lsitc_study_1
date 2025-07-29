from datetime import datetime

from sqlalchemy.orm import Session

from src.domain.answer.answer_model import AnswerCreate
from src.db.entity import QuestionEntity, AnswerEntity


def create_answer(db: Session, question: QuestionEntity, answer_create: AnswerCreate):
    db_answer = AnswerEntity(question=question,
                       content=answer_create.content,
                       create_date=datetime.now())
    db.add(db_answer)
    db.commit()
