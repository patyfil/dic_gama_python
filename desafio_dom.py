from dic_usuarios_inicial import dict_usuarios
# importa o dict_usuarios declarado no arquivo dic_usuarios_inicial.py
from dic_estados import estados
# importa o dicionário estados declarado no arquivo dic_estados.py


import json


def print_formatado(dados):
    print(json.dumps(dados, indent=2))


lista_usuarios = dict_usuarios["usuarios"]

    # 1 - Troque o nome completo do Estado pela sua respectiva sigla

for usuario in lista_usuarios:  # para cada usuario na lista_usuarios
    estado_do_usuario = usuario[
        "Estado"]  # a variável estado_do_usuario recebe/armazena o "Estado" correspondente a iteração Atual do usuario
    sigla_estados = estados[estado_do_usuario]  # sigla_estados recebe o valor do dic_estados\estados equivalente ao estado_do_usuario
    usuario["Estado"] = sigla_estados  # Armazena a variável sigla_estados na chave "Estado" da Iteração Atual

    # 2 - Sempre que houver um dado desconhecido trocar pela variável nula

    if usuario["nome completo"] == "desconhecido":
        usuario["nome completo"] = None

    if usuario["Estado"] == "desconhecido":
        usuario["Estado"] = None

    if usuario["phone"] == "desconhecido":
        usuario["phone"] = None

    if usuario["endereço"] == "desconhecido":
        usuario["endereço"] = None

    if usuario["CEP"] == "desconhecido":
        usuario["CEP"] = None


    # 3 - email - garantir que TODOS OS EMAILS estejam em letra minúscula (low case)
    usuario["email"] = usuario["email"].lower()
    # 3 - email - caso esteja como desconhecido trocar pelo modelo "nome.sobrenome@gmail.com"
    if usuario["email"] == "desconhecido":
        nome_separado = usuario["nome completo"].split()
        primeiro_nome = nome_separado[0]
        sobrenome = nome_separado[-1]
        novo_email = primeiro_nome + "." + sobrenome + "@gmail.com"
        usuario["email"] = (novo_email).lower()

    # 4 - Trocar o nome do curso "A melhor linguagem do mundo" para "Python"

    if "A melhor linguagem do mundo" in usuario["cursos"]:
        indice_do_python = usuario["cursos"].index("A melhor linguagem do mundo")
        usuario["cursos"][indice_do_python] = "Python"

    # 5 - Transformar o valor de cursos para o seguinte dicionário:
    # 'cursos': {'Quantidade de cursos':
    # 'Aluno Aplicado': True or False
    # 'Aluno da melhor professora': True or False
    # 'cursos do aluno': [lista dos cursos do aluno]}
    # O Aluno será aplicado se fizer mais de 2 cursos
    # O Aluno será aluno da melhor professora de estiver no curso de Python

    cursando = usuario["cursos"]
    usuario["cursos"] = {
        "Quantidade de cursos": len(cursando),
        "Aluno Aplicado": len(cursando) > 2,
        "Aluno da melhor professora": "Python" in usuario["cursos"],
        "cursos do aluno": cursando
    }
    print(cursando)

    print_formatado(usuario)

