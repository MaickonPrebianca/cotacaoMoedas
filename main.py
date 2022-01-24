from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("tela.kv")

class CotacaoMoedas(App):
    def build(self):
        return GUI

    def on_start(self):
        self.root.ids['moeda1'].text = f'Dólar para R$ {self.pegar_cotacao("USD")}'
        self.root.ids['moeda2'].text = f'Euro para R$ {self.pegar_cotacao("EUR")}'
        self.root.ids['moeda3'].text = f'Bitcoin para R$ {self.pegar_cotacao("BTC")}'
        self.root.ids['moeda4'].text = f'Ethereum para R$ {self.pegar_cotacao("ETH")}'
        #self.root.ids['dataHoraAtualizado'].text = f'Atualizado {self.pegar_cotacao("ETH")}'
        #return super().on_start()
    
    def pegar_cotacao(self, moeda):
        link = f'https://economia.awesomeapi.com.br/last/{moeda}-BRL'
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f'{moeda}BRL']['bid']
        #atualizacao = dic_requisicao[f'{moeda}BRL']['create_date']
        return cotacao #, atualizacao
        
CotacaoMoedas().run()