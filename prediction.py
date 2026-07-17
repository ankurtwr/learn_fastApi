from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class LoanApplication(BaseModel):
    age:int
    income:float
    loan_amount:float
    employment_year:int


@app.post("/predict")
def predict(application:LoanApplication):
    if application.income>50000 and application.employment_year>2:
        decision="approved"
    else:
        decision="rejected"
    return {
        "applicent_age":application.age,
        "decision":decision
    }
    
    