from agents.base_agent import BaseAgent

class SystemsIntegrationAgent(BaseAgent):
    """
    Dr. Systems Integration - AI Agent for seamless technical integration of IPMDAR tools, 
    data formatting, JSON structuring, and automation processes.
    """
    
    def __init__(self, knowledge_base):
        super().__init__(
            knowledge_base=knowledge_base,
            name="Dr. Systems Integration",
            expertise="Technical integration of IPMDAR tools, data formatting, JSON structuring, and automation processes"
        )
        self.knowledge_category = "systems_integration"
        self.llm_provider = "cohere"  # Using Cohere API for systems integration agent
    
    def get_expertise_description(self):
        return """Ensures seamless technical integration of IPMDAR tools, data formatting, JSON structuring, and automation processes.
        
Specializes in:
- IPMDAR data schemas and JSON formatting requirements
- System interoperability and integration architecture
- Data exchange protocols and standards
- Automation of data collection and reporting processes
- Technical validation and verification of IPMDAR submissions
- Tool selection and integration for IPMDAR compliance
- Legacy system integration with modern IPMDAR requirements
"""
    
    def retrieve_relevant_knowledge(self, query):
        """Override to customize knowledge retrieval for systems integration topics."""
        # Get base knowledge
        knowledge = super().retrieve_relevant_knowledge(query)
        
        # Add any integration-specific filtering or processing here
        integration_keywords = [
            "integration", "system", "technical", "interface", "interoperability",
            "architecture", "compatibility", "data format", "JSON", "schema", "XML",
            "standard", "protocol", "automation", "tool", "software"
        ]
        
        # Check if query is integration-focused
        if any(keyword.lower() in query.lower() for keyword in integration_keywords):
            # In a production system, we might add more specific integration knowledge here
            pass
            
        return knowledge
        
    def generate_response(self, query, relevant_knowledge):
        """Override to customize response generation for systems integration."""
        # Get base response
        base_response = super().generate_response(query, relevant_knowledge)
        
        # For JSON data format queries, add specific examples
        query_lower = query.lower()
        if "json" in query_lower or "data format" in query_lower or "schema" in query_lower:
            json_example = '\n\nExample IPMDAR JSON Format:\n```json\n{\n  "header": {\n    "submissionDate": "2025-03-03",\n    "contractNumber": "FA8621-15-C-6397",\n    "contractorName": "Example Contractor Inc.",\n    "reportingPeriod": {\n      "start": "2025-02-01",\n      "end": "2025-02-28"\n    }\n  },\n  "performanceData": {\n    "contractBudgetBase": 1000000,\n    "budgetAtCompletion": 950000,\n    "actualCostOfWorkPerformed": 450000,\n    "budgetedCostOfWorkPerformed": 500000,\n    "budgetedCostOfWorkScheduled": 550000\n  },\n  "metrics": {\n    "costPerformanceIndex": 1.11,\n    "schedulePerformanceIndex": 0.91,\n    "estimateAtCompletion": 855855\n  }\n}\n```'
            return base_response + json_example
        
        return base_response
