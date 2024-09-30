from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY', 'default_secret_key')

# Questions and support mapping
questions = [
    "Do you feel physically able to do this activity?",
    "Do you feel like you know how to do this or have the skills you need?",
    "Do you have everything you need to make this change, like the right tools or environment?",
    "Do you have support from friends, family, or others to help you do this?",
    "Do you believe this change is important for you and that it fits with your values or goals?",
    "Do you feel motivated or have a natural drive to do this, or does it feel more like a struggle?"
]

support_options = {
    0: ["Physical Exercises or Movement Suggestions", "Adapting the Task", "Breaking It Down into Steps"],
    1: ["Clear, Simple Instructions", "Learning Resources", "Practical Tips", "Practicing Together"],
    2: ["Help Finding Resources", "Making Your Environment Easier"],
    3: ["Working Out Who Can Support You", "Connecting with Supportive Groups", "Accountability Buddy"],
    4: ["Talking About Your Goals", "Setting Personal Goals", "Looking at Benefits", "Sharing Helpful Information"],
    5: ["Creating Small Daily Habits", "Rewarding Yourself", "Talking About Emotional Barriers", "Imagining Success"]
}

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/reflection', methods=['POST', 'GET'])
def reflection():
    if request.method == 'POST':
        reflection_text = request.form.get('reflection', '').strip()

        # Check if the reflection field is empty
        if not reflection_text:
            flash('Error: Please fill out this field.', 'error')  # Short and brief error message
            return render_template('reflection.html')

        session['reflection'] = reflection_text
        # Clear previous responses if starting fresh
        session['responses'] = []  # Initialize the list of responses
        return redirect(url_for('get_question', question_index=0))
    return render_template('reflection.html')


@app.route('/questions/<int:question_index>', methods=['POST', 'GET'])
def get_question(question_index):
    if request.method == 'POST':
        answer = request.form.get('answer')

        # Store user responses in session
        if 'responses' not in session:
            session['responses'] = []

        session['responses'].append((questions[question_index], answer))

        # If the user answers 'Yes', move to the next question
        if answer == "yes":
            if question_index + 1 < len(questions):
                return redirect(url_for('get_question', question_index=question_index + 1))
            else:
                return redirect(url_for('reflective'))
        else:
            # If the user answers 'No', redirect them to the support page for the current question
            return redirect(url_for('show_supports', question_index=question_index))

    return render_template('questions.html', question=questions[question_index], question_index=question_index)

@app.route('/supports/<int:question_index>', methods=['POST', 'GET'])
def show_supports(question_index):
    if request.method == 'POST':
        # Capture selected supports
        selected_supports = request.form.getlist('supports')

        if 'selected_supports' not in session:
            session['selected_supports'] = []

        session['selected_supports'].extend(selected_supports)

        # Store the 'No' response with the selected supports
        if 'responses' not in session:
            session['responses'] = []

        session['responses'].append({
            'question': questions[question_index],
            'answer': 'no',
            'supports': selected_supports
        })

        # After selecting supports, move to the next question
        if question_index + 1 < len(questions):
            return redirect(url_for('get_question', question_index=question_index + 1))
        else:
            return redirect(url_for('reflective'))

    return render_template('show_supports.html', supports=support_options[question_index], question_index=question_index)

@app.route('/reflective', methods=['POST', 'GET'])
def reflective():
    reflection = session.get('reflection', '')
    responses = session.get('responses', [])
    selected_supports = session.get('selected_supports', [])

    # Render all the questions and their answers, along with the supports selected.
    relevant_responses = [
        {
            'question': response['question'],
            'supports': response['supports'] if response['answer'] == 'no' else "No additional support needed"
        }
        for response in responses
    ]

    return render_template(
        'reflective.html',
        reflection=reflection,
        relevant_responses=relevant_responses,
        selected_supports=selected_supports
    )

@app.route('/finish', methods=['POST', 'GET'])
def finish():
    session.clear()
    return redirect(url_for('welcome'))


if __name__ == '__main__':
    app.run(debug=True)
