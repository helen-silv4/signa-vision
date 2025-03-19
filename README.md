## Configuração do Ambiente

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
Depois, abra o **VS Code**, pressione `Ctrl + Shift + P`, digite **Python: Select Interpreter**, e selecione o ambiente virtual `venv` que foi criado.
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
[Clonando repositório com suporte a Git LFS - SignaVisio](https://www.youtube.com/watch?v=TsR0uWyvNdk)