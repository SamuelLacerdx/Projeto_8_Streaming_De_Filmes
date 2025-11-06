from flask import Flask, jsonify, render_template

app = Flask(__name__)

filmes = [
    {
        "id": 1,
        "titulo": "O Senhor dos Anéis: A Sociedade do Anel",
        "diretor": "Peter Jackson",
        "genero": "Fantasia",
        "poster": "https://br.web.img3.acsta.net/medias/nmedia/18/92/91/32/20224832.jpg",
        "ano": 2001
    },
    {
        "id": 2,
        "titulo": "Matrix",
        "diretor": "Lana Wachowski, Lilly Wachowski",
        "genero": "Ficção Científica",
        "poster": "https://upload.wikimedia.org/wikipedia/pt/3/3a/Interstellar_Filme.png",
        "ano": 1999
    },
    {
        "id": 3,
        "titulo": "A Cinco Passos de Você",
        "diretor": "Justin Baldoni",
        "genero": "Romance/Drama",
        "poster": "https://m.media-amazon.com/images/I/81Hv3wRgZpL._UF1000,1000_QL80_.jpg",
        "ano": 2019
    }
]

# 🔗 Rota para retornar o catálogo em JSON
@app.route("/filmes", methods=["GET"])
def get_filmes():
    return jsonify(filmes)

# 🏠 Rota principal (página inicial)
@app.route("/", methods=["GET", "POST"])
def index():
    nome = "Vitoria" 
    ultima_letra = nome[-1].lower()

    # Define a cor do design
    if ultima_letra in ["a", "h", "l"]:
        cor = "vermelho"
    elif ultima_letra in ["e", "o", "y"]:
        cor = "azul"
    else:
        cor = "roxo"

    return render_template("index.html", filmes=filmes, cor=cor, nome=nome)


if __name__ == "__main__":
    app.run(debug=True)
