from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from random import randint 
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader

class Jogo(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lista= []
        self.som_vitoria = SoundLoader.load("vitoria.wav")
        self.som_perda = SoundLoader.load("derrota.wav")
        self.som_empate = SoundLoader.load("empate-1.wav")
    #utilizou-se a mesma linha de raciocínio para todos os eventos dos botões, mudando apenas a estrutura condicional
    
    def clica_pedra(self,**kwargs): 
        lista =("Pedra","Papel", "Tesoura")
        computador = randint(0,2)
        jogadacomput = format(lista[computador]) 
       
        if jogadacomput == "Pedra":
            self.ids.computador.text= "Pedra"
            self.ids.resultado.text = "Empate"
            self.som_empate.play() 
        
        elif jogadacomput == "Papel":
            self.ids.computador.text = "Papel"
            self.ids.resultado.text = "Você perdeu!"
            self.som_perda.play()
            self.ids.pontuacao_computador.text = str(int(self.ids.pontuacao_computador.text)+1)
           
                
        else:
            self.ids.computador.text = "Tesoura"
            self.ids.resultado.text = "Você ganhou!"
            self.som_vitoria.play()
            self.ids.pontuacao.text =str(int(self.ids.pontuacao.text)+1)
            
    def clica_papel(self,**kwargs):
        lista =("Pedra","Papel", "Tesoura")
        computador = randint(0,2)
        jogadacomput = format(lista[computador])
        
        if jogadacomput == "Papel":
            self.ids.computador.text = "Papel"
            self.ids.resultado.text = "Empate!"
            self.som_empate.play()
        
        elif jogadacomput == "Pedra":
            self.ids.computador.text = "Pedra"
            self.ids.resultado.text = "Você ganhou!"
            self.som_vitoria.play()
            self.ids.pontuacao.text =str(int(self.ids.pontuacao.text)+1)
        
        else:
            self.ids.computador.text = "Tesoura"
            self.ids.resultado.text = "Você perdeu!"
            self.som_perda.play()
            self.ids.pontuacao_computador.text = str(int(self.ids.pontuacao_computador.text)+1)
    
    def clica_tesoura(self,**kwargs):
        lista =("Pedra","Papel", "Tesoura")
        computador = randint(0,2)
        jogadacomput = format(lista[computador])
        
        if jogadacomput == "Tesoura":
            self.ids.computador.text = "Tesoura"
            self.ids.resultado.text = "Empate!"
            self.som_empate.play()
            
        elif jogadacomput == "Papel":
            self.ids.computador.text = "Papel"
            self.ids.resultado.text = "Você ganhou!"
            self.som_vitoria.play()
            self.ids.pontuacao.text =str(int(self.ids.pontuacao.text)+1)
    
        else:
            self.ids.computador.text = "Pedra"
            self.ids.resultado.text = "Você perdeu!"
            self.som_perda.play()
            self.ids.pontuacao_computador.text = str(int(self.ids.pontuacao_computador.text)+1)
   
    def controla_som(self, situacao):
        if situacao:
            self.som_vitoria.volume = 1
            self.som_perda.volume = 1
            self.som_empate.volume = 1
        else: 
            self.som_vitoria.volume = 0
            self.som_perda.volume = 0
            self.som_empate.volume = 0
    
    def restaurar(self):
        self.ids.pontuacao.text = "0"
        self.ids.pontuacao_computador.text = "0"
        self.ids.resultado.text =" "
    
class JogoApp(App):
    def build(self):
        Window.size = (700, 700)
        self.title = "Pedra, Papel,Tesoura"
        return Jogo()
JogoApp().run()                                                     
