import random


def verificar(número, base):
    for c in str(número):
        if int(c) >= base:
            return None
    return 1

    
def convert_decimal_to_baseX(base_para_conversão, número):
    resto = []
    
    while True:
        resto.append(int(número % base_para_conversão))
        número = número / base_para_conversão
        
        if int(número) == 0:
            break 

    resto.reverse()
    núm_basex = ''.join(map(str, resto))
    return núm_basex
    

def convert_baseX_to_decimal(base, número):
    for z in str(número):
        if int(z) >= base:
            print(f'Erro de digitação o número deve ser em base {base}')
            return None
        
    c = [x for x in range(0,len(str(número)))]
    c.reverse()

    resultados = []
    for idx,value in enumerate(str(número)):
        (s := int(value)*(base**c[idx]))   
        resultados.append(s)
    
    return sum(resultados)
