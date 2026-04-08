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
Generate ONLY ONE short title (maximum 6 words).
Return ONLY the title text.
Do not explain anything.

Note:
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

        title = data["response"].strip()

        title = title.split("\n")[0]

        return title