import logging
from .base_training import BaseTrainingModule

logger = logging.getLogger("Project Management Training")

class ProjectManagementTraining(BaseTrainingModule):
    """
    Training module for Project Management expertise.
    Focuses on tailoring IPMDAR deliverables, preparing CDRLs, 
    and implementing best practices.
    """
    
    def __init__(self):
        """Initialize the Project Management training module."""
        super().__init__(name="IPMDAR Project Management Training")
    
    def _get_default_training_materials(self):
        """Get default training materials if JSON data is not available."""
        return {
            "module_name": "project_management",
            "materials": [
                {
                    "id": "pm_101",
                    "title": "IPMDAR Tailoring Strategies",
                    "description": "Methodologies for tailoring IPMDAR requirements to program needs",
                    "content_sections": [
                        {
                            "title": "Contract Value-Based Tailoring",
                            "content": "Guidelines for tailoring IPMDAR requirements based on contract value thresholds, including simplified requirements for smaller contracts and comprehensive requirements for larger ones."
                        },
                        {
                            "title": "Contract Type Considerations",
                            "content": "Specific tailoring approaches for different contract types, including fixed-price, cost-plus, and time & materials contracts, with consideration for risk allocation and management visibility needs."
                        },
                        {
                            "title": "Tailoring Documentation",
                            "content": "Methods for documenting tailoring decisions in the CDRL and contractor's IPMDAR implementation plan, ensuring transparency and approval of tailored approaches."
                        }
                    ]
                },
                {
                    "id": "pm_102",
                    "title": "Work Breakdown Structure Development",
                    "description": "Best practices for WBS development and management in IPMDAR context",
                    "content_sections": [
                        {
                            "title": "WBS Development Standards",
                            "content": "Implementation of MIL-STD-881E standards for WBS development, including product-oriented decomposition and appropriate level of detail based on program complexity."
                        },
                        {
                            "title": "WBS Dictionary",
                            "content": "Creation of comprehensive WBS Dictionary entries that clearly define the scope, deliverables, and boundaries of each WBS element."
                        },
                        {
                            "title": "WBS Integration",
                            "content": "Methodologies for integrating the WBS with the Organizational Breakdown Structure (OBS) and establishing effective control accounts at the appropriate intersections."
                        }
                    ]
                },
                {
                    "id": "pm_103",
                    "title": "Integrated Master Schedule Management",
                    "description": "Techniques for developing and managing the Integrated Master Schedule",
                    "content_sections": [
                        {
                            "title": "IMS Development",
                            "content": "Best practices for developing an Integrated Master Schedule that accurately reflects the program work scope, realistic durations, and logical relationships between activities."
                        },
                        {
                            "title": "Critical Path Analysis",
                            "content": "Methodologies for identifying, monitoring, and managing the critical path, near-critical paths, and schedule margin to ensure program execution meets timeline objectives."
                        },
                        {
                            "title": "Schedule Risk Assessment",
                            "content": "Techniques for conducting schedule risk assessments, including identification of schedule drivers, uncertainty analysis, and development of risk mitigation strategies."
                        }
                    ]
                },
                {
                    "id": "pm_104",
                    "title": "IPMDAR Implementation Planning",
                    "description": "Comprehensive planning for IPMDAR implementation in a program",
                    "content_sections": [
                        {
                            "title": "Implementation Roadmap",
                            "content": "Development of a phased implementation roadmap that outlines the steps, timeline, and resources required for effective IPMDAR implementation."
                        },
                        {
                            "title": "Organizational Readiness",
                            "content": "Assessment and preparation of organizational capabilities, including skills assessment, training needs, and process development requirements."
                        },
                        {
                            "title": "Tool Selection and Configuration",
                            "content": "Criteria and methodology for selecting and configuring appropriate tools to support IPMDAR implementation, including EVM systems, scheduling tools, and reporting platforms."
                        }
                    ]
                }
            ]
        }
    
    def _get_default_assessments(self):
        """Get default assessments if JSON data is not available."""
        return {
            "module_name": "project_management",
            "assessments": [
                {
                    "id": "pm_assessment_1",
                    "title": "IPMDAR Tailoring Assessment",
                    "description": "Assessment of ability to appropriately tailor IPMDAR requirements",
                    "questions": [
                        {
                            "id": "q1",
                            "question": "What are the IPMDAR tailoring considerations for a $20M fixed-price development contract?",
                            "answer": "For a $20M fixed-price development contract, appropriate tailoring might include: reduced reporting frequency (quarterly vs. monthly), simplified formats focusing on schedule performance rather than detailed cost reporting, elimination of variance analysis requirements for variances less than 10%, and streamlined WBS reporting to level 3 rather than level 5.",
                            "difficulty": "intermediate"
                        },
                        {
                            "id": "q2",
                            "question": "How should IPMDAR requirements be tailored for a $150M cost-plus development contract with high technical risk?",
                            "answer": "For a $150M cost-plus development contract with high technical risk, tailoring should be minimal, with requirements for: monthly comprehensive reporting, detailed variance analysis at the control account level, WBS reporting to level 5, full implementation of all 32 EVMS criteria, incorporation of technical performance measures in the IPMDAR, and potentially adding more frequent reporting for high-risk areas or critical path activities.",
                            "difficulty": "advanced"
                        }
                    ]
                },
                {
                    "id": "pm_assessment_2",
                    "title": "WBS and IMS Assessment",
                    "description": "Assessment of WBS and IMS knowledge and application",
                    "questions": [
                        {
                            "id": "q1",
                            "question": "What are the key components that must be included in a WBS Dictionary entry?",
                            "answer": "A comprehensive WBS Dictionary entry should include: WBS element identifier, WBS element title, WBS element description, definition of work scope included, explicit statement of excluded work, deliverables associated with the element, acceptance criteria, specific dependencies, responsible organization/individual, and budget allocation.",
                            "difficulty": "intermediate"
                        },
                        {
                            "id": "q2",
                            "question": "Describe the process for conducting an Integrated Master Schedule health assessment.",
                            "answer": "An IMS health assessment process includes: validating the schedule against the 14-point assessment criteria (logical relationships, reasonable durations, no constraints, etc.), checking for missing dependencies, validating critical path integrity, ensuring activities align with the WBS, verifying resource loading is realistic, checking for appropriate use of lag/lead times, reviewing baseline vs. forecast dates, ensuring status is current, and validating schedule margin allocation and management.",
                            "difficulty": "advanced"
                        }
                    ]
                }
            ]
        }
    
    def train_tailoring_strategies(self, agent_id):
        """
        Specialized training on IPMDAR tailoring strategies.
        
        Args:
            agent_id: Unique identifier for the agent
            
        Returns:
            dict: Training results
        """
        logger.info(f"Training agent {agent_id} on IPMDAR tailoring strategies")
        
        return {
            'agent_id': agent_id,
            'module': self.name,
            'component': 'tailoring_strategies',
            'material_ids': ['pm_101'],
            'status': 'completed'
        }
    
    def train_wbs_development(self, agent_id):
        """
        Specialized training on WBS development and management.
        
        Args:
            agent_id: Unique identifier for the agent
            
        Returns:
            dict: Training results
        """
        logger.info(f"Training agent {agent_id} on WBS development and management")
        
        return {
            'agent_id': agent_id,
            'module': self.name,
            'component': 'wbs_development',
            'material_ids': ['pm_102'],
            'status': 'completed'
        }
    
    def train_ims_management(self, agent_id):
        """
        Specialized training on Integrated Master Schedule management.
        
        Args:
            agent_id: Unique identifier for the agent
            
        Returns:
            dict: Training results
        """
        logger.info(f"Training agent {agent_id} on IMS management")
        
        return {
            'agent_id': agent_id,
            'module': self.name,
            'component': 'ims_management',
            'material_ids': ['pm_103'],
            'status': 'completed'
        }
    
    def train_implementation_planning(self, agent_id):
        """
        Specialized training on IPMDAR implementation planning.
        
        Args:
            agent_id: Unique identifier for the agent
            
        Returns:
            dict: Training results
        """
        logger.info(f"Training agent {agent_id} on IPMDAR implementation planning")
        
        return {
            'agent_id': agent_id,
            'module': self.name,
            'component': 'implementation_planning',
            'material_ids': ['pm_104'],
            'status': 'completed'
        }
