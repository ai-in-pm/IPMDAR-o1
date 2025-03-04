# IPMDAR AI Expert System

An AI-driven chatbot system comprising six distinct PhD-level AI agents, each specialized in different aspects of the Integrated Program Management Data and Reporting (IPMDAR) implementation. This system provides users with tailored, accurate, and evidence-based assistance in navigating, implementing, and optimizing IPMDAR within DoD acquisition projects.

## System Overview

The IPMDAR AI Expert System leverages multiple language models and a comprehensive knowledge base derived from the IPMDAR Implementation and Tailoring Guide to provide expert guidance across various domains of IPMDAR implementation. The system features a modern, intuitive web interface that allows users to interact with individual AI agents or the entire expert panel simultaneously.

## AI Expert Panel

The system includes six specialized AI agents, each with a unique area of expertise:

1. **Dr. Compliance & Policy** - Expert in IPMDAR regulations, DoD acquisition policies, compliance standards, and data reporting requirements.

2. **Dr. Data Analytics** - Specialist in analyzing IPMDAR performance data, cost-schedule integration, and Earned Value Management (EVM) metrics.

3. **Dr. Project Management** - Provides detailed guidance on tailoring IPMDAR deliverables according to specific project needs, preparation of Contract Data Requirements Lists (CDRLs), and implementation best practices.

4. **Dr. Risk & Forecasting** - Focuses on predictive analytics, risk identification, and mitigation strategies using IPMDAR datasets.

5. **Dr. Systems Integration** - Ensures seamless technical integration of IPMDAR tools, data formatting, JSON structuring, and automation processes.

6. **Dr. Implementation Support** - Engages interactively with end-users, providing step-by-step implementation assistance, real-time answers, and procedural guidance for IPMDAR processes.

## Key Features

- **Evidence-Based Responses**: All outputs from AI agents are based on the IPMDAR Implementation and Tailoring Guide, ensuring 100% accuracy.
- **Accuracy Rating**: Each response includes an accuracy percentage rating, verifying alignment with IPMDAR standards and DoD guidelines.
- **Interactive Consultation**: Users can interact with individual agents or the entire expert panel for comprehensive guidance.
- **Real-time Assistance**: The system provides immediate, actionable support for effective IPMDAR implementation.
- **Modern Web Interface**: An intuitive, responsive design that facilitates seamless interaction with the AI expert panel.
- **Unified API Architecture**: All AI agents utilize a multi-provider architecture, providing consistent response quality and simplified system maintenance.

## Technical Architecture

### Backend Components

- **Flask Web Server**: Handles HTTP requests and serves the web application
- **AI Agent System**: Six specialized agents implemented as Python classes
- **PDF Processor**: Extracts and organizes knowledge from the IPMDAR guide
- **Knowledge Base**: Structured database of IPMDAR information categorized by domain
- **LLM Integration**: Connects to multiple language model providers (OpenAI, Anthropic, Groq, Google, Cohere, EmergenceAI) for language model capabilities
- **Competition Engine**: Facilitates agent competition with timing, analysis, and correction mechanisms

### Frontend Components

- **HTML/CSS/JavaScript**: Responsive web interface with Bootstrap and custom styling
- **Real-time Chat Interface**: Markdown rendering and dynamic message display
- **Agent Selection Panel**: Interactive sidebar for switching between expert agents
- **Competition Dashboard**: Charts and visualizations for agent performance metrics
- **Dynamic Analysis Display**: Collapsible sections for displaying agent analyses and corrections

## Multi-Provider Architecture

The IPMDAR AI Expert System supports a multi-provider architecture, allowing users to configure multiple language model providers. Each AI agent is configured to use a specific provider:

- **Dr. Compliance & Policy**: OpenAI
- **Dr. Data Analytics**: Anthropic
- **Dr. Project Management**: Groq
- **Dr. Risk & Forecasting**: Google Gemini
- **Dr. Systems Integration**: Cohere
- **Dr. Implementation Support**: EmergenceAI

If a specific API key is not available, the system will automatically use the first available provider as a fallback.

## Environment Variables

To configure the multi-provider architecture, set the following environment variables:

```
OPENAI_API_KEY="your-openai-api-key"
ANTHROPIC_API_KEY="your-anthropic-api-key"
GROQ_API_KEY="your-groq-api-key"
GOOGLE_API_KEY="your-google-api-key"
COHERE_API_KEY="your-cohere-api-key"
EMERGENCEAI_API_KEY="your-emergenceai-api-key"
```

## Installation and Setup

