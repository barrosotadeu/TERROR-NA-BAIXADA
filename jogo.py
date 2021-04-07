import time, random, sys, pyperclip

suspeitos = {} #dicionário com nomes de suspeitos e uma breve descrição. Conforme

 
 
def adicionaSuspeito(suspeito, descricao):    #essa função irá adicionar suspeitos e suas descrições ao dicionário
    suspeitos.setdefault(suspeito, descricao)
    print(f'{suspeito} foi adicionado à sua lista de suspeitos!')
    print(f'Descrição: {descricao}\n\n')
    print('Sua lista de suspeitos: ' + ', '.join(list(suspeitos.keys())) + '.\n\n')
    print('\n\n')
     
    

itens =[]  #lista de itens que serão coletados ao longo jogo. O fato do jogador coletar um determinado item poderá acarretar mudanças na história.

#essa função irá adicionar itens coletados à lista e printará um aviso para o jogador

def adicionaItem(item):
    itens.append(item)
    print(f"O item \'{item}\' foi adicionado ao seu inventário!")
    print("Sua lista de itens: "  +  ', '.join(itens) + ".\n \n")



#FUNÇÕES DE DIÁLOGOS CAPÍTULO 1: Essas funções irão imprimir diálogos que variarem conforme as decisões tomadas durante o jogo.
# essa função printa os diálogos de acordo com a sua escolha de levar carlinhos junto com você, logo após sua decisão de levá-lo ou não
def cap1_dialogo1(x):
    if x.strip().lower() == 's':
        print("""
        JOAO OSÓRIO: Beleza, Carlinhos?. Vamo andando, pode entrar no carro.
        CARLINHOS:   Tô na área, meu cumpadi. Aproveita e bota aquele dire straits pro pai.
        JOÃO OSÓRIO: Isso é que é som, meu parceiro. Então, Carlinhos, ainda não tive tempo de ler seu relatório. O que você descobriu de interessante?
        CARLINHOS:   Pois é, meu chefe. Deu aquela olhada no face e instagram, sabe como é. Parece que a menina namorava sério com um cara aí, tavam pra casar até.
                     Moço direito, evangélico também, não era desses zé droguinha.Diogo, o nome dele. Mas sabe como é, meio ciumento, a julgar por certos comentários nas postagens da moça.
        JOÃO OSÓRIO: Você acha que pode ter sido um crime passional?
        CARLINHOS:   Bom, acho que não podemos descartar a possibilidade. Mas até o momento nada concreto.
        JOÃO OSÓRIO: E o que mais você tem pra me falar?
        CARLINHOS:   Bom, não muito coisa. A menina era quietinha, sabe. Não é igual a maioria das de hoje em dia. Era mulher de igreja, fiel mesmo.
                     Agora, essa igreja que ela frequentava....
        JOÃO OSÓRIO: É uma dessas metida em escândalo, é?
        CARLINHOS:   Sim, Igreja Convenção de Jesus Cristo. Tava envolvida num esquema de exploração de fiéis e e lavagem de dinheiro um tempo atras.
                     E um pastor dessa igreja, um tal de Santiago, foi pego recentemente fazendo uma "festinha" particular com as varoas de uma congregação de um outro município da baixada.
        JOÃO OSÓRIO: Mostrou o "varão" pras elas hehehe. Desculpe, Carlinhos. Não pude resistir.
        CARLINHOS:   Jã estou acostumado com o seu jeito brincalhão, João...
        JOÃO OSÓRIO: Carlinhos, chegamos. Vamos descer e investigar.
            """)
        adicionaSuspeito('Diogo', 'Namorado de Camile. Aparentemente, um jovem de bem, embora um pouco ciumento. Terá sido um crime passional?')
        adicionaSuspeito('Pastor Santiago', 'Pastor da Igreja Convenção de Jesus Cristo, denominação neopentecostal muito popular na região da baixada Fluminense. Recentemente, foi acusado de envolvimento em um escândalo sexual com fiéis. Será que está envolvido com o caso de Camile?')
    elif x.strip().lower() == 'n':
        print('''
        JOÃO OSÓRIO: Esse Carlinhos é um puta mala. Sujeito enrolado que só, ia é atrapalhar minha investigação.
                     Vou dar uma olhada no relatório dele. Dessas coisas de fofocar da vida das pessoas na internet ele entende. o Safado passa o dia no zap...
                     Hnn... Namorado ciumento? Um crime passional, talvez? E essa igreja? Tem umas coisas estranhas né... Vou investigar isso tudo.

                    Bom, cheguei no local do crime. Hora de sair do carro''')
        print('\n\n')            
        adicionaSuspeito('Diogo', 'Namorado de Camile. Aparentemente, um jovem de bem, embora um pouco ciumento. Terá sido um crime passional?')
        adicionaSuspeito('Pastor Santiago', 'Pastor da Igreja Convenção de Jesus Cristo, denominação neopentecostal muito popular na região da baixada Fluminense. Recentemente, foi acusado de envolvimento em um escândalo sexual com fiéis. Será que está envolvido com o caso de Camile?')

