import json
from agents.reader_agent import ReaderAgent
from agents.summarizer_agent import SummarizerAgent
from agents.action_agent import ActionAgent
from agents.formatter_agent import FormatterAgent

def read_input():
    with open("input.txt", "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    text = read_input()

    reader = ReaderAgent()
    summarizer = SummarizerAgent()
    action_agent = ActionAgent()
    formatter = FormatterAgent()

    print("📥 Reader Agent processing...")
    clean_text = reader.run(text)

    print("🧠 Summarizer Agent working...")
    summary = summarizer.run(clean_text)

    print("📌 Action Agent extracting tasks...")
    actions = action_agent.run(clean_text)

    print("🧾 Formatter Agent assembling output...")
    output = formatter.run(summary, actions)

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print("✅ Multi-agent output saved to output.json")

    with open("output.json", "r", encoding="utf-8") as f:
        print(f.read())

