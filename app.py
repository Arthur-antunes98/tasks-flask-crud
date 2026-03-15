from flask import Flask # importando uma biblioteca seguida de uma classe

# __name__ = "__main__"
app = Flask(__name__) # variável
 
@app.route("/")                # rota; se comunicar com outros clientes; acessar via navegador 
def hello_world():             # definir função
    return "Hello World!"

@app.route("/about")
def about():
    return "Página sobre"

if __name__ == "__main__":
    app.run(debug=True)