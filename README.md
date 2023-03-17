# school-management-system
school management system




Introduction:
A school management system is an application designed to manage the school's day-to-day administrative tasks, such as student information management, attendance management, fee management, and other related tasks. In this project, we will build a basic school management system using Django Rest Framework (DRF). DRF is a powerful and flexible toolkit for building Web APIs, which makes it easier to build APIs quickly and efficiently.

Requirements:

Python 3.x
Django 3.x
Django Rest Framework (DRF)
PostgreSQL
Project Setup:

Create a new Django project using the command:
django-admin startproject school_management_system
Create a new Django app named "schools" using the command:
python manage.py startapp schools
Install DRF using the command: pip install djangorestframework
Create a new PostgreSQL database named "school_management_system".
Database Design:
We need two models for this project: School and Student.

The School model will have the following fields:

Name
Email
City
Pin Code
Password
The Student model will have the following fields:

Name
Username
Password
Grade (1-12)
School (Foreign Key to School model)
API Endpoints:

School Signup:

Endpoint: /api/v1/schools/signup/
Method: POST
Request Body:
perl
Copy code
{
    "name": "School Name",
    "email": "school@email.com",
    "city": "City",
    "pin_code": "123456",
    "password": "school_password"
}
Response Body:
perl
Copy code
{
    "school": {
        "id": 1,
        "name": "School Name",
        "email": "school@email.com",
        "city": "City",
        "pin_code": "123456"
    },
    "token": "<jwt_token>"
}
Student Bulk Creation:

Endpoint: /api/v1/students/bulk_create/
Method: POST
Request Body:
json
Copy code
{
    "students": [
        {
            "name": "Student Name 1",
            "username": "student1",
            "password": "student1_password",
            "grade": 8
        },
        {
            "name": "",
            "username": "student2",
            "password": "student2_password",
            "grade": 8
        },
        {
            "name": "Student Name 3",
            "username": "student3",
            "password": "student3_password",
            "grade": 9
        },
        {
            "name": "Student Name 4",
            "username": "student4",
            "password": "student4_password",
            "grade": 10
        }
    ]
}
Response Body:
json
Copy code
{
    "success": true
}
Login:

Endpoint: /api/v1/auth/login/
Method: POST
Request Body:
json
Copy code
{
    "username": "school_username_or_student_username",
    "password": "password"
}
Response Body:
json
Copy code
{
    "token": "<jwt_token>"
}
List and Filter Students:

Endpoint: /api/v1/students/
Method: GET
Query Parameters:
grade: Filter students by grade. (Optional)
school: Filter students by school. (Optional)
Response Body:
