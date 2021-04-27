"""
Grupo 4

Indice:
1. Definição de cores

2. Abertura do display, considerando altura e largura

3. Iniciado a função Clock

4. Carregando para a memória as músicas presentes./
   definido a função para o som das teclas
   
5. Carregando imagens para memória/redimensionando B1,
   referente a imagens, de setas e B3, referente a
   imagem da tela inicial.
   
6. Definida a função para a esfera rodar como sprite

7. Contém os textos de todo o jogo, assim como as funções
   que rodam esses textos.
   
8. Contem as chaves, em texto, que serão colocadas nas fases.

9. Lê valores das setas, Q e enter, retornando se estão ou não
   pressionados.
   
10. Contém as fases do jogos de 0 a 10, essas utilizam-se de
    outros elementos encontrados nos índices 7,8 e 14.4.
    Contendo também, na fase 10, uma varíavel que altera 16.1
    
11. Teclas de fase compreende, exclusivamente, a fase 3.

12. Tela inicial encontra-se dentro do loop de game, e
    aparece quando iniciar estiver em True. Também
    encontra-se a opção de instruções aqui.
    
13. 'O jogo' desenha e passa os sprites da Orbita (6.), também
    fornecendo qual fase deve ser rodada.
    
14. A lista de eventos é definida a cada passagem, sendo apagada
    no começo desse setor. Duas listas são formados: Eventos e
    Respostas.
    
15. Movimentação usa as informações de 9. Para definir a direção
    e quanto a esfera se moverá.
    
16. Regras impede a esfera de passar da tela e muda o limite dos
    sprites, fazendo a imagem mudar.
    
17. Utiliza-se da função relógio para reduzir a velocidade e
    atualiza o display.
    
"""

import pygame
import random

pygame.init()
#________________1.Cores________________

branco = (255,255,255)
vermelho = (255,0,0)
preto = (0,0,0)
cinza_escuro = (50,50,50)
#________________2.Set de display________________

dimensao_tela = [720,480]

tela = pygame.display.set_mode(dimensao_tela)
pygame.display.set_caption("Dark dimension")

posição_x = dimensao_tela[0]/2
posição_y = dimensao_tela[1]/2

#________________3.Set Clock________________

relogio = pygame.time.Clock()
#________________4.Set Musicas________________

soundtrack = pygame.mixer.Sound('musicas/smash_hit_ost_zen_mode.mp3')
soundtrack.set_volume(0.1)

inicial = pygame.mixer.Sound('musicas/inicio.mp3')
inicial.set_volume(0.2)

teclas = pygame.mixer.Sound('musicas/Click.mp3')
teclas.set_volume(0.2)

def som_teclas():
    soundtrack.stop()
    teclas.play(1)
    soundtrack.play(-1)

    
#________________5.Set imagens________________

#
esferas_1 = pygame.image.load('Esferas_180_1.png')
esferas_2 = pygame.image.load('Esferas_180_2.png')
esferas_3 = pygame.image.load('Esferas_180_3.png')
esferas_4 = pygame.image.load('Esferas_180_4.png')
esferas_5 = pygame.image.load('Esferas_180_5.png')
esferas_6 = pygame.image.load('Esferas_180_6.png')
esferas_7 = pygame.image.load('Esferas_180_7.png')
esferas_8 = pygame.image.load('Esferas_180_8.png')
esferas_9 = pygame.image.load('Esferas_180_9.png')
esferas_10 = pygame.image.load('Esferas_180_10.png')
esferas_11 = pygame.image.load('Esferas_180_11.png')
esferas_12 = pygame.image.load('Esferas_180_12.png')
esferas_13 = pygame.image.load('Esferas_180_13.png')
esferas_14 = pygame.image.load('Esferas_180_14.png')
esferas_15 = pygame.image.load('Esferas_180_15.png')

brilhar_0 = pygame.image.load('Transform/Esferas_Shine_0.png')
brilhar_1 = pygame.image.load('Transform/Esferas_Shine_1.png')
brilhar_2 = pygame.image.load('Transform/Esferas_Shine_2.png')
brilhar_3 = pygame.image.load('Transform/Esferas_Shine_3.png')
brilhar_4 = pygame.image.load('Transform/Esferas_Shine_4.png')
brilhar_5 = pygame.image.load('Transform/Esferas_Shine_5.png')
brilhar_6 = pygame.image.load('Transform/Esferas_Shine_6.png')
brilhar_7 = pygame.image.load('Transform/Esferas_Shine_7.png')
brilhar_8 = pygame.image.load('Transform/Esferas_Shine_8.png')
brilhar_9 = pygame.image.load('Transform/Esferas_Shine_9.png')
brilhar_10 = pygame.image.load('Transform/Esferas_Shine_10.png')
brilhar_11 = pygame.image.load('Transform/Esferas_Shine_11.png')
brilhar_12 = pygame.image.load('Transform/Esferas_Shine_12.png')

