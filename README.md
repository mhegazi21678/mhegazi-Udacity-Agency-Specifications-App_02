# Casting-Agency-Specifications

Casting Agency Specifications
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

Models:

Movies with attributes title and release date
Actors with attributes name, age and gender
Endpoints:
GET /actors and /movies
DELETE /actors/ and /movies/
POST /actors and /movies and
PATCH /actors/ and /movies/
Roles:
Casting Assistant
Can view actors and movies
Casting Director
All permissions a Casting Assistant has and…
Add or delete an actor from the database
Modify actors or movies
Executive Producer
All permissions a Casting Director has and…
Add or delete a movie from the database
Tests:
One test for success behavior of each endpoint
One test for error behavior of each endpoint
At least two tests of RBAC for each role

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

```bash
pip install virtualenv
virtualenv --no-site-packages env
source env/bin/activate
```

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
When testing locally, models.py should be:
```python
# database_path = os.environ['DATABASE_PATH']

database_filename = "database.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))
```
When testing on heroku, models.py should be:
```python
database_path = os.environ['DATABASE_PATH']

# database_filename = "database.db"
# project_dir = os.path.dirname(os.path.abspath(__file__))
# database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))
```

From the working folder in terminal run:
```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

## Running the server locally

To run the server, execute:

```bash
python app.py
```

## Running the server on heroku

I have already deployed the API in heroku and can use it directly. The host is:

https://mhegaziagencyspecifications.herokuapp.com/actors

The token is in the `setup.sh`, you can test the API like this:

```bash
source setup.sh
curl -H "Authorization: Bearer ${CASTINGASSISTANT_TOKEN}" https://mhegaziagencyspecifications.herokuapp.com/actors | jq 
```


## API document
```
Endpoints
GET '/actors'
POST '/actors'
PATCH '/actors/<actor_id>'
DELETE '/actors/<actor_id>'
GET '/movies'
POST '/movies'
PATCH '/movies/<movie_id>'
DELETE '/movies/<movie_id>'


GET '/actors'
- Get all actors' information
- Request Arguments: None
- Returns: A list contains all the actors' info.
http://127.0.0.1:5000/actors
{
    "actors": [
        {
            "age": 30,
            "gender": "Female",
            "id": 2,
            "name": "Sawsan Hetto"
        },
        {
            "age": 75,
            "gender": "Male",
            "id": 3,
            "name": "Adel Emam"
        },
        {
            "age": 42,
            "gender": "Male",
            "id": 1,
            "name": "Saleem Aaga"
        },
        {
            "age": 46,
            "gender": "Female",
            "id": 4,
            "name": "Hanan Tork"
        },
        {
            "age": 51,
            "gender": "Male",
            "id": 5,
            "name": "Ahmed Helmy"
        },
        {
            "age": 48,
            "gender": "Male",
            "id": 6,
            "name": "Ahmed El Sakka"
        },
        {
            "age": 32,
            "gender": "Male",
            "id": 7,
            "name": "Mohamed Ramadan"
        },
        {
            "age": 41,
            "gender": "Female",
            "id": 8,
            "name": "Hend Sabry"
        },
        {
            "age": 36,
            "gender": "Female",
            "id": 9,
            "name": "Donia Samir Ghanem"
        },
        {
            "age": 55,
            "gender": "Female",
            "id": 10,
            "name": "Ghada Abdel Razek"
        },
        {
            "age": 41,
            "gender": "Female",
            "id": 11,
            "name": "Yasmin Abdulaziz"
        },
        {
            "age": 44,
            "gender": "Female",
            "id": 12,
            "name": "Mona Zaki"
        },
        {
            "age": 41,
            "gender": "Female",
            "id": 13,
            "name": "Mai Ezz Eldin"
        },
        {
            "age": 38,
            "gender": "Female",
            "id": 14,
            "name": "Mais Hamdan"
        },
        {
            "age": 34,
            "gender": "Female",
            "id": 15,
            "name": "Ayten Amer"
        },
        {
            "age": 39,
            "gender": "Female",
            "id": 16,
            "name": "Nesreen Tafesh"
        },
        {
            "age": 95,
            "gender": "Male",
            "id": 17,
            "name": "Sameer Ganem"
        },
        {
            "age": 35,
            "gender": "Female",
            "id": 18,
            "name": "Nancy Ajram"
        },
        {
            "age": 49,
            "gender": "Female",
            "id": 19,
            "name": "Elissa"
        },
        {
            "age": 63,
            "gender": "Male",
            "id": 20,
            "name": "Kadim Al Shahir"
        },
        {
            "age": 55,
            "gender": "Female",
            "id": 21,
            "name": "Najwa Karam"
        },
        {
            "age": 51,
            "gender": "Female",
            "id": 22,
            "name": "Assala Nasri"
        },
        {
            "age": 53,
            "gender": "Female",
            "id": 23,
            "name": "Ahlam Al Shamsi"
        },
        {
            "age": 58,
            "gender": "Male",
            "id": 24,
            "name": "Ragheb Alama"
        },
        {
            "age": 59,
            "gender": "Male",
            "id": 25,
            "name": "Georges Wassouf"
        },
        {
            "age": 43,
            "gender": "Male",
            "id": 26,
            "name": "Tamer Hosny"
        },
        {
            "age": 11,
            "gender": "Male",
            "id": 27,
            "name": "Saeed Hegazi"
        }
    ],
    "success": true
}

