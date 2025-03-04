from agents.base_agent import BaseAgent

class RiskForecastingAgent(BaseAgent):
    """
    Dr. Risk & Forecasting - AI Agent for predictive analytics, 
    risk identification, and mitigation strategies using IPMDAR datasets.
    """
    
    def __init__(self, knowledge_base):
        super().__init__(
            knowledge_base=knowledge_base,
            name="Dr. Risk & Forecasting",
            expertise="Predictive analytics, risk identification, and mitigation strategies using IPMDAR datasets"
        )
        self.knowledge_category = "risk_forecasting"
        self.llm_provider = "google"  # Using Google's API for risk forecasting agent
    
    def get_expertise_description(self):
        return """Focuses on predictive analytics, risk identification, and mitigation strategies using IPMDAR datasets.
        
Specializes in:
- Predictive trend analysis using IPMDAR historical data
- Risk identification through performance metrics
- Cost and schedule risk assessment
- Mitigation strategy development and implementation
- Estimate at Completion (EAC) forecasting models
- Independent estimate analysis and validation
- Risk-adjusted schedule and cost projections
"""
    
    def retrieve_relevant_knowledge(self, query):
        """Override to customize knowledge retrieval for risk forecasting topics."""
        # Get base knowledge
        knowledge = super().retrieve_relevant_knowledge(query)
        
        # Add any risk-specific filtering or processing here
        risk_keywords = [
            "risk", "forecast", "prediction", "mitigation", "probability", "impact",
            "likelihood", "consequence", "uncertainty", "opportunity", "threat",
            "contingency", "reserve", "estimate", "projection", "future"
        ]
        
        # Check if query is risk-focused
        query_lower = query.lower()
        risk_focused = any(keyword in query_lower for keyword in risk_keywords)
        
        if risk_focused:
            # Add more risk-related knowledge if available
            for category in ["data_analytics", "project_management"]:
                if category in self.knowledge_base:
                    # Filter for risk-related items in other categories
                    for item in self.knowledge_base[category]:
                        item_lower = item.lower()
                        if any(keyword in item_lower for keyword in risk_keywords):
                            knowledge.append(item)
        
        return knowledge
        
    def generate_response(self, query, relevant_knowledge):
        """Override to customize response generation for risk forecasting."""
        # Get base response
        base_response = super().generate_response(query, relevant_knowledge)
        
        # For risk identification queries, add specific framework
        query_lower = query.lower()
        if "identif" in query_lower and "risk" in query_lower:
            risk_framework = "\n\nStandard IPMDAR Risk Identification Framework:\n1. Review performance metrics for negative trends\n2. Analyze CPI and SPI for early warning indicators\n3. Evaluate technical performance measures against requirements\n4. Assess critical path activities for schedule risks\n5. Identify cost drivers and potential overruns\n6. Categorize identified risks by impact and probability"
            return base_response + risk_framework
        
        return base_response
