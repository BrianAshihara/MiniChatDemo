import os
import logging
import contextlib
from llama_cpp import Llama

class LocalChatbot:
    def __init__(self, model_path, max_history=5, n_ctx=4096, n_threads=4,
                 suppress_startup_messages=True):

        logging.getLogger("llama_cpp").setLevel(logging.ERROR)

        self.history = []
        self.max_history = max_history

        if suppress_startup_messages:
            try:
                devnull = open(os.devnull, "w")
                with contextlib.redirect_stderr(devnull):
                    self.llm = Llama(model_path=model_path, n_ctx=n_ctx, n_threads=n_threads, verbose=False)
            finally:
                try:
                    devnull.close()
                except Exception:
                    pass
        else:
            self.llm = Llama(model_path=model_path, n_ctx=n_ctx, n_threads=n_threads, verbose=False)

    def build_prompt(self, user_message):
        system = (
            "Você é um assistente pessoal útil, conciso e educado. "
            "Se o usuário pedir comandos de sistema, responda normalmente."
        )

        history_text = ""
        for role, msg in self.history[-self.max_history:]:
            history_text += f"{role}: {msg}\n"

        prompt = (
            f"### Sistema:\n{system}\n\n"
            f"### Conversa:\n{history_text}"
            f"Usuário: {user_message}\n"
            f"Assistente:"
        )
        return prompt

    def ask(self, user_message):
        prompt = self.build_prompt(user_message)

        response = self.llm(
            prompt,
            max_tokens=300,
            temperature=0.7,
            stop=["Usuário:", "Assistente:"]
        )

        answer = response["choices"][0]["text"].strip()

        self.history.append(("Usuário", user_message))
        self.history.append(("Assistente", answer))

        return answer
