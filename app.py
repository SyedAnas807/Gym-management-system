from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Highlights can be passed dynamically to the template
    highlights = [
        {"icon": "⚡", "title": "24/7 Access", "desc": "Train on your schedule. We never close."},
        {"icon": "🔥", "title": "Elite Trainers", "desc": "Learn from pro bodybuilders and powerlifters."},
        {"icon": "💎", "title": "Premium Gear", "desc": "Hammer Strength, Eleiko, and Rogue equipment."}
    ]
    return render_template('index.html', highlights=highlights)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/membership')
def membership():
    return render_template('membership.html')

if __name__ == '__main__':
    app.run(debug=True)