import re
from validate_docbr import CPF

def cpf_invalido(numero_cpf):
    cpf = CPF()
    return not cpf.validate(numero_cpf)
    
def nome_invalido(nome):
    return not nome.isalpha()

def celular_invalido(celular):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return not resposta