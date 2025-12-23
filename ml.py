from transformers import pipeline
# 1. Load the Model
# We are using a pre-trained model that generates summaries.
print("Loading summary  Model... please wait...")
summary_pipeline = pipeline("summarization" ,model = "Falconsai/text_summarization")
def summarize_text(text: str):
    """
    Input: A long piece of text.
    Output: A summarized version of that text.
    """
    summary = summary_pipeline(text, max_length=50, min_length=25, do_sample=False)
    return summary[0]['summary_text']

print("Loading Ques/Ans  Model... please wait...")
QuesAns_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
def QuesAns(Ques: str, Context: str):
    """
   Input: Question, Context
   Outupt: Answer
    """
    query = {
        'question': Ques,
        'context': Context
    }
    ans = QuesAns_pipeline(query)
    return ans['answer']