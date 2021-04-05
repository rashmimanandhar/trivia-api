# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 




Endpoints
```
GET '/categories'
GET '/questions?page=<page_number>'
POST '/questions'
POST '/questions/search'
DELETE '/questions/<question_id>'
GET '/categories/<category_id>/questions'
POST '/quizzes'
```

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Request Body: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
```
{
    '1' : "Science",
    '2' : "Art",
    '3' : "Geography",
    '4' : "History",
    '5' : "Entertainment",
    '6' : "Sports"
}

```

GET '/questions?page=<page_number>'
- Fetches a paginated list of questions in the system
- Request Arguments: page_number(Optional)
- Request Body: None
- Returns: A list of questions, 
  number of total questions, current category, categories. 
```
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "current_category": null,
    "questions": [
        {
            "answer": "AnsCurlJson",
            "category": 3,
            "difficulty": 3,
            "id": 25,
            "question": "QuesCurlJson"
        },
        {
            "answer": "Rashmi",
            "category": 4,
            "difficulty": 1,
            "id": 27,
            "question": "what is your name"
        },
        {
            "answer": "1945",
            "category": 4,
            "difficulty": 1,
            "id": 28,
            "question": "when did world war 2 end"
        }
    ],
    "success": true,
    "total_questions": 23
}
```
POST '/questions'
- Adds a new question to the list of questions
- Request Arguments: None
- Request Body: `{question: string, answer: string, difficulty: int, category: string<category_id>}`
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
```
{
    "created": 27,
    "success": true
}
```
POST '/questions/search'
- fetches all the questions where the substring matches the search term 
- Request Arguments: None
- Request Body: `{search_term: string}`
- Returns : Any questions for whom the search term 
  is a substring of the question. 
- For search_term = "tom"
```
{
    "questions": [
        {
            "answer": "Apollo 13",
            "category": 5,
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        }
    ],
    "success": true,
    "total_questions": 1
}
```
DELETE '/questions/<question_id>'
- Deletes the question of the question id
- Request Arguments: question_id
- Request Body: None
```
{
    "deleted": 27,
    "success": true
}
```
GET '/categories/<category_id>/questions'
- Retrives all the question of the given category
- Request Arguments: category_id
- Request Body: None
- Returns: A list of questions of that category, number of total questions, current category, categories.
```
{
    "categories": [
        {
            "id": 2,
            "type": "Art"
        },
        {
            "id": 5,
            "type": "Entertainment"
        },
        {
            "id": 3,
            "type": "Geography"
        },
        {
            "id": 4,
            "type": "History"
        },
        {
            "id": 1,
            "type": "Science"
        },
        {
            "id": 6,
            "type": "Sports"
        }
    ],
    "current_category": 4,
    "questions": [
        {
            "answer": "Maya Angelou",
            "category": 4,
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "Muhammad Ali",
            "category": 4,
            "difficulty": 1,
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?"
        },
        {
            "answer": "George Washington Carver",
            "category": 4,
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
        },
        {
            "answer": "Scarab",
            "category": 4,
            "difficulty": 4,
            "id": 23,
            "question": "Which dung beetle was worshipped by the ancient Egyptians?"
        },
        {
            "answer": "1945",
            "category": 4,
            "difficulty": 1,
            "id": 28,
            "question": "when did world war 2 end"
        }
    ],
    "success": true,
    "total_questions": 22
}
```

POST '/quizzes'
- Retrives a question that has not already been asked to play the quiz 
- Request Arguments: None
- Request Body: 
```
 {
     "previous_questions": [],
            "quiz_category":{
                "id": "1",
                "type": "Science"
                }
 }
```
- Returns: A question of the given category
```
{
    "question": {
        "answer": "The Liver",
        "category": 1,
        "difficulty": 4,
        "id": 20,
        "question": "What is the heaviest organ in the human body?"
    },
    "success": true
}
```


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```