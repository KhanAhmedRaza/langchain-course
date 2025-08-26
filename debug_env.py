import os
from dotenv import load_dotenv

print("=== Environment Debug Script ===")
print(f"Python executable: {os.sys.executable}")
print(f"Current working directory: {os.getcwd()}")

# Get the current directory and explicitly load .env file
current_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(current_dir, '.env')

print(f"Script directory: {current_dir}")
print(f"Looking for .env file at: {env_path}")
print(f".env file exists: {os.path.exists(env_path)}")

if os.path.exists(env_path):
    print("Reading .env file contents:")
    with open(env_path, 'r') as f:
        content = f.read()
        # Hide the actual API key for security
        lines = content.split('\n')
        for line in lines:
            if line.startswith('OPENAI_API_KEY='):
                key_part = line.split('=')[1]
                print(f"OPENAI_API_KEY={key_part[:10]}... (length: {len(key_part)})")
            else:
                print(line)

# Load environment variables from .env file with explicit path
print("\nLoading .env file...")
load_dotenv(env_path)

# Check environment variables
print("\nEnvironment variables after loading .env:")
api_key = os.environ.get('OPENAI_API_KEY')
if api_key:
    print(f"✅ OPENAI_API_KEY found: {api_key[:10]}... (length: {len(api_key)})")
else:
    print("❌ OPENAI_API_KEY not found in environment")

langchain_tracing = os.environ.get('LANGCHAIN_TRACING_V2')
print(f"LANGCHAIN_TRACING_V2: {langchain_tracing}")

print("\n=== Debug Complete ===")
