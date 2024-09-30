from flask import Flask, render_template, request, redirect, url_for
import time  # Simulating processing time

app = Flask(__name__)

# Sample storage for user responses
responses = {
    'behavioral_goal': '',
    'barriers': []
}

questions = [
    "What behavior are you trying to change or adopt?",
    "What are some things in your life that you’re thinking about changing or improving?",
    "What physical challenges might you face?",
    "What parts of this change feel unclear or difficult for you?",
    "What about your environment or routine might help or make it harder to succeed with this change?",
    "Who in your life do you feel could support you in making this change, either practically or emotionally?",
    "How does this change fit with the bigger picture of what’s important to you in life?",
    "What tends to get in the way of you feeling motivated to take action?"
]

# Route for the question page
@app.route('/question/<int:question_number>', methods=['GET', 'POST'])
def question_page(question_number):
    if request.method == 'POST':
        answer = request.form['answer']
        if question_number == 1:
            responses['behavioral_goal'] = answer
        else:
            responses['barriers'].append(answer)

        if question_number < len(questions):
            return redirect(url_for('question_page', question_number=question_number + 1))
        else:
            return redirect(url_for('summary_page'))

    return render_template('question.html', question_number=question_number, 
                           question=questions[question_number - 1], 
                           progress_percent=(question_number / len(questions)) * 100, 
                           questions=questions)

# Route for the summary page
@app.route('/summary')
def summary_page():
    return render_template('summary.html', 
                           behavioral_goal=responses['behavioral_goal'], 
                           barriers=responses['barriers'])

# Route for Welcome page
@app.route('/')
def welcome():
    # Reset responses to start fresh
    responses['behavioral_goal'] = ''
    responses['barriers'] = []
    
    return render_template('welcome.html')

# Route for Get Started (shows loading, then feedback)
@app.route('/loading')
def loading():
    # Show loading page while processing
    return render_template('loading.html')

@app.route('/start')
def start():
    # Simulate analysis time (you can remove this in production)
    time.sleep(3)  # Simulating delay for processing

    # Trigger the analysis function here
    feedback = analyze_responses(responses)
    return render_template('feedback.html', feedback=feedback)

def analyze_responses(responses):
    behavioral_goal = responses['behavioral_goal']
    barriers = responses['barriers']

    # Example feedback based on the user's answers
    feedback = []
    
    # Analyze behavioral goal
    if "unclear" in behavioral_goal:
        feedback.append("Your goal seems unclear. Consider breaking it into smaller, achievable steps.")

    if "change" in behavioral_goal or "improve" in behavioral_goal:
        feedback.append("It sounds like you're ready for change. Focus on one small step at a time to build momentum.")
    
    # Analyze barriers
    for barrier in barriers:
        if "motivation" in barrier:
            feedback.append("Motivation seems to be a challenge. Try setting smaller goals and rewarding yourself for progress.")
        if "environment" in barrier:
            feedback.append("Your environment might be making it hard for you. Consider changing your surroundings or removing distractions.")
        if "unclear" in barrier:
            feedback.append("Some things are unclear. Try to clarify your next steps to avoid feeling overwhelmed.")
    
    # If no actionable feedback was found, provide a default message
    if not feedback:
        feedback.append("Based on your responses, it seems you might need a more structured plan. Consider reaching out to a coach or setting specific, measurable goals.")

    return feedback

if __name__ == '__main__':
    app.run(debug=True)
