## 📝 Manual do Usuário - Signa Vision

O **SignaVision** é um software de rastreamento de mãos que mapeia pontos de coordenadas em tempo real, possibilitando a interação com o computador por meio de gestos, incluindo funcionalidades como **teclado virtual** e **desenho**.

### 🌟 **Funcionalidades**

### 1️⃣ **Teclado Virtual**

#### 1.1 **Ativação**
- Levante **somente a mão esquerda** para ativar o teclado virtual.

#### 1.2 **Digitação**

- **Maiúsculas/Minúsculas:**
  - **Minúsculas**: Levante apenas o **dedo indicador da mão esquerda**.
  - **Maiúsculas**: Levante **todos os dedos da mão esquerda**.

- **Seleção de Teclas:**
  - Passe o **dedo indicador** sobre as teclas para destacá-las (mudança de cor para cinza).
  - Para digitar uma tecla, **aproxime o dedo indicador** até uma distância de **-85 pixels** da tela (a tecla ficará verde).
  - **Clique**: Realize um movimento de "ir e voltar rapidamente" com o dedo indicador para inserir a letra.

- **Apagar:**
  - Levante **apenas o dedo mindinho** da mão esquerda para apagar a última letra digitada.

#### 1.3 **Integração com Programas do Computador**

- É possível **digitar diretamente em programas** do seu computador (ex: Bloco de Notas).
- Para **abrir um programa**, utilize gestos específicos com a **mão direita** (ex: levante os dedos indicador e médio para abrir o Bloco de Notas).
- Após abrir o programa, ative o teclado virtual com a **mão esquerda** e digite normalmente.
- Para **fechar o bloco de notas**, levante a **mão direita** e abaixe todos os dedos.


### 2️⃣ **Desenho**

#### 2.1 **Ativação**
- **Mostre ambas as mãos** na tela para ativar o modo de desenho.
- A tela ficará **esbranquiçada** para facilitar a visualização do desenho.

#### 2.2 **Seleção de Cores**
- Utilize a **mão esquerda** para selecionar as cores do pincel.
- A **quantidade de dedos levantados** determina a cor selecionada (obs: a cor branca funciona como uma borracha).

#### 2.3 **Desenho na Tela**
- Utilize a **mão direita** para desenhar na tela.
- Para desenhar, **levante apenas o dedo indicador da mão direita**.
- Se **todos os dedos da mão direita** estiverem levantados, **nenhum desenho será feito**.
- Ao abaixar todos os dedos de ambas as mãos, o desenho é restaurado ao estado inicial.

### 3️⃣ **Encerramento do Programa**
- Levante a **mão direita** com **dedos indicador e mindinho levantados** para encerrar o programa.

### ⚠️ **Observações**
- A **precisão dos gestos** pode variar dependendo da **iluminação** e da **câmera** utilizada.
- Recomenda-se **praticar os gestos** para obter maior fluidez no uso do software.

### :thinking: Dúvidas
Ficou com alguma dúvida? Fique à vontade para abrir uma *issue* no repositório.

---

## ⚙️ Configuração do Ambiente

Este guia explica como clonar e configurar corretamente o repositório **Signa Vision**, garantindo que todos os arquivos, incluindo os rastreados pelo **Git LFS**, sejam baixados corretamente.

### 1️⃣ Requisitos
Antes de clonar o repositório, certifique-se de que possui os seguintes itens instalados:

- Uma conta no [GitHub](https://github.com/)
- O [Git](https://git-scm.com/downloads) instalado em sua máquina
- O [Git LFS](https://git-lfs.github.com/) instalado e configurado
- O [Visual Studio Code](https://code.visualstudio.com/) instalado
- O [Python](https://www.python.org/downloads/) instalado tanto no sistema operacional quanto no VS Code (via extensão Python)

### Instalando o Git LFS
Para instalar o **Git LFS**, siga os passos conforme seu sistema operacional:
- **Linux (Ubuntu/Debian)**:
  ```bash
  sudo apt install git-lfs
  ```
- **MacOS**:
  ```bash
  brew install git-lfs
  ```
- **Windows**:
  Baixe e instale o [Git LFS](https://git-lfs.github.com/)
  
### 2️⃣ Configurando o Git LFS

Se ainda não configurou o **Git LFS**, execute o seguinte comando:
```bash
git lfs install
```


### 3️⃣ Clonando o Repositório

Agora, clone o repositório para sua máquina local:
```bash
git clone https://github.com/helen-silv4/signa-vision.git
cd signa-vision
```
Se os arquivos rastreados pelo Git LFS não forem baixados automaticamente, execute o seguinte comando para garantir que todos sejam recuperados corretamente:
```bash
git lfs pull
```

### 4️⃣ Criando e selecionando um Ambiente Virtual

Crie um ambiente virtual para isolar as bibliotecas do projeto e evitar conflitos:
```bash
python -m venv venv
```
Depois, abra o **VS Code**, pressione `Ctrl + Shift + P`, digite **Python: Select Interpreter**, e selecione o ambiente virtual `venv` que foi criado.<br>
Em seguida, ative o ambiente virtual no terminal do **VS Code** com o seguinte comando:
```bash
.\venv\Scripts\Activate
```

### 5️⃣ Instalando Dependências
Instale a versão mais recente do pip, o gerenciador de pacotes do Python, com o seguinte comando:
```bash
python -m pip install --upgrade pip
```
Manter o `pip` atualizado garante compatibilidade com as versões mais recentes de pacotes e corrige possíveis falhas de segurança ou erros na instalação de dependências.

No terminal do **VS Code**, instale as bibliotecas necessárias:
```bash
pip install opencv-python
pip install mediapipe
pip install pynput
```

### 6️⃣ Pronto! 🎉
Agora você pode executar o projeto sem problemas. Caso tenha dúvidas, abra uma *issue* no repositório.

### 🔗 Tutorial
Se precisar de ajuda para baixar o projeto, assista ao tutorial:
[Clonando repositório com suporte a Git LFS - SignaVision](https://www.youtube.com/watch?v=TsR0uWyvNdk)