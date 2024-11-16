
from flask import Flask, render_template, request
import random

app = Flask(__name__)

story_templates = [
    "Once upon a time in a place called {place}, there was a person named {name}. They loved {activity} and dreamed of becoming the best in {place}.",
    "{name} was walking down the street of {place} when they suddenly found a magic {object}. Little did they know, it would change their life forever.",
    "In {place}, there lived a person named {name} who always wanted to {activity}. One day, they finally got the chance to make their dreams come true.",
    "It was a sunny day in {place} when {name} decided to go {activity}. But what happened next would be remembered forever in {place}.",
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_story():
    name = request.form['name']
    place = request.form['place']
    activity = request.form['activity']
    object = request.form['object']
    
    story_template = random.choice(story_templates)
    story = story_template.format(name=name, place=place, activity=activity, object=object)
    
    return render_template('index.html', story=story)

if __name__ == '__main__':
    app.run(debug=True)