#Diálogo impresso logo após à chegada a cena do crime. Irá variar de acordo com a sua escolha de levar o carlinhos ou não.
def cap1_dialogo2(x):
    if x == True:
        print('''
     CARLINHOS:   João, por onde nós vamos começar a vascular?
     JOÃO OSÓRIO: Olha, temos que olhar o corpo e ver se achamos algum tipo de marca que indique como o assassinato ocorreu.
                  Temos que colher também as impressões digitais no corpo e também nos objetos ao redor.Aliás, os objetos podem revelar algo sobre o crime...
     CARLINHOS:   Beleza, João. Mas não esquece de dar uma boa olhada nos bolsos da calça dela, hein. Tô com um palpite que lá pode ter algo.''')
    else:
        print('''
     JOÃO OSÓRIO: Hora de começar a vascular.
                  Vou olhar se tem marcas no corpo que possam ajudar a identificar a forma como o assassinato foi realizado.
                  Vou também procurar por objetos que possam estar relacionados com o crime, além de coletar as impressões digitais.''')



def cap1_dialogo3(x):
    while True:
        if x == True:
            coisas_para_investigar = 3
            escolha_do_jogador = input("O que você irá fazer primeiro? Olhar os (b)olsos, pegar as (i)mpressões digitais ou procurar por (m)arcas ou objetos? Aperte b, i ou m para decidir: ")
            while escolha_do_jogador.strip().lower() != 'b' and escolha_do_jogador.strip().lower() != 'i' and escolha_do_jogador.strip().lower() != 'm':
                print('''
      CARLINHOS: João, cê tá doido? Para de viajar e vamo logo olhar disso direito''')
                escolha_do_jogador = input("O que você irá fazer primeiro? Olhar os (b)olsos, pegar as (i)mpressões digitais ou procurar por (m)arcas ou objetos? Aperte b, i ou m para decidir: ")
            if escolha_do_jogador.strip().lower() == 'b':
                print('''
      JOÃO OSÓRIO: Olha, tem um papel no bolso dela. Vamos ver do que se trata.
                   hnnn... parece ser uma mensagem...

      CARTA NO BOLSO DE CAMILE: A ALMA DESSA JOVEM FOI OFERECIDA POR NÓS AO NOSSO SENHOR LÚCIFER.
                                AQUELES QUE FICAREM NO NOSSO CAMINHO TERÃO O MESMO DESTINO.


                                ASSINADO: F.R

      CARLINHOS: Uma mensagem assinada pela Falange Rubra. Parece que o assassinato fez parte de um tipo de ritual satânico.
      JOÃO OSÓRIO: Eu não sei se podemos confiar plenamente no que está escrito aí. Pode ser alguém usando o nome deles pra confundir nossa investigação.
      CARLINHOS : Não sei não, João. Esses vagabundos são capazes de tudo.\n \n''')
                adicionaItem('carta')
                coisas_para_investigar = 2
                escolha_do_jogador = input("O que você irá fazer agora? Pegar as (i)mpressões digitais ou procurar por (m)arcas ou objetos? Aperte i ou m para decidir: ")
                while escolha_do_jogador.strip().lower() != 'i' and escolha_do_jogador.strip().lower() != 'm':
                    print('''
      CARLINHOS: João, cê tá doido? Para de viajar e vamo logo olhar isso direito''')
                    escolha_do_jogador = input("O que você irá fazer agora? Pegar as (i)mpressões digitais ou procurar por (m)arcas ou objetos? Aperte i ou m para decidir: ")
                if escolha_do_jogador.strip().lower() == 'i':
                    print('''
      JOÃO OSÓRIO: Hora de coletar as impressões digitais para levarmos para o Borges analisar na delegacia. Certamente vamos descobrir alguma coisa. \n \n''')
                    adicionaItem('impressões digitais no corpo da camile')
                    coisas_para_investigar = 1
                    escolha_do_jogador = input("Agora só falta procurar por (m)arcas e objetos. Aperte m para procurar: ")
                    while escolha_do_jogador.strip().lower() != 'm':
                        print('''
      CARLINHOS: João, cê tá doido? Para de viajar e vamo logo olhar isso direito''')
                        escolha_do_jogador = input("Agora só falta procurar por (m)arcas e objetos. Aperte m para procurar: ")
                    if escolha_do_jogador.strip().lower() == 'm':
                        print('''
      JOÃO OSÓRIO: Hnnn...Podemos ver marcas nas cordas e no pescoço. Ela provavelente foi esfaqueada.
                   Há também marcas nos pulsos, o que pode indicar que ela foi amarrada.
                   Hnnn... o que é isso? Uma faca ensaguentada próxima ao corpo... e luvas?
                   Vou coletar estes objetos. \n \n''')
                        adicionaItem('faca')
                        adicionaItem('luvas')
                        coisas_para_investigar = 0
                elif escolha_do_jogador.strip().lower() == 'm':
                    print('''
      JOÃO OSÓRIO: Hnnn...Podemos ver marcas nas cordas e no pescoço. Ela provavelente foi esfaqueada.
                   Há também marcas nos pulsos, o que pode indicar que ela foi amarrada.
                   Hnnn... o que é isso? Uma faca ensaguentada próxima ao corpo... e luvas?
                   Vou coletar estes objetos. \n \n''')
                    adicionaItem('faca')
                    adicionaItem('luva')
                    coisas_para_investigar = 1
                    escolha_do_jogador = input('Agora só falta pegar as impressões. Aperte i para coletá-las: ')
                    while escolha_do_jogador.strip().lower() != 'i':
                        print('''
      CARLINHOS: João, cê tá doido? Para de viajar e vamo logo olhar isso direito''')
                        escolha_do_jogador = input('Agora só falta pegar as impressões. Aperte i para coletá-las: ')
                    if escolha_do_jogador.strip().lower() == 'i':
                        print('''
      JOÃO OSÓRIO: Hora de coletar as impressões digitais para levarmos para o Borges analisar na delegacia. Certamente vamos descobrir alguma coisa. \n \n''')
                        adicionaItem('impressões digitais no corpo da camile')
                        coisas_para_investigar = 0
            elif escolha_do_jogador.strip().lower() == 'i':
                print('''
      JOÃO OSÓRIO: Hora de coletar as impressões digitais para levarmos para o Borges analisar na delegacia. Certamente vamos descobrir alguma coisa. \n \n''')
                adicionaItem('impressões digitais no corpo da camile')
                coisas_para_investigar = 2
                escolha_do_jogador = input("O que você irá fazer agora? Olhar nos (b)olsos da jovem ou procurar por (m)arcas ou objetos? Aperte b ou m para decidir: ")
                while escolha_do_jogador.strip().lower() != 'b' and escolha_do_jogador != 'm':
                    print('''
      CARLINHOS: João, cê tá doido? Para de viajar e vamo logo olhar isso direito''')
                    escolha_do_jogador = input("O que você irá fazer agora? Olhar nos (b)olsos da jovem ou procurar por (m)arcas ou objetos? Aperte b ou m para decidir: ")
                if escolha_do_jogador.strip().lower() == 'b':
                    print('''
      JOÃO OSÓRIO: Olha, tem um papel no bolso dela. Vamos ver do que se trata.
                   hnnn... parece ser uma mensagem...

      CARTA NO BOLSO DE CAMILE: A ALMA DESSA JOVEM FOI OFERECIDA POR NÓS AO NOSSO SENHOR LÚCIFER.
                                AQUELES QUE FICAREM NO NOSSO CAMINHO TERÃO O MESMO DESTINO.


                                ASSINADO: F.R

      CARLINHOS: Uma mensagem assinada pela Falange Rubra. Parece que o assassinato fez parte de um tipo de ritual satânico.
      JOÃO OSÓRIO: Eu não sei se podemos confiar plenamente no que está escrito aí. Pode ser alguém usando o nome deles pra confundir nossa investigação.
      CARLINHOS : Não sei não, João. Esses vagabundos são capazes de tudo.\n \n''')
                    print('A carta foi adicionada ao seu inventário de itens!')
                    adicionaItem('carta')
                    coisas_para_investigar = 1
                    escolha_do_jogador = input("Agora só falta procurar por (m)arcas e objetos. Aperte m para procurar: ")
                    while escolha_do_jogador.strip().lower() != 'm':
                        print('''
      CARLINHOS: João, cê tá doido? Para de viajar e vamo logo olhar isso direito''')
                        escolha_do_jogador = input("Agora só falta procurar por (m)arcas e objetos. Aperte m para procurar: ")
                    if escolha_do_jogador.strip().lower() == 'm':
                        print('''
      JOÃO OSÓRIO: Hnnn...Podemos ver marcas nas cordas e no pescoço. Ela provavelente foi esfaqueada.
                   Há também marcas nos pulsos, o que pode indicar que ela foi amarrada.
                   Hnnn... o que é isso? Uma faca ensaguentada próxima ao corpo... e luvas?
                   Vou coletar estes objetos. \n \n''')
                        adicionaItem('faca')
                        adicionaItem('luvas')
                        coisas_para_investigar = 0
                elif escolha_do_jogador.strip().lower() == 'm':
                    print('''
      JOÃO OSÓRIO: Hnnn...Podemos ver marcas nas cordas e no pescoço. Ela provavelente foi esfaqueada.
                   Há também marcas nos pulsos, o que pode indicar que ela foi amarrada.
                   Hnnn... o que é isso? Uma faca ensaguentada próxima ao corpo... e luvas?
                   Vou coletar estes objetos. \n \n''')
                    adicionaItem('faca')
                    adicionaItem('luvas')
                    coisas_para_investigar = 1
                    escolha_do_jogador = input("Agora só falta procurar por pistas nos (b)olsos da jovem. Aperte b para procurar: ")
                    while escolha_do_jogador.strip().lower() != 'b':
                        print('''
      CARLINHOS: João, cê tá doido? Para de viajar e vamo logo olhar isso direito''')
                        escolha_do_jogador = input("Agora só falta procurar por pistas nos (b)olsos da jovem. Aperte b para procurar: ")
                    if escolha_do_jogador.strip().lower() == 'b':
                        print('''
      JOÃO OSÓRIO: Olha, tem um papel no bolso dela. Vamos ver do que se trata.
                   hnnn... parece ser uma mensagem...

      CARTA NO BOLSO DE CAMILE: A ALMA DESSA JOVEM FOI OFERECIDA POR NÓS AO NOSSO SENHOR LÚCIFER.
                                AQUELES QUE FICAREM NO NOSSO CAMINHO TERÃO O MESMO DESTINO.


                                ASSINADO: F.R

      CARLINHOS: Uma mensagem assinada pela Falange Rubra. Parece que o assassinato fez parte de um tipo de ritual satânico.
      JOÃO OSÓRIO: Eu não sei se podemos confiar plenamente no que está escrito aí. Pode ser alguém usando o nome deles pra confundir nossa investigação.
      CARLINHOS : Não sei não, João. Esses vagabundos são capazes de tudo.\n \n''')
                        adicionaItem('carta')
                        coisas_para_investigar = 0
            elif escolha_do_jogador.strip().lower() == 'm':
                print('''
      JOÃO OSÓRIO: Hnnn...Podemos ver marcas nas cordas e no pescoço. Ela provavelente foi esfaqueada.
                   Há também marcas nos pulsos, o que pode indicar que ela foi amarrada.
                   Hnnn... o que é isso? Uma faca ensaguentada próxima ao corpo... e luvas?
                   Vou coletar estes objetos. \n \n''')
                adicionaItem('faca')
                adicionaItem('luvas')
                coisas_para_investigar = 2
                escolha_do_jogador = input("O que você irá fazer agora? Olhar nos (b)olsos da jovem ou coletar as (i)mpressões digitais? Aperte b ou i para decidir ")
                while escolha_do_jogador.strip().lower() != 'b' and escolha_do_jogador.lower() != 'i':
                    print('''
      CARLINHOS: João, cê tá doido? Para de viajar e vamo logo olhar isso direito''')
                    escolha_do_jogador = input("O que você irá fazer agora? Olhar nos (b)olsos da jovem ou coletar as (i)mpressões digitais? Aperte b ou i para decidir ")
                if escolha_do_jogador.strip().lower() == 'b':
                    print('''
      JOÃO OSÓRIO: Olha, tem um papel no bolso dela. Vamos ver do que se trata.
                   hnnn... parece ser uma mensagem...

      CARTA NO BOLSO DE CAMILE: A ALMA DESSA JOVEM FOI OFERECIDA POR NÓS AO NOSSO SENHOR LÚCIFER.
                                AQUELES QUE FICAREM NO NOSSO CAMINHO TERÃO O MESMO DESTINO.


                                ASSINADO: F.R

      CARLINHOS: Uma mensagem assinada pela Falange Rubra. Parece que o assassinato fez parte de um tipo de ritual satânico.
      JOÃO OSÓRIO: Eu não sei se podemos confiar plenamente no que está escrito aí. Pode ser alguém usando o nome deles pra confundir nossa investigação.
      CARLINHOS : Não sei não, João. Esses vagabundos são capazes de tudo.\n \n''')
                    adicionaItem('carta')
                    coisas_para_investigar = 1
                    escolha_do_jogador = input('Agora só falta pegar as impressões. Aperte i para coletá-las: ')
                    while escolha_do_jogador.strip().lower() != 'i':
                        print('''
      CARLINHOS: João, cê tá doido? Para de viajar e vamo logo olhar isso direito''')
                    if escolha_do_jogador.strip().lower() == 'i':
                        print('''
      JOÃO OSÓRIO: Hora de coletar as impressões digitais para levarmos para o Borges analisar na delegacia. Certamente vamos descobrir alguma coisa. \n \n''')
                        adicionaItem('impressões digitais no corpo da camile')
                        coisas_para_investigar = 0
                elif escolha_do_jogador.strip().lower() == 'i':
                        print('''
      JOÃO OSÓRIO: Hora de coletar as impressões digitais para levarmos para o Borges analisar na delegacia. Certamente vamos descobrir alguma coisa. \n \n''')
                        adicionaItem('impressões digitais no corpo da camile')
                        coisas_para_investigar = 1
                        escolha_do_jogador = input("Agora só falta procurar por pistas nos (b)olsos da jovem. Aperte b para procurar: ")
                        while escolha_do_jogador.strip().lower() != 'b':
                            print('''
      CARLINHOS: João, cê tá doido? Para de viajar e vamo logo olhar isso direito''')
                            input("Agora só falta procurar por pistas nos (b)olsos da jovem. Aperte b para procurar: ")
                        if escolha_do_jogador.strip().lower() == 'b':
                            print('''
      JOÃO OSÓRIO: Olha, tem um papel no bolso dela. Vamos ver do que se trata.
                   hnnn... parece ser uma mensagem...

      CARTA NO BOLSO DE CAMILE: A ALMA DESSA JOVEM FOI OFERECIDA POR NÓS AO NOSSO SENHOR LÚCIFER.
                                AQUELES QUE FICAREM NO NOSSO CAMINHO TERÃO O MESMO DESTINO.


                                ASSINADO: F.R

      CARLINHOS: Uma mensagem assinada pela Falange Rubra. Parece que o assassinato fez parte de um tipo de ritual satânico.
      JOÃO OSÓRIO: Eu não sei se podemos confiar plenamente no que está escrito aí. Pode ser alguém usando o nome deles pra confundir nossa investigação.
      CARLINHOS : Não sei não, João. Esses vagabundos são capazes de tudo.\n \n''')
                            adicionaItem('carta')
                            coisas_para_investigar = 0


            if coisas_para_investigar == 0:
                break

        else:
            coisas_para_investigar = 2
            escolha_do_jogador = input("O que você irá fazer primeiro? Pegar as (i)mpressões digitais ou procurar por (m)arcas ou objetos? Aperte i ou m para decidir: ")
            while escolha_do_jogador.strip().lower() != 'i' and escolha_do_jogador.strip().lower() != 'm':
                print('''
      JOÃO OSÓRIO: Não é hora para ficar com o pensamento vagando... Preciso me concentar na investigação.''')
                escolha_do_jogador = input("O que você irá fazer primeiro? Pegar as (i)mpressões digitais ou procurar por (m)arcas ou objetos? Aperte i ou m para decidir: ")
            if escolha_do_jogador.strip().lower() == 'i':
                print('''
      JOÃO OSÓRIO: Hora de coletar as impressões digitais para levarmos para o Borges analisar na delegacia. Certamente vamos descobrir alguma coisa. \n \n''')
                adicionaItem('impressões digitais no corpo da camile')
                coisas_para_investigar = 1
                escolha_do_jogador = input("Agora só falta procurar por (m)arcas e objetos. Aperte m para procurar: ")
                while escolha_do_jogador.strip().lower() != 'm':
                    print('''
      JOÃO OSÓRIO: Não é hora para ficar com o pensamento vagando... Preciso me concentar na investigação.''')
                    escolha_do_jogador = input("Agora só falta procurar por (m)arcas e objetos. Aperte m para procurar: ")
                if escolha_do_jogador.strip().lower() == 'm':
                    print('''
      JOÃO OSÓRIO: Hnnn...Podemos ver marcas nas cordas e no pescoço. Ela provavelente foi esfaqueada.
                   Há também marcas nos pulsos, o que pode indicar que ela foi amarrada.
                   Hnnn... o que é isso? Uma faca ensaguentada próxima ao corpo... e luvas?
                   Vou coletar estes objetos. \n \n''')
                    adicionaItem('faca')
                    adicionaItem('luvas')
                    coisas_para_investigar = 0
            elif escolha_do_jogador.strip().lower() == 'm':
                print('''JOÃO OSÓRIO: Hnnn...Podemos ver marcas nas cordas e no pescoço. Ela provavelente foi esfaqueada.
                   Há também marcas nos pulsos, o que pode indicar que ela foi amarrada.
                   Hnnn... o que é isso? Uma faca ensaguentada próxima ao corpo... e luvas?
                   Vou coletar estes objetos. \n \n''')
                adicionaItem('faca')
                adicionaItem('luvas')
                escolha_do_jogador = input('Agora só falta pegar as impressões. Aperte i para coletá-las: ')
                while escolha_do_jogador.strip().lower() != 'i':
                    print('''JOÃO OSÓRIO: Não é hora para ficar com o pensamento vagando... Preciso me concentar na investigação.''')
                    escolha_do_jogador = input('Agora só falta pegar as impressões. Aperte i para coletá-las: ')
                if escolha_do_jogador.strip().lower() == 'i':
                    print('''JOÃO OSÓRIO: Hora de coletar as impressões digitais para levarmos para o Borges analisar na delegacia. Certamente vamos descobrir alguma coisa. \n \n''')
                    adicionaItem('impressões digitais no corpo da camile')
                    coisas_para_investigar = 0
            if coisas_para_investigar == 0:
                break

