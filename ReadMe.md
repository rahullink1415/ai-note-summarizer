# AI Note Summarizer — README

Short README for setting up a Python virtual environment and running this project against local Ollama models.

## Requirements
- Python 3.9+ recommended
- Ollama installed locally (see Ollama docs for installation)

## 1. Create and activate a virtual environment
macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows (cmd):
```cmd
python -m venv .venv
.venv\Scripts\activate
```

Windows (PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

## 2. Install Python dependencies
If a requirements.txt exists:
```bash
pip install -r requirements.txt
```
Or install only what you need, e.g.:
```bash
pip install requests
# pip install ollama    # if using the ollama python client (optional)
```

## 3. Prepare local Ollama model
1. Install Ollama (follow official docs).
2. Pull the model you want to use:
```bash
ollama pull <model-name>
# example: ollama pull llama2
```
3. Option A — Run the model interactively:
```bash
ollama run <model-name>
```
3. Option B — Use the Ollama HTTP API (daemon provides a local REST endpoint, default port 11434):
```bash
# Example: quick test via curl
curl -s -X POST http://localhost:11434/api/generate \
    -H "Content-Type: application/json" \
    -d '{"model":"<model-name>","prompt":"Summarize the following notes:\n\n..."}'
```

Note: replace `<model-name>` with the model you pulled (or your preferred local model name).

## 4. Configure your app to use Ollama
- If your app uses HTTP to call Ollama, set the base URL (default):
```bash
export OLLAMA_URL="http://localhost:11434"
```
- If your app accepts a model name argument, run:
```bash
python summarize.py --input notes.txt --model <model-name>
```
(Adjust script name and flags to match your repository.)

## 5. Example workflow
1. Create venv and activate.
2. pip install -r requirements.txt
3. ollama pull <model-name>
4. Start Ollama or ensure daemon is running.
5. Run the summarizer:
```bash
python summarize.py --input notes.md --model <model-name>
```

## Tips
- Test the Ollama endpoint with curl before running the app.
- Use small models locally while developing to reduce memory/CPU usage.
- Add any project-specific flags or config to this README as needed.

That's it — modify script names and flags to match this repository.

Run using command
  python orchestrator.py

  
  