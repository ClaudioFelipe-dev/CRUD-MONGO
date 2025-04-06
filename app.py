from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient("mongodb+srv://teste:teste@cluster0.bir3rnp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['contato_db']
contatos = db['contatos']

@app.route('/')
def index():
    lista_contatos = list(contatos.find())
    return render_template('index.html', contatos=lista_contatos)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.form.get('nome')
    telefone = request.form.get('telefone')
    if nome and telefone:
        contatos.insert_one({'nome': nome, 'telefone': telefone})
    return redirect('/')

@app.route('/deletar/<id>')
def deletar(id):
    from bson.objectid import ObjectId
    contatos.delete_one({'_id': ObjectId(id)})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
