import logging
from .base_training import BaseTrainingModule

logger = logging.getLogger("Implementation Support Training")

class ImplementationSupportTraining(BaseTrainingModule):
    """
    Training module for Implementation Support expertise.
    Focuses on practical implementation strategies, transition planning,
    and organizational change management for IPMDAR adoption.
    """
    
    def __init__(self):
        """Initialize the Implementation Support training module."""
        super().__init__(name="IPMDAR Implementation Support Training")
    
    def _get_default_training_materials(self):
        """Get default training materials if JSON data is not available."""
        return {
            "module_name": "implementation_support",
            "materials": [
                {
                    "id": "is_101",
                    "title": "IPMDAR Transition Planning",
                    "description": "Methodologies for transitioning from legacy IPMSR/CSDR to IPMDAR",
                    "content_sections": [
                        {
                            "title": "Gap Analysis Methodology",
                            "content": "Structured approach to identifying gaps between current reporting capabilities and IPMDAR requirements, including assessment frameworks for data systems, processes, and organizational readiness. Includes step-by-step process for conducting gap analysis workshops and documenting findings."
                        },
                        {
                            "title": "Transition Strategy Development",
                            "content": "Methodologies for developing a phased transition strategy, including parallel operations planning, risk mitigation approaches, and establishment of transition metrics to track progress. Covers both government and contractor perspectives on transition."
                        },
                        {
                            "title": "Pilot Program Implementation",
                            "content": "Frameworks for implementing IPMDAR pilot programs, including selection criteria for pilot projects, test case development, evaluation metrics, and mechanisms for incorporating lessons learned into full implementation."
                        }
                    ]
                },
                {
                    "id": "is_102",
                    "title": "Organizational Change Management",
                    "description": "Strategies for managing organizational change during IPMDAR implementation",
                    "content_sections": [
                        {
                            "title": "Stakeholder Analysis and Engagement",
                            "content": "Techniques for identifying and analyzing stakeholders, developing tailored engagement strategies, and creating effective communication plans for different stakeholder groups impacted by IPMDAR implementation."
                        },
                        {
                            "title": "Training Program Development",
                            "content": "Frameworks for developing comprehensive IPMDAR training programs, including needs analysis, curriculum development, delivery methods, and effectiveness assessment for both government and contractor personnel."
                        },
                        {
                            "title": "Resistance Management",
                            "content": "Approaches to identifying and addressing resistance to change, including root cause analysis, targeted intervention strategies, and mechanisms for feedback collection and incorporation throughout the implementation process."
                        }
                    ]
                },
                {
                    "id": "is_103",
                    "title": "Implementation Roadmap Development",
                    "description": "Techniques for creating effective IPMDAR implementation roadmaps",
                    "content_sections": [
                        {
                            "title": "Organizational Readiness Assessment",
                            "content": "Frameworks for assessing organizational readiness for IPMDAR implementation, including evaluation of technical capabilities, process maturity, staff competencies, and leadership alignment. Includes scorecard development and interpretation."
                        },
                        {
                            "title": "Phased Implementation Planning",
                            "content": "Methodologies for developing phase-gated implementation plans, including objective setting, milestone development, resource allocation, and critical path identification specific to IPMDAR implementation contexts."
                        },
                        {
                            "title": "Implementation Governance",
                            "content": "Approaches to establishing effective governance structures for IPMDAR implementation, including steering committee formation, decision rights allocation, escalation paths, and progress tracking mechanisms."
                        }
                    ]
                },
                {
                    "id": "is_104",
                    "title": "IPMDAR Process Integration",
                    "description": "Methods for integrating IPMDAR into existing program management processes",
                    "content_sections": [
                        {
                            "title": "Process Mapping and Redesign",
                            "content": "Techniques for mapping existing program management processes and redesigning them to incorporate IPMDAR requirements, including workflow analysis, process optimization, and integration points with other program management activities."
                        },
                        {
                            "title": "Data Collection and Validation Processes",
                            "content": "Frameworks for establishing robust data collection and validation processes to support IPMDAR reporting, including data source identification, collection timing, quality control mechanisms, and reconciliation procedures."
                        },
                        {
                            "title": "Program Review Integration",
                            "content": "Approaches to integrating IPMDAR data and analysis into existing program review structures, including meeting cadence, agenda development, visualization techniques, and effective presentation methods for various stakeholder audiences."
                        }
                    ]
                }
            ]
        }
    
    def _get_default_assessments(self):
        """Get default assessments if JSON data is not available."""
        return {
            "module_name": "implementation_support",
            "assessments": [
                {
                    "id": "is_assessment_1",
                    "title": "Transition Planning Assessment",
                    "description": "Assessment of IPMDAR transition planning capabilities",
                    "questions": [
                        {
                            "id": "q1",
                            "question": "Develop a 12-month transition plan for a mid-sized defense contractor transitioning from IPMSR to IPMDAR, assuming they currently use a commercial EVM system and have moderate EVMS maturity.",
                            "answer": "A comprehensive 12-month transition plan would include: Phase 1 (Months 1-3): 1) Establish transition team with clear roles and responsibilities; 2) Conduct detailed gap analysis between current IPMSR capabilities and IPMDAR requirements; 3) Evaluate EVM system vendor's IPMDAR support roadmap; 4) Develop detailed requirements for system updates or configuration changes; 5) Create stakeholder engagement and communication plan. Phase 2 (Months 4-6): 1) Configure and test EVM system updates for IPMDAR compatibility; 2) Develop new/modified data collection procedures; 3) Create data validation routines; 4) Develop training curriculum; 5) Establish parallel processing approach for trial submissions. Phase 3 (Months 7-9): 1) Conduct staff training; 2) Implement process changes; 3) Perform pilot IPMDAR generation and internal validation; 4) Conduct table-top reviews with government counterparts; 5) Refine processes based on pilot results. Phase 4 (Months 10-12): 1) Conduct parallel IPMSR and IPMDAR reporting for 2-3 cycles; 2) Perform comprehensive validation between formats; 3) Address any discrepancies; 4) Obtain government acceptance of IPMDAR submissions; 5) Document lessons learned and establish ongoing support mechanisms. Key success factors include: executive sponsorship, dedicated resources, early engagement with government counterparts, and rigorous testing of data consistency between formats.",
                            "difficulty": "advanced"
                        },
                        {
                            "id": "q2",
                            "question": "Identify the top five risks typically encountered during IPMDAR transition and appropriate mitigation strategies for each.",
                            "answer": "Top five transition risks and mitigations: 1) EVM System Capability Gaps - Risk: Existing system unable to generate compliant IPMDAR. Mitigation: Early vendor engagement, detailed requirements analysis, contingency plans for manual processing if needed, consideration of third-party tools for gap coverage. 2) Data Quality Issues - Risk: Data inconsistencies between IPMDAR components or missing required data. Mitigation: Implement comprehensive data validation routines, establish clear data ownership, conduct data quality assessments before transition, implement data governance procedures. 3) Staff Knowledge Gaps - Risk: Personnel lack understanding of IPMDAR requirements and processes. Mitigation: Develop role-based training program, create detailed procedure documentation, establish expert support network, consider external expertise augmentation during transition. 4) Resource Constraints - Risk: Insufficient resources for parallel operations during transition. Mitigation: Secure executive commitment for temporary resource augmentation, prioritize critical activities, leverage automation where possible, consider phased implementation approach. 5) Government Acceptance - Risk: Submissions rejected due to compliance issues. Mitigation: Early engagement with government counterparts, formal review checkpoints before submission, adherence to DoD implementation guide examples, participation in industry working groups to understand common issues.",
                            "difficulty": "intermediate"
                        }
                    ]
                },
                {
                    "id": "is_assessment_2",
                    "title": "Organizational Change and Process Integration Assessment",
                    "description": "Assessment of organizational change management and process integration capabilities",
                    "questions": [
                        {
                            "id": "q1",
                            "question": "Design a comprehensive stakeholder engagement strategy for IPMDAR implementation within a large government program office that oversees multiple contractors.",
                            "answer": "A comprehensive stakeholder strategy would include: 1) Stakeholder Identification and Analysis: Map all stakeholder groups (program leadership, financial managers, schedule analysts, engineering leads, contractor interfaces, oversight organizations) with their specific interests, influence levels, and potential concerns regarding IPMDAR; develop influence/interest grid to prioritize engagement approaches. 2) Tailored Messaging: Develop messaging tailored to each stakeholder group focusing on specific benefits (e.g., for leadership: improved decision-making; for analysts: better data quality and analytical capabilities; for contractors: clearer expectations and potentially streamlined reporting). 3) Communication Channels: Establish multi-channel communication approach including formal briefings for leadership, working groups for practitioners, detailed guidance documents, FAQ resources, and regular status updates. 4) Engagement Sequence: Begin with leadership alignment sessions to establish vision and expectations, follow with practitioner education and input sessions, then conduct joint sessions with contractors to align on implementation approach. 5) Feedback Mechanisms: Implement structured feedback collection through surveys, focus groups, and lessons-learned sessions after initial implementation phases. 6) Contractor Engagement: Establish contractor working group with representatives from each prime contractor to address common challenges and share best practices. 7) Implementation Involvement: Create opportunities for key stakeholders to participate in implementation decisions to build ownership and address concerns early. 8) Success Measurement: Develop metrics to assess stakeholder engagement effectiveness, including perception surveys and participation rates in optional activities.",
                            "difficulty": "advanced"
                        },
                        {
                            "id": "q2",
                            "question": "How would you redesign the monthly program management review process to effectively incorporate IPMDAR data for a major defense acquisition program?",
                            "answer": "An effective PMR redesign would include: 1) Pre-meeting Analysis Process: Establish a structured analysis team meeting 1 week before PMR to analyze IPMDAR data, identify key insights, develop recommended focus areas, and prepare standardized visualizations. 2) Tiered Review Structure: Implement a tiered approach with technical deep-dives at lower levels feeding summary insights to executive reviews, all using consistent IPMDAR-based metrics. 3) Standard Analysis Products: Develop standard analysis templates showing period-to-period trends, variance analyses, and forecasts derived directly from IPMDAR data elements with drill-down capabilities for areas of concern. 4) Integrated Performance Perspective: Create integrated cost-schedule-technical performance views that leverage the connections between IPMDAR components rather than treating them as separate data sources. 5) Exception-Based Reporting: Implement threshold-based exception reporting to focus management attention on significant variances and emerging risks identified through IPMDAR analysis. 6) Contractor Alignment: Align contractor IPMDAR submission timing to support the PMR cycle, with submissions required 10 business days before reviews to allow adequate analysis time. 7) Progressive Elaboration: Structure the PMR agenda to begin with summary metrics derived from IPMDAR, then progressively elaborate on problem areas with supporting IPMDAR data. 8) Action Item Integration: Link PMR action items directly to IPMDAR elements requiring attention, with tracking of resolution through subsequent reporting cycles. 9) Predictive Focus: Shift emphasis from historical reporting to forward-looking analysis using IPMDAR forecast data and trend analysis, with dedicated time for discussing risk mitigation approaches.",
                            "difficulty": "advanced"
                        }
                    ]
                }
            ]
        }
    
    def train_transition_planning(self, agent_id):
        """
        Specialized training on IPMDAR transition planning.
        
        Args:
            agent_id: Unique identifier for the agent
            
        Returns:
            dict: Training results
        """
        logger.info(f"Training agent {agent_id} on IPMDAR transition planning")
        
        return {
            'agent_id': agent_id,
            'module': self.name,
            'component': 'transition_planning',
            'material_ids': ['is_101'],
            'status': 'completed'
        }
    
    def train_change_management(self, agent_id):
        """
        Specialized training on organizational change management.
        
        Args:
            agent_id: Unique identifier for the agent
            
        Returns:
            dict: Training results
        """
        logger.info(f"Training agent {agent_id} on organizational change management")
        
        return {
            'agent_id': agent_id,
            'module': self.name,
            'component': 'change_management',
            'material_ids': ['is_102'],
            'status': 'completed'
        }
    
    def train_implementation_roadmap(self, agent_id):
        """
        Specialized training on implementation roadmap development.
        
        Args:
            agent_id: Unique identifier for the agent
            
        Returns:
            dict: Training results
        """
        logger.info(f"Training agent {agent_id} on implementation roadmap development")
        
        return {
            'agent_id': agent_id,
            'module': self.name,
            'component': 'implementation_roadmap',
            'material_ids': ['is_103'],
            'status': 'completed'
        }
    
    def train_process_integration(self, agent_id):
        """
        Specialized training on IPMDAR process integration.
        
        Args:
            agent_id: Unique identifier for the agent
            
        Returns:
            dict: Training results
        """
        logger.info(f"Training agent {agent_id} on IPMDAR process integration")
        
        return {
            'agent_id': agent_id,
            'module': self.name,
            'component': 'process_integration',
            'material_ids': ['is_104'],
            'status': 'completed'
        }