POST '/actors'
- Add a actor
- Request Arguments: name, age, gender
{
            "age": 11,
            "gender": "Male",
            "name": "Saeed Hegazi"
}
- Returns: The actor info which we added with this request.
{
    "actors": {
        "age": 11,
        "gender": "Male",
        "id": 27,
        "name": "Saeed Hegazi"
    },
    "success": true
}

PATCH '/actors/<actor_id>'
- Update a actor's information
- Request Arguments: name, age, gender
        {
            "age": 51,
            "gender": "Male",
            "name": "Ahmad Helmy"
        }
- Returns: The actor info which we updated with this request.
http://127.0.0.1:5000/actors/5
{
    "actors": {
        "age": 51,
        "gender": "Male",
        "id": 5,
        "name": "Ahmad Helmy"
    },
    "success": true
}

DELETE '/actors/<actor_id>'
- Delete a actor
- Request Arguments: actor_id
- Returns: The id of the actor which was deleted 
http://127.0.0.1:5000/actors/10
{
    "actors": "10",
    "success": true
}

# ****************************************************************************************************** #

GET '/movies'
- Get all movies' information
- Request Arguments: None
- Returns: A list contains all the movies' info.
http://127.0.0.1:5000/movies
{
    "movies": [
        {
            "id": 2,
            "release_date": "1982-04-22",
            "title": "Hanafe el Obaha"
        },
        {
            "id": 1,
            "release_date": "1978-06-21",
            "title": "my story"
        },
        {
            "id": 3,
            "release_date": "2014-01-01",
            "title": "Theeb"
        },
        {
            "id": 4,
            "release_date": "2011-01-01",
            "title": "Broken Cameras"
        },
        {
            "id": 5,
            "release_date": "2018-01-01",
            "title": "The Day I Lost My Shadow"
        },
        {
            "id": 6,
            "release_date": "2009-01-01",
            "title": "The Time That Remains"
        },
        {
            "id": 7,
            "release_date": "2009-01-01",
            "title": "Amreeka"
        },
        {
            "id": 8,
            "release_date": "2015-01-01",
            "title": "Very Big Shot"
        },
        {
            "id": 9,
            "release_date": "2007-01-01",
            "title": "Under the Bombs"
        },
        {
            "id": 10,
            "release_date": "2009-05-01",
            "title": "Ajami"
        },
        {
            "id": 11,
            "release_date": "2017-09-23",
            "title": "Photocopy"
        },
        {
            "id": 12,
            "release_date": "2016-07-15",
            "title": "Barakah Meets Barakah"
        },
        {
            "id": 13,
            "release_date": "2012-08-10",
            "title": "Wadjda"
        },
        {
            "id": 14,
            "release_date": "2011-05-20",
            "title": "Where Do We Go Now"
        },
        {
            "id": 15,
            "release_date": "2017-02-04",
            "title": "Sheikh Jackson"
        },
        {
            "id": 16,
            "release_date": "2016-01-09",
            "title": "Clash"
        },
        {
            "id": 17,
            "release_date": "2016-09-09",
            "title": "Blessed Benefit"
        },
        {
            "id": 18,
            "release_date": "2015-10-01",
            "title": "Very Big Shot"
        },
        {
            "id": 19,
            "release_date": "2016-10-01",
            "title": "Six Windows in the Desert"
        },
        {
            "id": 21,
            "release_date": "2013-11-11",
            "title": "Villa 69"
        },
        {
            "id": 22,
            "release_date": "1955-05-01",
            "title": "Qaser el Shoq"
        }
    ],
    "success": true
}

POST '/movies'
- Add a movie
- Request Arguments: title, release_date
        {
            "release_date": "1955-05-01",
            "title": "Qaser el Shoq"
        }
- Returns: The movie info which we added with this request.
POST: http://127.0.0.1:5000/movies
{
    "movies": {
        "id": 22,
        "release_date": "1955-05-01",
        "title": "Qaser el Shoq"
    },
    "success": true
}


PATCH '/movies/<movie_id>'
- Update a movie's information
- Request Arguments: title, release_date
        {
            "release_date": "2018-10-10",
            "title": "The Day I Lost My Shadow"
        }
- Returns: The movie info which we updated with this request.
http://127.0.0.1:5000/movies/5
{
    "movies": {
        "id": 5,
        "release_date": "2018-10-10",
        "title": "The Day I Lost My Shadow"
    },
    "success": true
}


DELETE '/movies/<movie_id>'
- Delete a movie
- Request Arguments: movie_id
- Returns: The id of the movie which was deleted 
http://127.0.0.1:5000/movies/10
{
    "movies": "10",
    "success": true
}
```

## Testing
To run the tests, run

```python
pytest test_app.py
```

