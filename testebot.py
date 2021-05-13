import os


def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}, na minha visão vale muito apena, pois a área de tecnologia está em ascenção e com muitas vagas no mercado, além disso a tecnogia vai acabar sendo introduzida em todo mercado, assim deixando traz quem não tem conhecimento. {os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}, eu acho que não podemos dizer que uma linguagem é melhor ou pior que outra, mas escolhemos uma linguagem por alguns motivos seja eles "obvios" ou não, mas algumas das liguangens mais usadas são: Python, C#(CSharp), JavaScript, Java e Go. {os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, primeiro entenda, ninguém vai te dizer ou chegar magicamente um dia e te dizer que você está BOM o suficiente para conseguir um emprego ou fazer dinheiro com seu conhecimento de programação, seja em Python ou qualquer outra linguagem ou habilidade, você simplesmente tem que começar dar a sua cara a tapa e começar a aplicar para oportunidades ou até mesmo começar a criar elas, desde o dia que você já domina os fundamentos de uma linguagem.{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome}, você pode estudar através de vídeos gratúitos no YouTube, livros e sites de programação, mas se quiser ter um diploma ou até mesmo ter uma interação presencial o curso tecnico do Senai pode ser uma boa forma de aprender. {os.linesep}')
    else:
        print('Digite apenas 1, 2, 3 ou 4')


def start():
    # Apresentar o chatbot
    print('Olá! Bem-vindo ao TesteBot')
    # pedir o nome
    nome = input('Digite seu nome: ')
    # pedir o e-mail
    email = input('Digite seu e-mail: ')
    while True:
        # Oferer o menu de opções
        resposta = input(
            f'O que gostaria de saber hoje?{os.linesep}[1] - Vale a pena aprender Programação?{os.linesep}[2] - Quais as melhores linguagens de programação?{os.linesep}[3] - Quando vou saber que estou BOM o suficiente para conseguir um emprego?{os.linesep}[4] - Onde me recomenda estudar Programação?{os.linesep}')
        # Processar a resposta enviada
        processar_resposta(resposta, nome)


if __name__ == '__main__':
    start()
