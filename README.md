# Práticas de Programação FIAP

Este repositório contém práticas de programação realizadas durante as aulas da FIAP, incluindo exemplos em Java e Python para operações básicas e manipulação de dados JSON.

## Estrutura do Projeto

### Pasta `calculadora/`
Contém implementações de uma calculadora simples em diferentes linguagens:

- **calculadora.java**: Programa em Java que solicita dois números ao usuário e exibe a soma deles. Utiliza a classe Scanner para entrada de dados.
- **calculadora.py**: Script em Python que pede dois números ao usuário e mostra a soma. Utiliza a função input para entrada de dados.

### Pasta `json-python/`
Contém scripts em Python para manipulação de arquivos JSON e configuração:

- **agenda.json**: Arquivo JSON de exemplo contendo dados de uma agenda.
- **arquivo.txt**: Arquivo de texto simples para demonstração.
- **config.ini**: Arquivo de configuração no formato INI.
- **configparser.py**: Script que demonstra o uso do módulo configparser para ler arquivos INI.
- **dict-para-json.py**: Script que converte um dicionário Python para JSON.
- **funcao-read.py**: Exemplo de leitura de arquivos.
- **funcao-write.py**: Exemplo de escrita em arquivos.
- **json-para-dict.py**: Script que converte JSON para dicionário Python.
- **with.py**: Demonstração do uso de context managers (`with`) para manipulação de arquivos.

Esses exemplos demonstram operações básicas de entrada, processamento e saída, além de manipulação de dados estruturados em JSON e arquivos de configuração.

## Como Executar

### Calculadora Java
```bash
cd calculadora
javac calculadora.java
java calculadora
```

### Calculadora Python
```bash
cd calculadora
python calculadora.py
```

### Scripts JSON Python
```bash
cd json-python
python nome_do_script.py
```

## Requisitos
- Java JDK (para calculadora.java)
- Python 3.x (para scripts Python)