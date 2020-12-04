import time, random, sys

def cap1_dialogo1(x):
    if x == 's':
        print("""
        JOAO OSÓRIO: Beleza, Carlinhos?. Vamo andando, pode entrar no carro.
        CARLINHOS:   Tô na área, meu cumpadi. Aproveita e bota aquele dire straits pro pai.
        JOÃO OSÓRIO: Isso é que é som, meu parceiro. Então, Carlinhos, ainda não tive tempo de ler seu relatório. O que você descobriu de interessante?
        CARLINHOS:   Pois é, meu chefe. Deu aquela olhada no face e instagram, sabe como é. Parece que a menina namorava sério com um cara aí, tavam pra casar até.
                     Moço direito, evangélico também, não era desses zé droguinha. Mas sabe como é, meio ciumento, a julgar por certos comentários nas postagens da moça.
        JOÃO OSÓRIO: Você acha que pode ter sido um crime passional?
        CARLINHOS:   Bom, acho que não podemos descartar a possibilidade. Mas até o momento nada concreto.
        JOÃO OSÓRIO: E o que mais você tem pra me falar?
        CARLINHOS:   Bom, não muito coisa. A menina era quietinha, sabe. Não é igual a maioria das de hoje em dia. Era mulher de igreja, fiel mesmo.
                     Agora, essa igreja que ela frequentava....
        JOÃO OSÓRIO: É uma dessas metida em escândalo, é?
        CARLINHOS:   Sim, Igreja Convenção de Jesus Cristo. Tava envolvida num esquema de exploração de fiéis e e lavagem de dinheiro um tempo atras.
                     E um pastor dessa igreja foi pego recentemente fazendo uma "festinha" particular com as varoas de uma congregação de um outro município da baixada.
        JOÃO OSÓRIO: Mostrou o "varão" pras elas hehehe. Desculpe, Carlinhos. Não pude resistir.
        CARLINHOS:   Jã estou acostumado com o seu jeito brincalhão, João...
        JOÃO OSÓRIO: Carlinhos, chegamos. Vamos descer e investigar.
            """)

    elif x == 'n':
        print('''
        JOÃO OSÓRIO: Esse Carlinhos é um puta mala. Sujeito enrolado que só, ia é atrapalhar minha investigação.
                     Vou dar uma olhada no relatório dele. Dessas coisas de fofocar da vida das pessoas na internet ele entende. o Safado passa o dia no zap...
                     Hnn... Namorado ciumento? Um crime passional, talvez? E essa igreja? Tem umas coisas estranhas né... Vou investigar isso tudo.

                    Bom, cheguei no local do crime. Hora de sair do carro''')

print('''TERROR NA BAIXADA FLUMINENSE''')
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
    resposta_carlinhos = input("Responda (s)im ou (n)ão ")
    if resposta_carlinhos != 's' and resposta_carlinhos != 'n':
        print("DELEGADO TEIXEIRA: Responde direito, João. Tá de ressaca?")
        continue

    if resposta_carlinhos == 's':
        carlinhos = True
        break
    elif resposta_carlinhos == 'n':
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

if carlinhos == True:
    print('''
     CARLINHOS:   João, por onde nós vamos começar a vascular?
     JOÃO OSÓRIO: Olha, temos que olhar o corpo e ver se achamos algum tipo de marca que indique como o assassinato ocorreu.
                  Temos que colher também as impressões digitais no corpo e também nos objetos ao redor.Aliás, os objetos podem revelar algo sobre o crime...
     CARLINHOS:   Beleza, João. Mas não esquece de dar uma boa olhada nos bolsos da calça dela, hein. Tô com um palpite que lá pode ter algo''')