import ConversorDeBases
import random

def converter(num, base_n):
    converted_number = ConversorDeBases.convert_decimal_to_baseX(base_n, num)

def gerar():
    num = random.randint(2,999)
    base = random.randint(2,16)
    
    converted_n = ConversorDeBases.convert_decimal_to_baseX(base, num)
    return converted_n, base


def iniciar():
    num, base = gerar()

    print(f'A base é {base}')
    print(num)

    while  GuessN := int(input('Digite um número na base apropriada: ')):
        if int(GuessN) == int(num):
            break

        if ConversorDeBases.verificar(GuessN, base) == None:
            print('Números Devem estar na base apropriada!')
            continue


iniciar()
