from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

customers=[
    
    {"id":101,"name":"ankur","age":"22","city":"banglore","risk":"medium"},
    {"id":102,"name":"anuj","age":"21","city":"pune","risk":"low"},
    {"id":103,"name":"shubham","age":"29","city":"banglore","risk":"high"}
    
]

@app.get("/customer")
def get_customer_data(city:str,risk:str):
    filtered=[
        c for c in customers
        if c["city"]==city and c["risk"]==risk
    ]
    
    
    return {
        # "city":city,
        # "risk":risk,
        "count":len(filtered),
        "result":filtered
    }