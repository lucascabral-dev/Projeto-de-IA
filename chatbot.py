import json
import os

arquivo_memoria = "memoriaIA.json"

# Carrega o arquivo da memoria
if os.path.exists(arquivo_memoria):
    with open(arquivo_memoria, "r", encoding="utf-8") as f:
        memoria = json.load(f)

# Se o arquivo da memoria nao existir, ele cria.
else:
    memoria = {}

# Resposta da IA
def resposta_IA(pergunta):
    pergunta = pergunta.lower() # define que as perguntas fiquem em letras minusculas
    if pergunta in memoria: # Se pergunta estivert dentro de memoria, ela retorna a memoria com a pergunta
        return memoria[pergunta]
    
    else: # Senao, a IA aprende
        print("Não sei responder isso ainda.")
        nova_resposta = input("Como devo responder? ")
        memoria[pergunta] = nova_resposta
        salvar_memoria()
        return "Obrigado por ter me ensinado algo novo para te responder melhor!"

def salvar_memoria(): # Salva a memoria
    with open(arquivo_memoria, "w", encoding="utf-8") as f:
        json.dump(memoria, f, ensure_ascii=False, indent=2)

print('=' * 30)
print("LUNEX IA")
print('=' * 30)
print("Digite 'sair' para parar a conversa.\n")
print("AVISO: Pergunte com uma linguagem formal para que sua experiencia seja a melhor possivel!")

while True: # Loop de conversa
    pergunta = input("\nVocê: ")
    if pergunta.lower() == "sair":
        print("Lunex IA: Tchau !")
        break
    resposta = resposta_IA(pergunta)
    print("\nLunex IA:", resposta)

