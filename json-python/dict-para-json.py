# Importando o módulo JSON
import json

# Criando dicionário

contatos = {
    "Gabriel Ignacio":
        {"nome" : "1199999",
         "Email":"gabriel@email.com"},

    "Júlia Mendes":
        {"nome":"1198888",
         "Email":"julia@email.com"},
}

# Convertendo Dicionário -> String com formatação JSON
conteudo_string = (json.dumps(contatos, indent=4, ensure_ascii=False))

# Criando arquivo
arquivo = open("C:\\Users\\Gabriel\\Documents\\Gabriel\\Garoto de Programa\\fiap\\aulas-fiap\\fiap-praticas\\json-python\\agenda.json", "w", encoding="UTF-8")

# Escrevendo conteúdo no arquivo
arquivo.write(conteudo_string)

# Fechando arquivo[
arquivo.close()