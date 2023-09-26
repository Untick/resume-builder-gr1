import os

import getpass
import openai
import tiktoken

openai_key = getpass.getpass("OpenAI API Key:")
os.environ["OPENAI_API_KEY"] = openai_key
openai.api_key = openai_key


class GPTAssistaintCV:
    def __init__(self,
                 model,
                 prompt_creator,
                 corrections,
                 user_info,
                 addition_user_info):
        self.model = model                                     # используемая модель
        self.prompt_creator = prompt_creator                   # создатель промпта (system)
        self.corrections = corrections                         # корретировки (base_info)
        self.user_info = user_info                             # основной запрос пользователя/основная информация (question)
        self.addition_user_info = addition_user_info           # Дополнительная информация, связанная с проф деятельностью (assist1, assist2)

    def num_tokens_from_messages(self, messages):
        try:
            encoding = tiktoken.encoding_for_model(self.model)
        except KeyError:
            encoding = tiktoken.get_encoding("cl100k_base")

        if self.model in ["gpt-3.5-turbo-0301", "gpt-3.5-turbo-0613", "gpt-3.5-turbo-16k", "gpt-3.5-turbo"]:
            num_tokens = 0
            for message in messages:
                num_tokens += 4
                for key, value in message.items():
                    num_tokens += len(encoding.encode(value))
                    if key == "name":
                        num_tokens -= 1
            num_tokens += 2
            return num_tokens
        else:
            raise NotImplementedError(
                f"""num_tokens_from_messages() is not presently implemented for model {self.model}.""")

    def generate_response(self, temperature=0.5):

        if self.addition_user_info:
            messages = [
                {"role": "system", "content": self.prompt_creator},
                {"role": "assistant", "content": self.addition_user_info },
                {"role": "user", "content": f"{self.corrections}\n{self.user_info}"},
            ]
        else:
            messages = [
                {"role": "system", "content": self.prompt_creator},
                {"role": "user", "content": f"{self.corrections}\n{self.user_info}"},
            ]

        result = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
        )

        message = result['choices'][0]['message']['content']
        wrapped_text = textwrap.fill(message, width=80)

        return wrapped_text
