import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from .functions.get_files_info import schema_get_files_info

load_dotenv()


def main():
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    system_prompt = """
You are a helpful AI coding agent.

You have access to tools that you may use when necessary.

Available operations:
- List files and directories

Only call a function when it is necessary to answer the user's request.
If you can answer the user's question without inspecting files, respond normally.

All paths provided to functions must be relative to the working directory.
The working directory is automatically injected for security reasons.
"""

    if len(sys.argv) < 2:
        print("Please provide a prompt")
        sys.exit(1)

    verbose_flag = False

    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        verbose_flag = True

    prompt = sys.argv[1]

    message = [types.Content(role="user", parts=[types.Part(text=prompt)])]

    available_functions = types.Tool(function_declarations=[schema_get_files_info])

    config = types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    )

    response = client.models.generate_content(
        model="gemini-3.6-flash", contents=message, config=config
    )

    if response is None or response.usage_metadata is None:
        return

    if verbose_flag:
        print("User Prompt: ", prompt)
        print("Response Token: ", response.usage_metadata.prompt_token_count)
        print("Candidate Token: ", response.usage_metadata.candidates_token_count)

    if response.function_calls:

        for function_call_part in response.function_calls:
            print(
                f"Calling functions: {function_call_part.name}({function_call_part.args})"
            )

    else:
        print("Response: ", response.text)
