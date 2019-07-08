#!/usr/bin/python

import sys
from datetime import datetime

#Exemplo chamada prompt:
#python3 dvCampoLivreCEF.py 6561667 14000000000000041 29-04-16 0000020889
#python3 dvCampoLivreCEF.py 6561667 14000000000001381 30-07-16 0000000100

codigo_banco = '104'
moeda = '9'
codigo_beneficiario = sys.argv[1]
nosso_numero = sys.argv[2]
data_vencimento = sys.argv[3]
valor_documento = sys.argv[4]

data_inicial = datetime.strptime('07-10-97', '%d-%m-%y').date()
data_vencto = datetime.strptime(data_vencimento, '%d-%m-%y').date()
fator = (data_inicial - data_vencto).days

#Calculo DV Campo Livre

c1 = codigo_beneficiario[:6]  #CODIGO BENEFICIARIO, EX: 656166
c2 = codigo_beneficiario[6:7] #DV BENEFICIARIO, EX: 7
c3 = nosso_numero[2:5]        #NN SEQ 1, EX: NN 000000000000003, 000 OS TRES PRIMEIROS 
c4 = '1'                      #C1 Tipo de Cobrança (1-Registrada / 2-Sem Registro)
c5 = nosso_numero[5:8]        #NN SEQ 2, EX: NN 000000000000003, 000 DO 4o. ao 6o. DIGITO
c6 = '4'                      #Identificador da Emissão do Boleto (4-Beneficiário)
c7 = nosso_numero[8:17]       #9ª a 17ª posição do Nosso Número

campos_campo_livre = c1 + ' ' + c2 + ' ' + c3 + ' ' + c4 + ' ' + c5 + ' ' + c6 + ' ' + c7

digitos = c1 + c2 + c3 + c4 + c5 + c6 + c7

x = 9
soma = 0
for i in digitos:
    soma += int(i) * x
    x -= 1
    if x == 1:
    	x = 9

resto = soma % 11

dv_campo_livre = 11 - resto

if dv_campo_livre > 9:
	dv_campo_livre = 0

#Calculo DV Geral Codigo Barra

c1 = codigo_banco
c2 = moeda
c3 = str(fator * -1)
c4 = valor_documento
c5 = codigo_beneficiario[:6]  #CODIGO BENEFICIARIO, EX: 656166
c6 = codigo_beneficiario[6:7] #DV BENEFICIARIO, EX: 7
c7 = nosso_numero[2:5]        #NN SEQ 1, EX: NN 000000000000003, 000 OS TRES PRIMEIROS 
c8 = '1'                      #C1 Tipo de Cobrança (1-Registrada / 2-Sem Registro)
c9 = nosso_numero[5:8]        #NN SEQ 2, EX: NN 000000000000003, 000 DO 4o. ao 6o. DIGITO
c10 = '4'                     #Identificador da Emissão do Boleto (4-Beneficiário)
c11 = nosso_numero[8:17]      #9ª a 17ª posição do Nosso Número
c12 = str(dv_campo_livre)

campos_codigo_barra = c1 + ' ' + c2 + ' ' + c3 + ' ' + c4 + ' ' + c5 + ' ' + c6 + ' ' + c7 + ' ' + c8 + ' ' + c9 + ' ' + c10 + ' ' + c11 + ' ' + c12

digitos = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 + c10 + c11 + c12

x = 4
soma = 0
for i in digitos:
    soma += int(i) * x
    x -= 1
    if x == 1:
    	x = 9

resto = soma % 11

dv_geral_codigo_barra = 11 - resto

if dv_geral_codigo_barra == 0 or dv_geral_codigo_barra > 9:
	dv_geral_codigo_barra = 1

codigo_barra = c1 + c2 + str(dv_geral_codigo_barra) + c3 + c4 + c5  + c6 + c7 + c8 + c9 + c10 + c11 + c12

# LINHA DIGITÁVEL / REPRESENTAÇÃO NUMÉRICA

c1 = codigo_banco
c2 = moeda
c3 = codigo_barra[19:24]

campo1 = c1 + c2 + c3

x = 2
soma = 0
for i in campo1:
	res_mult = int(i) * x
	if res_mult > 9:
	    dig1 = res_mult // 10
	    dig2 = res_mult % 10
	    res_mult = dig1 + dig2
	soma += res_mult
	x -= 1
	if x == 0:
		x = 2

