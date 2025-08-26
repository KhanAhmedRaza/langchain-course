import sys
import os

print("=== Python Environment Check ===")
print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")
print(f"Current working directory: {os.getcwd()}")

# Check if dotenv is available
try:
    import dotenv
    print("✅ python-dotenv is available")
except ImportError:
    print("❌ python-dotenv is NOT available")

# Check if langchain packages are available
try:
    import langchain_openai
    print("✅ langchain_openai is available")
except ImportError:
    print("❌ langchain_openai is NOT available")

try:
    import langchain_core
    print("✅ langchain_core is available")
except ImportError:
    print("❌ langchain_core is NOT available")

print("=== Check Complete ===")


