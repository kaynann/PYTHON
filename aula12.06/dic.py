# CRUD - Created, Readed, Update, Delete

dic1 = {'nome': 'kaynan'} # created
dic2 = dict(idade =  23) # created

dic1['nome'] # readed
reading = dic2.get('idade') # readed

dic1.update(sobrenome = 'junior') # update

print(dic1)
print(dic2)
 
# quando se adiciona um interável que não seja um dicionário, no dicionário você tem que colocar uma virgula depois do interavel

tupla = ('peso', 60), 
lista = ['data', '29/09/2004'],

dic1.update(tupla)
dic1.update(lista)

print(dic1)

dic1.clear()

print(f'Dados do dicionário: { dic1 }') # deleted