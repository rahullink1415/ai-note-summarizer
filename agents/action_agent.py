from utils import run_local_llm

class ActionAgent:
    def run(self, text):
        result = run_local_llm(
            system_prompt="Extract clear action items as bullet points.",
            user_text=text
        )
        return [line.strip("-• ") for line in result.split("\n") if line.strip()]
