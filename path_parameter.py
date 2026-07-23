from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

customer_risk_profiles={
    101:{"name":"ravi","salary":"20000","age":"26","risk":"low","score":0.12},
    102:{"name":"kisan","salary":"10000","age":"25","risk":"medium","score":0.36},
    103:{"name":"shyam","salary":"1000","age":"22","risk":"high","score":0.55}
}




#path parameters
@app.get("/customer/{customer_id}")
def get_customer_risk(customer_id:int):
    if customer_id not in customer_risk_profiles:
        return {"error, customer do not exist"}
    else:
        profile=customer_risk_profiles[customer_id]
        return {
            "customer_id":customer_id,
            "customer_name":profile["name"],
            "customer_salary":profile["salary"],
            "customer_age":profile["age"],
            "customer_risk":profile["risk"],
            "customer_score":profile["score"]
            }
        

   