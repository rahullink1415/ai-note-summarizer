from utils import run_local_llm

class ReaderAgent:
    def run(self, text):
        return run_local_llm(
            system_prompt="You analyze and clean raw text.",
            user_text=text
        )
