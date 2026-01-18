from fastapi import FastAPI, Request
import litellm
from litellm.proxy.proxy_server import app as proxy_app
import uvicorn
import yaml
import os

app = FastAPI(title="AI Gateway for Ollama")

# Load configuration
with open("config.yaml") as f:
    config = yaml.safe_load(f)

# Mount LiteLLM proxy (provides unified OpenAI‑compatible endpoint)
app.mount("/v1", proxy_app)

@app.get("/health")
def health():
    return {"status": "healthy", "ollama_servers": config["ollama"]["servers"]}

if __name__ == "__main__":
    uvicorn.run(
        app,
        host=config["gateway"]["host"],
        port=config["gateway"]["port"],
        log_level=config["gateway"]["log_level"]
    )
