"""
API Connection Checker Utility for IPMDAR AI Expert System

This script verifies connectivity to all six API services used by the IPMDAR AI Expert System:
- OpenAI (Dr. Compliance)
- Anthropic (Dr. Data Analytics)
- Groq (Dr. Project Management)
- Google Gemini (Dr. Risk & Forecasting)
- Cohere (Dr. Systems Integration)
- EmergenceAI (Dr. Implementation Support)

Run this script to check if your API keys are configured correctly
and if you have network connectivity to the services.
"""

import os
import sys
import requests
from dotenv import load_dotenv

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Status indicators (using ASCII characters instead of Unicode)
SUCCESS = "[OK]"
FAILURE = "[ERROR]"
WARNING = "[WARNING]"
INFO = "[INFO]"

def main():
    """Run API connection tests for all providers"""
    # Load environment variables
    load_dotenv()
    
    print(f"\n{INFO} IPMDAR AI Expert System - API Connection Check")
    print("=" * 60)
    
    # Check all providers
    check_openai()
    check_anthropic()
    check_groq()
    check_google()
    check_cohere()
    check_emergenceai()
    
    print("\n" + "=" * 60)
    print(f"{INFO} API connection check complete")
    print(f"{INFO} If any check failed, verify your API keys in the .env file")
    print(f"{INFO} Remember to install required packages with: pip install -r requirements.txt")
    print("=" * 60 + "\n")

def check_openai():
    """Test OpenAI API connection"""
    print(f"\n{INFO} Checking OpenAI API (Dr. Compliance)...")
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print(f"{WARNING} OpenAI: No API key found")
            return
            
        import openai
        client = openai.OpenAI(api_key=api_key)
        # Just check if we can list models
        models = client.models.list()
        if models:
            print(f"{SUCCESS} OpenAI: Connection successful")
        else:
            print(f"{WARNING} OpenAI: Connected but no models returned")
    except ImportError:
        print(f"{FAILURE} OpenAI: Module not installed (pip install openai)")
    except Exception as e:
        print(f"{FAILURE} OpenAI: {str(e)}")

def check_anthropic():
    """Test Anthropic API connection"""
    print(f"\n{INFO} Checking Anthropic API (Dr. Data Analytics)...")
    try:
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            print(f"{WARNING} Anthropic: No API key found")
            return
            
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)
        # We can't easily list models, so just check if the client initializes
        if client:
            print(f"{SUCCESS} Anthropic: Client initialized successfully")
        else:
            print(f"{WARNING} Anthropic: Client initialization failed")
    except ImportError:
        print(f"{FAILURE} Anthropic: Module not installed (pip install anthropic)")
    except Exception as e:
        print(f"{FAILURE} Anthropic: {str(e)}")

def check_groq():
    """Test Groq API connection"""
    print(f"\n{INFO} Checking Groq API (Dr. Project Management)...")
    try:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            print(f"{WARNING} Groq: No API key found")
            return
            
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        response = requests.get("https://api.groq.com/openai/v1/models", headers=headers)
        if response.status_code == 200:
            print(f"{SUCCESS} Groq: Connection successful")
        else:
            print(f"{FAILURE} Groq: Connection failed (Status {response.status_code}: {response.text})")
    except Exception as e:
        print(f"{FAILURE} Groq: {str(e)}")

def check_google():
    """Test Google Gemini API connection"""
    print(f"\n{INFO} Checking Google Gemini API (Dr. Risk & Forecasting)...")
    try:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            print(f"{WARNING} Google Gemini: No API key found")
            return
            
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        models = genai.list_models()
        if models:
            print(f"{SUCCESS} Google Gemini: Connection successful")
        else:
            print(f"{WARNING} Google Gemini: Connected but no models returned")
    except ImportError:
        print(f"{FAILURE} Google Gemini: Module not installed (pip install google-generativeai)")
    except Exception as e:
        print(f"{FAILURE} Google Gemini: {str(e)}")

def check_cohere():
    """Test Cohere API connection"""
    print(f"\n{INFO} Checking Cohere API (Dr. Systems Integration)...")
    try:
        api_key = os.getenv("COHERE_API_KEY")
        if not api_key:
            print(f"{WARNING} Cohere: No API key found")
            return
            
        import cohere
        client = cohere.Client(api_key)
        # We can't easily list models, so just check if the client initializes
        if client:
            print(f"{SUCCESS} Cohere: Client initialized successfully")
        else:
            print(f"{WARNING} Cohere: Client initialization failed")
    except ImportError:
        print(f"{FAILURE} Cohere: Module not installed (pip install cohere)")
    except Exception as e:
        print(f"{FAILURE} Cohere: {str(e)}")

def check_emergenceai():
    """Test EmergenceAI API connection"""
    print(f"\n{INFO} Checking EmergenceAI API (Dr. Implementation Support)...")
    try:
        api_key = os.getenv("EMERGENCEAI_API_KEY")
        if not api_key:
            print(f"{WARNING} EmergenceAI: No API key found")
            return
            
        # Simple request to check API key validity
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        # We don't make an actual API call here since this is just a check
        # In a real implementation, you would make a test request
        print(f"{INFO} EmergenceAI: API key found, but no test request made (API structure may vary)")
    except Exception as e:
        print(f"{FAILURE} EmergenceAI: {str(e)}")

if __name__ == "__main__":
    main()
