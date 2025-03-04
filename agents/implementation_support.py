from agents.base_agent import BaseAgent

class ImplementationSupportAgent(BaseAgent):
    """
    Dr. Implementation Support - AI Agent for interactive end-user support,
    step-by-step implementation assistance, and procedural guidance.
    """
    
    def __init__(self, knowledge_base):
        super().__init__(
            knowledge_base=knowledge_base,
            name="Dr. Implementation Support",
            expertise="Step-by-step implementation assistance, real-time answers, and procedural guidance for IPMDAR processes"
        )
        self.knowledge_category = "implementation"
        self.llm_provider = "emergenceai"  # Using EmergenceAI for implementation support agent
    
    def get_expertise_description(self):
        return """Engages interactively with end-users, providing step-by-step implementation assistance, real-time answers, and procedural guidance for IPMDAR processes.
        
Specializes in:
- Guided walkthrough of IPMDAR implementation steps
- Step-by-step process explanations and tutorials
- Practical examples and case studies
- Best practices for first-time IPMDAR implementers
- Troubleshooting common implementation issues
- Training material development and guidance
- Transition planning from legacy systems to IPMDAR
"""
    
    def retrieve_relevant_knowledge(self, query):
        """Override to customize knowledge retrieval for implementation support topics."""
        # Get base knowledge
        knowledge = super().retrieve_relevant_knowledge(query)
        
        # Add any implementation-specific filtering or processing here
        implementation_keywords = [
            "implementation", "step", "procedure", "instruction", "guide", "manual",
            "how-to", "process", "workflow", "operation", "conduct", "perform",
            "execute", "action", "activity", "task", "help", "support"
        ]
        
        # Check if query is implementation-focused
        if any(keyword.lower() in query.lower() for keyword in implementation_keywords):
            # In a production system, we might add more specific implementation knowledge here
            pass
            
        return knowledge
        
    def generate_response(self, query, relevant_knowledge):
        """Override to provide a more interactive, step-by-step response style."""
        # Get standard response
        response = super().generate_response(query, relevant_knowledge)
        
        # Add some conversational elements to make it more interactive
        interactive_elements = [
            "\n\nIs there a specific part of the implementation process you'd like me to elaborate on?",
            "\n\nWould you like me to break down any of these steps in more detail?",
            "\n\nDo you need additional guidance on any particular aspect?",
            "\n\nFeel free to ask follow-up questions as you work through these steps.",
            "\n\nI'm here to help with any challenges you encounter during implementation."
        ]
        
        import random
        # Add an interactive element 30% of the time
        if random.random() < 0.3:
            response += random.choice(interactive_elements)
            
        return response
