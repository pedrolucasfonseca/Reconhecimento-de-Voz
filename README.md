# 📝 Reconhecimento de Voz com Python

Um projeto simples em Python que utiliza a biblioteca `SpeechRecognition` para capturar áudio do microfone e transcrevê-lo para texto em português.

## 🚀 Funcionalidades

- Captura de áudio via microfone
- Transcrição automática usando o serviço da Google
- Suporte ao idioma português (pt-BR)

## 📁 Estrutura do Projeto

```bash

├── tarefas.py         # Script principal
```

## 💻 Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/pedrolucasfonseca/Reconhecimento-de-Voz.git
   cd Reconhecimento-de-Voz
   ```

2. Instale as dependências:
   ```bash
   pip install SpeechRecognition
   pip install pyaudio
   ```

3. Execute o script:
   ```bash
   python reconhecimento voz.py
   ```

## 🧠 Como Funciona

- O script ajusta o microfone ao ruído ambiente.
- Grava o áudio por um tempo definido (padrão: 10 segundos).
- Utiliza o serviço de reconhecimento de voz da Google para transcrever o áudio.

## 📌 Requisitos

- Python 3.10 ou superior
- Microfone funcional

## 📷 Exemplo de Uso

```bash
Escutando...
Transcrição: Olá, este é um teste de reconhecimento de voz.
```