biblioteca_1 = pygame.image.load('Navigation_keys(1).png')
biblioteca_1 = pygame.transform.scale(biblioteca_1, [120, 100])

biblioteca_2 = pygame.image.load('Coruja(1).png')

biblioteca_3 = pygame.image.load('universe.jpg')
biblioteca_3 = pygame.transform.scale(biblioteca_3, [200, 200])


lista_esfera = [esferas_1,esferas_2,esferas_3,esferas_4,
                esferas_5,esferas_6,esferas_7,esferas_8,
                esferas_9,esferas_10,esferas_11,esferas_12,
                esferas_13,esferas_14,esferas_15,
                brilhar_0,brilhar_1,brilhar_2,brilhar_3,
                brilhar_4,brilhar_5,brilhar_6,brilhar_7,
                brilhar_8,brilhar_9,brilhar_10,brilhar_11,
                brilhar_12]
quantidade_sprite = len(lista_esfera)

# 5.1-> Centro de imagens B1 e B3
centro1 = []
centro3 = []
for i in biblioteca_3.get_rect():
    centro3.append(i)
for i in biblioteca_1.get_rect():
    centro1.append(i)

#________________6.Formas________________
        
tamanho = 10    
def orbitas():
    global largura
    global altura 
    largura = 259
    altura = 259
    tela.blit(lista_esfera[sprite],(posição_x-(largura/2),posição_y-(altura/2)))
    
#________________7.Textos________________

mensagem = ["Olá... tente... espaço","sinto que está perdido",
            "Mas já sabe se mover...","Isso é bom...",
            "se for mais fácil...","segure Q","Agora podemos seguir",
            "Talvez...","eu consiga facilitar...","Melhor?",
            "Acredito que sim...","Agora ouça...","Aqui... não é seguro",
            "Não sei como veio parar aqui","Mas tem de achar a chave!",
            "encontre a chave...","Fim da fase",
            
            "Fase 2: Repita", "Muito bem...","a primeira porta foi aberta",
            "está indo bem...","mas não deve parar","Outra chave está perdida",
            "encontre-a","Fim da fase",
            
            "Fase 3: Una","Cada passo é um passo...", "As vezes",
            "o começo será arduo",
            "mas veja...", "podia ser pior","imagine se tivesse mais de uma?",
            "Opa, acho que falei demais hihi","Fim da fase",

            "Fase 4: Tente","Nunca duvidei!","ta...quando apertou o primeiro",
            "até duvidei",
            "mas sabia que conseguiria!","...sei que estamos chegando",
            "quase posso sentir","uma pitada do fim...",
            "Mas... temos um problema","Eles sabem que estamos aqui",
            "A chave... ela se move!","Boa sorte...", "Fim da fase",

            "Fase 5: Escolha","Há muitas coisas curiosas aqui","Notou?",
            "Veja... Não é apenas preto",
            "Você é a luz desse lugar!","Que poético...","Ou pelo menos seria",
            "Se não estivesse preso aqui","Por isso...","Sem chave dessa vez",
            "Me responda de forma simples","Você quer sair daqui?","Sim ou Não",
            "Ok... vamos recomeçar","Então vamos continuar!",

            "Fase 6: Reconheça","O quê?","Ah, isso de chave e tudo mais",
            "É... elas nunca foram necessárias","Sabe... eu tentei",
            "Realmente tentei tornar isso mais fácil",
            "Mas eu prevejo que continuará",
            "Retomando ao começo","Sendo tão simples achar a saída",
            "Apenas me diga","O que é isso?","Fim da fase",

            "Fase 7: Ouça","A coruja... ela é uma base muito boa",
            "para o que quero explicar",
            "Uma ave observadora","tratada como a sabedoria",
            "é sempre isso que buscamos","Mas não importe o quão corra atrás",
            "nunca alcaçará...","Por isso, aceitamos nossos erros",
            "E mesmo que não saiba responder a próxima","não se preocupe",
            "Apenas tente novamente","veja... sequer notou os números",
            "que passou por toda essa fase...","elas são sua saída",
            "diga-me","Quais foram?","Viu... não foi tão ruim",
            "Agora calma... leia tudo e responda",
            "Some o primeio com o ultimo","eleve a",
            "soma do segundo com o penultimo","E então me diga",
            "Qual a chave da sabedoria?",
            "Não era bem isso o que eu esperava...","Fim da fase",

            "Fase 8: Perdoe","Okay... desculpa","Foi intensional a pergunta passada",
            "Eu não quero que fique irritado","ou algo do tipo","Apenas...",
            "Queria que ficasse um pouco mais","Estamos perto do fim",
            "E... também não quero","que seu esforço seja em vão",
            "Aquela conta que lhe pedi...","só... me diga o resultado",
            "Fim da fase",

            "Fase 9: Não esqueça","É isso...","Este é o fim",
            "O ultimo dos desafios",
            "Assim que terminar, poderá ir","Não quero que seja difícil",
            "Só que... represente seu tempo aqui","Por isso...",
            "Lembra das letras que pegou?","Faltou uma",
            "Ela esteve em algum lugar","Mas não sei onde","Porém...",
            "Não precisa voltar","Ela completa uma palavra",
            "E só dela que preciso","Qual é... a palavra?", "Obrigado..."

            "Seu tempo foi precioso","E mesmo assim","Insisto em perguntar",
            "Você quer ficar?","Sim ou Não?","Eu gosto de você, vamos de novo",
            "Okay... já não há limites... Ande, vá","Fim"]
