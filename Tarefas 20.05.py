# #ORGANIZADOR DE TAREFAS
# import os
#
# print("\n***Organizador de Tarefas*** ")
# while True:
#     print("\n Lista de Comandos Permitidos:")
#     print("Listar Tarefas")
#     print("Desfazer Adição de Tarefas")
#     print("Refazer Adição de Tarefas")
#     print("Limpar Lista de Tarefas")
#     print("Sair da Lista de Tarefas")
#
#     tarefa = input("Digite uma tarefa ou um comando ").strip().upper()
#
# if tarefa not in "LISTARDESFAZERREFAZERLIMPARSAIR":
#     lista.append(tarefa)
#     print("Tarefa adionada com sucesso!")
# elif tarefa == "LISTAR":
#     if not lista:
#         print("Não é possivel listar ! Lista vazia")
#     else:
#         print(lista)
# elif tarefa == "DESFAZER":
#     if not lista:
#         print("Não é possivel desfazer! Lista vazia!")
#     else:
#         print("Atividade removida com sucesso!")
#     item_removido = lista.pop()
# elif tarefa == "REFAZER":
#     if not lista:
#         print("Não é possivel refazer! Lista vazia!")
#     else:
#         lista.append(item_removido)
# elif tarefa == "LIMPAR":
#     sistema_operacional = os.name
#     if sistema_operacional == "nt":
#         os.sytem("cls")
#     elif sistema_operacional == "posix":
#         os.sytem("clear")
#     else:
#         print("Erro! Sistema operacional incopativel")
# elif tarefa == "SAIR":
#     break

print("JOGO DE PERGUNTAS E RESPOSTAS")

while True:
    entrada = input("Digite I para iniciar ou S para sair:").strip().upper()
    if entrada not in "IS":
        print("Erro! Opção invalida!")
    elif entrada == "S":
        break
    elif entrada == "I":
         perguntas = [
             {
                 "pergunta": "Qual a altura do Cristo Redentor?",
                 "alternativas" :["10 metros", "20 metros","30 metros"],
                 "resposta": "30 metros"
             },
             {
                 "pergunta": " De quem é a famosa frase “Penso, logo existo”?",
                 "alternativas": ["platão", "Galileu" , "Descarte"],
                 "respota": "Descartes"
             },
             {
                 "pergunta": " Qual o menor pais do mundo”?",
                 "alternativas": ["Vaticano", "Russia", "França"],
                 "respota": "Vaticano"
             },
             {
                 "pergunta": " Qual o ano da ultima constituição Brasileira”?",
                 "alternativas": ["1900", "1950", "1988"],
                 "respota": "1988"

             },
         ]
    contador = 0

    def jogo(pergunta):
        print(pergunta["pergunta"])

        for opcao, alternativa in enumerate(pergunta["alternativas"],start=1):
            print(f"{opcao}.{alternativa}")
        while True:
            resposta = input("Digite o numero da resposta:")
            if resposta == pergunta["resposta"]:
                print("Resposta Correta!")
            else:
                print("Resposta Incorreta!")

        for pergunta in perguntas:
            jogo(pergunta)
            input("Precione ENTER para a proxima pergunta")





