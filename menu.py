import cadastro
import json
import os

ficha = list()

resposta = 0
print('SISTEMA DE NOTAS PROGRAMAÇÃO I')
nome = input('Bem-vindo, me informe o seu nome: ')
print('{}, o que você deseja fazer?\n'.format(nome))

while resposta != 15:
    cadastro.importar_json(ficha)
     
    while resposta == 0:
        print('SISTEMA DE CADASTRO - PROGRAMAÇÃO I')
        print('-=' * 30)        
        print('1. Adicionar Aluno \n2. Adicionar Nota \n3. Remover Aluno\n4. Remover Nota\n5. Editar Nome Aluno \n6. Editar Nota Aluno\n7. Buscar Aluno Por Nome\n8. Calcular Média da turma\n9. Exibir Melhor Aluno\n10.Exibir Alunos Em Ordem Alfabética\n11.Exibir Aluno Por Ordenados Por Nota\n12.Exibir alunos aprovados por média (>=7)\n13.Exibir Alunos Na Final (>=5)\n14.Exibir Alunos Reprovados (<5)\n15.Encerra o Programa' 
        )
        print('-=' * 30)
        try :
            resposta = int(input('\nselecione a opção desejada: '))
        except Exception as erro:
            print('Ocorreu um erro ao selecionar a resposta')
            print(f'O erro é {erro}')    
        
        if resposta == 1:
            cadastro.cadastro_aluno(ficha)
                                            
        elif resposta == 2:
            cadastro.adicionar_nota(ficha)    
            
        elif resposta == 3:
            cadastro.remover_aluno(ficha)
                   
        elif resposta == 4:
            cadastro.remover_nota(ficha)
            
        elif resposta == 5:
            cadastro.editar_nome(ficha)
            
        elif resposta == 6:
            cadastro.editar_nota(ficha)
            
        elif resposta == 7:
            cadastro.buscar_aluno(ficha)
            
        elif resposta == 8:
            cadastro.media_turma(ficha)
           
        elif resposta == 9:
            cadastro.melhor_aluno(ficha)
              
        elif resposta == 10:
            cadastro.classificacao_alfabetica(ficha)
             
        elif resposta == 11:
            cadastro.classificacao_media(ficha)
                   
        elif resposta == 12:
            cadastro.aprovados(ficha)
            
        elif resposta == 13:
            cadastro.alunos_final(ficha)
         
        elif resposta == 14:
            cadastro.reprovados(ficha)
                     
        elif resposta == 15:
            resp = input('Deseja salvar o contéudo? (S/N)\n')
            if resp in 'Ss':
                cadastro.salvar_json(ficha)
            print('Obrigado por utilizar o programa. Bye bye')
            
        elif resposta not in range(1,16):
            print('\nOpção inválida. Tente novamente\n')
            resposta = 0
            
        if resposta != 15:
            os.system('pause')
            os.system('cls')
            resposta = 0
