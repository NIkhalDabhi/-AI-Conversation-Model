from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

class ConversationModel:
    def __init__(self, csv_file):
        self.questions = []
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.questions.append(row)

    def ask_question(self, question):
        return question

    def get_next_question(self, answer, user_answer, gender_value):
        for question in self.questions:
            if question['Question'] == answer:
                if answer == "AI : What is your gender ?":
                    if user_answer.lower() == 'male':
                        gender_value = 'M'
                    else:
                        gender_value = 'F'
                continue
            else:
                if gender_value == question['gender']:
                    return question['Question'], gender_value
        return None, None
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/conversation', methods=['GET', 'POST'])
def conversation():
    if request.method == 'POST':
        model = ConversationModel('C:/Users/nikha/Downloads/question.csv')
        current_question = 'AI : What is your name ?'
        gender = ''
        responses = []

        while current_question:
            responses.append({'question': current_question, 'answer': request.form['answer']})
            current_question, gender = model.get_next_question(current_question, request.form['answer'], gender)

        return render_template('index.html', responses=responses)

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
