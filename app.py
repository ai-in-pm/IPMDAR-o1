from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import json
import time
import random
import threading
from dotenv import load_dotenv
import openai
import requests
from agents.compliance_policy import ComplianceAgent
from agents.data_analytics import DataAnalyticsAgent
from agents.project_management import ProjectManagementAgent
from agents.risk_forecasting import RiskForecastingAgent
from agents.systems_integration import SystemsIntegrationAgent
from agents.implementation_support import ImplementationSupportAgent
from utils.pdf_processor import extract_pdf_text, create_knowledge_base
from ipmdar_camp import IPMDARTrainingCamp

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure API keys for multiple providers
api_keys = {
    "openai": os.getenv("OPENAI_API_KEY"),
    "anthropic": os.getenv("ANTHROPIC_API_KEY"),
    "groq": os.getenv("GROQ_API_KEY"),
    "google": os.getenv("GOOGLE_API_KEY"),
    "cohere": os.getenv("COHERE_API_KEY"),
    "emergenceai": os.getenv("EMERGENCEAI_API_KEY")
}

# Log which providers are available
available_providers = [provider for provider, key in api_keys.items() if key]
print(f"Available API providers: {', '.join(available_providers) if available_providers else 'None'}")

# Set fallback provider
fallback_provider = "openai" if api_keys["openai"] else None
if not fallback_provider and available_providers:
    fallback_provider = available_providers[0]
    print(f"OpenAI API key not found. Using {fallback_provider} as fallback provider.")
elif not fallback_provider:
    print("WARNING: No API providers available. Agent responses will fail.")

# Initialize knowledge base
pdf_path = "IPMDAR Implementation and Tailoring Guide_Stamped.pdf"
ipmdar_text = extract_pdf_text(pdf_path)
knowledge_base = create_knowledge_base(ipmdar_text)

# Initialize IPMDAR Training Camp
training_camp = IPMDARTrainingCamp(knowledge_base)

# Function to check and assign provider based on availability
def get_provider_or_fallback(preferred_provider):
    if preferred_provider in available_providers:
        return preferred_provider
    elif fallback_provider:
        print(f"Provider {preferred_provider} not available. Using fallback provider {fallback_provider}.")
        return fallback_provider
    else:
        print(f"Provider {preferred_provider} not available and no fallback provider set.")
        return "openai"  # Default to OpenAI even if the key isn't available

# Initialize AI agents with appropriate providers
compliance_agent = ComplianceAgent(knowledge_base)
compliance_agent.llm_provider = get_provider_or_fallback("openai")

data_analytics_agent = DataAnalyticsAgent(knowledge_base)
data_analytics_agent.llm_provider = get_provider_or_fallback("anthropic")

project_management_agent = ProjectManagementAgent(knowledge_base)
project_management_agent.llm_provider = get_provider_or_fallback("groq")

risk_forecasting_agent = RiskForecastingAgent(knowledge_base)
risk_forecasting_agent.llm_provider = get_provider_or_fallback("google")

systems_integration_agent = SystemsIntegrationAgent(knowledge_base)
systems_integration_agent.llm_provider = get_provider_or_fallback("cohere")

implementation_support_agent = ImplementationSupportAgent(knowledge_base)
implementation_support_agent.llm_provider = get_provider_or_fallback("emergenceai")

# Print agent-provider assignments for debugging
print(f"Agent-Provider Assignments:")
print(f"- Dr. Compliance: {compliance_agent.llm_provider}")
print(f"- Dr. Data Analytics: {data_analytics_agent.llm_provider}")
print(f"- Dr. Project Management: {project_management_agent.llm_provider}")
print(f"- Dr. Risk & Forecasting: {risk_forecasting_agent.llm_provider}")
print(f"- Dr. Systems Integration: {systems_integration_agent.llm_provider}")
print(f"- Dr. Implementation Support: {implementation_support_agent.llm_provider}")

# Train agents if not already certified
agent_types = {
    "compliance": "compliance_policy",
    "data_analytics": "data_analytics",
    "project_management": "project_management",
    "risk_forecasting": "risk_forecasting",
    "systems_integration": "systems_integration",
    "implementation_support": "implementation_support"
}

