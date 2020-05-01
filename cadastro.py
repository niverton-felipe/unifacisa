import json

notas = list()
medias = list()
auxiliar = list()


def cadastro_aluno(ficha):
    cont = 0
    resp = 'S'
    print('\nCADASTRAR ALUNO\n')
    while cont < 1 and resp in 'Ss' :
        aluno = input('Digite o nome do aluno: ')
        cad = 0
        for alunos in ficha:
            for nome in alunos:
                if nome == aluno:
                    print('Aluno já cadastrado. Deseja cadastrar outro aluno? (S/N)')
                    resp = input()
                    cad += 1
                
        if cad == 0: 
            auxiliar.append(aluno)
            auxiliar.append(notas[:])
            auxiliar.append(medias[:])
            ficha.append(auxiliar[:])
            auxiliar.clear()
            cont += 1
       
   
def adicionar_nota(ficha):
    cont = 0
    resp = 'S'
    print('\nADICIONANDO NOTA\n')
    while cont < 1 and resp in 'Ss':    
        cad = 0
        if len(ficha) <= 0:
            print('Ficha ainda não possui alunos cadastrados.\n')
            cont += 1
        else:
            nome_pesquisado = input('Digite o nome do aluno: ')
            for aluno in ficha:
                if aluno[0] == nome_pesquisado:
                    cont2 = True
                    while cont2:
                        try :
                            nota = float(input('Digite a nota do aluno (0.0 - 10.0): '))
                        
                            if (10 >= nota >= 0) and len(aluno[1]) < 3:                
                                aluno[1].append(nota)
                                cad += 1
                                cont += 1
                                cont2 = False
                                media = 0
                                for nota in aluno[1]:
                                    media += nota
                                media /= len(aluno[1])
                                aluno[2].clear()
                                aluno[2].append(media) 
                            elif len(aluno[1]) >= 3:
                                print('Aluno já possui 3 notas')
                                print('Utilize a opção 6 se deseja editar a nota do aluno')
                                cont2 = False                
                            else:
                                print('Nota fora do intervalo. Tente novamente')
                        except Exception as erro:
                            print('Erro ao digitar nota')
                            print(f'O erro foi {erro}')
            if cad >= 1:        
                print('Nota adicionada\n')    
            else:
                print('Nota não cadastrada. Verifique se o nome do aluno foi digitado corretamente.\n')
                resp = input('Deseja tentar novamente? (S/N): ')
    
  
def remover_aluno(ficha):
    print('\nREMOVER ALUNO\n') 
    cont = 0
    while cont < 1:
        if len(ficha) <= 0:
            print('Ficha ainda não possui alunos cadastrados.\n')
            cont += 1
        else:
            cad = 0
            nome_pesquisado = input('Digite o nome do aluno: ')
            for aluno in ficha:
                if aluno[0] == nome_pesquisado:
                    ficha.remove(aluno)
                    cad += 1
                    cont += 1            
            if cad == 1:
                print(f'O(A) aluno(a) {nome_pesquisado} removido(a)')
            elif nome_pesquisado == 'sair':
                cont +=1
            else:
                print(f'O nome {nome_pesquisado} não foi encontrado')
                print('Digite sair para voltar ao menu')
    
def remover_nota(ficha):
    print('\nREMOVER NOTA\n') 
    cont = 0  
    while cont < 1:
        if len(ficha) <= 0:
            print('Ficha ainda não possui alunos cadastrados.\n')
            cont += 1
        else:
            cad = 0
            id_nota = True
            nome_pesquisado = input('Digite o nome do aluno: ')
            for aluno in ficha:
                if aluno[0] == nome_pesquisado:
                    try :
                        nota_pesquisada = int(input('Digite número da nota que deseja remover (1ª, 2ª ou 3ª nota): ')) 
                        if len(aluno[1]) >= nota_pesquisada:
                            aluno[1].pop(nota_pesquisada - 1)
                            cont += 1
                            cad += 1
                            media = 0
                            for nota in aluno[1]:
                                media += nota
                            if len(aluno[1]) > 0:
                                media /= len(aluno[1])
                                aluno[2].clear()
                                aluno[2].append(media)
                            else:
                                aluno[2].clear()
                        else:
                            id_nota = False
                        
                    except Exception as erro:
                        print('Erro ao digitar a nota')
                        print(f'O erro foi {erro}')
                        id_nota = False

            if cad == 1:
                print(f'A nota {nota_pesquisada} foi removida.')
            elif not(id_nota):
                print(f'A nota não foi não encontrada')
            else:
                print(f'{nome_pesquisado} não foi encontrado')
        
