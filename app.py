from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

books = [
    {"id": 1, "title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "year": 1997},
    {"id": 2, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"id": 3, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 4, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 5, "title": "A Promised Land", "author": "Barack Obama", "year": 2020}
]

@app.route('/hetic', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/quisuisje', methods=['GET'])
def qui_suis_je():
    return 'Marcel MISSIHOUN'

@app.route('/quisuisjev2/<name>', methods=['GET', 'POST'])
def dynamic_qui_suis_je(name):
    return f'Bonjour, {name}! 🔥'

@app.route('/api/v1/addition/<a>/<b>', methods=['GET'])
def add(a, b):
    c = int(a) + int(b)
    return str(c)

@app.route('/api/v1/books', methods=['GET'])
def get_books_by_author():
    author = request.args.get('author')
    if author:
        result = [book for book in books if book['author'].lower() == author.lower()]
        return jsonify(result)
    return jsonify([])

@app.route('/search', methods=['GET'])
def search_form():
    query = request.args.get('query')
    if query:
        result = [book for book in books if query.lower() in book['author'].lower()]
        if result:
            return render_template('search_results.html', books=result)
        else:
            return render_template('search_results.html', error="Aucun livre trouvé pour cet auteur.")
    return render_template('search.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
        username = request.form['username']
        password = request.form['password']
        # Vous pouvez ajouter ici la logique de vérification du login et du mot de passe
        if username == 'admin' and password == 'password':  # Exemple de vérification simple
            return render_template('index.html')
        else:
            error = 'Nom d\'utilisateur ou mot de passe incorrect'
            return render_template('login.html', error=error)
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)