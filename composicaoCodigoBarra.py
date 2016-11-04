#!/usr/bin/python

import sys

#print('Number of arguments:', len(sys.argv), 'arguments.')
#print('Argument List:', str(sys.argv))

codigo_beneficiario = sys.argv[1]
nosso_numero = sys.argv[2]

digitos =  codigo_beneficiario[:6]  #CODIGO BENEFICIARIO, EX: 656166
digitos += codigo_beneficiario[6:7] #DV BENEFICIARIO, EX: 7
digitos += nosso_numero[2:5]        #NN SEQ 1, EX: NN 000000000000003, 000 OS TRES PRIMEIROS 
digitos += '1'                      #C1 Tipo de Cobrança (1-Registrada / 2-Sem Registro)
digitos += nosso_numero[6:9]        #NN SEQ 2, EX: NN 000000000000003, 000 DO 4o. ao 6o. DIGITO

print(digitos)
