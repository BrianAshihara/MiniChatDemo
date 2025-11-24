# 🚀 Chatbot Local com IA — 100% Offline, Privado e Gratuito

Este projeto implementa um **chatbot de Inteligência Artificial totalmente local**, rodando em sua máquina sem usar APIs pagas, sem enviar dados para a internet e sem depender de serviços externos.

Ele utiliza o modelo **Llama 2 7B Chat** no formato **GGUF**, carregado pelo backend otimizado `llama-cpp-python`, garantindo desempenho mesmo em CPUs comuns.

O objetivo é servir como um projeto de portfólio sólido, demonstrando conhecimento prático em:

* **Modelos LLM (Large Language Models)**
* **Execução local de IA**
* **Python**
* **Construção de prompts**
* **Manuseio de contexto / histórico de conversas**
* **Arquitetura simples, clara e eficiente**

---

## 📌 Funcionalidades

* 🤖 **Chatbot inteligente** que roda na sua máquina
* 🔒 **Zero internet** — total privacidade
* 🧠 **IA open-source** usando Llama 2
* 💬 **Histórico de conversas** com contexto
* 🆓 **100% gratuito**

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.11**
* `llama-cpp-python`
* **Modelos LLM** no formato **GGUF**
* VSCode / PowerShell
---

## 🧠 Como o chatbot funciona
* **Este projeto utiliza um Large Language Model (LLM): um modelo treinado em bilhões de palavras para aprender padrões da linguagem humana.**

Etapas internas:

- Você envia uma mensagem.

- O código constrói um prompt, incluindo histórico e instruções.

- O modelo Llama 2 processa o texto e prevê a próxima palavra.

- A IA repete esse processo milhares de vezes por segundo.

- O modelo devolve uma resposta completa e coerente.

Importante: Não há regras programadas. A inteligência emerge do treinamento massivo do modelo.

## 🎯 Objetivo do Projeto
- Este projeto foi criado para:

- Demonstrar habilidades com IA moderna

- Apresentar domínio prático de LLMs em Python

- Construir um chatbot totalmente funcional

- Garantir privacidade (nenhum dado sai da sua máquina)

## 📦 Instalação

### 1. Clone o repositório

- git clone [https://github.com/brianashihara/MiniChatDemo.git](https://github.com/brianashihara/MiniChatDemo.git)
2. Crie e ative o ambiente virtual
- py -3.11 -m venv venv
- venv\Scripts\activate
3. Instale as dependências

- pip install -r requirements.txt
4. Baixe o modelo de IA
- Acesse a página do modelo:

- 👉 https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF

- Baixe o arquivo recomendado:

- llama-2-7b-chat.Q4_K_M.gguf

- Coloque este arquivo dentro da pasta "model/" e renomeie o arquivo para model.gguf


## 📄 Licença
* Este projeto é livre para uso pessoal, educacional e para portfólio.