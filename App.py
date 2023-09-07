from flask import Flask, request, render_template, redirect, session
from form import ResumeForm  

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mys@cretk@y'

@app.route("/")
def home():
    return render_template('base.html')


@app.route('/resume',)

def personal_info():
    form = ResumeForm()
    return render_template('personal_info.html', resume_form=form)

@app.route('/education')
def education():
    form = ResumeForm()
    return render_template('education.html', resume_form=form)

@app.route('/experience')
def experience():
    form = ResumeForm()
    return render_template('experience.html', resume_form=form)

@app.route('/skill')
def skill():
    form = ResumeForm()
    return render_template('skill.html', resume_form=form)

if __name__ == '__main__':
    app.run(debug=True)