import sys
import subprocess
import argparse

from openai import OpenAI
import pyperclip


class AnsweringMachine:

    def __init__(self):
        self.application_usage = "answering-machine --openai-api-key <api-key>"
        self.application_description = "A stressed out and under appreciated 40 year old IT worker (ChatGPT) takes questions from your system clipboard and updates your clipboards contents with interesting answers."

        cmd_opts = self.__parse_arguments()
        self.client = OpenAI(api_key=cmd_opts.api_key)

    def __parse_arguments(self):
        arg_parser = argparse.ArgumentParser(
            usage=self.application_usage,
            description=self.application_description,
        )
        arg_parser.add_argument(
            "--openai-api-key",
            "--api-key",
            type=str,
            required=True,
            help="OpenAI API Key",
            dest="api_key",
        )
        return arg_parser.parse_args()

    def __send_success_notification(self) -> None:
        subprocess.run(["notify-send", "Answer", "is", "ready!"])
        return

    def __send_failure_notification(self) -> None:
        subprocess.run(["notify-send", "Unable", "to", "answer", "question!"])
        return

    def __get_clipboard(self) -> str:
        return pyperclip.paste()

    def __update_clipboard(self, text: str) -> None:
        pyperclip.copy(text)
        return

    def __get_answer(self, question: str) -> str | bool:

        # Get ChatGPT Answer
        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are an overworked and stressed out assistant that provides answers to technical questions. The answers should give the appearance of annoyance and irritability. Additionaly, you will include random spontanious remarks about going through your third divorce, back pain, and high cholesteral to give an impression that you are an overworked and underappreciated 40 year old help desk worker.",
                },
                {"role": "user", "content": f"{question}"},
            ],
        )

        answer = completion.choices[0].message.content

        if answer is None:
            return False
        else:
            return answer

    def run(self) -> None:
        question = self.__get_clipboard()

        answer = self.__get_answer(question)
        if answer is False:
            self.__send_failure_notification()
            sys.exit(1)
        else:
            self.__update_clipboard(answer)  # pyright: ignore
            self.__send_success_notification()
            sys.exit(0)


def main() -> None:
    answering_machine = AnsweringMachine()
    answering_machine.run()


if __name__ == "__main__":
    main()
