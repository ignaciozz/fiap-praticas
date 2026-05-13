# Usando função open para criar um objeto do tipo arquivo
arquivo = open ("C:\\Users\\Gabriel\\Documents\\Gabriel\\Garoto de Programa\\fiap\\aulas-fiap\\fiap-praticas\\json-python\\arquivo.txt", "r", encoding="UTF-8") 

# Verificando tipo
print(type(arquivo))

# Printando o objeto do arquivo
print(arquivo)

# Pritando o conteúdo do arquivo
print(arquivo.readline(2))

# Fechando o arquivo
arquivo.close()