tamanho_mensagem = len(mensagem)-1


mensagem1 = 0
def Informações_texto():
    global cor
    global tamanho_fonte
    global posição_txt_y
    cor = cinza_escuro
    tamanho_fonte = 30
    posição_txt_y = dimensao_tela[1] - 70

def txt():
    font = pygame.font.SysFont('lucidacalligraphy',tamanho_fonte)
    texto = font.render(mensagem[mensagem1],10,cor)
    
    centro = []
    for i in texto.get_rect():
        centro.append(i)
    posição_txt_x = (dimensao_tela[0]/2)-(centro[2]/2)

    tela.blit(texto,[posição_txt_x,posição_txt_y])
# 7.1 -> Textos tela inicial
def outros_texto():
# -> Título
    font = pygame.font.SysFont("CASTELLAR", 45)
    nome_jogo = font.render("Dark World", 45, (75,0,130))
    tela.blit(nome_jogo, [200, (dimensao_tela[1] / 2 - 20)])
    
# -> Texto "Começar" Centralizado
    font = pygame.font.SysFont("lucidacalligraphy", 25)
    começar = font.render("Começar", 45, cor1)
    centro = []
    for i in começar.get_rect():
        centro.append(i)
    posição_txt_x = (dimensao_tela[0]/2)-(centro[2]/2)
    tela.blit(começar, [posição_txt_x, (dimensao_tela[1] / 2)+50])
    
# -> Texto "Instruções" centralizados
    font = pygame.font.SysFont("lucidacalligraphy", 25)
    começar = font.render("Instruções", 45, cor2)
    centro = []
    for i in começar.get_rect():
        centro.append(i)
    posição_txt_x = (dimensao_tela[0]/2)-(centro[2]/2)
    tela.blit(começar, [posição_txt_x, (dimensao_tela[1] / 2)+90])

# 7.2 -> Textos de Instruções
def txt_instruções():
    font = pygame.font.SysFont("lucidacalligraphy", 15)
    esc_ins = font.render(" |Esc para voltar ao menu", 45, (255,255,255))
    tela.blit(esc_ins, [dimensao_tela[0]-290, (dimensao_tela[1]-120)])
    
    font = pygame.font.SysFont("lucidacalligraphy", 15)
    nome_jogo = font.render(" |Segure q para melhor ver", 45, (255,255,255))
    tela.blit(nome_jogo, [dimensao_tela[0]-290, (dimensao_tela[1] -80)])

    font = pygame.font.SysFont("lucidacalligraphy", 15)
    nome_jogo = font.render(" |Use letras e números para fases", 45, (255,255,255))
    tela.blit(nome_jogo, [dimensao_tela[0]-290, (dimensao_tela[1]-40)])
#________________8.Chaves________________
chaves = ["Pressione: H","U","M","A","N","2","7","8","3","1","5"]

