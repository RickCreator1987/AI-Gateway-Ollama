# AI-Gateway-Ollama
# AI Gateway for Ollama

A lightweight, Python‑based API gateway that routes requests to Ollama instances with features like load balancing, rate limiting, and OLLAMA_TOKEN authentication.

## Features
- OpenAI‑compatible endpoint (`/v1/chat/completions`)
- Configurable Ollama server routing
- Rate limiting & OLLAMA_TOKEN authentication
- Health checks & metrics
- Docker & Kubernetes ready

## Quick Start
1. Clone the repo: `git clone https://github.com/rickcreator1987/AI-Gateway-Ollama`
2. Install dependencies: `pip install -r requirements.txt`
3. Configure `config.yaml` and set environment variables.
4. Run: `python app.py`

## API Usage
```bash
curl -X POST http://localhost:8080/v1/chat/completions \
  -H "Authorization: OLLAMA_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"model": "llama3.1:8b", "messages": [{"role": "user", "content": "Hello"}]}'
