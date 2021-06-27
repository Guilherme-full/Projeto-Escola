# Projeto Escola (Guilherme Xavier Souza)

## Download do Projeto
```
gh repo clone Guilherme-full/Projeto-Escola
```

|          | Linux | macOS | Windows |
|   :---   | :---: | :---: | :---:   |
| Chromium <!-- GEN:chromium-version -->93.0.4543.0<!-- GEN:stop --> | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| WebKit <!-- GEN:webkit-version -->14.2<!-- GEN:stop --> | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Firefox <!-- GEN:firefox-version -->89.0<!-- GEN:stop --> | :white_check_mark: | :white_check_mark: | :white_check_mark: |

## Descrição

Projeto realizado em Python, no qual é um sistema para uma escola, com opções de cadastro, agendamento de atividade/prova,  cadastro de resultado da Avaliação da Turma, impressão
de resultados, gerador de arquivo.txt de resultado da turma por Bimestre, verificar alunos cadastrados.

## Bibliotecas 

```
from datetime import datetime
from Biblioteca import *
```

## Funções
```
turma = []
def cadastroAluno():
    aluno = []
    print('--- Cadastro de Aluno')
    print('----------------------------------')
    aluno.append(input('Turma       : '))
    aluno.append(int(input('RM          : ')))
    aluno.append(input('Nome        : ').upper())
    aluno.append(input('Dt_Nasc     : '))
    aluno.append(input('Responsável : ').upper())
    aluno.append(input('E-mail      : '))
    turma.append(aluno)
    print('----------------------------------')
    print()
    arquivo = open('CadAluno.txt','a')
    qtdEspacosNome  = 34-len(aluno[2])
    qtdEspacosEmail = 35-len(aluno[5])
    arquivo.write('\n'+str(aluno[1])+' '+aluno[2]+qtdEspacosNome*' '+aluno[0]+'        '+aluno[5]+qtdEspacosEmail*' '+aluno[3]+'  '+aluno[4])
    arquivo.close()


def importaAluno():
    arquivo = open('CadAluno.txt','r')
    arq     = arquivo.readlines()
    for linha in arq:
        aluno = []
        aluno.append(linha[40:41])
        aluno.append(int(linha[0:6]))
        aluno.append(linha[6:40])
        aluno.append(linha[84:95])
        aluno.append(linha[96:].rstrip('\n')) #removesuffix('\n') replace('\n','')
        aluno.append(linha[49:84].split())
        turma.append(aluno)
    arquivo.close()



agenda = []
def cadastroAgenda():
    evento = []
    print('--- Cadastro de Agenda')
    print('----------------------------------')
    evento.append(input('Turma       : '))
    evento.append(int(input('Bimestre    : ')))
    evento.append(input('Evento - P/A: '))
    evento.append(input('Data        : '))
    agenda.append(evento)
    print('----------------------------------')
    print()


resultado = []
def cadastraResultado():
    print('--- Cadastro de Resultado')
    print('----------------------------------')
    evento = []
    evento.append(input('Turma       : '))
    evento.append(int(input('Bimestre    : ')))
    evento.append(input('Evento      : '))
    evento.append(int(input('RM          : ')))
    evento.append(input('Resultado   : '))
    resultado.append(evento)
    print('-------------------------------')
    print()


def imprimeResultado(qualTurma):
    existe = False
    for i in turma:
        if qualTurma in i:
            existe = True
    if existe:
        print('--- Relatório de Resultados')
        print('----------------------------------')
        print('Turma ', qualTurma)
        print('RM           Nome                                     Idade      Prova    Atividade')
        for x in turma:
           if x[0] == qualTurma:
               print(x[1], '      ',x[2],'       ', idade(x[3]),'       ',  avaliacao(x[1],'P',resultado), '        ',avaliacao(x[1],'A',resultado))
        print('----------------------------------')
        print()
    else:
        print('******  turma não existe *******')
        print()


def arquivoResultado(qualTurma):
    nomeRelatorio = 'Relatorio_'+qualTurma+'.txt'
    arquivo = open(nomeRelatorio,'w')
    existe = False
    for i in turma:
        if qualTurma in i:
            existe = True
    if existe:
        arquivo.write('--- Relatório de Resultados'+'\n')
        arquivo.write('----------------------------------'+'\n')
        arquivo.write('Turma '+qualTurma+'\n')
        arquivo.write('RM         Nome         Idade    Prova    Atividade'+'\n')
        for x in turma:
           if x[0] == qualTurma:
               arquivo.write(str(x[1])+'      '+x[2]+'       '+str(idade(x[3]))+'       '+str(avaliacao(x[1],'P',resultado))+ '        '+str(avaliacao(x[1],'A',resultado))+'\n')
        print('----------------------------------')
        print('Relatorio Gerado em Arquivo')
    else:
        print('******  turma não existe *******')
        print()
    arquivo.close()

def arquivoTurma(qualTurma):
    nomeRelatorio = 'Relatorio_Turma_'+qualTurma+'.txt'
    arquivo = open(nomeRelatorio,'w')
    arquivo.write('Relatório de alunos por Turma'+'\n')
    arquivo.write('Turma: '+ qualTurma+'\n')
    arquivo.write('RM   Nome        Idade     Responsável      E-mail'+'\n')
    for aluno in turma:
        if aluno[0] == qualTurma:
            arquivo.write(str(aluno[1])+'      '+aluno[2]+'       '+str(idade(aluno[3]))+'      '+aluno[4]+'      '+aluno[5]+'\n')
    arquivo.close()
    print('----------------------------------')
    print('Relatorio Gerado em Arquivo')
    print()
```

## Funções Importadas da Biblioteca

```
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
```

## Corpo Principal do Programa

```
importaAluno()
while True:
    print('  ***  Sistema Escola Junior  ***')
    print()
    print('Escolha a opção desejada pelo número')
    print()
    print(' 1) Cadastro de aluno')
    print(' 2) Cadastro de Evento de Avaliação na Agenda da Turma')
    print(' 3) Cadastro de resultado da Avaliação da Turma')
    print(' 4) Imprime resultado da turma por Bimestre')
    print(' 5) Gera arquivo txt de resultado da turma por Bimestre')
    print(' 6) Gera arquivo da turma ')
    print(' 7) Verificar alunos cadastrados')
    print()
    opcao = int(input('    Digite sua opção: '))
    print()
    print()

    if   opcao == 1:
        cadastroAluno()
    elif opcao == 2:
        cadastroAgenda()
    elif opcao == 3:
        cadastraResultado()
    elif opcao == 4:
        opcaoTurma = input('Qual turma você deseja: ')
        imprimeResultado(opcaoTurma)
    elif opcao == 5:
        opcaoTurma = input('Qual turma você deseja: ')
        arquivoResultado(opcaoTurma)
    elif opcao == 6:
        opcaoTurma = input('Qual turma você deseja: ')
        arquivoTurma(opcaoTurma)
    elif opcao == 7:
        verificaralunos()
    else:
        print('Opção inválida')
```

## Ferramenta e Linguagem
<img align="center"  alt="Python" heigth= "40" width ="60" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"></img>
<img align="center"  alt="Pycharm" heigth= "40" width ="60" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pycharm/pycharm-original.svg"></img>
