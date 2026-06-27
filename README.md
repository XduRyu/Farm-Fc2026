# ⚽ FC 26 Auto SBC Farm

Automação desenvolvida em **Python** para agilizar tarefas repetitivas no **EA SPORTS FC 26**, utilizando a biblioteca **PyAutoGUI** para simular cliques do mouse.

> **Projeto para fins educacionais**, demonstrando conceitos de automação de interface gráfica (GUI) com Python.

---

## 📌 Funcionalidades

- ✅ Acessa automaticamente o menu de SBC (Melhoria de Criação).
- ✅ Seleciona o AutoSBC.
- ✅ Ativa a opção de itens transferíveis.
- ✅ Constrói o SBC automaticamente.
- ✅ Troca os atletas utilizados.
- ✅ Resgata o pacote de recompensa.
- ✅ Executa o processo em loop.

Além disso, o projeto possui scripts auxiliares para localizar coordenadas do mouse e testar cliques antes da execução principal.

---

## 📂 Estrutura do Projeto

```
FC26-Auto-Farm/
│
├── Farm_fifa.py        # Script principal da automação
├── pegar_pick.py       # Captura a posição atual do mouse
├── testas_pick.py      # Testa um clique em uma coordenada específica
└── README.md
```

---

## 🛠 Tecnologias Utilizadas

- Python 3
- PyAutoGUI
- Time

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/fc26-auto-farm.git
```

Entre na pasta:

```bash
cd fc26-auto-farm
```

Instale as dependências:

```bash
pip install pyautogui
```

---

## ▶ Como utilizar

### 1. Descobrir coordenadas

Execute:

```bash
python pegar_pick.py
```

Após alguns segundos, posicione o mouse onde desejar.

O programa exibirá:

```
Mouse position: x=000, y=000
```

---

### 2. Alterar as coordenadas

Abra o arquivo **Farm_fifa.py** e substitua as coordenadas pelos valores do seu monitor.

Exemplo:

```python
py.click(x=543, y=488)
```

---

### 3. Executar a automação

```bash
python Farm_fifa.py
```

O script iniciará automaticamente o ciclo de criação do SBC.

---

## ⚠ Observações

- O script depende da resolução da tela.
- Não mova a janela do jogo durante a execução.
- Caso utilize outro monitor ou resolução, será necessário recalibrar as coordenadas.
- Os tempos (`sleep`) podem precisar de ajustes dependendo do desempenho do computador.

---

## 📄 Scripts

### `Farm_fifa.py`

Responsável por toda a automação do processo:

- Abrir SBC
- Selecionar AutoSBC
- Construir
- Trocar jogadores
- Coletar recompensa
- Repetir

---

### `pegar_pick.py`

Ferramenta para descobrir rapidamente as coordenadas do mouse.

---

### `testas_pick.py`

Realiza apenas um clique em uma posição específica para validar se a coordenada está correta.

---

## 🚀 Melhorias futuras

- Interface gráfica (GUI)
- Configuração automática das coordenadas
- Atalho para iniciar e parar o script
- Suporte a diferentes resoluções
- Sistema de logs
- Configuração via arquivo `.json`

---

## 👨‍💻 Autor

**Eduardo Montanha**

Desenvolvido para estudos de automação em Python utilizando PyAutoGUI.
