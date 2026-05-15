import requests

def ask_ollama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2:1b",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_predict": 80
                }
            },
            timeout=30
        )

        return response.json().get("response", "No response from Ollama.")

    except Exception as e:
        return f"Ollama error: {str(e)}"