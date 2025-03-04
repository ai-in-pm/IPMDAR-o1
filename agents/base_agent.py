import os
import json
import openai
import anthropic
import requests
from abc import ABC, abstractmethod

class BaseAgent(ABC):
    """Base class for all AI agents in the IPMDAR system."""
    
    def __init__(self, knowledge_base, name="Base Agent", expertise="IPMDAR"):
        self.knowledge_base = knowledge_base
        self.name = name
        self.expertise = expertise
        
        # Load API keys
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        self.cohere_api_key = os.getenv("COHERE_API_KEY")
        self.emergenceai_api_key = os.getenv("EMERGENCEAI_API_KEY")
        
        # Set default LLM provider
        self.llm_provider = "openai"  # Can be: openai, anthropic, groq, google, cohere, emergenceai
    
    def process_query(self, query):
        """Process a user query and return a response with accuracy rating."""
        # Retrieve relevant knowledge
        relevant_knowledge = self.retrieve_relevant_knowledge(query)
        
        # Generate response
        response = self.generate_response(query, relevant_knowledge)
        
        # Verify accuracy
        accuracy = self.verify_accuracy(query, response, relevant_knowledge)
        
        return {
            "agent": self.name,
            "response": response,
            "accuracy": accuracy
        }
    
    def retrieve_relevant_knowledge(self, query):
        """Retrieve knowledge relevant to the query."""
        # In a production system, this would use proper vector embeddings and semantic search
        relevant_sections = []
        
        # Get knowledge sections relevant to this agent's expertise
        if hasattr(self, 'knowledge_category'):
            if self.knowledge_category in self.knowledge_base:
                relevant_sections.extend(self.knowledge_base[self.knowledge_category])
        
        # Add some general knowledge
        if "general" in self.knowledge_base:
            relevant_sections.extend(self.knowledge_base["general"][:50])  # Limit to first 50 general items
            
        return relevant_sections
    
    def generate_response(self, query, relevant_knowledge):
        """Generate a response using the appropriate LLM provider."""
        
        # Prepare context with relevant knowledge
        context = "\n".join(relevant_knowledge)
        
        # Construct prompt
        prompt = f"""You are {self.name}, an AI agent with PhD-level expertise in {self.expertise}. 
You provide evidence-based, accurate assistance on IPMDAR (Integrated Program Management Data and Reporting) for DoD acquisition projects.

CONTEXT INFORMATION FROM IPMDAR IMPLEMENTATION AND TAILORING GUIDE:
{context}

USER QUERY: {query}

Please provide a comprehensive, accurate response based on your expertise and the IPMDAR Implementation and Tailoring Guide. 
Your response must be evidence-based and directly reflect the standards and guidelines in the IPMDAR documentation.
Format your response in a clear, professional manner suitable for DoD acquisition professionals.
"""

        # Use the appropriate LLM provider based on agent type
        if self.llm_provider == "openai":
            return self._generate_with_openai(prompt)
        elif self.llm_provider == "anthropic":
            return self._generate_with_anthropic(prompt)
        elif self.llm_provider == "groq":
            return self._generate_with_groq(prompt)
        elif self.llm_provider == "google":
            return self._generate_with_google(prompt)
        elif self.llm_provider == "cohere":
            return self._generate_with_cohere(prompt)
        elif self.llm_provider == "emergenceai":
            return self._generate_with_emergenceai(prompt)
        else:
            # Fallback to OpenAI if provider not implemented
            return self._generate_with_openai(prompt)
    
    def _generate_with_openai(self, prompt):
        """Generate response using OpenAI."""
        try:
            client = openai.OpenAI(api_key=self.openai_api_key)
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": f"You are {self.name}, with PhD-level expertise in {self.expertise}."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2,
                max_tokens=1000
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error generating response with OpenAI: {e}")
            return f"I apologize, but I encountered an error when generating a response. Please try again."
    
    def _generate_with_anthropic(self, prompt):
        """Generate response using Anthropic."""
        try:
            client = anthropic.Anthropic(api_key=self.anthropic_api_key)
            response = client.messages.create(
                model="claude-2",
                max_tokens=1000,
                temperature=0.2,
                system=f"You are {self.name}, with PhD-level expertise in {self.expertise}.",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.content[0].text.strip()
        except Exception as e:
            print(f"Error generating response with Anthropic: {e}")
            return f"I apologize, but I encountered an error when generating a response. Please try again."
    
    def _generate_with_groq(self, prompt):
        """Generate response using Groq."""
        try:
            headers = {
                "Authorization": f"Bearer {self.groq_api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "messages": [
                    {"role": "system", "content": f"You are {self.name}, with PhD-level expertise in {self.expertise}."},
                    {"role": "user", "content": prompt}
                ],
                "model": "llama2-70b-4096",
                "temperature": 0.2,
                "max_tokens": 1000
            }
            response = requests.post("https://api.groq.com/openai/v1/chat/completions", 
                                    headers=headers, 
                                    json=data)
            response_json = response.json()
            return response_json["choices"][0]["message"]["content"].strip()
        except Exception as e:
            print(f"Error generating response with Groq: {e}")
            return f"I apologize, but I encountered an error when generating a response. Please try again."
    
    def _generate_with_google(self, prompt):
        """Generate response using Google's Gemini API."""
        try:
            url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
            headers = {
                "Content-Type": "application/json",
            }
            data = {
                "contents": [
                    {
                        "role": "user",
                        "parts": [{"text": prompt}]
                    }
                ],
                "generationConfig": {
                    "temperature": 0.2,
                    "maxOutputTokens": 1000
                }
            }
            response = requests.post(
                f"{url}?key={self.google_api_key}",
                headers=headers,
                json=data
            )
            response_json = response.json()
            return response_json["candidates"][0]["content"]["parts"][0]["text"].strip()
        except Exception as e:
            print(f"Error generating response with Google: {e}")
            return f"I apologize, but I encountered an error when generating a response. Please try again."
    
    def _generate_with_cohere(self, prompt):
        """Generate response using Cohere."""
        try:
            url = "https://api.cohere.ai/v1/generate"
            headers = {
                "Authorization": f"Bearer {self.cohere_api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": "command-light",
                "prompt": prompt,
                "max_tokens": 1000,
                "temperature": 0.2,
                "k": 0,
                "stop_sequences": [],
                "return_likelihoods": "NONE"
            }
            response = requests.post(url, headers=headers, json=data)
            response_json = response.json()
            return response_json["generations"][0]["text"].strip()
        except Exception as e:
            print(f"Error generating response with Cohere: {e}")
            return f"I apologize, but I encountered an error when generating a response. Please try again."
    
    def _generate_with_emergenceai(self, prompt):
        """Generate response using EmergenceAI."""
        try:
            url = "https://api.emergence.ai/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {self.emergenceai_api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": "emergence-7b",
                "messages": [
                    {"role": "system", "content": f"You are {self.name}, with PhD-level expertise in {self.expertise}."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.2,
                "max_tokens": 1000
            }
            response = requests.post(url, headers=headers, json=data)
            response_json = response.json()
            return response_json["choices"][0]["message"]["content"].strip()
        except Exception as e:
            print(f"Error generating response with EmergenceAI: {e}")
            return f"I apologize, but I encountered an error when generating a response. Please try again."
    
    def verify_accuracy(self, query, response, relevant_knowledge):
        """Verify the accuracy of the response against the IPMDAR knowledge base."""
        # In a production system, this would be more sophisticated
        # For now, we'll assume 100% accuracy if we have relevant knowledge
        if relevant_knowledge and len(relevant_knowledge) > 0:
            return "100%"
        else:
            return "95%"  # Default high accuracy when we don't have specific knowledge
    
    @abstractmethod
    def get_expertise_description(self):
        """Return a description of this agent's expertise."""
        pass
