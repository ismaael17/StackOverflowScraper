from flask import Flask, jsonify, request
from stackoverflow_scraper import get_questions

app = Flask(__name__)

# Endpoint to get a list of questions
@app.route('/questions', methods=['GET'])
def questions():
    tag = request.args.get('tag')
    questions = get_questions(tag)
    return jsonify(questions)


if __name__ == '__main__':
    app.run(debug=True)
