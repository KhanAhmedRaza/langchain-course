import os

from dotenv import load_dotenv

load_dotenv()


def main():
    print("Hello from langchain-course!")
    print("LANGCHAIN_ENDPOINT:", os.getenv("LANGCHAIN_ENDPOINT"))
    print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
    print("LANGCHAIN_TRACING_V2:", os.getenv("LANGCHAIN_TRACING_V2"))
    print("GROQ_API_KEY:", os.getenv("GROQ_API_KEY"))
    print("TAVILY_API_KEY:", os.getenv("TAVILY_API_KEY"))
    print("LANGCHAIN_API_KEY:", os.getenv("LANGCHAIN_API_KEY"))


if __name__ == "__main__":
    main()