posição_chave_x = dimensao_tela[0] - 200
posição_chave_y = 50
tamanho_chave = 20
fase = 0
def keys():
    font_chave = pygame.font.SysFont('lucidacalligraphy',tamanho_chave)
    chave = font_chave.render(chaves[chave_fase],10,preto)
    tela.blit(chave,[posição_chave_x,posição_chave_y])
    

#________________9.Comandos________________

def left_is_down():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        return True
    return False

def right_is_down():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        return True
    return False

def up_is_down():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        return True
    return False

def down_is_down():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        return True
    return False

def q_is_down():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        return True
    return False
def enter_is_down():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_KP_ENTER]:
        return True
    return False

#________________10.Fases________________
def phase_1():
    global mensagem1
    global cor
    global tamanho_fonte
    global posição_txt_y
    global fase
    global chave_fase 
    if mensagem1 <= 8:
        cor = preto
        tamanho_fonte = 55
        posição_txt_y = dimensao_tela[1]/2 - 170
    if "espaço" in eventos:
        if mensagem1 < 15:
            mensagem1 += 1
        if mensagem1 >= 17:
            mensagem1 = 0
    if mensagem1 == 15:
        chave_fase = 0
        keys()
    if "h" in eventos:
        mensagem1 = 16            
        fase = 1
        
    txt()

def phase_2():
    global mensagem1
    global posição_chave_x
    global posição_chave_y
    global fase
    global chave_fase
    if "espaço" in eventos:
        if mensagem1 < 23:
            mensagem1 += 1
    if mensagem1 == 23:
        posição_chave_x = 50
        posição_chave_y = dimensao_tela[1] -120
        chave_fase = 1
        keys()
    if "u" in eventos:
        mensagem1 = 24
        fase = 2
    
    txt()
def phase_3():
    global mensagem1
    global posição_chave_x
    global posição_chave_y
    global fase
    global chave_fase
    if "espaço" in eventos:
        if mensagem1 < 32:
            mensagem1 += 1
    if mensagem1 == 32:
        posição_chave_x = 15
        posição_chave_y = dimensao_tela[1] -30
        chave_fase = 2
        keys()

        posição_chave_x = dimensao_tela[0] -200
        posição_chave_y = dimensao_tela[1]/2
        chave_fase = 3
        keys()
    if "ma" in eventos:
        mensagem1 = 33
        fase = 3
    
    txt()


def phase_4():
    global mensagem1
    global posição_chave_x
    global posição_chave_y
    global fase
    global chave_fase
    if "espaço" in eventos:
        if mensagem1 < 45:
            mensagem1 += 1
    if mensagem1 == 45:
        posição_chave_x = random.randint(30,dimensao_tela[0])-10
        posição_chave_y = random.randint(30,dimensao_tela[1])-20
        chave_fase = 4
        keys()
    if "n" in eventos:
        mensagem1 = 46
        fase = 4
    
    txt()
    
def phase_5():
    global mensagem1
    global respostas
    global fase
    if len(respostas)>3:
        respostas.clear()
    if "espaço" in eventos:
        if mensagem1 < 59:
            mensagem1 += 1
    if ["S","I","M"] == respostas:
        mensagem1 = 61
        fase = 5
        respostas.clear()
    if ["N","A","O"] == respostas:
        mensagem1 = 60
        fase = 0
        respostas.clear()
    print(respostas)    
    txt()
tempo_aparição = 0
def phase_6():
    global mensagem1
    global respostas
    global fase
    global tempo_aparição
    
    if len(respostas)>6:
        respostas.clear()
    if "espaço" in eventos:
        if mensagem1 < 72:
            mensagem1 += 1
    if mensagem1 == 72:
        tempo_aparição += 1
        if tempo_aparição < 10:
            tela.blit(biblioteca_2,[dimensao_tela[0]-150,
                                    dimensao_tela[1]-150])
        elif tempo_aparição == 30:
            tempo_aparição = 0
    if ["C","O","R","U","J","A"] == respostas:
        mensagem1 = 73
        fase = 6
        respostas.clear()
    print (respostas)  
    txt()