def editar_nome(ficha):
    print('\nEDITAR NOME\n') 
    cont = 0 
    while cont < 1:
        if len(ficha) <= 0:
            print('Ficha ainda não possui alunos cadastrados.\n')
            cont += 1
        else:
            cad = 0
            nome_pesquisado = input('Digite o nome do aluno: ')
            for aluno in ficha:
                if aluno[0] == nome_pesquisado:            
                    nome = input('Digite o novo nome: ')
                    aluno[0] = nome
                    cont += 1
                    cad += 1
                        
        if cad == 1:
            print('Nome editado')
        elif nome_pesquisado == 'sair':
            cont += 1
        else:
            print('Aluno não encontrado\n Digite sair para voltar ao menu')
    
def editar_nota(ficha):
    print('\nEDITAR NOTA\n')
    if len(ficha) <= 0:
        print('Ficha ainda não possui alunos cadastrados.\n')
        
    else:
        cont = 0 
        while cont < 1:
            cad = 0
            id_nota = True
            nome_pesquisado = input('Digite o nome do aluno: ')
            for aluno in ficha:
                if aluno[0] == nome_pesquisado:
                    try :
                        nota_pesquisada = int(input('Digite número da nota que deseja editar (1ª, 2ª ou 3ª nota): ')) 
                        
                        if len(aluno[1]) >= nota_pesquisada:
                            nota = float(input('Digite a nova nota: '))
                            aluno[1].pop(nota_pesquisada - 1)
                            aluno[1].insert(nota_pesquisada - 1, nota)
                            cont += 1
                            cad += 1
                            media = 0
                            for nota in aluno[1]:
                                media += nota
                            if len(aluno[1]) > 0:
                                media /= len(aluno[1])
                                aluno[2].clear()
                                aluno[2].append(media)
                            else:
                                aluno[2].clear()
                        else:
                            id_nota = False

                    except Exception as erro:
                        print('Ocorreu erro ao buscar nota')
                        print(f'O erro foi {erro}')
                        id_nota = False
                        
            if cad == 1:
                print(f'A nota {nota_pesquisada} foi alterada com sucesso')
            elif not(id_nota):
                print(f'A nota não foi encontrada')
            else:
                print(f'{nome_pesquisado} não foi encontrado')
   
    print(ficha)  

def buscar_aluno(ficha):
    print('\nBUSCAR ALUNO POR NOME\n') 
    cont = 0 
    while cont < 1:
        if len(ficha) <= 0:
            print('Ficha ainda não possui alunos cadastrados.\n')
            cont += 1
        else:
            cad = False
            nome_pesquisado = input('Digite o nome do aluno: ')
            for aluno in ficha:        
                if nome_pesquisado in aluno[0]:
                    notas = str()
                    media = 0.0
                    for nota in aluno[1]:                                
                        notas += str(nota) + " "
                    for nota in aluno[2]:
                        media += nota                           
                    print('Nome: {0}. Notas: {1}. Média: {2:.2f}'.format(str(aluno[0]).lower().capitalize(), notas, media))
                    cont += 1
                    cad = True
            
            if not(cad) and nome_pesquisado != 'SAIR':
                print('Aluno não encontrado\nTente novamente ou digite SAIR para voltar ao menu inicial')
            elif nome_pesquisado == 'SAIR':
                cont += 1
        
def media_turma(ficha):
    print('\nMÉDIA DA TURMA\n') 
    cont = 0 
    while cont < 1:                
        if len(ficha) <= 0:
            print('Ficha ainda não possui alunos cadastrados.')
            cont += 1
        else:     
            media_turma = 0
            for aluno in ficha:  
                for media in aluno[2]:
                    media_turma += media
            media_turma /= len(ficha)
            cont += 1
            print('A media da turma é {0:.2f}\n'.format(media_turma))
    
def melhor_aluno(ficha):
    print('\nMELHOR ALUNO\n') 
    cont = 0 
    
    while cont < 1:
        if len(ficha) <= 0:
            print('Ficha ainda não possui alunos cadastrados.')
            cont += 1
        else:
            maior = 0       
            for aluno in ficha:                        
                for media in aluno[2]:
                    if maior < media:
                        maior = media
            for aluno in ficha:             
                notas = str()
                for nota in aluno[1]:                                
                    notas += str(nota) + " "
                for media in aluno[2]:
                    if maior == media:                                                        
                        print('{0}. Notas: {1}. Media: {2:.2f}'.format(str(aluno[0]).lower().capitalize(), notas, media))
                    cont += 1
                
            print()

