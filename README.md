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

## API Calls Using Postman

##### 1. First Step Is to create new User 

API Call - http://localhost:8000/api/register/  <br/>
method - POST <br/>
body = { <br/>
    "username" : "username_value", <br/>
    "password" : "user_password", <br/>
    "email" : "user_email" <br/>
}

![](img/1.png)


##### 2. Generating Token for API authentication

API Call - http://localhost:8000/api-token-auth/ <br/>
method - POST <br/>
body = { <br/>
    "username" : "username_value", <br/>
    "password" : "user_password", <br/>
} 

Output - Token 

![](img/2.png)


##### 3. Create New Course

API Call - http://localhost:8000/api/course/course-create/ <br/>
method - POST <br/>
header = { "Authorization": "Token token_from_above_step"} <br/>
body = { <br/>
    "name" : "Database", <br/>
    "information" : "some information", <br/>
} 

![](img/3.png)


##### 4. Create New Course

API Call - http://localhost:8000/api/course/course-create/ <br/>
method - POST <br/>
header = { "Authorization": "Token token_from_above_step"} <br/>
body = { <br/>
    "name" : "Database", <br/>
    "information" : "some information", <br/>
} 

![](img/4.png)


##### 5. Create New Student

API Call - http://localhost:8000/api/student/student-create/ <br/>
method - POST <br/>
header = { "Authorization": "Token token_from_above_step"} <br/>
body = { <br/>
    "first_name" : "alice", <br/>
    "last_name" : "evans", <br/>
} 

![](img/5.png)


##### 6. Retrieve Single Course Data

API Call - http://localhost:8000/api/course/course-detail/<course_id>/ <br/>
method - GET <br/>
header = { "Authorization": "Token token_from_above_step"} <br/>

![](img/6.png)


##### 7. Update Course Data

API Call - http://localhost:8000/api/course/course-update/<course_id>/ <br/>
method - POST <br/>
header = { "Authorization": "Token token_from_above_step"} <br/>
body = { <br/>
    "course_id" : 1, <br/>
    "name" : "database", <br/>
    "information" : "database", <br/>
} 

![](img/7.png)


##### 8. Delete Course Data

API Call - http://localhost:8000/api/course/course-delete/<course_id>/ <br/>
method - DELETE <br/>
header = { "Authorization": "Token token_from_above_step"} <br/>

![](img/8.png)


##### 9. Show students related to specific course

API Call - http://localhost:8000/api/course/<course_id>/student/ <br/>
method - GET <br/>
header = { "Authorization": "Token token_from_above_step"} <br/>

![](img/9.png)


##### 10. Add student related to specific course

API Call - http://localhost:8000/api/course/<course_id>/student/add/ <br/>
method - POST <br/>
header = { "Authorization": "Token token_from_above_step"} <br/>
body = { <br/>
    "student" : 1, <br/>
} 

![](img/10.png)


##### 11. Delete student related to specific course

API Call - http://localhost:8000/api/course/<course_id>/student/<student_id>/ <br/>
method - DELETE <br/>
header = { "Authorization": "Token token_from_above_step"} <br/>

![](img/11.png)


##### 12. Retrieve Student List

API Call - http://localhost:8000/api/student/ <br/>
method - GET <br/>
header = { "Authorization": "Token token_from_above_step"} <br/>

![](img/12.png)


##### 13. Retrieve Single Student Data

API Call - http://localhost:8000/api/student/student-detail/<student_id>/ <br/>
method - GET <br/>
header = { "Authorization": "Token token_from_above_step"} <br/>

![](img/13.png)


##### 14. Update Single Student Data

API Call - http://localhost:8000/api/student/student-update/<student_id>/ <br/>
method - POST <br/>
header = { "Authorization": "Token token_from_above_step"} <br/>
body = { <br/>
    "student_id" : 1, <br/>
    "first_name" : "alice", <br/>
    "last_name" : "evans", <br/>
} 

![](img/14.png)


##### 15. Delete Single Student Data

API Call - http://localhost:8000/api/student/student-delete/<student_id>/ <br/>
method - DELETE <br/>
header = { "Authorization": "Token token_from_above_step"} <br/>

![](img/15.png)


##### 16. Show course associated to specific student

API Call - http://localhost:8000/api/student/<student_id>/course/ <br/>
method - GET <br/>
header = { "Authorization": "Token token_from_above_step"} <br/>

![](img/16.png)


##### 17. Add course associated to specific student

API Call - http://localhost:8000/api/student/<student_id>/course/add/ <br/>
method - POST <br/>
header = { "Authorization": "Token token_from_above_step"} <br/>
body = { <br/>
    "course" : 7 <br/>
}  

![](img/17.png)


##### 18. Delete course associated to specific student

API Call - http://localhost:8000/api/student/<student_id>/course/<course_id>/ <br/>
method - DELETE <br/>
header = { "Authorization": "Token token_from_above_step"} <br/>

![](img/18.png)


## Note: 

In the document provided it was mentioned that the Student Id and Course Id should be automatically incremented numerical values,
that's why I added these fields in the model. 