1. Clone the repository:
   ```
   git clone https://github.com/your-username/ipmdar-ai-expert-system.git
   cd ipmdar-ai-expert-system
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a .env file in the root directory with your API keys:
   ```
   OPENAI_API_KEY="your-openai-api-key"
   ANTHROPIC_API_KEY="your-anthropic-api-key"
   GROQ_API_KEY="your-groq-api-key"
   GOOGLE_API_KEY="your-google-api-key"
   COHERE_API_KEY="your-cohere-api-key"
   EMERGENCEAI_API_KEY="your-emergenceai-api-key"
   ```

4. Run the application:
   ```
   python app.py
   ```

5. Open your browser and navigate to:
   ```
   http://localhost:8888
   ```

### Troubleshooting

If you encounter a socket permission error when starting the Flask application:

```
An attempt was made to access a socket in a way forbidden by its access permissions
```

This is typically caused by security restrictions or another application using the same port. Try these solutions:

1. **Run as Administrator**: Right-click on your terminal/command prompt and select "Run as Administrator" 
2. **Specify a different port**: Edit app.py and change the port number to an available port
   ```python
   app.run(debug=True, port=7000)  # Try a different port like 7000, 3000, etc.
   ```
3. **Check firewall settings**: Ensure your firewall allows Flask to bind to the specified port
4. **Verify no other applications are using the port**: Use a command like `netstat -ano | findstr :8888`

## IPMDAR Training Camp

The IPMDAR AI Expert System includes a comprehensive Training Camp for AI agents, ensuring that each specialized agent undergoes rigorous training and certification before providing responses to user queries.

### Features

- **Comprehensive Training Modules**: Each agent undergoes specialized training in its domain expertise
- **Certification Process**: Formal assessment and certification to validate domain mastery
- **Cross-Domain Training**: Agents learn to collaborate and understand related domains
- **Continuous Learning**: Scheduled refresher training to keep agents up-to-date
- **Visual Certification Status**: UI indicators show which agents are certified and ready to use
- **Agent Training Management**: Interactive interface for initiating training and viewing certification details

### Training Modules

The training camp includes specialized modules for each agent type:

1. **Base Training Module** - Core IPMDAR knowledge required by all agents
2. **Compliance & Policy Training** - Regulatory requirements and DoD policy knowledge
3. **Data Analytics Training** - Performance data analysis and metrics interpretation
4. **Project Management Training** - Program management and IPMDAR implementation strategies
5. **Risk & Forecasting Training** - Risk analysis and EAC forecasting methodologies
6. **Systems Integration Training** - Technical integration patterns and data architectures
7. **Implementation Support Training** - Process integration and organizational change management

### Training Material Format

Training materials are stored in structured JSON format with the following components:

```json
{
  "module_name": "Module Title",
  "version": "1.0",
  "topics": [
    {
      "title": "Topic Title",
      "content": "Detailed educational content",
      "learning_objectives": [
        "Objective 1",
        "Objective 2"
      ]
    }
  ],
  "assessment_questions": [
    {
      "question": "Assessment question text",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "correct_answer": "Option B",
      "explanation": "Detailed explanation of the correct answer"
    }
  ]
}
```

Custom training materials can be added to the `ipmdar_camp/training_materials/` directory.

### API Endpoints

The Training Camp includes the following API endpoints:

- **GET /api/training/status** - Get certification status for all agents
- **GET /api/training/status?agent_id={id}** - Get detailed certification information for a specific agent
- **POST /api/training/train** - Initiate training for a specific agent
  - Request body: `{"agent_id": "agent_name", "force_retrain": false}`

### User Interface Features

The IPMDAR AI Expert System UI includes visual indicators for agent certification status:

- **Certification Badges**: Each agent in the sidebar displays a colored badge indicating certification status:
  - Green checkmark: Certified agent
  - Yellow hourglass: Training in progress
  - Red X: Not certified

- **Certification Details**: When selecting an individual agent, detailed certification information is displayed:
  - Certification score
  - Certification date
  - Training button for uncertified agents

## Usage Examples

The IPMDAR AI Expert System can assist with a wide range of IPMDAR-related queries, including:

- "What are the requirements for tailoring IPMDAR for a fixed-price contract?"
- "How do I calculate the Cost Performance Index using IPMDAR data?"
- "What is the proper JSON schema for IPMDAR data submission?"
- "Can you help me identify potential schedule risks in my program?"
- "What steps should I follow to implement IPMDAR in my organization?"
- "How do I ensure compliance with the latest DoD acquisition policies?"

## System Requirements

- Python 3.8 or higher
- Modern web browser (Chrome, Firefox, Edge, Safari)
- Internet connection for accessing the OpenAI API
- IPMDAR Implementation and Tailoring Guide (included in the repository)

## Development and Customization

The system is designed to be extensible and customizable. To add new capabilities:

1. **Extend Agent Classes**: Add new methods to existing agent classes or create new specialized agents
2. **Enhance Knowledge Base**: Implement more sophisticated knowledge retrieval mechanisms
3. **Improve UI**: Customize the frontend interface for specific organizational needs
4. **Add Data Visualization**: Implement charts and graphs for data analytics capabilities

## License

This project is proprietary and confidential. All rights reserved.

## Contact

For support or inquiries, please contact the development team at [contact information].

---

 2025 IPMDAR AI Expert System. All rights reserved.
