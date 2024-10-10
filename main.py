
from fastapi import FastAPI

app = FastAPI()


@app.get("/get")
def get():
    return{
        "msg":"hello to all.... welcome to RCV"
    }

@app.post("/post")
def post():
    return{'msg':"adding the details"}

@app.delete("/delete")
def delete():
    return{"msg":"deleting the data"}

@app.put("/update")
def update():
    return{"msg":"updating the data"}
        
       


