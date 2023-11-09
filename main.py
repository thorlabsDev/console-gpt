import asyncio
import httpx
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"


async def async_gptbot(session_data, query, temperature=0.8):
    """
    Async function to interact with OpenAI's GPT model.

    :param session_data: The conversation history (list of messages).
    :param query: The user's query string.
    :param temperature: The temperature for the GPT model's response.
    :return: Updated session data including the response.
    """
    if not OPENAI_API_KEY:
        print("Error: OPENAI_API_KEY is not set.")
        return session_data

    # Append the new user message to the session
    session_data.append({"role": "user", "content": query})

    data = {
        "model": "gpt-4",
        # The current implementation uses GPT-4, but OpenAI offers a range of models
        # with different capabilities. For more information and to explore other models,
        # refer to the OpenAI documentation: https://platform.openai.com/docs/models

        "messages": session_data,
        "temperature": temperature
    }

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.post(OPENAI_API_URL, json=data, headers=headers)

            if response.status_code == 200:
                response_json = response.json()
                bot_message = response_json["choices"][0]["message"]["content"].strip()
                # Append bot's response to the session data
                session_data.append({"role": "assistant", "content": bot_message})
                return session_data
            else:
                print(f"Error: Received status code {response.status_code}")
                return session_data

        except Exception as e:
            print(f"Error during chatbot query: {type(e).__name__} - {str(e)}")
            return session_data


async def main():
    session_data = [{"role": "system", "content": "You are a helpful assistant."}]
    print("GPT Chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Exiting chatbot.")
            break
        session_data = await async_gptbot(session_data, user_input)
        print("GPT:", session_data[-1]['content'])


if __name__ == "__main__":
    asyncio.run(main())
