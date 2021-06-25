def idade(data_nascimento):
    from datetime import datetime
    ano_nascimento = int(data_nascimento[6:10])
    mes_nascimento = int(data_nascimento[3:5])
    dia_nascimento = int(data_nascimento[0:2])
    ano_atual      = datetime.today().date().year
    mes_atual      = datetime.today().date().month
    dia_atual      = datetime.today().date().day
    resultadoIdade = ano_atual - ano_nascimento
    if mes_nascimento > mes_atual:
        resultadoIdade = resultadoIdade - 1
    if mes_nascimento == mes_atual and dia_nascimento > dia_atual:
        resultadoIdade = resultadoIdade + 1
    return resultadoIdade


def avaliacao(rm, tipo, matrixresultado) :
    nota = 0
    for y in matrixresultado :
        if y[3] == rm and y[2] == tipo :
            nota = y[4]
    return nota


def verificaralunos():
    arq = open('CadAluno.txt', 'r')
    arquivo = arq.readlines()
    for x in arquivo:
        print(x)
    print('-' * 120)