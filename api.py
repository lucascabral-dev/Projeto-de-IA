# API RESTful

# Então uma API RESTful é uma interface que permite aplicações trocarem dados de forma padronizada usando a web.

from flask import Flask, jsonify, request

api = Flask(__name__) # Cria o app

projetos = [] # Banco de dados local

@api.route('/projetos', methods=['GET']) # -> Metodo GET: Para buscar coisas na API | endpoint
def listar_projetos():
    return jsonify(projetos)

@api.route('/projetos', methods=['POST']) # -> Metodo POST: Para adicionar coisas na API | endpoint
def criar_projeto():
    novo = request.json # Dados para enviar para a API
    novo['id'] = len(projetos) + 1
    projetos.append(novo)
    
    return jsonify(novo), 201

@api.route('/projetos/<int:id>', methods=['DELETE']) # -> Metodo DELETE: Para deletar coisas na API | endpoint
def deletar_projeto(id):
    for i in projetos:
        if i['id'] == id:
            projetos.remove(i)
            return jsonify({"mensagem": f"Projeto com id {id} foi removido com sucesso da API"})         
    return jsonify({"error": f"Projeto com id {id} teve algum erro na hora de sua remocao"}), 404

@api.route('/projetos/<int:id>', methods=['PUT']) # -> Metodo PUT: Para atualizar totalmente alguma informaçao da API | endpoint
def atualizar_api(id):
    dados = request.json # Dados para enviar para a API
    dados.pop("id", None) # Remove o campo id se ele vir na requisiçao
    
    for x in projetos:
        if x['id'] == id:
            x.update(dados)
            return jsonify({"mensagem": f"Projeto com id {id} foi atualizado com sucesso",
                            "projeto_novo": x
                            })
    return jsonify({"error": f"Projeto com id {id} teve algum erro em sua atualizacao"}), 404

if __name__ == '__main__':
    api.run(debug=True)
