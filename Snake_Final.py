from Tkinter import *
import time
import threading
import random



                                                            #################################
#############################################################     TEMA 14 // Grupo MAA      ###############################################################################################
                                                            #                               #
                                                            #         SNAKE GAME            #
                                                            #                               #
                                                            #:::::::: criado por :::::::::::#
                                                            #                               #
                                                            #         Lucas Helio           #
                                                            #                               #
                                                            #                               #
                                                            #################################









class jogo:
    def __init__(self, master):
        self.frame = Frame(master, bg = "darkgreen")
        self.direitasup = Frame(master, bg = "darkgreen")
        self.direitameio = Frame(master, bg = "darkgreen")
        self.direitainf = Frame(master, bg = "darkgreen")
        self.canvas = Canvas(self.frame, bg = "black", height = 500, width = 500)


        ### Variaveis para evitar que o jogo trave com comandos muito rapidos  ###
        self.podeMover = True 
        self.podeReceber = True

        
        ### Eventos para mudanca da Variavel de Deslocamento  ###
        self.canvas.bind("<Up>", self.Sentido)
        self.canvas.bind("<Down>", self.Sentido)
        self.canvas.bind("<Left>", self.Sentido)
        self.canvas.bind("<Right>", self.Sentido)
        self.canvas.focus_set() 


        ###  Labels ao lado do jogo com pontuacao e dificuldade  ###
        self.lbl = Label(self.direitasup, text = "Score", font = ("Arial", 30), fg = "white", bg = "darkgreen")
        self.pontos = Label(self.direitasup, text = "0", font = ("Arial", 20), fg = "white", bg = "darkgreen")
        self.lbl2 = Label(self.direitainf, text = "'Dificuldade'",font = ("Arial", 10), fg = "white", bg = "darkgreen")
        self.lbl3 = Label(self.direitainf, text = "Normal", font = ("Arial", 8), fg = "black", bg = "darkgreen")
        self.lbl4 = Label(self.direitameio, text = "", font = ("Arial", 30), fg = "red", bg = "darkgreen")
        self.lbl5 = Label(self.direitameio, text = "", font = ("Arial", 10), fg = "red", bg = "darkgreen")
        

        ###     Configuracao dos menus    ###
        self.menuprincipal = Menu(master)

        self.submenu1 = Menu(self.menuprincipal, tearoff = 0)
        self.menuprincipal.add_cascade(label = "options", menu = self.submenu1)
        self.submenu1.add_command(label = "Sair", command = self.Sair)
        self.submenu1.add_command(label = "Reiniciar", command = self.Reiniciar)

        self.submenu2 = Menu(self.menuprincipal, tearoff = 0)
        self.menuprincipal.add_cascade(label = "Dificuldade", menu = self.submenu2)
        self.submenu2.add_command(label = "Facil", command = self.Facil)
        self.submenu2.add_command(label = "Normal", command = self.Normal)
        self.submenu2.add_command(label = "Dificil", command = self.Dificil)

                
        master.config(menu = self.menuprincipal)

        
        ###     Packs da Tela   ###
        self.frame.pack(side= LEFT, expand = 1)
        self.direitasup.pack(expand = 1,fill = BOTH)
        self.direitameio.pack(expand = 1,fill = BOTH)
        self.direitainf.pack(expand = 1,fill = BOTH)
        self.canvas.pack(side = LEFT, expand = 1, fill = BOTH)
        self.lbl.pack(fill = BOTH)
        self.lbl4.pack(fill = BOTH)
        self.lbl5.pack(fill = BOTH)
        self.lbl2.pack(fill = BOTH)
        self.lbl3.pack(fill = BOTH)
        self.pontos.pack(fill = BOTH)

        ###     Posicoes da Comida // Posicoes da Cobra// Coordenadas em X e Y do Corpo da Cobra // Variavel que se altera quando utilizado o Reiniciar    ### 
        self.posicoespossiveis = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205, 215, 225, 235, 245, 255, 265, 275, 285, 295, 305, 315, 325, 335, 345, 355, 365, 375, 385, 395, 405, 415, 425, 435, 445, 455, 465, 475, 485, 495]
        self.posicoes = []
        self.cobra_x = []
        self.cobra_y = []
        


        self.Iniciar()

        


    def Iniciar(self):

        ###     Variavel inicial da dificuldade // Coordenadas em X e Y da Cabeca da Cobra // Variaveis de Deslocamento da Cobra em X e Y // Coordenadas em X e Y da Comida // Numero de blocos no Corpo da Cobra    ###
        self.Dificuldade = 0.05
        self.x = 55
        self.y = 55
        self.des_x = 10
        self.des_y = 0
        self.pos_com_x = 100
        self.pos_com_y = 100
        self.tamanho = 1
        self.loop = True

        

    
        
        ###   Primeiras funcoes chamadas   ###
        self.Comida()
        t = threading.Timer(self.Dificuldade, self.Atualiza) 
        t.start()




    ###     Atualiza a Tela e executa as Funcoes (Fica em Loop)  ###
    def Atualiza(self): 
        while (self.loop):
            if self.podeMover:
                self.desenhaCobra(self.canvas)
                self.Move(self.desenhaCobra, self.Sentido)
                if self.x == self.pos_com_x and self.y == self.pos_com_y:
                    self.Comeu()
                self.podeReceber = True
        
            ###    Identifica quando a cobra passa por si mesma    ###
            for i in range (1, len (self.cobra_x)-1): 
                if self.x == self.cobra_x[i]:
                    if self.y == self.cobra_y[i]:
                        self.Bateu()
            time.sleep(self.Dificuldade)
        self.lbl4["text"] = "Game Over"
        self.lbl5["text"] = "utilize options para reiniciar"




    ###     Desenha a Cobra     ###
    def desenhaCobra(self, canvas):
        if self.podeMover:
            print (self.x-5,self.y-5,self.x+5,self.y+5)            
            self.quadrado = self.canvas.create_rectangle(self.x-5,self.y-5,self.x+5,self.y+5, fill = "red")

            self.posicoes.append(self.quadrado)
            self.cobra_x.append(self.x)
            self.cobra_y.append(self.y)
                
            if len(self.posicoes) > self.tamanho:
                self.canvas.delete(self.posicoes[0])
                del self.posicoes[0]
                del self.cobra_x[0]
                del self.cobra_y[0]
            


    ###     Altera as coordenadas da Cabeca da Cobra    ###
    def Move(self, desenho, sentido):
        self.x += self.des_x
        self.y += self.des_y

        if self.x<5:
            self.x = 495

        elif self.x> 495:
            self.x = 5

        if self.y < 5:
            self.y = 495

        elif self.y > 495:
            self.y = 5



    ###     Aumenta o Tamanho da Cobra // Aumenta a Pontuacao // Deleta a Comida // Chama a funcao Comida   ###
    def Comeu(self):
            self.tamanho += 1
            self.canvas.delete(self.comida)
            i = int(self.pontos["text"]) + 1
            self.pontos["text"] = str(i)
            self.Comida()


    ###     Sorteia Posicoes Possiveis e Cria a Comida  ###
    def Comida(self):
        x = random.randint(0, 49)
        y = random.randint(0,49)

        self.pos_com_x = self.posicoespossiveis[x]
        self.pos_com_y = self.posicoespossiveis[y]


        self.comida = self.canvas.create_rectangle(self.pos_com_x-5,self.pos_com_y-5,self.pos_com_x+5,self.pos_com_y+5, fill = "green")        

    
    ###     Altera as Variaveis de Deslocamento em X e Y baseado nos Eventos    ###
    def Sentido(self, event):
        self.podeMover = False
        if self.podeReceber:
            self.podeReceber = False
            if event.keysym == "Up":
                if self.des_y != 10 and self.des_x != 0 :
                    self.des_x = 0
                    self.des_y = -10
            elif event.keysym == "Down":
                if self.des_y != -10 and self.des_x != 0 :
                    self.des_x = 0
                    self.des_y = 10

            elif event.keysym == "Right":
                if self.des_x != -10 and self.des_y != 0 :
                    self.des_x = 10
                    self.des_y = 0

            elif event.keysym == "Left":
                if self.des_x != 10 and self.des_y != 0 :
                    self.des_x = -10
                    self.des_y = 0
        self.podeMover = True
        
        
        
    ###     Alteram o valor da Variavel da dificuldade, tornando a Cobra mais rapida ou mais lenta  ###
    def Facil(self):
        self.Dificuldade = 0.3
        self.lbl3["text"] = "Facil"
        self.lbl3["fg"] = "white"

    def Normal(self):
        self.Dificuldade = 0.05
        self.lbl3["text"] = "Normal"
        self.lbl3["fg"] = "black"

    def Dificil(self):
        self.Dificuldade = 0.01
        self.lbl3["text"] = "Dificil"
        self.lbl3["fg"] = "red"


    ###    Cancela o loop do atualiza   ###
    def Bateu(self):
        self.loop = False

        

    ###     Apaga as telas e reinicia o jogo    ###
    def Reiniciar(self):
        self.frame.destroy()
        self.direitasup.destroy()
        self.direitainf.destroy()
        self.direitameio.destroy()
        jogo(gui)


    ###     Termina o jogo  ###
    def Sair(self):
        gui.destroy()




        
gui = Tk()
gui.title("Snake Game")
app = jogo(gui)
gui.mainloop()
