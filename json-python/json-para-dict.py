# Importando módulo JSON
import json

# Criando arquivo
arquivo = open("C:\\Users\\Gabriel\\Documents\\Gabriel\\Garoto de Programa\\fiap\\aulas-fiap\\fiap-praticas\\json-python\\agenda.json", "r", encoding="UTF-8")

# Exibindo arquivo como variável String
dicionario = json.loads(arquivo.read())

# Fechando arquivo
arquivo.close()

# Printando chave específica do arquivo 
print(dicionario["Gabriel Ignacio"])