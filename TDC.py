#Tuplas
meses = (
 "Janeiro", "Fevereiro", "Março", "Abril",
 "Maio", "Junho", "Julho", "Agosto",
 "Setembro", "Outubro", "Novembro", "Dezembro"
)

print("Primeiro mês:", meses[0])
print("Último mês:", meses[-1])

for mes in meses:
    print(mes)

#Conjuntos
nomes = set()

for i in range(5):  
    nome = input("Digite um nome: ")
    nomes.add(nome)

print("Nomes sem repetição:")
for nome in nomes:
    print(nome)

#Dicionários
aluno = {
    "nome": input("Nome: "),
    "idade": input("Idade: "),
    "curso": input("Curso: ")
}

for chave, valor in aluno.items():
    print(chave, ":", valor)
