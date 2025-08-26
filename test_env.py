import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

if __name__ == "__main__":
    print("Testing .env file loading...")
    
    # Check if the API key is set
    api_key = os.environ.get('OPENAI_API_KEY')
    if api_key:
        print(f"✅ API Key found: {api_key[:10]}...")  # Only show first 10 characters for security
        print("✅ .env file is being loaded correctly!")
    else:
        print("❌ Warning: OPENAI_API_KEY environment variable is not set!")
        print("❌ .env file is not being loaded correctly!")
    
    # Check other environment variables
    langchain_tracing = os.environ.get('LANGCHAIN_TRACING_V2')
    print(f"LANGCHAIN_TRACING_V2: {langchain_tracing}")


