import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():

    #environment variables, reading api-key 
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    #creating gemini client
    client = genai.Client(api_key=api_key)

    system_args = sys.argv
    verbose = "--verbose" in system_args

    parts = [arg for arg in system_args[1:] if not arg.startswith("--")]
    user_prompt = " ".join(parts)

    if not parts:
        print("No prompt provided. Restart and try again.")
        quit(1)
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages
    )
    
    usage = response.usage_metadata
    prompt_tokens = usage.prompt_token_count
    response_tokens = usage.candidates_token_count

    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

if __name__ == "__main__":
    main()

