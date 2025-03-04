import logging
from .base_training import BaseTrainingModule

logger = logging.getLogger("Data Analytics Training")

class DataAnalyticsTraining(BaseTrainingModule):
    """
    Training module for Data Analytics expertise.
    Focuses on analyzing IPMDAR performance data, cost-schedule integration, 
    and Earned Value Management (EVM) metrics.
    """
    
    def __init__(self):
        """Initialize the Data Analytics training module."""
        super().__init__(name="IPMDAR Data Analytics Training")
    
    def _get_default_training_materials(self):
        """Get default training materials if JSON data is not available."""
        return {
            "module_name": "data_analytics",
            "materials": [
                {
                    "id": "da_101",
                    "title": "EVMS Fundamentals for Data Analysis",
                    "description": "Core concepts of Earned Value Management Systems for data analysis",
                    "content_sections": [
                        {
                            "title": "EVMS Data Structures",
                            "content": "The fundamental data structures in an EVMS, including Work Breakdown Structure (WBS), Organizational Breakdown Structure (OBS), and Control Accounts."
                        },
                        {
                            "title": "EVM Metrics Calculation",
                            "content": "Formulas and methodologies for calculating key EVM metrics including CPI, SPI, CV, SV, VAC, EAC, and TCPI."
                        },
                        {
                            "title": "Performance Measurement Baseline",
                            "content": "Structure and maintenance of the Performance Measurement Baseline (PMB) as the foundation for performance analysis."
                        }
                    ]
                },
                {
                    "id": "da_102",
                    "title": "Advanced Performance Analysis Techniques",
                    "description": "Sophisticated methods for analyzing program performance data",
                    "content_sections": [
                        {
                            "title": "Variance Analysis",
                            "content": "Detailed methodologies for analyzing cost and schedule variances, including root cause analysis and trend identification."
                        },
                        {
                            "title": "Statistical Methods",
                            "content": "Application of statistical methods including regression analysis, confidence intervals, and statistical process control to EVM data."
                        },
                        {
                            "title": "Forecast Modeling",
                            "content": "Various EAC calculation methods and their appropriate applications, including index-based, regression-based, and Monte Carlo simulation approaches."
                        }
                    ]
                },
                {
                    "id": "da_103",
                    "title": "Data Visualization for IPMDAR",
                    "description": "Effective visualization techniques for IPMDAR performance data",
                    "content_sections": [
                        {
                            "title": "Performance Charts",
                            "content": "Design and interpretation of standard EVM charts including S-curves, performance indices over time, and variance trends."
                        },
                        {
                            "title": "Executive Dashboards",
                            "content": "Design principles for effective executive dashboards that communicate program status clearly and actionably."
                        },
                        {
                            "title": "Interactive Analytics",
                            "content": "Implementation of interactive data visualization tools to enable drill-down analysis and exploration of performance data."
                        }
                    ]
                }
            ]
        }
    
    def _get_default_assessments(self):
        """Get default assessments if JSON data is not available."""
        return {
            "module_name": "data_analytics",
            "assessments": [
                {
                    "id": "da_assessment_1",
                    "title": "EVM Metrics Calculation Assessment",
                    "description": "Assessment of ability to calculate and interpret EVM metrics",
                    "questions": [
                        {
                            "id": "q1",
                            "question": "Calculate the Cost Performance Index (CPI) given: BCWP = $500,000 and ACWP = $550,000",
                            "answer": "0.91",
                            "difficulty": "basic"
                        },
                        {
                            "id": "q2",
                            "question": "Calculate the Schedule Performance Index (SPI) given: BCWP = $500,000 and BCWS = $600,000",
                            "answer": "0.83",
                            "difficulty": "basic"
                        },
                        {
                            "id": "q3",
                            "question": "Using the CPI-based method, calculate the EAC given: ACWP = $2,000,000, BAC = $10,000,000, and CPI = 0.8",
                            "answer": "$12,500,000",
                            "difficulty": "intermediate"
                        }
                    ]
                },
                {
                    "id": "da_assessment_2",
                    "title": "Performance Analysis Interpretation Assessment",
                    "description": "Assessment of ability to interpret performance analysis results",
                    "questions": [
                        {
                            "id": "q1",
                            "question": "A program has a CPI of 0.85 and an SPI of 1.05. Provide a concise interpretation of the program's performance status.",
                            "answer": "The program is ahead of schedule but over budget. The cost efficiency is poor (spending more than planned for the work completed), but schedule performance is good (accomplishing more work than planned for this point in time).",
                            "difficulty": "intermediate"
                        },
                        {
                            "id": "q2",
                            "question": "A program's CPI has been consistently declining from 1.0 to 0.9 over the past six months while the SPI has remained steady at 0.95. What does this trend suggest, and what actions might be appropriate?",
                            "answer": "The trend suggests increasing cost inefficiency while maintaining a slightly behind schedule status. This could indicate resource constraints, scope creep, or declining productivity. Appropriate actions might include a root cause analysis of cost drivers, review of estimating assumptions, and potential corrective actions focused on cost control while monitoring schedule impacts.",
                            "difficulty": "advanced"
                        }
                    ]
                }
            ]
        }
    
    def train_evm_metrics(self, agent_id):
        """
        Specialized training on EVM metrics calculation and interpretation.
        
        Args:
            agent_id: Unique identifier for the agent
            
        Returns:
            dict: Training results
        """
        logger.info(f"Training agent {agent_id} on EVM metrics")
        
        return {
            'agent_id': agent_id,
            'module': self.name,
            'component': 'evm_metrics',
            'material_ids': ['da_101'],
            'status': 'completed'
        }
    
    def train_performance_analysis(self, agent_id):
        """
        Specialized training on advanced performance analysis techniques.
        
        Args:
            agent_id: Unique identifier for the agent
            
        Returns:
            dict: Training results
        """
        logger.info(f"Training agent {agent_id} on advanced performance analysis")
        
        return {
            'agent_id': agent_id,
            'module': self.name,
            'component': 'performance_analysis',
            'material_ids': ['da_102'],
            'status': 'completed'
        }
    
    def train_data_visualization(self, agent_id):
        """
        Specialized training on data visualization for IPMDAR.
        
        Args:
            agent_id: Unique identifier for the agent
            
        Returns:
            dict: Training results
        """
        logger.info(f"Training agent {agent_id} on data visualization for IPMDAR")
        
        return {
            'agent_id': agent_id,
            'module': self.name,
            'component': 'data_visualization',
            'material_ids': ['da_103'],
            'status': 'completed'
        }
