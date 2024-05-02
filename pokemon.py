#Começamos o código importando comandos.
import random

import subprocess

#Utilizando o def para criar uma função que da clear no terminal.

def limpar_terminal():
    subprocess.call('cls' if subprocess._mswindows else 'clear', shell=True)

while True:
    #Iniciando o jogo.
    limpar_terminal()
    print(30*'-')
    nome = input('Saudações! O universo pokemon lhe aguarda, os pokemons são como o nosso mundo funciona, são criaturas incriveis.\n\nPara prosseguirmos, me informe o seu nome: \n\n')
    limpar_terminal()
    print(f'\nSeja bem vindo{nome}!!\n' + 30*'-')

    #Aqui começamos com a escolha dos pokemons inciciais criando uma lista  e mais uma estrutura de repetição


    pokemons = []

    while True:
        opcao = input(f'Para iniciar a sua jornada, escolha seu primeiro pokemon, ele será o seu maior aliado!\n\n 1 - Charmander\n 2 - Squirtle\n 3 - Bulbassaur\n\n')

        if opcao != '1' and opcao != '2' and opcao != '3':
            print ('\nOpção inválida\n')
        elif opcao == '1':
            pokemon_inicial = 'Charmander'
            pokemons.append(pokemon_inicial)
            limpar_terminal()
            print(f'{pokemon_inicial}, uma ótima escolha, um pokemon do tipo fogo perfeito para começar a sua jornada!\n')
            break
        elif opcao == '2':
            pokemon_inicial = 'Squirtle'
            pokemons.append(pokemon_inicial)
            limpar_terminal()
            print(f'{pokemon_inicial}, Um pokemon do tipo água, perfeito para pokemons do tipo fogo, com certeza será muito util na sua aventura!!\n')
            break
        elif opcao == '3':
            pokemon_inicial = 'Bulbassaur'
            pokemons.append(pokemon_inicial)
            limpar_terminal()
            print(f'Uau uma escolha ótima, {pokemon_inicial} é um pokemon do tipo natureza que será muito util em sua jornada!\n')
            break
    
    #aqui começaremos a fazer a linha do caminho do jogador, por onde ele irá seguir.

    rota_pokemon = []
    rota = ''

    while True:

        opcao = int(input('Para onde deseja seguir?\n\n1 - Caverna\n2 - Floresta\n3 - pokedex\n4 - Sair do jogo\n\n '))

        if opcao == 1:
            rota = 'Caverna'
            limpar_terminal()
            print('\n Você decidiu ir para a Caverna\n' + 30*'-')
            rota_pokemon = ['Aron', 'Larvitar', 'Geodude',]
        
        elif opcao == 2:
            rota = 'Floresta'
            limpar_terminal()
            print('\n Você decidiu ir para a caverna\n')
            rota_pokemon = ['Odish', 'Caterpie', 'Chikorita']
        
        elif opcao == 3:
            limpar_terminal()
            print(30*'-')
            print(f'\nPokedex - {pokemons}\n')
            print(30*'-')

        elif opcao == 4:
            print('\n Saindo do jogo.')
            print(30*'-')
            break
        else:
            print('Você Não pode sair ainda')
        
        if opcao == 1 or opcao == 2:
            while True:
                
                pokemon_encontrado = rota_pokemon[random.randint(0, len(rota_pokemon) - 1)]
                opcao = int(input(f'\nlocal: {rota}\n\nVocê encontrou um {pokemon_encontrado}!, prosiga com sua escolha?\n\n1 - Capturar\n2 - Ignorar\n\n' ))
                if opcao == 2:
                    print(30*'-')
                    limpar_terminal()
                    print(f'Você ignorou o {pokemon_encontrado}')
                    print(30*'-')
                    break
            
                elif opcao == 1 and rota == 'Floresta':
                    limpar_terminal()
                    tentativas_de_captura = 3
                    capturar = None
                    while tentativas_de_captura > 0:
                        limpar_terminal()
                        print(30*'-')
                        print(f'\nTentando capturar {pokemon_encontrado}\n\ntentativas: {tentativas_de_captura}\n' )
                        probabilidade = random.random()
                            
                        if probabilidade <= 0.5:
                            capturar = True
                            break
                        else:
                            print(30*'-')
                            tentarNovamente = int(input(f'{pokemon_encontrado} fugiu da pokebola!\n\nTentar novamente?\n\n1 - sim\n2 - nao\n\n'))
                            
                            if tentarNovamente == 2:
                                print('\nVocê desistiu!')
                                capturar = False
                                

                                break
                                

                            elif tentarNovamente == 1:
                                limpar_terminal()
                                tentativas_de_captura -= 1
                                
                                if tentativas_de_captura == 0:
                                    limpar_terminal()
                                    capturar = False
                                    break
                                print('\nTentando novamente...\n')
                                
                    
                    if capturar:
                        limpar_terminal()
                        print(f'\nVocê capturou o {pokemon_encontrado}!\n' )
                        print(30*'-')
                        pokemons.append(pokemon_encontrado)
                        break
                    if capturar == False:
                        print(f'\n{pokemon_encontrado} escapou!' )
                        print(30*'-')
                        break
                elif opcao == 1 and rota == 'Caverna':
                    tentativas_de_captura = 3
                    capturar = None
                    while tentativas_de_captura > 0:
                        limpar_terminal()
                        print(30*'-')
                        print(f'\nTentando capturar {pokemon_encontrado}\n\ntentativas: {tentativas_de_captura}\n' )
                        probabilidade = random.random()
                        print(30*'-')
                        if probabilidade <= 0.35:
                            capturar = True
                            break
                        else:
                            
                            tentarNovamente = int(input(f'{pokemon_encontrado} fugiu da pokebola!\n\nTentar novamente?\n\n1 - sim\n2 - nao\n\n'))
                            
                            if tentarNovamente == 2:
                                print(30*'-')
                                print('\nVocê desistiu!')
                                capturar = False
                                print(30*'-')

                                break
                                

                            elif tentarNovamente == 1:
                                
                                tentativas_de_captura -= 1
                                
                                if tentativas_de_captura == 0:
                                    capturar = False
                                    break
                                print('\nTentando novamente...\n')
                                
                    
                    if capturar:
                        limpar_terminal()
                        print(f'\nVocê capturou o {pokemon_encontrado}!\n' )
                        print(30*'-')
                        pokemons.append(pokemon_encontrado)
                        break
                    if capturar == False:
                        limpar_terminal()
                        print(f'\n{pokemon_encontrado} escapou!' )
                        print(30*'-')
                        break
                else:
                    print('Opçao inválida!')
        
    break


