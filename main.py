import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from functions.call_function import call_function, available_functions

def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("ERROR")
        sys.exit(1)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")
 
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    result = generate_content(client, messages, verbose)

def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )

    if not response.function_calls:
        return response.text

    tool_responses = []
    for function_call_part in response.function_calls:
        tool_response = call_function(function_call_part, verbose=verbose)
        tool_responses.append(tool_response)

    return tool_responses


if __name__ == "__main__":
    main()
