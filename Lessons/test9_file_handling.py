# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 12:54:35 2026

@author: mmerc
"""

import json

# Exercise 1

students = [
    {
        "name": "Alice",
        "grade": 88
    },
    {
        "name": "Bob",
        "grade": 74
    }
]

with open("students.json","w") as file:
    
    json.dump(students, file, indent=4)

with open("students.json","r") as file:
    
    print(json.load(file))
    