if soma < 10:
 	dv_campo1 = 10 - soma
else:
    resto = soma % 10
    if resto == 0:
    	dv_campo1 = 0
    else:
    	dv_campo1 = 10 - resto


c1 = codigo_barra[24:34]

campo2 = c1

x = 1
soma = 0
for i in campo2:
	res_mult = int(i) * x
	if res_mult > 9:
	    dig1 = res_mult // 10
	    dig2 = res_mult % 10
	    res_mult = dig1 + dig2
	soma += res_mult
	x -= 1
	if x == 0:
		x = 2

if soma < 10:
 	dv_campo2 = 10 - soma
else:
    resto = soma % 10
    if resto == 0:
    	dv_campo2 = 0
    else:
    	dv_campo2 = 10 - resto


c1 = codigo_barra[34:44]

campo3 = c1

x = 1
soma = 0
for i in campo3:
	res_mult = int(i) * x
	if res_mult > 9:
	    dig1 = res_mult // 10
	    print(dig1)
	    dig2 = res_mult % 10
	    print(dig2)
	    res_mult = dig1 + dig2
	soma += res_mult
	x -= 1
	if x == 0:
		x = 2

if soma < 10:
 	dv_campo3 = 10 - soma
else:
    resto = soma % 10
    if resto == 0:
    	dv_campo3 = 0
    else:
    	dv_campo3 = 10 - resto

campo4 = str(dv_geral_codigo_barra)

campo5 = str(fator * -1) + valor_documento

linha_digitavel =  campo1[:5] + '.' + campo1[5:9]  + str(dv_campo1) + ' ' 
linha_digitavel += campo2[:5] + '.' + campo2[5:10] + str(dv_campo2) + ' ' 
linha_digitavel += campo3[:5] + '.' + campo3[5:10] + str(dv_campo3) + ' '
linha_digitavel += campo4 + ' ' + campo5

linha_codigo_barra = codigo_barra[:3]    + '.' + codigo_barra[3:4]   + '.' + codigo_barra[4:5]   + '.' + \
					 codigo_barra[5:9]   + '.' + codigo_barra[9:19]  + '.' + codigo_barra[19:25] + '.' + \
					 codigo_barra[25:26] + '.' + codigo_barra[26:29] + '.' + codigo_barra[29:30] + '.' + \
					 codigo_barra[30:33] + '.' + codigo_barra[33:34] + '.' + codigo_barra[34:43] + '.' + \
					 codigo_barra[43:44]
separador_codigo_barra = '===.=.=.====.==========.======.=.===.=.===.=.=========.='
contador_codigo_barra =  '123.4.5.6789.0123456789.012345.6.789.0.123.4.567890123.4'
separador_linha = '=====.===== =====.====== =====.====== = =============='
contador_linha  = '12345.12345 12345.123456 12345.123456 1 12345678901234'

print("========")
print("CNAB 240")
print("========")
print("Codigo do Beneficiario....: " + codigo_beneficiario)
print("Nosso Número..............: " + nosso_numero)
print("Campos Campo Livre........: " + campos_campo_livre)
print("DV Campo Livre............: " + str(dv_campo_livre))
print("Fator.....................: " + str(fator * -1))
print("Campos Código de Barra....: " + campos_codigo_barra)
print("DV Geral Codigo de Barra..: " + str(dv_geral_codigo_barra))
print("Codigo de Barra...........: " + codigo_barra)
print("Codigo de Barra...........: " + linha_codigo_barra)
print("Separador Codigo de Barra.: " + separador_codigo_barra)
print("Contador Código de Barra..: " + contador_codigo_barra)
print("Digitos Codigo de Barra...: " + str(len(codigo_barra)))
print("Campo1....................: " + campo1 + str(dv_campo1))
print("Campo2....................: " + campo2 + str(dv_campo2))
print("Campo3....................: " + campo3 + str(dv_campo3))
print("Campo4....................: " + campo4)
print("Campo5....................: " + campo5)
print("Linha Digitavel...........: " + linha_digitavel)
print("Separador Linha Digitavel.: " + separador_linha)
print("Contador Linha Digitavel..: " + contador_linha)
print("========")
