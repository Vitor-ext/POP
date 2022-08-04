from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    dados = {"I0": "0", "I1": "0", "O0": "0", "O1": "0"}
    return render_template('geral.html', dados=dados)


@app.route('/status_xml')
def xml():
    xml = {"I0": "0", "I1": "0", "O0": "0", "O1": "0"}
    return render_template('xml.html', xml=xml)


###### Para Desenvolvimento #########
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int("8000"), debug=True)

###### Para Produção - obs. Comentar o de cima #########
# app.run(host="127.0.0.1", port=int("8000"))