def classificacao_alfabetica(ficha):
    print('\nALUNOS EM ORDEM ALFABÉTICA\n')
    if len(ficha) <= 0:
       print('Ficha ainda não possui alunos cadastrados.\n')
    else:
        pos = 0
        while pos < len(ficha):
            pos2 = pos
            while (ficha[pos2][0] < ficha[pos2 - 1][0]) and pos2 > 0 :
                aux = ficha[pos2]
                ficha[pos2] = ficha[pos2 - 1]
                ficha[pos2 - 1] = aux
                pos2 -= 1
            pos += 1

        for aluno in ficha:
            if len(aluno[1]) > 0:
                notas = str()
                media = 0

                for nota in aluno[1]:
                    notas += str(nota) + ' '
                for nota in aluno[2]:
                    media += nota
            else:
                media = 0
                notas = '- '
                        
            print('Nome: {0} Notas: {1} Média: {2:.2f}'.format(aluno[0], notas, media))   
    
    print()

def classificacao_media(ficha):
    print('\nALUNOS CLASSIFICADOS POR MEDIA\n')
    if len(ficha) <= 0:
        print('Ficha ainda não possui alunos cadastrados.\n')
    else:
        pos = 0
        while pos < len(ficha):
            pos2 = pos
            while (ficha[pos2][2] > ficha[pos2 - 1][2]) and pos2 > 0 :
                aux = ficha[pos2]
                ficha[pos2] = ficha[pos2 - 1]
                ficha[pos2 - 1] = aux
                pos2 -= 1
            pos += 1
    
        for aluno in ficha:
            if len(aluno[1]) > 0:
                notas = str()
                media = 0
               
                for nota in aluno[1]:
                    notas += str(nota) + ' '
                    
                for nota in aluno[2]:
                    media += nota
            else:
                notas = '- '
                media = 0
            print('Nome: {0} Notas: {1} Média: {2:.2f}'.format(str(aluno[0]).lower().capitalize(), notas, media))
    
    print()

def aprovados(ficha):

    print('\nAPROVADOS POR MEDIA\n')
    cont = 0
    while cont < 1:
        if len(ficha) <= 0:
            print('Ficha ainda não possui alunos cadastrados.\n')
            cont += 1
        else:
            cad = False
            for aluno in ficha:
                media = 0
                notas = str()
                for nota in aluno[1]:
                    notas += str(nota) + ' '
                for nota in aluno[2]:
                    media += nota        
                if media >= 7:
                    print('{0}. Notas: {1}. Média: {2}'.format(aluno[0], notas, media))            
                    cad = True        
                    cont += 1
            if not(cad):
                print('Não houve alunos aprovados\n')
        
        print()

def alunos_final(ficha):
    print('\nALUNOS NA FINAL\n')
    cont = 0
    while cont < 1:
        if len(ficha) <= 0:
            print('Ficha ainda não possui alunos cadastrados.\n')
            cont += 1
        else:
            cad = False
            for aluno in ficha:
                media = 0
                notas = str()
                for nota in aluno[1]:
                    notas += str(nota) + ' '
                for nota in aluno[2]:
                    media += nota        
                if 5 <= media < 7:
                    print('{0}. Notas: {1}. Média: {2}'.format(aluno[0], notas, media))            
                    cad = True        
                    
            if not(cad):
                print('Não houve alunos na final\n')
        cont += 1

def reprovados(ficha):
    print('\nALUNOS REPROVADOS\n')
    cont = 0
    while cont < 1:
        if len(ficha) <= 0:
            print('Ficha ainda não possui alunos cadastrados.\n')
            cont += 1
        else:
            cad = False
            for aluno in ficha:
                if len(aluno[1]) > 0:
                    media = 0
                    notas = str()
                    for nota in aluno[1]:
                        notas += str(nota) + ' '
                    for nota in aluno[2]:
                        media += nota        
                    if  media < 5:
                        print('{0}. Notas: {1}. Média: {2}'.format(aluno[0], notas, media))            
                        cad = True     
                    
            if not(cad):
                print('Não houveram alunos reprovados\n')
        cont += 1
        
def salvar_json(ficha) :
    
    lista_salvar = [
        dict(nome = aluno[0], notas = aluno[1], media = aluno[2])
        for aluno in ficha
    ]

    dict_salvar = {"Ficha": lista_salvar}
    dict_salvar = json.dumps(dict_salvar, indent = 4, sort_keys = False)

    try:
        arquivo_json = open("dados.json", "w")
        arquivo_json.write(dict_salvar)
        arquivo_json.close()

    except Exception as erro:
        print('Ocorreu um erro ao carregar o arquivo.')
        print('O erro é: {}'.format(erro))

def importar_json(ficha):
    arquivo_json = open('dados.json', 'r')
    dados_json = json.load(arquivo_json)
    alunos = dados_json['Ficha']

    try :
        for aluno in alunos :
            auxiliar.append(aluno['nome'])
            auxiliar.append(aluno['notas'])
            auxiliar.append(aluno['media'])
            ficha.append(auxiliar[:])
            auxiliar.clear()
    except Exception as erro:
        print('Ocorreu um erro')
        print(f'O erro é {erro}')