for agent_id, agent_type in agent_types.items():
    if not training_camp.verify_agent_certification(agent_id):
        training_camp.train_agent(agent_id, agent_type)

# Map agent names to agent instances
agents = {
    "compliance": compliance_agent,
    "data_analytics": data_analytics_agent,
    "project_management": project_management_agent,
    "risk_forecasting": risk_forecasting_agent,
    "systems_integration": systems_integration_agent,
    "implementation_support": implementation_support_agent,
    "all": None  # Special case for consulting all agents
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/query', methods=['POST'])
def query():
    data = request.json
    user_query = data.get('query', '')
    agent_name = data.get('agent', 'all')
    
    if not user_query:
        return jsonify({"error": "No query provided"}), 400
    
    if agent_name not in agents:
        return jsonify({"error": f"Agent '{agent_name}' not found"}), 404
    
    # Process query with the appropriate agent(s)
    if agent_name == "all":
        # Collect responses from all agents
        responses = []
        for name, agent in agents.items():
            if name != "all":
                # Verify agent certification before processing query
                if training_camp.verify_agent_certification(name):
                    try:
                        response = agent.process_query(user_query)
                        responses.append({
                            "agent": name,
                            "response": response["response"],
                            "accuracy": response["accuracy"],
                            "certified": True,
                            "provider": agent.llm_provider
                        })
                    except Exception as e:
                        print(f"Error with {name} agent: {str(e)}")
                        responses.append({
                            "agent": name,
                            "response": f"I apologize, but I encountered an error when generating a response. Please try again.",
                            "accuracy": "0%",
                            "certified": True,
                            "provider": agent.llm_provider,
                            "error": str(e)
                        })
                else:
                    responses.append({
                        "agent": name,
                        "response": "This agent has not completed certification and cannot provide expert answers.",
                        "accuracy": "0%",
                        "certified": False
                    })
        return jsonify({"responses": responses})
    else:
        # Process with single agent
        agent = agents[agent_name]
        if training_camp.verify_agent_certification(agent_name):
            try:
                response = agent.process_query(user_query)
                response["certified"] = True
                response["provider"] = agent.llm_provider
                return jsonify(response)
            except Exception as e:
                print(f"Error with {agent_name} agent: {str(e)}")
                return jsonify({
                    "agent": agent_name,
                    "response": f"I apologize, but I encountered an error when generating a response. Please try again.",
                    "accuracy": "0%",
                    "certified": True,
                    "provider": agent.llm_provider,
                    "error": str(e)
                })
        else:
            return jsonify({
                "response": "This agent has not completed certification and cannot provide expert answers.",
                "accuracy": "0%",
                "certified": False
            })

@app.route('/api/compete', methods=['POST'])
def compete():
    """
    Handles the competitive response process where agents race to respond first
    and then analyze each other's responses for accuracy.
    """
    data = request.json
    user_query = data.get('query', '')
    
    if not user_query:
        return jsonify({"error": "No query provided"}), 400
    
    # Function to simulate agent competition with randomized response times
    def agent_competition():
        agent_results = {}
        finish_times = {}
        for name, agent in agents.items():
            if name != "all":
                # Only include certified agents
                if training_camp.verify_agent_certification(name):
                    # Random response time between 1-5 seconds to simulate different processing speeds
                    response_time = random.uniform(1, 5)
                    # Actual response generation
                    try:
                        response = agent.process_query(user_query)
                        
                        # Store both the response and the simulated finish time
                        agent_results[name] = response
                        finish_times[name] = response_time
                    except Exception as e:
                        print(f"Error with {name} agent in competition: {str(e)}")
                        # Skip this agent in the competition
                        continue
        
        # Determine winner (fastest response)
        if finish_times:
            winner = min(finish_times, key=finish_times.get)
            winning_time = finish_times[winner]
            winning_response = agent_results[winner]
            
            # Have other agents analyze the winning response
            analyses = {}
            corrections = {}
            
            for name, agent in agents.items():
                if name != "all" and name != winner:
                    # Each agent analyzes the winning response
                    try:
                        analysis_prompt = f"The following is a response to the query: '{user_query}'. Please analyze it for accuracy and provide feedback: {winning_response['response']}"
                        analysis = agent.process_query(analysis_prompt)
                        analyses[name] = analysis["response"]
                        
                        # Determine if correction is needed based on keywords in the analysis
                        correction_indicators = ["incorrect", "inaccurate", "error", "mistake", "wrong", "false"]
                        if any(indicator in analysis["response"].lower() for indicator in correction_indicators):
                            # Agent proposes a correction
                            correction_prompt = f"The following response to '{user_query}' contains inaccuracies. Please provide a corrected response: {winning_response['response']}"
                            correction = agent.process_query(correction_prompt)
                            # Random correction time between 1-3 seconds
                            correction_time = random.uniform(1, 3)
                            corrections[name] = {
                                "response": correction["response"],
                                "time": correction_time
                            }
                    except Exception as e:
                        print(f"Error with {name} agent during analysis: {str(e)}")
                        analyses[name] = f"I apologize, but I encountered an error when analyzing the response. Please try again."
            
            # Determine if there's a correction winner
            correction_winner = None
            correction_response = None
            if corrections:
                correction_winner = min(corrections, key=lambda x: corrections[x]["time"])
                correction_response = corrections[correction_winner]["response"]
            
            return {
                "winner": winner,
                "winning_time": winning_time,
                "winning_response": winning_response["response"],
                "winning_provider": agents[winner].llm_provider,
                "analyses": analyses,
                "correction_needed": bool(corrections),
                "correction_winner": correction_winner,
                "correction_response": correction_response
            }
        else:
            return {"error": "No certified agents available to compete"}
    
    # Run the competition
    return jsonify(agent_competition())

@app.route('/api/agents', methods=['GET'])
def get_agents():
    """
    Returns information about all available agents
    """
    agent_info = []
    for name, agent in agents.items():
        if name != "all":
            agent_info.append({
                "id": name,
                "name": agent.name,
                "expertise": agent.expertise,
                "provider": agent.llm_provider,
                "certified": training_camp.verify_agent_certification(name),
                "description": agent.get_expertise_description()
            })
    return jsonify({"agents": agent_info})

@app.route('/api/training/status', methods=['GET'])
def get_training_status():
    """
    Returns the training status of all agents
    """
    status = {}
    for agent_id in agent_types.keys():
        status[agent_id] = {
            "certified": training_camp.verify_agent_certification(agent_id),
            "score": training_camp.get_agent_certification_score(agent_id)
        }
    return jsonify(status)

@app.route('/api/training/train/<agent_id>', methods=['POST'])
def train_agent(agent_id):
    """
    Trains a specific agent
    """
    if agent_id not in agent_types:
        return jsonify({"error": f"Agent '{agent_id}' not found"}), 404
    
    # Run training in a background thread to not block the request
    def background_training():
        print(f"Starting training for {agent_id} agent...")
        training_camp.train_agent(agent_id, agent_types[agent_id])
        print(f"Training completed for {agent_id} agent.")
    
    thread = threading.Thread(target=background_training)
    thread.start()
    
    return jsonify({
        "message": f"Training started for {agent_id} agent. Check the /api/training/status endpoint for progress."
    })

if __name__ == '__main__':
    try:
        # Use port 8888 as the default
        print("Starting Flask app on http://127.0.0.1:8888")
        app.run(debug=True, port=8888)
    except Exception as e:
        print(f"Error starting Flask app: {e}")
        # Add OSError with Errno 98 (Address already in use)
        if isinstance(e, OSError) and e.errno == 98:
            print("Port 8888 is already in use. Try a different port or stop the existing process.")
            alternate_port = 8889
            print(f"Attempting to start on alternate port {alternate_port}...")
            try:
                app.run(debug=True, port=alternate_port)
            except Exception as alt_e:
                print(f"Error starting on alternate port: {alt_e}")
        elif isinstance(e, OSError) and e.errno == 10013:  # Windows permission error
            print("Permission denied for port 8888. Try a higher port number or run as administrator.")
            alternate_port = 8889
            print(f"Attempting to start on alternate port {alternate_port}...")
            try:
                app.run(debug=True, port=alternate_port)
            except Exception as alt_e:
                print(f"Error starting on alternate port: {alt_e}")
