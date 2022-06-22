from funcoes import pygame, random, time, dados

dados()

pygame.init()

largura = 1076
altura = 600
tamanho = (largura, altura)
pygameDisplay = pygame.display

pygameDisplay.set_caption("BOB ESPONJA CALÇA QUADRADA")
gameDisplay = pygame.display.set_mode(tamanho)
gameIcon = pygame.image.load("bobicon.ico")
pygameDisplay.set_icon(gameIcon)

bg = pygame.image.load("fundo.png")
bg_destroy = pygame.image.load("gif.jpg")
# Aqui Começa o jogo

impactoSound = pygame.mixer.Sound("perda.mp3")
impactoSound.set_volume(0.5)

black = (0, 0, 0)
white = (255, 255, 255)
clock = pygame.time.Clock()

gameEvents = pygame.event


def dead(pontos):

    gameDisplay.blit(bg_destroy, (0, 0))
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(impactoSound)
    fonte = pygame.font.Font("Spongeboy Me Bob.ttf", 24)
    fonteContinue = pygame.font.Font("Spongeboy Me Bob.ttf", 24)

    texto = fonte.render("Você Perdeu com "+str(pontos) +
                         " pontos!", True, white)
    textoContinue = fonteContinue.render(
        "Pressione enter para continuar...", True, white)

    gameDisplay.blit(textoContinue, (50, 200))
    gameDisplay.blit(texto, (50, 100))

    pygameDisplay.update()


def jogo():
    posicaoX = 0
    posicaoY = random.randrange(0, altura)
    direcao = True
    velocidade = 3
    posicaoXBob = 100
    posicaoYBob = 100
    movimentoXBob = 0
    movimentoYBob = 0
    pontos = 0
    plankton = pygame.image.load("plankton.png")
    bob = pygame.image.load("bob.png")

    plankton = pygame.transform.flip(plankton, True, False)
    pygame.mixer.music.load("trilha.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1)

    alturaBob = 143
    larguraBob = 190

    jogando = True
    virouEsquerda = True

    while True:
        # aqui é lido os eventos da tela
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    jogo()
                if event.key == pygame.K_LEFT:
                    movimentoXBob = - 15
                    if virouEsquerda == False:
                        bob = pygame.transform.flip(bob, True, False)
                        virouEsquerda = True
                elif event.key == pygame.K_RIGHT:
                    movimentoXBob = 15
                    if virouEsquerda == True:
                        virouEsquerda = False
                        bob = pygame.transform.flip(bob, True, False)
                elif event.key == pygame.K_UP:
                    movimentoYBob = -15
                elif event.key == pygame.K_DOWN:
                    movimentoYBob = 15
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    movimentoXBob = 0
                    movimentoYBob = 0

        if jogando == True:
            # travando o movimento na tela
            posicaoXBob = posicaoXBob + movimentoXBob
            posicaoYBob = posicaoYBob + movimentoYBob
            if posicaoXBob < 0:
                posicaoXBob = 0
            elif posicaoXBob >= largura - larguraBob:
                posicaoXBob = largura - larguraBob

            if posicaoYBob < 0:
                posicaoYBob = 0
            elif posicaoYBob >= altura - alturaBob:
                posicaoYBob = altura - alturaBob

            gameDisplay.blit(bg, (0, 0))

            if direcao == True:
                if posicaoX < largura-150:
                    posicaoX = posicaoX + velocidade
                else:
                    direcao = False
                    posicaoY = random.randrange(0, altura)
                    velocidade = velocidade + 1
                    plankton = pygame.transform.flip(plankton, True, False)
                    pontos = pontos + 1
            else:
                if posicaoX >= 0:
                    posicaoX = posicaoX - velocidade
                else:
                    direcao = True
                    posicaoY = random.randrange(0, altura)
                    velocidade = velocidade + 1
                    plankton = pygame.transform.flip(plankton, True, False)
                    pontos = pontos + 1

            gameDisplay.blit(plankton, (posicaoX, posicaoY))
            gameDisplay.blit(bob, (posicaoXBob, posicaoYBob))

            fonte = pygame.font.Font("Spongeboy Me Bob.ttf", 24)
            texto = fonte.render("Pontos: "+str(pontos), True, white)
            gameDisplay.blit(texto, (20, 20))

        
            bobRect = bob.get_rect()
            bobRect.x = posicaoXBob
            bobRect.y = posicaoYBob

            planktonRect = plankton.get_rect()
            planktonRect.x = posicaoX
            planktonRect.y = posicaoY

            if bobRect.colliderect(planktonRect):
                dead(pontos)
                time.sleep(3)
                quit()
            else:
                print("Ainda vivo...")


        pygameDisplay.update()
        clock.tick(60)
jogo()