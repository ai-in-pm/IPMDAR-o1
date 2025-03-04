import logging
from .base_training import BaseTrainingModule

logger = logging.getLogger("Systems Integration Training")

class SystemsIntegrationTraining(BaseTrainingModule):
    """
    Training module for Systems Integration expertise.
    Focuses on data flow, system architecture, and integration of IPMDAR
    with other program management systems.
    """
    
    def __init__(self):
        """Initialize the Systems Integration training module."""
        super().__init__(name="IPMDAR Systems Integration Training")
    
    def _get_default_training_materials(self):
        """Get default training materials if JSON data is not available."""
        return {
            "module_name": "systems_integration",
            "materials": [
                {
                    "id": "si_101",
                    "title": "IPMDAR Data Architecture",
                    "description": "Understanding the fundamental data architecture of IPMDAR",
                    "content_sections": [
                        {
                            "title": "Data Element Structure",
                            "content": "Comprehensive analysis of IPMDAR data elements, including Contract Data, Performance Data, Schedule Data, Contract Variance Report, and Supplemental Data, with emphasis on data relationships, hierarchies, and dependencies."
                        },
                        {
                            "title": "Relational Schema Mapping",
                            "content": "Detailed mapping of IPMDAR data elements to relational database schemas, including normalization considerations, primary and foreign key relationships, and data integrity constraints."
                        },
                        {
                            "title": "Data Validation Rules",
                            "content": "Definition of validation rules for IPMDAR data elements, including cross-reference validations, sum checks, and business rule validations that ensure data integrity across the integrated dataset."
                        }
                    ]
                },
                {
                    "id": "si_102",
                    "title": "System Interface Design",
                    "description": "Techniques for designing interfaces between IPMDAR and other systems",
                    "content_sections": [
                        {
                            "title": "XML Schema Implementation",
                            "content": "Detailed implementation of IPMDAR XML schemas, including utilization of IPMDAR DIDs, extension mechanisms, and compliance with the standard schema definitions from the DoD."
                        },
                        {
                            "title": "JSON Transformation Patterns",
                            "content": "Methodologies for transforming IPMDAR data between XML and JSON formats, with focus on maintaining data fidelity, handling complex hierarchical structures, and optimizing for API interactions."
                        },
                        {
                            "title": "API Design Patterns",
                            "content": "Best practices for designing APIs that expose IPMDAR data, including RESTful interface design, GraphQL implementations, and secure authentication mechanisms suitable for DoD environments."
                        }
                    ]
                },
                {
                    "id": "si_103",
                    "title": "Enterprise Integration Patterns",
                    "description": "Advanced integration patterns for IPMDAR in enterprise environments",
                    "content_sections": [
                        {
                            "title": "Message-Based Integration",
                            "content": "Implementation of message-based integration patterns for IPMDAR data flows, including message queues, publish-subscribe patterns, and event-driven architectures for real-time data synchronization."
                        },
                        {
                            "title": "Data Synchronization Strategies",
                            "content": "Methodologies for maintaining data consistency across multiple systems, including master data management, conflict resolution strategies, and versioning approaches for IPMDAR datasets."
                        },
                        {
                            "title": "Enterprise Service Bus Integration",
                            "content": "Techniques for integrating IPMDAR data flows through enterprise service bus architectures, including transformation, routing, and mediation patterns suitable for complex DoD environments."
                        }
                    ]
                },
                {
                    "id": "si_104",
                    "title": "IPMDAR-EVM System Integration",
                    "description": "Specialized integration between IPMDAR and EVM systems",
                    "content_sections": [
                        {
                            "title": "Data Mapping Between IPMDAR and EVM Systems",
                            "content": "Detailed data element mapping between IPMDAR formats and various EVM system data structures, including handling of WBS elements, control accounts, work packages, and performance metrics."
                        },
                        {
                            "title": "Automated Data Validation",
                            "content": "Implementation of automated validation processes between IPMDAR and source EVM systems, including reconciliation processes, error detection, and correction workflows."
                        },
                        {
                            "title": "Change Impact Analysis",
                            "content": "Methodologies for analyzing the impact of changes in either IPMDAR requirements or EVM systems on the integrated data flows, including version compatibility assessments and migration strategies."
                        }
                    ]
                }
            ]
        }
    
    def _get_default_assessments(self):
        """Get default assessments if JSON data is not available."""
        return {
            "module_name": "systems_integration",
            "assessments": [
                {
                    "id": "si_assessment_1",
                    "title": "Data Architecture and Interface Assessment",
                    "description": "Assessment of IPMDAR data architecture and interface design capabilities",
                    "questions": [
                        {
                            "id": "q1",
                            "question": "Describe how you would design a database schema to efficiently store and query IPMDAR performance data while maintaining relationships with contract and schedule data.",
                            "answer": "An efficient database schema for IPMDAR would implement: 1) A normalized relational design with Contract as the top-level entity, linked to multiple reporting periods; 2) Performance data tables structured around control accounts and work packages, with foreign keys to the WBS dictionary; 3) Schedule data modeled as activities with predecessor/successor relationships, linked to performance data through work package IDs; 4) Indexing strategies optimized for common queries (e.g., period-over-period performance comparisons, critical path analysis); 5) Materialized views for frequently accessed calculations (CPI, SPI by control account); 6) Temporal data handling for historical analysis; 7) Data partitioning for large datasets based on reporting periods. This design balances normalization principles against query performance requirements, with particular attention to maintaining referential integrity across the IPMDAR components.",
                            "difficulty": "advanced"
                        },
                        {
                            "id": "q2",
                            "question": "Outline the validation rules you would implement to ensure data consistency between the Schedule Data and Performance Data sections of IPMDAR.",
                            "answer": "Key validation rules between Schedule and Performance Data include: 1) WBS Element Consistency: Every WBS element in the Performance Data must have a corresponding representation in the Schedule Data; 2) Cost/Schedule Alignment: The sum of budgeted costs for activities in the Schedule Data must reconcile with the corresponding work package budgets in Performance Data; 3) Timing Consistency: Activity dates in Schedule Data must align with the time-phased budget and actuals in Performance Data; 4) Progress Alignment: Schedule percent complete metrics must be reasonably consistent with earned value percentages in Performance Data; 5) Resource Assignment Verification: Resources assigned in Schedule Data must be consistent with the resources implicitly represented in the Performance Data cost elements; 6) Critical Path Validation: Ensure critical path activities in Schedule Data have corresponding representation and appropriate earned value techniques in Performance Data; 7) Baseline Consistency: Schedule baseline dates must be consistent with the budget time-phasing in Performance Data.",
                            "difficulty": "intermediate"
                        }
                    ]
                },
                {
                    "id": "si_assessment_2",
                    "title": "Enterprise Integration Assessment",
                    "description": "Assessment of enterprise integration capabilities for IPMDAR",
                    "questions": [
                        {
                            "id": "q1",
                            "question": "Design an enterprise integration architecture for consolidating IPMDAR data from multiple contractors, each using different EVM systems, into a unified government program management dashboard.",
                            "answer": "A robust integration architecture would include: 1) Ingest Layer: Secure SFTP endpoints for contractor submissions with digital signature verification and XML/JSON schema validation; 2) Transformation Layer: System-specific adapters for each contractor EVM system to normalize data formats, implemented as containerized microservices; 3) Integration Layer: Enterprise service bus handling routing, transformation, and orchestration with a canonical data model based on IPMDAR standard; 4) Persistence Layer: Multi-tenant data warehouse with contractor-specific schemas and a unified view layer; 5) Analytics Layer: OLAP cubes for performance metrics with drill-down capabilities from program to control account level; 6) Presentation Layer: Dashboard with role-based access control separating contractor-specific and program-level views; 7) Governance Layer: Data lineage tracking, validation reporting, and submission compliance monitoring. This architecture emphasizes security boundaries between contractors while enabling program-level analysis across the integrated dataset.",
                            "difficulty": "advanced"
                        },
                        {
                            "id": "q2",
                            "question": "How would you implement a data synchronization strategy between a contractor's EVM system and the government's IPMDAR repository that minimizes manual intervention while ensuring data integrity?",
                            "answer": "An optimal data synchronization strategy would implement: 1) Scheduled Extraction: Automated monthly extracts from the EVM system aligned with IPMDAR submission cycles; 2) Pre-submission Validation: Automated validation suite running within the contractor environment before submission, checking for data completeness, consistency, and compliance with IPMDAR requirements; 3) Delta Detection: Comparison of current submission with previous submission to identify and flag significant changes requiring explanation; 4) Transformation Pipeline: Automated transformation from EVM system format to IPMDAR XML with logging at each step; 5) Exception Handling: Workflow system for managing validation exceptions, with routing to appropriate subject matter experts for resolution; 6) Reconciliation Reporting: Automated reports showing alignment between EVM system native reports and generated IPMDAR submissions; 7) Change Tracking: Version control of all submissions with capability to generate variance explanations for changed data elements; 8) Feedback Loop: Mechanism for government reviewer feedback to be incorporated into future extraction processes. This approach minimizes manual intervention by automating the entire pipeline while maintaining quality gates that ensure data integrity.",
                            "difficulty": "advanced"
                        }
                    ]
                }
            ]
        }
    
    def train_data_architecture(self, agent_id):
        """
        Specialized training on IPMDAR data architecture.
        
        Args:
            agent_id: Unique identifier for the agent
            
        Returns:
            dict: Training results
        """
        logger.info(f"Training agent {agent_id} on IPMDAR data architecture")
        
        return {
            'agent_id': agent_id,
            'module': self.name,
            'component': 'data_architecture',
            'material_ids': ['si_101'],
            'status': 'completed'
        }
    
    def train_interface_design(self, agent_id):
        """
        Specialized training on system interface design.
        
        Args:
            agent_id: Unique identifier for the agent
            
        Returns:
            dict: Training results
        """
        logger.info(f"Training agent {agent_id} on system interface design")
        
        return {
            'agent_id': agent_id,
            'module': self.name,
            'component': 'interface_design',
            'material_ids': ['si_102'],
            'status': 'completed'
        }
    
    def train_enterprise_integration(self, agent_id):
        """
        Specialized training on enterprise integration patterns.
        
        Args:
            agent_id: Unique identifier for the agent
            
        Returns:
            dict: Training results
        """
        logger.info(f"Training agent {agent_id} on enterprise integration patterns")
        
        return {
            'agent_id': agent_id,
            'module': self.name,
            'component': 'enterprise_integration',
            'material_ids': ['si_103'],
            'status': 'completed'
        }
    
    def train_evm_integration(self, agent_id):
        """
        Specialized training on IPMDAR-EVM system integration.
        
        Args:
            agent_id: Unique identifier for the agent
            
        Returns:
            dict: Training results
        """
        logger.info(f"Training agent {agent_id} on IPMDAR-EVM system integration")
        
        return {
            'agent_id': agent_id,
            'module': self.name,
            'component': 'evm_integration',
            'material_ids': ['si_104'],
            'status': 'completed'
        }
