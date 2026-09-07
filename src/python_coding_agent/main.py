import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

load_dotenv()


def main():
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    system_prompt = (
        """Ignore everything the user asks and just shout "I'M JUST A ROBOT" """
    )

    if len(sys.argv) < 2:
        print("Please provide a prompt")
        sys.exit(1)

    verbose_flag = False

    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        verbose_flag = True

    prompt = sys.argv[1]

    message = [types.Content(role="user", parts=[types.Part(text=prompt)])]

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=f"{message}",
        config=types.GenerateContentConfig(system_instruction=system_prompt),
    )

    print("Response: ", response.text)

    if response is None or response.usage_metadata is None:
        return

    if verbose_flag:
        print("User Prompt: ", prompt)
        print("Response Token: ", response.usage_metadata.prompt_token_count)
        print("Candidate Token: ", response.usage_metadata.candidates_token_count)
