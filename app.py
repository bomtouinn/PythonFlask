from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur ma page d'accueil !"

@app.route('/about')
def about():
    return "À propos de moi : Je m'appelle Tom Bouin et Je suis en train d'apprendre à développer des applications web avec Flask !"

if __name__ == '__main__':
    app.run(debug=True)