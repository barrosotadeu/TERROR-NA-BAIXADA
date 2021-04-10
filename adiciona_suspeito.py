suspeitos = {} #dicionário com nomes de suspeitos e uma breve descrição. Conforme



def adicionaSuspeito(suspeito, descricao):    #essa função irá adicionar suspeitos e suas descrições ao dicionário
    suspeitos.setdefault(suspeito, descricao)
    print(f'{suspeito} foi adicionado à sua lista de suspeitos!')
    print(f'Descrição: {descricao}\n\n')
    print('Sua lista de suspeitos: ' + ', '.join(list(suspeitos.keys())) + '.\n\n')
    print('\n\n')