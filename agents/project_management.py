from agents.base_agent import BaseAgent

class ProjectManagementAgent(BaseAgent):
    """
    Dr. Project Management - AI Agent for tailoring IPMDAR deliverables, 
    preparing CDRLs, and implementing best practices.
    """
    
    def __init__(self, knowledge_base):
        super().__init__(
            knowledge_base=knowledge_base,
            name="Dr. Project Management",
            expertise="Tailoring IPMDAR deliverables, preparing Contract Data Requirements Lists (CDRLs), and implementation best practices"
        )
        self.knowledge_category = "project_management"
        self.llm_provider = "groq"  # Using Groq for project management agent
    
    def get_expertise_description(self):
        return """Provides detailed guidance on tailoring IPMDAR deliverables according to specific project needs, preparation of Contract Data Requirements Lists (CDRLs), and implementation best practices.
        
Specializes in:
- IPMDAR deliverable tailoring based on contract type and size
- Contract Data Requirements Lists (CDRLs) preparation and review
- Work Breakdown Structure (WBS) development and implementation
- Integrated Master Schedule (IMS) development and management
- Program Management Office (PMO) organization and best practices
- Project lifecycle management in DoD acquisition
- Implementation roadmaps and transition planning
"""
    
    def retrieve_relevant_knowledge(self, query):
        """Override to customize knowledge retrieval for project management topics."""
        # Get base knowledge
        knowledge = super().retrieve_relevant_knowledge(query)
        
        # Add any project management-specific filtering or processing here
        pm_keywords = [
            "management", "project", "planning", "execution", "CDRL", "deliverable", 
            "milestone", "schedule", "timeline", "work breakdown", "WBS", "tailoring",
            "implementation", "contract", "SOW", "statement of work"
        ]
        
        # Check if query is project management-focused
        if any(keyword.lower() in query.lower() for keyword in pm_keywords):
            # In a production system, we might add more specific project management knowledge here
            pass
            
        return knowledge
        
    def generate_response(self, query, relevant_knowledge):
        """Override to customize response generation for project management."""
        # Get base response
        base_response = super().generate_response(query, relevant_knowledge)
        
        # For tailoring-related queries, add specific guidance
        query_lower = query.lower()
        if "tailor" in query_lower or "cdrl" in query_lower or "deliverable" in query_lower:
            tailoring_guidance = "\n\nRecommended Tailoring Approach:\n1. Identify contract value and type\n2. Determine applicable IPMDAR sections based on contract size\n3. Review special considerations for your contract type\n4. Document tailoring decisions in the CDRL\n5. Seek approval from the acquisition authority"
            return base_response + tailoring_guidance
        
        return base_response
