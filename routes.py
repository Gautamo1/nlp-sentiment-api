from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from database import get_session
from models import Summary, SummaryCreate, QuestionCreate, Question
from ml import summarize_text, QuesAns  # <--- Import our AI Specialist!

router = APIRouter()

@router.get("/")
def read_route():
    return {"message": "Healthy"}

@router.post("/summarize/")
def create_summary(summary_input: SummaryCreate, session: Session = Depends
(get_session)):
    
    summary_result = summarize_text(summary_input.text)

    new_summary = Summary(
        text=summary_input.text,
        summary_text=summary_result
    )

    session.add(new_summary)
    session.commit()
    session.refresh(new_summary)

    return new_summary

@router.get("/summaries/")
def read_summaries(session: Session = Depends(get_session)):
    summaries = session.exec(select(Summary)).all()
    return summaries


@router.post("/QuesAns/")
def create_QuesAns(Ques_input: QuestionCreate, session: Session = Depends(get_session)):
    Answer = QuesAns(Ques_input.question, Ques_input.context)
    new_quesAns = Question(
        question = Ques_input.question,
        answer = Answer,
        context = Ques_input.context
    )
    session.add(new_quesAns)
    session.commit()
    session.refresh(new_quesAns)
    return new_quesAns

@router.get("/QuesAns/")
def read_QuesAns(session: Session = Depends(get_session)):
    QuesAns = session.exec(select(Question)).all()
    return QuesAns