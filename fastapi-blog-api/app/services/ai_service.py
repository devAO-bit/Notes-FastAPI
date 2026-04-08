import httpx

OLLAMA_URL = "http://localhost:11434/api/generate"


async def summarize_text(text: str):

    prompt = f"Summarize this note in 1-2 sentences:\n{text}"

    async with httpx.AsyncClient(timeout=60) as client:

        response = await client.post(
            OLLAMA_URL,
            json={
                "model": "gemma:2b",
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()

        return data["response"]


async def generate_title(content: str):

    prompt = f"""
Generate a short and clear title (max 8 words) for this note:

{content}
"""

    async with httpx.AsyncClient(timeout=60) as client:

        response = await client.post(
            OLLAMA_URL,
            json={
                "model": "gemma:2b",
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()

        return data["response"].strip()