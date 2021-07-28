![](https://github.com/harshvardhan0709/django_surf/workflows/Django%20Surf/badge.svg)

# Django Surf

Created a Django application that provide a rest API to manage students, courses and students in courses in a many to many relationship.

## Running Django Surf Locally

Command:

 ```bash
 
 git clone https://github.com/harshvardhan0709/django_surf.git

 cd django_surf

 docker-compose build 

 docker-compose up

 ```




##### 1. First Step Is to create new User 

Api call - http://localhost:8000/api/register/  <br/>
method - POST <br/>
body = { <br/>
    "username" : "username_value", <br/>
    "password" : "user_password", <br/>
    "email" : "user_email" <br/>
}

![](img/1.png)



##### 2. Generating Token for API authentication

Api call - http://localhost:8000/api-token-auth/ <br/>
method - POST <br/>
body = { <br/>
    "username" : "username_value", <br/>
    "password" : "user_password", <br/>
} 

Output - Token 

![](img/2.png)



##### 3. Create New Course

Api call - http://localhost:8000/api/course/course-create/ <br/>
method - POST <br/>
header = { "Authorization": "Token token_from_above_step"} <br/>
body = { <br/>
    "name" : "Database", <br/>
    "information" : "some information", <br/>
} 

![](img/3.png)