def cap1_dialogo4(x):
    while True:
        if x == True:
            escolhas = 3
            print('''
            JOÃO OSÓRIO: Ok, carlinhos. Agora temos que prosseguir nossa investigação à luz das evidências coletadas
            e dos suspeitos que temos. Preciso fazer uma visita ao namorado e à igreja, ambos mencionados no seu relatório.
            Também precisamos levar as impressões digitais, a faca e a luva para o Bores analisar. O que você acha, Carlinhos?
            Onde devemos ir primeiro?
            CARLINHOS: João, acho que devemos ir atrás da Falange Rubra logo. Se o que está escrito na carta for verdade,
            só Jesus sabe que tipo de atrocidade eles estão fazendo por aí. Parece que eles tão metido com esse negócio de ritual
            satânico. Talvez o pastar da igreja saiba alguma coisa.
            ''')
            escolha_do_jogador = input('O que você irá fazer agora? Levar o material coletado para o (B)orges, ir falar com o (n)amorado ou fazer uma visita à (i)greja? Aperte b, n ou i para decidir:')
            while escolha_do_jogador.strip().lower() != 'b' and escolha_do_jogador.strip().lower() != 'n' and escolha_do_jogador.strip().lower() != 'i':
                print('''
                CARLINHOS: Bora, João. Decide longo pra onde nós vamos, campeão. Já falei que na igreja derrepente a gente descobre algo.''')
                escolha_do_jogador = input('O que você irá fazer agora? Levar o material coletado para o (B)orges, ir falar com o (n)amorado ou fazer uma visita à (i)greja? Aperte b, n ou i para decidir:') 
      

