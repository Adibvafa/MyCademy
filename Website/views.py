from flask import Blueprint, redirect, render_template, request, flash, jsonify, url_for
# from flask_login import login_required, current_user
# from .models import Note
# from . import db
# from sqlalchemy.sql import func
import json
import string

from .Creator import Create_Course
from .Get_Question import Get_Question
from .Chat import Answer_Question
from .Summarize import Create_Summary
import random

# courseText
# quizQuestions
# response
# summary
# images

prompt = "default"
courseParagraphs = []
courseImages = []
courseHeaders = []

# usually easier to keep the name the same as the file
views = Blueprint('views', __name__)

# homepage


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form.get('query')
        print(query)

        if len(query) < 1:
            flash('Query is too short!', category="error")
        else:
            global prompt, courseParagraphs, courseImages, courseHeaders
            prompt = string.capwords(query, sep=None)

            temp, courseImages = Create_Course(query)

            for i in range(len(temp)):
                courseHeaders.append(temp[i][:temp[i].find(':') + 1])
                courseParagraphs.append(temp[i][temp[i].find(':') + 1:])

            return redirect(url_for('views.query'))
            # new_note = Note(data=note, user_id=current_user.id)
            # print(current_user.id)
            # db.session.add(new_note)
            # db.session.commit()
            # flash("Note added!")

    return render_template("home.html")


@views.route('/query', methods=['GET', 'POST'])
def query():
    return render_template('query.html', prompt=prompt, courseParagraphs=courseParagraphs, courseImages=courseImages, courseHeaders=courseHeaders)


@views.route('/generate-response', methods=['POST'])
def generate_response():
    prompt = json.loads(request.data)
    promptText = prompt['text']
    print(promptText)
    return jsonify({"resp": Answer_Question(promptText)})


@views.route('/generate-summary', methods=['POST'])
def generate_summary():
    # prompt = json.loads(request.data)
    # promptText = prompt['text']
    # print(promptText)
    return jsonify({"resp": Create_Summary(courseParagraphs)})


@views.route('/generate-quiz', methods=['POST'])
def generate_quiz():
    # prompt = json.loads(request.data)
    # promptText = prompt['text']
    # print(promptText)

    # return jsonify({"question": "What are the first 10 digits of pi?", "answer": "3.141592653", "reference": 3})
    question = get_question(courseParagraphs)
    print(question)
    return jsonify({"question": question["question"], "reference": question["reference"], "answer": question["answer"]})