primeira_parte = False
def phase_7():
    global mensagem1
    global posição_chave_x
    global posição_chave_y
    global respostas
    global fase
    global chave_fase
    global primeira_parte

    if "espaço" in eventos:
        if mensagem1 < 90:
            mensagem1 += 1
            
        elif primeira_parte:
            if mensagem1 < 97:
                mensagem1 += 1
    if mensagem1 == 75:
        posição_chave_x = 50
        posição_chave_y = dimensao_tela[1] -120
        chave_fase = 5
        keys()
    elif mensagem1 == 79:
        posição_chave_x = dimensao_tela[0] -100
        posição_chave_y = 120
        chave_fase = 6
        keys()
    elif mensagem1 == 82:
        posição_chave_x = dimensao_tela[0] -300
        posição_chave_y = dimensao_tela[1] -120
        chave_fase = 7
        keys()
    elif mensagem1 == 85:
        posição_chave_x = dimensao_tela[0]/2
        posição_chave_y = -40
        chave_fase = 8
        keys()
    elif mensagem1 == 87:
        posição_chave_x = 50
        posição_chave_y = dimensao_tela[1] -120
        chave_fase = 9
        keys()
    elif mensagem1 == 90:
        posição_chave_x = dimensao_tela[0]/2
        posição_chave_y = dimensao_tela[1]/2
        chave_fase = 10
        keys()
    if ["2","7","8","3","1","5"] == respostas:
        primeira_parte = True
        mensagem1 = 91
        respostas.clear()


    if ["C","O","R","U","J","A"] == respostas:
        fase = 7
        mensagem1 = 99
        respostas.clear()
    if len(respostas)>6:
        fase = 0
        mensagem1 = 98
        respostas.clear()
    print(respostas) 
    txt()

def phase_8():
    global mensagem1
    global respostas
    global fase
    if len(respostas)>7:
        respostas.clear()
    if "espaço" in eventos:
        if mensagem1 < 111:
            mensagem1 += 1
    if ["5","7","6","4","8","0","1"] == respostas:
        mensagem1 = 112
        fase = 8
        respostas.clear()
    print (respostas)  
    txt()

def phase_9():
    global mensagem1
    global respostas
    global fase
    if len(respostas)>7:
        respostas.clear()
    if "espaço" in eventos:
        if mensagem1 < 129:
            mensagem1 += 1
    if ["H","U","M","A","N","O"] == respostas:
        mensagem1 = 130
        fase = 9
        respostas.clear()
    print (respostas)  
    txt()

limite = True    
def phase_10():
    global mensagem1
    global fase
    global limite
    global posição_txt_y
    
    if "espaço" in eventos:
        if mensagem1 < 134:
            mensagem1 += 1
            
    if ["S","I","M"] == respostas:
        mensagem1 = 135
        fase = 0
        respostas.clear()
    if ["N","A","O"] == respostas:
        mensagem1 = 136
        limite = False
        respostas.clear()

    if posição_x-(largura/2) >= dimensao_tela[0]+200:
        posição_txt_y = dimensao_tela[1]/2
        mensagem1 = 137
    if posição_x-(largura/2) <= 0-200:
        posição_txt_y = dimensao_tela[1]/2
        mensagem1 = 137
    if posição_y-(altura/2) <= 0-200:
        posição_txt_y = dimensao_tela[1]/2
        mensagem1 = 137
    if posição_y-(altura/2) >= dimensao_tela[1]+200:
        posição_txt_y = dimensao_tela[1]/2
        mensagem1 = 137
    print(respostas)    
    txt()
#________________11.Teclas de fases________________
"tecla fase 3"
def m_is_down():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_m]:
        return True
    return False
def a_is_down():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        return True
    return False

"__________________________________Game__________________________________"
# -> Pré informações de game
sair = True
sprite = 0
eventos = []
respostas = []
velocidade_de_mov = 15

vermelho_em = "começar"
iniciar = True
instruções = False

cor1 = vermelho
cor2 = branco
inicial.play(-1)
musica = 1

# -> Loop de Game
while sair:
    tela.fill(preto)

#________________12.tela inicial game________________
    if "esc" in eventos:
        instruções = False
        iniciar = True

    if iniciar:
        tela.blit(biblioteca_3,[(dimensao_tela[0]/2)-centro3[2]/2,20])
        outros_texto()       
        
        if up_is_down():
            vermelho_em = "começar"
            cor1 = vermelho
            cor2 = branco
        if down_is_down():
            vermelho_em = "instruções"
            cor1 = branco
            cor2 = vermelho
            
        if vermelho_em == "começar" and "enter" in eventos:
            iniciar = False
            inicial.stop()
        if vermelho_em == "instruções" and "enter" in eventos:
            instruções = True
        if instruções:
            tela.blit(biblioteca_1,[(140)-centro1[2]/2,370])
            txt_instruções()
            
            
