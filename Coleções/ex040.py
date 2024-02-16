"""
Exercício 040:
    Faça um programa que receba o nome de 5 alunos de dois cursos, depois mostre na tela todos os alunos dos dois
cursos, os alunos que participam dos dois cursos ao mesmo tempo e os alunos que participam de um curso apenas e não do
outro...
"""
# Variáveis
alunos_mysql = set({})
alunos_python = set({})

# Entrada de dados
print("Alunos do curso de MySQL:")
for cont in range(5):
    alunos_mysql.add(str(input(f"{cont+1}° aluno de MySQL: ")))

print("\nAlunos do curso de Python:")
for cont in range(5):
    alunos_python.add(str(input(f"{cont+1}° aluno de python: ")))

# Saída de dados
print(f"\nTodos os alunos de ambos os cursos--> {alunos_mysql.union(alunos_python)}")
print(f"Alunos que participam de ambos os cursos--> {alunos_mysql.intersection(alunos_python)}")
print(f"Alunos que participam apenas do curso de MySQL--> {alunos_mysql.difference(alunos_python)}")
print(f"Alunos que participam apenas do curso de Python--> {alunos_python.difference(alunos_mysql)}")
