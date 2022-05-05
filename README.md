​<div align ="center">

## <font size="7">**Course organizer**</font>

</div>
<br></br>
<div align ="center" >

<font size="6">Description </font>

</div>
<br></br>
<div align ="center" font size="4">
<font size="4">This is an API for a school, that allows instructors, facilitators and students to register, create courses, activities and
submit them. The technologies used were, Django, Django rest_framework and SQLite.

License: MIT</font>

</div>
<div align ="center" >

<font size="6">Base URL: </font>

</div>
<div align ="center">
<font size="4">/api</font>
</div>

<div align ="center">
 <font size="6">How to install</font>
</div>
​

<div align ="center" font size="4">
<font size="4">On your terminal, choose where you would like to clone the project, paste git clone paste_the_copy_link_here, then cd course.
Create a virtual environment: python -m venv venv, get inside the venv source venv/bin/activate, now install all dependencies:

pip install -r requirements.txt

Now let's create the database and the tables with this two commands:

python manage.py makemigrations

python manage.py migrate

In order to use this app you should use an application for API testing, like postman, insomnia, etc.</font>

</div>
<br></br>
<div align ="center">
<font size="6">Routes</font>
</div>
<br></br>
<div align ="center">

<font size="4">POST /accounts/</font>
<br></br>
<font size="4">Register users</font>

</div>

<font size="4">To create an student, pass is_superuser and is_staff as False, for an instructor pass is_superuser and is_staff as True, to create
a facilitator pass is_superuser as False and is_staff as True.</font>

​
<font color="caramel"> Request </font>

```json
{
  "username": "Dean",
  "password": "1234",
  "is_superuser": false,
  "is_staff": false
}
```

​
<font color="yellow"> _Response_ </font>
​

```json
{
  "id": 10,
  "username": "Dean",
  "is_superuser": false,
  "is_staff": false
}
```

<div align ="center">

<font size="4">POST /login/</font>
<br></br>
<font size="4">Login</font>

</div>
<font color="caramel"> Request </font>
​

```json
{
  "username": "Chris",
  "password": "Ni342ki"
}
```

<font color="caramel"> Response </font>
​

```json
{
  "token": "f1010393c1e863de87e757500219e2cf7c134f0d"
}
```

​

​<div align ="center">

<font size="4">POST /courses/</font>
<br></br>
<font size="4">Create a course</font>

</div>
<div align ="center">
<font size="4">You must be an instructor to create a course.</font>

</div>
<br></br>
<font color="caramel"> Request </font>
​

```json
{
  "name": "Literature"
}
```

​
<font color="yellow"> _Response_ </font>
​

```json
{
  "id": 6,
  "name": "Literature",
  "users": []
}
```

​​<div align ="center">

<font size="4">GET /courses/</font>
<br></br>
<font size="4">List of all courses</font>

</div>

<font color="caramel"> Response </font>

```json
{
  {
    "id": 2,
    "name": "Culinary",
    "users": []
  },
  {
    "id": 3,
    "name": "History",
    "users": []
  },
}
```

<br></br>

<div align ="center">

<font size="4">PUT /courses/<int:course_id>/</font>
<br></br>
<font size="4">Change a course name</font>
<br></br>
<font size="4">You must be an instructor to change the course name.</font>

</div>

<font color="caramel"> Request </font>

```json
{
  "name": "English"
}
```

​
<font color="yellow"> _Response_ </font>
​

```json
{
  "id": 2,
  "name": "English",
  "users": []
}
```

<br></br>

<div align ="center">

<font size="4">PUT /courses/<int:course_id>/registrations/</font>
<br></br>
<font size="4">Change the course students</font>
<br></br>
<font size="4">You must be an instructor to change the course students.</font>

</div>

<font color="caramel"> Request </font>

​

```json
{
  "user_ids": [3, 10]
}
```

​
<font color="yellow"> _Response_ </font>
​

```json
{
  "id": 2,
  "name": "English",
  "users": [
    {
      "id": 3,
      "username": "Rory"
    },
    {
      "id": 10,
      "username": "Dean"
    }
  ]
}
```

<br></br>

<div align ="center">

<font size="4">GET /courses/<int:course_id>/</font>
<br></br>
<font size="4">Return a specific course</font>

