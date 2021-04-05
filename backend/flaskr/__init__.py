import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import sys
import traceback
from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, selection):
    page = request.args.get("page", 1, type=int)
    print(page)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    questions = [question.format() for question in selection]
    current_questions = questions[start:end]
    return current_questions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    """
    @TODO:
    Set up CORS. Allow '*' for origins.
    Delete the sample route after completing the TODOs
    """
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type, Authorization, true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods",
            "GET, POST, PUT, PATCH, DELETE, OPTIONS"
        )
        return response

    @app.route("/categories")
    def retrieve_categories():
        categories = Category.query.order_by(Category.type).all()
        formatted_categories =
        {category.id: category.type for category in categories}
        if len(categories) == 0:
            abort(404)
        return jsonify(
            {
                "success": True,
                "categories": formatted_categories,
                "total_categories": len(categories),
            }
        )

    @app.route("/questions")
    def retrieve_questions():
        selection = Question.query.order_by(Question.id).all()
        current_questions = paginate_questions(request, selection)

        categories = Category.query.order_by(Category.type).all()
        formatted_categories =
        {category.id: category.type for category in categories}
        if len(current_questions) == 0:
            abort(404)
        return jsonify(
            {
                "success": True,
                "questions": current_questions,
                "total_questions": len(Question.query.all()),
                "current_category": None,
                "categories": formatted_categories,
            }
        )

    @app.route("/questions/<int:question_id>", methods=["DELETE"])
    def delete_questions(question_id):
        try:
            question =
            Question.query.filter(Question.id == question_id).one_or_none()
            question.delete()
            return jsonify({"success": True, "deleted": question_id})
        except:
            abort(422)

    @app.route("/questions", methods=["POST"])
    def post_questions():
        body = request.get_json()
        if not (
            "question" in body and
            "answer" in body and
            "difficulty" in body and
            "category" in body
        ):
            abort(422)
        new_question = body.get("question", None)
        new_answer = body.get("answer", None)
        new_category = body.get("category", None)
        new_difficulty_score = body.get("difficulty", None)

        try:
            question = Question(
                question=new_question,
                answer=new_answer,
                category=new_category,
                difficulty=new_difficulty_score,
            )
            question.insert()

            return jsonify({"success": True, "created": question.id})
        except:
            e = sys.exc_info()[0]
            traceback.print_exc()
            abort(422)

    @app.route("/questions/search", methods=["POST"])
    def search_questions():
        body = request.get_json()

        if not ("search_term" in body):
            abort(400)

        search_term = body.get("search_term", None)

        try:
            search_results = Question.query.filter(
                Question.question.ilike("%{}%".format(search_term))
            ).all()

            return jsonify(
                {
                    "success": True,
                    "questions":
                    [question.format() for question in search_results],
                    "total_questions": len(search_results),
                }
            )
        except:
            abort(422)

    @app.route("/categories/<int:category_id>/questions")
    def retrieve_questions_by_category(category_id):
        selection = Question.query.filter(
          Question.category == category_id).all()
        current_questions = paginate_questions(request, selection)

        categories = Category.query.order_by(Category.type).all()

        if len(current_questions) == 0:
            abort(404)
        return jsonify(
            {
                "success": True,
                "questions": current_questions,
                "total_questions": len(Question.query.all()),
                "current_category": category_id,
                "categories": [category.format() for category in categories],
            }
        )

    @app.route("/quizzes", methods=["POST"])
    def play_quiz():
        body = request.get_json()
        try:
            if not ("quiz_category" in body and "previous_questions" in body):
                abort(400)

            category = body.get("quiz_category")
            previous_questions = body.get("previous_questions")
            if category["id"] == 0:
                available_questions = Question.query.filter(
                    Question.id.notin_((previous_questions))
                ).all()
            else:
                available_questions = (
                    Question.query.filter_by(category=category["id"])
                    .filter(Question.id.notin_((previous_questions)))
                    .all()
                )

            if len(available_questions) > 0:
                new_question = available_questions[
                    random.randrange(0, len(available_questions))
                ].format()
            else:
                new_question = None

            return jsonify({"success": True, "question": new_question})
        except:
            abort(422)

    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify({
              "success": False,
              "error": 404,
              "message": "resource not found"
            }),
            404,
        )

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
              "success": False,
              "error": 422,
              "message": "unprocessable entity"
              }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
          "success": False,
          "error": 400,
          "message": "bad request"
          }), 400

    @app.errorhandler(405)
    def bad_request(error):
        return jsonify({
              "success": False,
              "error": 405,
              "message": "method not allowed"
              }), 405

    @app.errorhandler(500)
    def bad_request(error):
        return jsonify({
              "success": False,
              "error": 500,
              "message": "internal server error"}
            ), 500

    return app
