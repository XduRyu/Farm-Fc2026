FC 26 Auto Farm

Automação desenvolvida em Python para executar tarefas repetitivas no FC 26 utilizando a biblioteca PyAutoGUI. O script simula cliques do mouse em posições específicas da tela para agilizar a execução de desafios de criação de elenco (DME/SBC), reduzindo a necessidade de interação manual.

Aviso: Este projeto é apenas para fins de estudo e aprendizado em automação com Python.

Funcionalidades
Acessa automaticamente o menu de Melhoria de Criação.
Seleciona o filtro desejado.
Habilita itens transferíveis.
Constrói o desafio automaticamente.
Troca os atletas utilizados.
Resgata a recompensa.
Repete todo o processo em loop.
Tecnologias utilizadas
Python 3
PyAutoGUI
Time
Instalação

Clone o repositório:

git clone https://github.com/seu-usuario/fc26-auto-farm.git

Entre na pasta:

cd fc26-auto-farm

Instale a dependência:

pip install pyautogui
Como usar
Abra o FC 26.
Configure a resolução utilizada durante a gravação das coordenadas.
Posicione o jogo na tela.
Execute:
python main.py

O script iniciará automaticamente a sequência de cliques.

Estrutura
📂 fc26-auto-farm
 ├── main.py
 ├── README.md
 └── requirements.txt
Observações
As coordenadas do mouse são fixas.
Caso utilize outra resolução ou monitor, será necessário alterar os valores de x e y.
Os tempos (sleep) podem precisar de ajustes dependendo do desempenho do computador.
Dependências
pyautogui
Licença

Este projeto é distribuído sob a licença MIT.

Autor

Eduardo Montanha
