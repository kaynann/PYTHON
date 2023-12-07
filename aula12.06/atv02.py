# 2 . Ainda sobre a questão 01. Inserir  mais quatro alunos e notas no seu dicionário

dic = {}
lista = [['Felipe', 7], ['Geisa', 8], ['Mikael', 9], ['Wesley', 10]]

dic.update(lista)
print(dic)

lista_adicao = [['Elvis', 8], ['Eduardo', 9], ['Lucas CPF', 8], ['Francisco', 8]]
dic.update(lista_adicao)
print(dic)