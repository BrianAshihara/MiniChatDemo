from core.chatbot import LocalChatbot
from tools.system_tools import list_files, current_time, read_text_file

MODEL_PATH = "model/model.gguf"

chatbot = LocalChatbot(MODEL_PATH)

print("🤖 Chatbot Local — rodando offline totalmente!\n")
print("Digite 'sair' para encerrar.\n")

while True:
    user = input("Você: ")

    if user.lower() == "sair":
        print("Encerrando...")
        break

    # Comandos especiais
    if user.startswith("listar"):
        path = user.replace("listar ", "").strip()
        print(list_files(path if path else "."))
        continue

    if user == "hora":
        print(current_time())
        continue

    if user.startswith("ler "):
        filename = user.replace("ler ", "")
        print(read_text_file(filename))
        continue

    # IA responde
    answer = chatbot.ask(user)
    print("\nAssistente:", answer, "\n")
