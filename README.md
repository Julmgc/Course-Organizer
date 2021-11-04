## <font size="7">**Kanvas**</font>

​

```json
This is an app for a school, that allows instructors, facilitators and students to register, create courses, activities and
submit them. The technologies used were, Django, Django rest_framework and SQLite.

License: MIT

```

## <font size="4">Base URL: </font>

## <font size="3">/api </font>

<br></br>

## <font size="3"> How to install </font>

​

```json
On your terminal, choose where you would like to clone the project, paste git clone paste_the_copy_link_here, then cd kanvas.
Create a virtual environment: python -m venv venv, get inside the venv source venv/bin/activate, now install all dependencies:

pip install -r requirements.txt

Now let's create the database and the tables with this two commands:

python manage.py makemigrations

python manage.py migrate

In order to use this app you should use an application for API testing, like postman, insomnia, etc.

```

## <font size="6">Routes</font>

### <font color="gree"> POST </font> Register

​

```json
/api/accounts/
```

<font color="caramel"> _Request_ </font>

```json
To create an student, pass is_superuser and is_staff as False, for an instructor pass is_superuser and is_staff as True, to create
a facilitator pass is_superuser as False and is_staff as True.
```

​

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

### <font color="gree"> POST </font> Login

​

```json
/api/login
```

<font color="caramel"> _Request_ </font>
​

```json
{
  "token": "f1010393c1e863de87e757500219e2cf7c134f0d"
}
```

​

### <font color="gree"> POST </font> Create a course

​

```json
freeladev.com/api/login
```

```json
You must be an instructor to create a course.
```

<font color="caramel"> _Request_ </font>
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

### <font color="purple"> GET </font> List of all courses **\***

​

```json
/api/courses
```

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

### <font color="gree"> PUT </font> Change a course name

​

```json
/api/courses/<int:course_id>/
```

```json
You must be an instructor to change the course name.
```

<font color="caramel"> _Request_ </font>
​

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

### <font color="gree"> PUT </font> Change the course students

​

```json
/api/courses/<int:course_id>/registrations/
```

```json
You must be an instructor to change the course students.
```

<font color="caramel"> _Request_ </font>
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

### <font color="purple"> GET </font> list a specific course

​

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

### <font color="gree"> DELETE </font> Delete a course

​

```json
/api/courses/<int:course_id>/
```

```json
You must be an instructor to delete a course.
```

​
<font color="yellow"> _Response_ </font>
​

```json
NO CONTENT, 204
```

### <font color="gree"> POST </font> Create an activity

​

```json
/api/activities/
```

```json
You must be an instructor or a facilitator in order to create an activity.
```

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

### <font color="purple"> GET </font> List all activities

​

```json
/api/activities/
```

```json
You must be an instructor or a facilitator in order to create an activity.
```

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

### <font color="gree"> PUT </font> Change the title and the points of an activity

​

```json
/api/activities/<int:activity_id>/
```

```json
You must be an instructor or a facilitator in order to create an activity.
```

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

### <font color="gree"> POST </font> Submit an activity

​

```json
/api/activities/
```

```json
You must be a student in order to submit an activity.
```

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

### <font color="gree"> PUT </font> Evaluate an activity submission.

​

```json
/api/submissions/>int:submission_id>/
```

```json
You must be an instructor or a facilitator in order evaluate an activity submission.
```

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

### <font color="purple"> GET </font> List all submissions

​

```json
/api/submissions/
```

```json
You need a token to access this route, if the token is from a student, it'll show hers/his submissions, if it's
an instructor or facilitator it'll list all student's submissions.
```

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
