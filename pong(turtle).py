from random import randint
import turtle
#Estabelecendo o inicio, tamanho, tela
wn = turtle.Screen() #Estabeleceu que a janela é 'wn'
wn.title('Pong pelo Ian')#titulo do jogo
wn.bgcolor('black')# cor da tela
wn.setup(width= 800, height = 700)# tamanho e possibilidades de outro funcionamento. 400 pra cima e 400 pra baixo. 350 pra direita e 350 pra esquerda
wn.tracer(0)

#Score
score_a = 0
score_b = 0



#Barra A(esquerda)
barra_a = turtle.Turtle()
barra_a.speed(0) #Deixa a tela em velocidade real(não é a velocidade da barra)
barra_a.shape("square")
barra_a.shapesize(stretch_wid=5, stretch_len=0.5) #A barra padrão é 20 pixels, usando o stretch_wid ele multiplica pelo valor depois do =, logo vai ser 20.5, 100. Já o len, seria o comprimento e e a mesma ideia da outra
barra_a.penup() #Para que não deixe um traço ao se mexer, pois o uso de turtle fará isso, então usa o penup pra tirar
barra_a.goto(-350, 250) #Posição inicial (x,y). Plano carteseano começa no canto superior direito, sendo y positivo pra baixo e x positivo pra direita
barra_a.color("red")

#Barra B
barra_b = turtle.Turtle() #Declara objeto
barra_b.speed(0) #Deixa a tela em velocidade real(não é a velocidade da barra)
barra_b.shape("square")
barra_b.shapesize(stretch_wid=5, stretch_len=0.5) #A barra padrão é 20 pixels, usando o stretch_wid ele multiplica pelo valor depois do =, logo vai ser 20.5, 100. Já o len, seria o comprimento e e a mesma ideia da outra
barra_b.penup() #Para que não deixe um traço ao se mexer, pois o uso de turtle fará isso, então usa o penup pra tirar
barra_b.goto(350, 250) #Posição inicial (x,y). Plano carteseano começa no canto superior direito, sendo y positivo pra baixo e x positivo pra direita
barra_b.color("blue")

#Bola
bola = turtle.Turtle() #Declarar que é um objeto
bola.speed(0)
bola.shape('circle')
bola.color("white")
bola.goto(0,0)# Para começar no meio
bola.penup()


#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() #Esconde para não ser visto
pen.goto(0, 300)
pen.write("PlayerA = 0   PlayerB = 0", align= "center", font= ("Courier", 20, "normal"))



#criando funções para mover as barras para cima
def barra__a__up():
    y = barra_a.ycor() # A função 'ycor' rastreia aonde está o objeto dado ( no caso a barra A)
    y += 20 # Vai adicionar 20 pixels ( que é o tamanho padrão da barra) para cima
    barra_a.sety(y) #Vai fazer a a barra ir para a posição definida em y ( no caso +20) e por ser y vai pra cima ou baixo
def barra__b__up():
    y = barra_b.ycor()
    y += 20
    barra_b.sety(y)
#Criando função para mover para baixo
def barra__a__down():
        y = barra_a.ycor() # Para a barra ir para baixo
        y -= 20
        barra_a.sety(y)
def barra__b__down():
    y = barra_b.ycor() # Para a barra ir para baixo
    y -= 20
    barra_b.sety(y)

#Usando o teclado pra dar o comando
wn.listen()     #Esta dizendo pra a tela (definida como 'wn' pra ouvir o input( no caso vai ser as teclas)
wn.onkeypress( barra__a__up,'w')#Puxa a função criada barra__a__up quando o teclado pressionar 'w' usando a função 'onkey'
wn.onkeypress(barra__a__down, "s")
wn.onkeypress(barra__b__up, "Up")    # O Maiusculo no inicio fez com que se referisse a seta pra cima
wn.onkeypress(barra__b__down, "Down")    #Seta pra baixo por causa do 'D'


#Movendo a bola ( criando duas variaveis e aplicar no loop do jogo)
bola.dx = 0.45  # o número determina a velocidade que vai pros lados
bola.dy = 0.45  # O numero determina a velocidade que vai pros lados

#Loop principal do jogo
while True:
    wn.update()

    #Movendo a bola
    bola.setx(bola.xcor() + bola.dx) #A bola vai se mexer para = a soma de onde ela está + a bola.dx( que eu deteriminei)
    bola.sety(bola.ycor() + bola.dy)

    #Checando a bola para voltar quando bater na tela
    if bola.ycor() > 330 :       #330 porque é 350(tamanho da parte de cima) - 20(tamanho da bola)
        bola.sety(330)
        bola.dy *= -1 #Faz agora ir para baixo, pois agora será negativo
    if bola.ycor() < -330:
        bola.sety(-330)
        bola.dy *= -1
    if bola.xcor() > 380  :
        bola.goto(0, randint(0,150))
        bola.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("PlayerA = {}   PlayerB = {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))
    if  bola.xcor() < -380 :
        bola.goto(0, randint(0,150))
        bola.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("PlayerA = {}   PlayerB = {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))

    #Bola batendo na barra
    if bola.xcor() > 340 and bola.xcor() < 350and (bola.ycor() < barra_b.ycor() + 50 and bola.ycor() > barra_b.ycor() - 50):
        bola.setx(340)
        bola.dx *= - 1
    if bola.xcor() < -340 and bola.xcor() > -350 and (bola.ycor() < barra_a.ycor() + 50 and bola.ycor() > barra_a.ycor() - 50):
        bola.setx(-340)
        bola.dx *= - 1