#introdução do jogo
print('''TERROR NA BAIXADA FLUMINENSE'''.rjust(100))
print('\n \n \n \n')
time.sleep(2)
print('''
Um terrível crime ocorreu no município de nova iguaçu:
Camile, uma pacata jovem evangélica, foi encontrada morta em sua residência, no bairro de cabuçu.
Na cena do crime, óbvios indícios de um brutal assassinato.
Mas quem e por qual motivo alguém cometeria tal crime contra essa tão pacata e inocente moça?
Você é João Osório, policial civil  do estado do Rio de Janeiro, e seu dever é investigar esse misterioso crime.''')
time.sleep(1)
#capítulo 1



print("""

DELEGADO TEIXEIRA: Bom dia, João.
JOÃO OSÓRIO: Bom dia, delegado.

DELEGADO TEIXEIRA: João, hoje tenho uma missão especial para você.
                   Uma jovem foi assassinada em nova iguaçu. Moça de família, evangélica. Não tinha envolvimento com coisa errada. Um crime sem explicação.
                   Eu vou mandar você pra investigar.

JOÃO OSÓRIO:       Entendi, delegado. Já temos suspeitos? Será que o grupo de extermínio vingadores está envolvido? Ou a falange rubra?

DELEGADO TEIXEIRA: Não sabemos ainda, João. Mas, ao que tudo indica, ela não era dessas de se meter com vagabundo. O marido é um varão da igreja, garoto bom. Coitado, tá arrasado.

JOÃO OSÓRIO:       Entendido, chefe. Estou me encaminhando agora mesmo para o local do crime.

DELEGADO TEIXEIRA: Tá beleza, João. O carlinhos fez uma pré investigação. Vasculhou a vida da menina, viu redes sociais, essas coisas. Eu tô com o relatório dele aqui, pode pegar.
                   Você quer que eu chame ele pra te acompanhar nessa investigação?""")

while True:
    resposta_carlinhos = input("Responda (s)im ou (n)ão. Aperte s ou n para decidir ")
    if resposta_carlinhos.strip().lower() != 's' and resposta_carlinhos.strip().lower() != 'n':
        print("DELEGADO TEIXEIRA: Responde direito, João. Tá de ressaca?")
        continue

    if resposta_carlinhos.strip().lower() == 's':
        carlinhos = True
        break
    elif resposta_carlinhos.strip().lower() == 'n':
        carlinhos = False
        break

cap1_dialogo1(resposta_carlinhos)

time.sleep(2)

print('A CENA DO CRIME')

print('\n')
print('''
Nosso herói João finalmente chega na cena do crime.
O policial se choca ao ver o corpo inerte e sem vida da jovem estirado no chão. João, porém é um homem da lei e, como tal, precisa ser frio.
Ele se aproxima do cadáver de camile e inicia sua investigação''')

cap1_dialogo2(carlinhos)
print('\n')
print('\n')


cap1_dialogo3(carlinhos)

cap1_dialogo4(carlinhos)
