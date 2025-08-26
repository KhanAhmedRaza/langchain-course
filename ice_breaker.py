import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq
from third_parties.linkedin import scrape_linkedin_profile
from agent.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parsers import summary_parser
from output_parsers import Summary
from typing import Tuple
# Disable LangChain tracing
os.environ["LANGCHAIN_TRACING_V2"] = "false"
#os.environ["LANGCHAIN_ENDPOINT"] = ""
# Ensure Ollama host is set
os.environ["OLLAMA_HOST"] = "http://localhost:11434"

# Get the current directory and explicitly load .env file
current_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(current_dir, '.env')

print(f"Current directory: {current_dir}")
print(f"Looking for .env file at: {env_path}")
print(f".env file exists: {os.path.exists(env_path)}")

# Load environment variables from .env file with explicit path
load_dotenv(env_path)
def ice_break_with(name:str) -> Tuple[Summary, str]:
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username, mock=True)
    # Check if the API key is set
    api_key = os.environ.get('OPENAI_API_KEY')
    if api_key:
        print(f"API Key found: {api_key[:10]}...")  # Only show first 10 characters for security
        print(f"API Key length: {len(api_key)} characters")
    else:
        print("Warning: OPENAI_API_KEY environment variable is not set!")
        print("Please set it using: $env:OPENAI_API_KEY = 'your-actual-api-key'")

    summary_template = """
    Given the information about a person from Linkedin:
    {information}

    Please return a JSON object in the following format:
    {{
        "summary": "A short summary here.",
        "facts": [
            "First interesting fact.",
            "Second interesting fact."
        ]
    }}

    Only return valid JSON. Do not include any other text or explanation.
    {format_instructions}
    """
    
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template,
                                             partial_variables={"format_instructions": summary_parser.get_format_instructions()})

    # Try different models in order of preference - prioritize Groq Llama3.1, then Mistral (Ollama), then others
    models_to_try = [
        ("llama3.1", "Groq - Llama3.1"),
        ("mistral", "Ollama - Mistral"),
        ("llama3", "Ollama - Llama3"), 
        ("llama2", "Ollama - Llama2"),
        ("codellama", "Ollama - CodeLlama"),
        ("openai", "OpenAI - GPT-3.5-turbo")
    ]
    
    llm = None
    model_name = None
    
    for model, display_name in models_to_try:
        try:
            print(f"\nTrying {display_name}...")
            if model == "openai":
                llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
            elif model == "llama3.1":
                # Use Groq Chat API
                groq_key = os.environ.get("GROQ_API_KEY")
                if not groq_key:
                    raise RuntimeError("GROQ_API_KEY not set in environment/.env")
                groq_model = os.environ.get("GROQ_MODEL", "llama-3.1-8b-instant")
                llm = ChatGroq(model=groq_model, temperature=0)
            else:
                # Default to Ollama for the remaining model names
                llm = ChatOllama(model=model, temperature=0, base_url=os.environ.get("OLLAMA_HOST", "http://localhost:11434"))
            
            # Test the model with a simple prompt
            _ = llm.invoke("Hello")
            print(f"✅ Successfully connected to {display_name}")
            model_name = display_name
            break
            
        except Exception as e:
            print(f"❌ Failed to connect to {display_name}: {str(e)}")
            continue
    
    if llm is None:
        print("\n❌ Could not connect to any model. Please check your setup.")
        exit(1)

    chain = summary_prompt_template | llm | summary_parser
    
    print(f"\n" + "="*50)
    print(f"GENERATING SUMMARY AND FACTS USING {model_name}...")
    print("="*50)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/khanahmedraza/")
    res:Summary = chain.invoke(input={"information": linkedin_data})

   # print("\n" + "="*50)
    #print("RESULT:")
    #print("="*50)
   # print(res.summary)
   # print(res.facts)
   # print("="*50)
    return res, linkedin_data.get("photoUrl")

if __name__ == "__main__":
    print("Ice Breaker Enter!")
    ice_break_with("Ahmed Raza Khan")
    
   
   

    
    
   







