# -*- coding: utf-8 -*-
"""
Created on Wed May 23 12:23:51 2018

@author: Lenovo
"""
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 10:28:37 2018

@author: Lenovo
"""
import requests
from pymongo import MongoClient
from datetime import datetime
#import json

client = MongoClient('localhost', 27017)
mydb = client.db_University

def add_client(student_name, student_age, student_email, student_roll_number,student_branch):
    unique_client = mydb.forsk_clients.find_one({"student Roll":student_roll_number}, {"_id":0})
    if unique_client:
        return "Client already exists"
    else:
        mydb.forsk_clients.insert(
                {
                "Student Name" : student_name,
                "Student Age" : student_age,
                "Student Email" : student_email,
                "Roll Number" : student_roll_number,
                "S_Branch" : student_branch,
                "Date-Time" : datetime.now()
                })
        return "Student added successfully"

def view_client(student_roll_number):
    user = mydb.forsk_clients.find_one({"Roll Number":student_roll_number}, {"_id":0})
    if user:
        student = user["Student Name"]
        Age = user["Student Age"]
        email = user["Student Email"]
        Roll_number = user["Roll Number"]
        Branch = user["S_Branch"]
        time = user["Date-Time"]
        return {"Student Name":student,"Student Age":Age,"Student Email":email,"Roll Number":Roll_number,"S_Branch":Branch}
    else:
        return "Sorry, No such user exists"


student_name = input("Enter Student Name: ")
student_age = input("Enter age: ")
student_email = input("Enter student Email: ")
student_roll_number = input("Enter Roll Number: ")
student_branch = input("Enter Branch: ")

print(add_client(student_name, student_age, student_email, student_roll_number,student_branch))

user = input("Enter Student Roll to find: ")
user_data = view_client(user)

print( user_data)
url2 = 'https://api.mlab.com/api/1/databases/forsk_1/collections/student?apiKey=MHLx2UluHewnBnQetNlO4ZI2y_jl-BPs'
r = requests.post(url2, json=user_data)
print (r.text)



