from utils import run_local_llm

class SummarizerAgent:
    def run(self, text):
        return run_local_llm(
            system_prompt="Summarize the content clearly in 2–3 lines.",
            user_text=text
        )
