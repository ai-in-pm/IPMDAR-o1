import logging
from .base_training import BaseTrainingModule

logger = logging.getLogger("Compliance Policy Training")

class CompliancePolicyTraining(BaseTrainingModule):
    """
    Training module for Compliance & Policy expertise.
    Focuses on IPMDAR regulations, DoD acquisition policies, compliance standards, 
    and data reporting requirements.
    """
    
    def __init__(self):
        """Initialize the Compliance & Policy training module."""
        super().__init__(name="IPMDAR Compliance & Policy Training")
    
    def _get_default_training_materials(self):
        """Get default training materials if JSON data is not available."""
        return {
            "module_name": "compliance_policy",
            "materials": [
                {
                    "id": "cp_101",
                    "title": "IPMDAR Regulatory Framework",
                    "description": "Core regulatory requirements that govern IPMDAR implementation",
                    "content_sections": [
                        {
                            "title": "Statutory Basis",
                            "content": "The statutory basis for IPMDAR includes relevant sections of U.S. Code Title 10 for Defense Acquisition, as well as the requirement for earned value management systems as defined in OMB Circular A-11."
                        },
                        {
                            "title": "DoD Instruction 5000.02",
                            "content": "DoD Instruction 5000.02 establishes the management framework for defense acquisition programs, including requirements for performance measurement and reporting."
                        },
                        {
                            "title": "DFARS Requirements",
                            "content": "The Defense Federal Acquisition Regulation Supplement (DFARS) contains specific clauses related to IPMDAR implementation, particularly in DFARS 252.234-7001 and 252.234-7002."
                        }
                    ]
                },
                {
                    "id": "cp_102",
                    "title": "Compliance Verification Methodology",
                    "description": "Techniques for verifying compliance with IPMDAR requirements",
                    "content_sections": [
                        {
                            "title": "Compliance Matrices",
                            "content": "Development and use of compliance matrices to verify alignment with all IPMDAR requirements."
                        },
                        {
                            "title": "Audit Preparation",
                            "content": "Procedures for preparing for compliance audits, including documentation requirements and validation processes."
                        },
                        {
                            "title": "Corrective Action Plans",
                            "content": "Development and implementation of corrective action plans to address compliance deficiencies."
                        }
                    ]
                },
                {
                    "id": "cp_103",
                    "title": "CDRL Development for IPMDAR",
                    "description": "Contract Data Requirements Lists specific to IPMDAR",
                    "content_sections": [
                        {
                            "title": "CDRL Structure",
                            "content": "Detailed structure and components of a properly formatted CDRL for IPMDAR reporting."
                        },
                        {
                            "title": "DID References",
                            "content": "Appropriate Data Item Description (DID) references for IPMDAR deliverables."
                        },
                        {
                            "title": "Tailoring Guidelines",
                            "content": "Guidelines for tailoring CDRLs based on contract type, size, and program requirements."
                        }
                    ]
                }
            ]
        }
    
    def _get_default_assessments(self):
        """Get default assessments if JSON data is not available."""
        return {
            "module_name": "compliance_policy",
            "assessments": [
                {
                    "id": "cp_assessment_1",
                    "title": "IPMDAR Regulatory Knowledge Assessment",
                    "description": "Assessment of knowledge in IPMDAR regulatory requirements",
                    "questions": [
                        {
                            "id": "q1",
                            "question": "What is the primary DoD instruction that establishes the framework for defense acquisition programs?",
                            "answer": "DoD Instruction 5000.02",
                            "difficulty": "basic"
                        },
                        {
                            "id": "q2",
                            "question": "Which DFARS clauses specifically relate to Earned Value Management System requirements?",
                            "answer": "DFARS 252.234-7001 and 252.234-7002",
                            "difficulty": "intermediate"
                        },
                        {
                            "id": "q3",
                            "question": "What are the key components that must be included in a Contract Data Requirements List (CDRL) for IPMDAR?",
                            "answer": "Data Item Description (DID) reference, delivery schedule, format requirements, distribution requirements, and applicable tailoring instructions.",
                            "difficulty": "advanced"
                        }
                    ]
                },
                {
                    "id": "cp_assessment_2",
                    "title": "Compliance Verification Assessment",
                    "description": "Assessment of compliance verification methodologies",
                    "questions": [
                        {
                            "id": "q1",
                            "question": "What is the purpose of an IPMDAR compliance matrix?",
                            "answer": "To systematically verify and document alignment with all IPMDAR requirements specified in the contract.",
                            "difficulty": "intermediate"
                        },
                        {
                            "id": "q2",
                            "question": "What documentation should be prepared for an EVMS compliance audit?",
                            "answer": "System Description, WBS Dictionary, Control Account Plans, EVM procedures, previous surveillance reports, metrics history, and corrective action plans.",
                            "difficulty": "advanced"
                        }
                    ]
                }
            ]
        }
    
    def train_regulatory_frameworks(self, agent_id):
        """
        Specialized training on regulatory frameworks for IPMDAR.
        
        Args:
            agent_id: Unique identifier for the agent
            
        Returns:
            dict: Training results
        """
        logger.info(f"Training agent {agent_id} on IPMDAR regulatory frameworks")
        
        # In a full implementation, this would include detailed regulatory training
        
        return {
            'agent_id': agent_id,
            'module': self.name,
            'component': 'regulatory_frameworks',
            'material_ids': ['cp_101', 'cp_103'],
            'status': 'completed'
        }
    
    def train_compliance_verification(self, agent_id):
        """
        Specialized training on compliance verification techniques.
        
        Args:
            agent_id: Unique identifier for the agent
            
        Returns:
            dict: Training results
        """
        logger.info(f"Training agent {agent_id} on compliance verification techniques")
        
        return {
            'agent_id': agent_id,
            'module': self.name,
            'component': 'compliance_verification',
            'material_ids': ['cp_102'],
            'status': 'completed'
        }
    
    def train_cdrl_development(self, agent_id):
        """
        Specialized training on CDRL development for IPMDAR.
        
        Args:
            agent_id: Unique identifier for the agent
            
        Returns:
            dict: Training results
        """
        logger.info(f"Training agent {agent_id} on CDRL development for IPMDAR")
        
        return {
            'agent_id': agent_id,
            'module': self.name,
            'component': 'cdrl_development',
            'material_ids': ['cp_103'],
            'status': 'completed'
        }
