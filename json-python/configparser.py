# Importando módulos
import configparser
import os


config = configparser.ConfigParser()
config_file = "C:\\Users\\Gabriel\\Documents\\Gabriel\\Garoto de Programa\\fiap\\aulas-fiap\\fiap-praticas\\json-python\\config.ini"


config.read(config_file)


print(type(config))


print(config["general"] ["app_name"])