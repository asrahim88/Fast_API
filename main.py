from fastapi import FastAPI, Path, HTTPException
import json


app = FastAPI()

def loadData():
    with open("students.json", "r") as f:
        data  = json.load(f)
        return data

@app.get("/")
def hello():
    return "Student management System API"

@app.get("/about")
def about():
    return "A fully functional API to manage our students records."

@app.get("/view")
def view():
    data = loadData()
    return data

@app.get("/view/{student_id}")
def view_student_by_id(student_id: str = Path(...,  description= "Student id of the student.", example= "S001")):
    data = loadData()
    
    print(len(data))
    
    if student_id.upper() in data:
        return data[student_id.upper()]
    else:
        raise HTTPException(status_code=400, detail="Student Not Found")
        
        
