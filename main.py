import os
from dotenv import load_dotenv
from google import genai

def main():

    #environment variables, reading api-key 
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    print("API key present: ", bool(api_key))
    #creating gemini client
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents='Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.'
    )
    print(response.text)

    usage = response.usage_metadata
    prompt_tokens = usage.prompt_token_count
    response_tokens = usage.candidates_token_count

    print("Prompt tokens: " + str(prompt_tokens))
    print("Response tokens: " + str(response_tokens))



if __name__ == "__main__":
    main()
