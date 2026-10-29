from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

students = {
    1: {
        "name": "Himansh",
        "age": 22,
        "course": "btech"
    },
    2: {
        "name": "Ravi",
        "age": 21,
        "course": "bca"
    }
}

class Student(BaseModel):
    name: str
    age: int
    course: str

class UpdateStudent(BaseModel):
    # name: Optional[str] = None
    # age: Optional[int] = None
    # course: Optional[str] = None
    name: str = None
    age: int = None
    course: str = None

@app.get("/") #this means home page
def index():
    return {"name": "Himansh"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    return students[student_id]

@app.get("/get-by-name")
def get_student(name: str = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student already exists"}
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student doesn't exist"}
    if student.name != None:
        students[student_id]['name'] = student.name
    if student.age != None:
        students[student_id]['age'] = student.age
    if student.course != None:
        students[student_id]['course'] = student.course
    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student doesn't exist"}
    del students[student_id]
    return {"Success": "Record deleted successfully!" }