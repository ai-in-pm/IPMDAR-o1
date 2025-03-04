from agents.base_agent import BaseAgent

class DataAnalyticsAgent(BaseAgent):
    """
    Dr. Data Analytics - AI Agent for analyzing IPMDAR performance data, 
    cost-schedule integration, and Earned Value Management (EVM) metrics.
    """
    
    def __init__(self, knowledge_base):
        super().__init__(
            knowledge_base=knowledge_base,
            name="Dr. Data Analytics",
            expertise="IPMDAR performance data analysis, cost-schedule integration, and Earned Value Management (EVM) metrics"
        )
        self.knowledge_category = "data_analytics"
        self.llm_provider = "anthropic"  # Using Anthropic for data analytics agent
    
    def get_expertise_description(self):
        return """Specialist in analyzing IPMDAR performance data, cost-schedule integration, and Earned Value Management (EVM) metrics.
        
Specializes in:
- Earned Value Management System (EVMS) principles and metrics
- Cost Performance Index (CPI) and Schedule Performance Index (SPI) analysis
- Variance analysis and trend identification
- Data visualization and reporting
- Contract Performance Reports (CPR) and Integrated Program Management Report (IPMR) analysis
- Performance measurement baselines and control accounts
- Estimate at Completion (EAC) and Estimate to Complete (ETC) calculations
"""
    
    def retrieve_relevant_knowledge(self, query):
        """Override to customize knowledge retrieval for data analytics topics."""
        # Get base knowledge
        knowledge = super().retrieve_relevant_knowledge(query)
        
        # Add any analytics-specific filtering or processing here
        analytics_keywords = [
            "analytics", "metrics", "measurement", "data", "report", "dashboard", 
            "analysis", "trend", "statistic", "calculation", "EVM", "earned value", 
            "performance", "indicator", "SPI", "CPI", "variance", "forecast"
        ]
        
        # Check if query is analytics-focused
        query_lower = query.lower()
        analytics_focused = any(keyword in query_lower for keyword in analytics_keywords)
        
        if analytics_focused:
            # Add more analytics-related knowledge if available
            for category in ["risk_forecasting", "implementation"]:
                if category in self.knowledge_base:
                    # Filter for analytics-related items in other categories
                    for item in self.knowledge_base[category]:
                        item_lower = item.lower()
                        if any(keyword in item_lower for keyword in analytics_keywords):
                            knowledge.append(item)
        
        return knowledge
        
    def generate_response(self, query, relevant_knowledge):
        """Override to customize response generation for data analytics."""
        # In a real implementation, this could include data visualization code
        # or analytics-specific formatting
        base_response = super().generate_response(query, relevant_knowledge)
        
        # Add standard note about data analytics best practices
        note = "\n\nNote: All data analytics recommendations follow the standard IPMDAR metrics and calculations as defined in the IPMDAR Implementation and Tailoring Guide."
        
        return base_response + note
