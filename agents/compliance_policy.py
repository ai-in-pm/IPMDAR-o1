from agents.base_agent import BaseAgent

class ComplianceAgent(BaseAgent):
    """
    Dr. Compliance & Policy - AI Agent for IPMDAR regulations, DoD acquisition 
    policies, compliance standards, and data reporting requirements.
    """
    
    def __init__(self, knowledge_base):
        super().__init__(
            knowledge_base=knowledge_base,
            name="Dr. Compliance & Policy",
            expertise="IPMDAR regulations, DoD acquisition policies, compliance standards, and data reporting requirements"
        )
        self.knowledge_category = "compliance_policy"
    
    def get_expertise_description(self):
        return """Expert in IPMDAR regulations, DoD acquisition policies, compliance standards, and data reporting requirements.
        
Specializes in:
- Interpretation of IPMDAR guidelines and DoD Instruction 5000.02
- Contract Data Requirements Lists (CDRLs) compliance
- Federal Acquisition Regulation (FAR) and Defense Federal Acquisition Regulation Supplement (DFARS) requirements
- Data reporting requirements and submission formats
- Compliance matrices and checklists
- Audit preparation and compliance verification
"""
    
    def retrieve_relevant_knowledge(self, query):
        """Override to customize knowledge retrieval for compliance topics."""
        # Get base knowledge
        knowledge = super().retrieve_relevant_knowledge(query)
        
        # Add any compliance-specific filtering or processing here
        compliance_keywords = [
            "compliance", "regulation", "policy", "requirement", "guideline", 
            "standard", "DFARS", "FAR", "CFR", "approval", "authorize", 
            "statute", "mandate", "directive", "DCMA"
        ]
        
        # Check if query is compliance-focused
        if any(keyword.lower() in query.lower() for keyword in compliance_keywords):
            # In a production system, we might add more specific compliance knowledge here
            pass
            
        return knowledge
