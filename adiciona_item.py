itens =[]  #lista de itens que serão coletados ao longo jogo. O fato do jogador coletar um determinado item poderá acarretar mudanças na história.

#essa função irá adicionar itens coletados à lista e printará um aviso para o jogador

def adicionaItem(item):
    itens.append(item)
    print(f"O item \'{item}\' foi adicionado ao seu inventário!")
    print("Sua lista de itens: "  +  ', '.join(itens) + ".\n \n")