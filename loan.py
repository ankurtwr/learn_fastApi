from fastapi import FastAPI
from pydantic import BaseModel 

app= FastAPI()

class LoanApplication(BaseModel):
    age:int
    income:float
    loan_amount:float
    employment_years:int

@app.post("/predict")
def predict_loan(application:LoanApplication):
    
    #pretendiing this is a trained model 
    if application.income> 50000 and application.employment_years> 2 :
        decision="approved"
    else:
        decision="rejected"
    return {
        "applicent_age":application.age,
        "decision":decision 
        
        }