#________________13.O jogo________________
    else:
        
        orbitas()
        sprite += 1
        soundtrack.play(-1)
        
        Informações_texto()    
        if fase == 0:
            phase_1()
        elif fase == 1:
            phase_2()
        elif fase == 2:
            phase_3()
        elif fase == 3:
            phase_4()
        elif fase == 4:
            phase_5()
        elif fase == 5:
            phase_6()
        elif fase == 6:
            phase_7()
        elif fase == 7:
            phase_8()
        elif fase == 8:
            phase_9()
        elif fase == 9:
            phase_10()
#________________14.Eventos________________
#14.1-> Sair
    if "sair" in eventos:
        sair = False
    eventos.clear()  #limpeza de eventos
    
    for event in pygame.event.get():     
        if event.type == pygame.QUIT:
            eventos.append("sair")
            
#14.2-> Teclas de alterar texto
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                eventos.append("espaço")
#14.3-> Teclas do início
            if event.key == pygame.K_RETURN:
                eventos.append("enter")
            if event.key == pygame.K_ESCAPE:
                eventos.append("esc")
#14.4-> Teclas Chaves
            if event.key == pygame.K_h:
                eventos.append("h")
                som_teclas()
            if event.key == pygame.K_u:
                eventos.append("u")
                som_teclas()
            if m_is_down():    
                if event.key == pygame.K_a:
                    eventos.append("ma")
                    som_teclas()                
            if a_is_down():    
                if event.key == pygame.K_m:
                    eventos.append("ma")
                    som_teclas()
            if event.key == pygame.K_n:
                eventos.append("n")
                som_teclas()

#14.4-> Teclas de Respostas
            if event.key == pygame.K_s:
                respostas.append("S")
                som_teclas()
            if event.key == pygame.K_i:
                respostas.append("I")
                som_teclas()
            if event.key == pygame.K_m:
                respostas.append("M")
                som_teclas()
                    
            if event.key == pygame.K_n:
                respostas.append("N")
                som_teclas()
            if event.key == pygame.K_a:
                respostas.append("A")
                som_teclas()
            if event.key == pygame.K_o:
                respostas.append("O")
                som_teclas()
                    

            if event.key == pygame.K_c:
                respostas.append("C")
                som_teclas()
            if event.key == pygame.K_r:
                respostas.append("R")
                som_teclas()
            if event.key == pygame.K_u:
                respostas.append("U")
                som_teclas()
            if event.key == pygame.K_j:
                respostas.append("J")
                som_teclas()

  
            if event.key == pygame.K_0:
                respostas.append("0")
                som_teclas()
            if event.key == pygame.K_1:
                respostas.append("1")
                som_teclas()
            if event.key == pygame.K_2:
                respostas.append("2")
                som_teclas()
            if event.key == pygame.K_3:
                respostas.append("3")
                som_teclas()
            if event.key == pygame.K_4:
                respostas.append("4")
                som_teclas()
            if event.key == pygame.K_5:
                respostas.append("5")
                som_teclas()
            if event.key == pygame.K_6:
                respostas.append("6")
                som_teclas()
            if event.key == pygame.K_7:
                respostas.append("7")
                som_teclas()
            if event.key == pygame.K_8:
                respostas.append("8")
                som_teclas()
            if event.key == pygame.K_9:
                respostas.append("9")
                som_teclas()


            if event.key == pygame.K_h:
                respostas.append("H")
                som_teclas()
 
#________________15.Movimentação________________  

    if left_is_down():
        posição_x += -velocidade_de_mov

    if right_is_down():
        posição_x += velocidade_de_mov

    if up_is_down():
        posição_y += -velocidade_de_mov

    if down_is_down():
        posição_y += velocidade_de_mov

#________________16.Regras________________
# 16.1-> Não ultrapasse o limite da tela
    if limite:
        if posição_x + tamanho >= dimensao_tela[0]:
            posição_x += -velocidade_de_mov
        if posição_x <= 0:
            posição_x += velocidade_de_mov
        if posição_y + tamanho >= dimensao_tela[1]:
            posição_y += -velocidade_de_mov
        if posição_y <= 0:
            posição_y += velocidade_de_mov
# 16.2-> Se pressionar Q sua forma muda
    if q_is_down():       
        if sprite == quantidade_sprite:
            sprite = quantidade_sprite -4
    else:
        if sprite > quantidade_sprite - 13:
            sprite +=-2
        elif sprite == quantidade_sprite - 13:
            sprite = 0

#________________17.Atual. Dysplay________________
    relogio.tick(10)
    pygame.display.update()

    


pygame.quit()
quit()
