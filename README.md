# AI Gateway for Ollama

![Ollama](https://img.shields.io/badge/ollama-%23000000.svg?style=for-the-badge&logo=ollama&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/your-username/your-repo/your-workflow.yml)](https://github.com/your-username/your-repo/actions) ![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
https://img.shields.io/badge/ollama-%23000000.svg?style=for-the-badge&logo=ollama&logoColor=white
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![LangChain](https://img.shields.io/badge/langchain-%231C3C3C.svg?style=for-the-badge&logo=langchain&logoColor=white)

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

``````python
from typing import Dict, List, Optional

Import your provider clients
from providers.github_models import GitHubModelsClient
from providers.deepseek import DeepSeekClient
from providers.openai_provider import OpenAIClient
from providers.ollama_provider import OllamaClient


class AIProviderRouter:
    """
    Unified router for all AI providers.
    Routes requests based on model name, provider name, or governance rules.
    """

    def init(self):
        # Instantiate provider clients
        self.providers = {
            "github": GitHubModelsClient(),
            "deepseek": DeepSeekClient(),
            "openai": OpenAIClient(),
            "ollama": OllamaClient(),
        }

        # Model → Provider mapping
        # You can expand this as your ecosystem grows
        self.model_map = {
            # GitHub Models
            "meta/": "github",
            "microsoft/": "github",
            "phi-": "github",

            # DeepSeek
            "deepseek-": "deepseek",

            # OpenAI
            "gpt-": "openai",

            # Ollama (local)
            "ollama/": "ollama",
        }

    # ---------------------------------------------------------
    # Provider Resolution
    # ---------------------------------------------------------
    def resolve_provider(self, model: str, provider: Optional[str] = None) -> str:
        """
        Determine which provider should handle the request.
        Priority:
        1. Explicit provider override
        2. Model prefix mapping
        3. Error if unknown
        """

        # Explicit override
        if provider:
            if provider not in self.providers:
                raise ValueError(f"Unknown provider: {provider}")
            return provider

        # Prefix-based routing
        for prefix, mappedprovider in self.modelmap.items():
            if model.startswith(prefix):
                return mapped_provider

        raise ValueError(f"No provider found for model: {model}")

    # ---------------------------------------------------------
    # Unified Completion API
    # ---------------------------------------------------------
    def complete(
        self,
        model: str,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        top_p: float = 1.0,
        max_tokens: Optional[int] = None,
        provider: Optional[str] = None,
    ) -> str:
        """
        Unified non-streaming completion interface.
        """

        resolved = self.resolve_provider(model, provider)

        # Normalize model name for Ollama
        if resolved == "ollama" and model.startswith("ollama/"):
            model = model.replace("ollama/", "")

        client = self.providers[resolved]

        return client.complete(
            model=model,
            messages=messages,
            temperature=temperature,
            topp=topp,
            maxtokens=maxtokens,
        )

    # ---------------------------------------------------------
    # Unified Streaming API
    # ---------------------------------------------------------
    def stream(
        self,
        model: str,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        top_p: float = 1.0,
        max_tokens: Optional[int] = None,
        provider: Optional[str] = None,
    ):
        """
        Unified streaming interface.
        """

        resolved = self.resolve_provider(model, provider)

        # Normalize model name for Ollama
        if resolved == "ollama" and model.startswith("ollama/"):
            model = model.replace("ollama/", "")

        client = self.providers[resolved]

        return client.stream(
            model=model,
            messages=messages,
            temperature=temperature,
            topp=topp,
            maxtokens=maxtokens,
        )
```

.
```

---

🧩 How This Fits Into Your Ecosystem

Your backend now has:

$
`
/providers
  github_models.py
  deepseek.py
  openai_provider.py
  ollama_provider.py

ai_router.py
`


Usage Example

`python
router = AIProviderRouter()

response = router.complete(
    model="ollama/llama3.2",
    messages=[
        {"role": "user", "content": "Explain zero-knowledge proofs simply."}
    ]
)

print(response)
```


```

Or GitHub Models:

```python
response = router.complete(
    model="meta/Llama-4-Scout-17B-16E-Instruct",
    messages=[{"role": "user", "content": "Summarize this document."}]
)
```



```

Or DeepSeek:

```python
response = router.complete(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "Optimize this Python code."}]
)
```