</div>

<font color="caramel"> Response </font>

```json
/api/courses/<int:course_id>/
```

```json
{
  "id": 1,
  "name": "Chemestry",
  "users": []
}
```

<br></br>

<div align ="center">

<font size="4">DELETE /courses/<int:course_id>/</font>
<br></br>
<font size="4">Delete a course</font>
<br></br>
<font size="4">You must be an instructor to delete a course.</font>

</div>

​
<font color="yellow"> _Response_ </font>
​

```json
NO CONTENT, 204
```

<br></br>

<div align ="center">

<font size="4">POST /activities/</font>
<br></br>
<font size="4">Create an activity</font>
<br></br>
<font size="4">You must be an instructor or a facilitator in order to create an activity.</font>

</div>

<font color="caramel"> _Request_ </font>
​

```json
{
  "title": "Write a 5 page essay about the second world war.",
  "points": 10
}
```

​
<font color="yellow"> _Response_ </font>
​

```json
{
  "id": 2,
  "title": "Write a 5 page essay about the second world war.",
  "points": 10,
  "submissions": []
}
```

<br></br>

<div align ="center">

<font size="4">GET /activities/</font>
<br></br>
<font size="4"> List all activities</font>
<br></br>
<font size="4">You must be an instructor or a facilitator in order to see all activities.</font>

</div>

<font color="yellow"> _Response_ </font>
​

```json
{
  {
    "id": 1,
    "title": "Write a 3 page essay about the first world war.",
    "points": 10,
    "submissions": []
  },
  {
    "id": 2,
    "title": "Write a 3 page essay about the great recession.",
    "points": 10,
    "submissions": []
  }
}
```

<br></br>

<div align ="center">

<font size="4">PUT /activities/<int:activity_id>/</font>
<br></br>
<font size="4"> Change the title and the points of an activity</font>
<br></br>
<font size="4">You must be an instructor or a facilitator in order to change an activity.</font>

</div>

<font color="caramel"> _Request_ </font>
​

```json
{
  "title": "Write a 3 page essay about the great recession.",
  "points": 10
}
```

​
<font color="yellow"> _Response_ </font>
​

```json
{
  "id": 2,
  "title": "Write a 3 page essay about the great recession.",
  "points": 10,
  "submissions": []
}
```

<br></br>

<div align ="center">

<font size="4">POST /activities/<int:activity_id>/submissions/</font>
<br></br>
<font size="4"> Submit an activity</font>
<br></br>
<font size="4">You must be a student in order to submit an activity.</font>

</div>

<font color="caramel"> _Request_ </font>
​

```json
{
  "repo": "gitlab.rory543"
}
```

​
<font color="yellow"> _Response_ </font>
​

```json
{
  "id": 2,
  "grade": null,
  "repo": "gitlab.rory543",
  "user_id": 4,
  "activity_id": 2
}
```

<br></br>

<div align ="center">

<font size="4">PUT /activities/<int:activity_id>/submissions/</font>

<br></br>
<font size="4"> Evaluate an activity submission.</font>
<br></br>
<font size="4">You must be an instructor or a facilitator in order evaluate an activity submission.</font>

</div>

<font color="caramel"> _Request_ </font>
​

```json
{
  "grade": 10
}
```

​
<font color="yellow"> _Response_ </font>
​

```json
{
  "id": 2,
  "grade": 10,
  "repo": "gitlab.rory543",
  "user_id": 4,
  "activity_id": 2
}
```

<br></br>

<div align ="center">

<font size="4">GET /submissions/</font>

<br></br>
<font size="4"> List all submissions</font>
<br></br>
<font size="4">You need a token to access this route, if the token is from a student, it'll show hers/his submissions, if it's
an instructor or a facilitator it'll list all student's submissions.</font>

</div>

<font color="yellow"> _Response_ </font>
​

```json
{
  {
    "id": 1,
    "grade": null,
    "repo": "gitlab.julmgc09",
    "user_id": 10,
    "activity_id": 2
  },
  {
    "id": 2,
    "grade": null,
    "repo": "gitlab.rory543",
    "user_id": 4,
    "activity_id": 2
  }
}
```
