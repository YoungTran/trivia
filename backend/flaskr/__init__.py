import os
import random

from flask import Flask, abort, jsonify, request
from flask.helpers import send_from_directory
from flask.templating import render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from models import Category, Question, setup_db

QUESTIONS_PER_PAGE = 10

# def create_app(test_config=None):
# create and configure the app
project_root = os.path.abspath(os.path.join(os.getcwd(), '..', 'frontend/build'))
print(project_root)
# BASE_DIR = os.path.abspath(os.path.join(os.path.dirname( app.instance_path ), '..', 'frontend/build'))
app = Flask(__name__, static_folder=project_root, template_folder=project_root)

# setup_db(app)


'''
@TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
'''
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if(path == ""):
        return send_from_directory(project_root, 'index.html')
    else:
        if(os.path.exists(os.path.join(project_root, path))):
            return send_from_directory(project_root, path)
        else:
            return send_from_directory(project_root, 'index.html')

'''
@TODO: Use the after_request decorator to set Access-Control-Allow
'''

'''
@TODO: 
Create an endpoint to handle GET requests 
for all available categories.
'''


'''
@TODO: 
Create an endpoint to handle GET requests for questions, 
including pagination (every 10 questions). 
This endpoint should return a list of questions, 
number of total questions, current category, categories. 

TEST: At this point, when you start the application
you should see questions and categories generated,
ten questions per page and pagination at the bottom of the screen for three pages.
Clicking on the page numbers should update the questions. 
'''

'''
@TODO: 
Create an endpoint to DELETE question using a question ID. 

TEST: When you click the trash icon next to a question, the question will be removed.
This removal will persist in the database and when you refresh the page. 
'''

'''
@TODO: 
Create an endpoint to POST a new question, 
which will require the question and answer text, 
category, and difficulty score.

TEST: When you submit a question on the "Add" tab, 
the form will clear and the question will appear at the end of the last page
of the questions list in the "List" tab.  
'''

'''
@TODO: 
Create a POST endpoint to get questions based on a search term. 
It should return any questions for whom the search term 
is a substring of the question. 

TEST: Search by any phrase. The questions list will update to include 
only question that include that string within their question. 
Try using the word "title" to start. 
'''

'''
@TODO: 
Create a GET endpoint to get questions based on category. 

TEST: In the "List" tab / main screen, clicking on one of the 
categories in the left column will cause only questions of that 
category to be shown. 
'''


'''
@TODO: 
Create a POST endpoint to get questions to play the quiz. 
This endpoint should take category and previous question parameters 
and return a random questions within the given category, 
if provided, and that is not one of the previous questions. 

TEST: In the "Play" tab, after a user selects "All" or a category,
one question at a time is displayed, the user is allowed to answer
and shown whether they were correct or not. 
'''

'''
@TODO: 
Create error handlers for all expected errors 
including 404 and 422. 
'''


if __name__ == '__main__':
  app.run()