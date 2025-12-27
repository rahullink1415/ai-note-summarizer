import sys
from pathlib import Path

# Ensure project root is on sys.path so sibling packages (like `agents`) can be imported
# This makes running `python webui/app.py` work from the repo root as well as
# `python -m webui.app`.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from flask import Flask, render_template, request, jsonify
from agents.reader_agent import ReaderAgent
from agents.summarizer_agent import SummarizerAgent
from agents.action_agent import ActionAgent
from agents.formatter_agent import FormatterAgent

app = Flask(__name__, template_folder="templates")


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/summarize", methods=["POST"])
def summarize():
    # Accept form-encoded or JSON body
    if request.is_json:
        body = request.get_json(silent=True) or {}
        text = body.get("text")
    else:
        text = request.form.get("text")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Run the same pipeline as orchestrator, but use the submitted text
    reader = ReaderAgent()
    summarizer = SummarizerAgent()
    action_agent = ActionAgent()
    formatter = FormatterAgent()

    clean_text = reader.run(text)
    summary = summarizer.run(clean_text)
    actions = action_agent.run(clean_text)
    output = formatter.run(summary, actions)

    return jsonify(output)


if __name__ == "__main__":
    # Debug server for local use. Use a production server for deployment.
    app.run(host="0.0.0.0", port=7860, debug=True)
