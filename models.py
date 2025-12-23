from sqlmodel import SQLModel, Field

# The "Base" Model
class SummaryModel(SQLModel):
    text: str

class SummaryCreate(SummaryModel):
    pass

class Summary(SummaryModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    summary_text: str | None = None

class SummaryRead(SummaryModel):
    id: int | None = None
    summary_text: str | None = None


class QuestionModel(SQLModel):
    question: str


class QuestionCreate(QuestionModel):
    context: str

class Question(QuestionCreate, table=True):
    id: int | None = Field(default=None, primary_key=True)
    answer: str | None = None
    
class QuestionRead(QuestionModel):
    answer: str | None = None