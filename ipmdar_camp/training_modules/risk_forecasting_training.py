import logging
from .base_training import BaseTrainingModule

logger = logging.getLogger("Risk Forecasting Training")

class RiskForecastingTraining(BaseTrainingModule):
    """
    Training module for Risk & Forecasting expertise.
    Focuses on predictive analytics, risk identification, and 
    mitigation strategies using IPMDAR datasets.
    """
    
    def __init__(self):
        """Initialize the Risk & Forecasting training module."""
        super().__init__(name="IPMDAR Risk & Forecasting Training")
    
    def _get_default_training_materials(self):
        """Get default training materials if JSON data is not available."""
        return {
            "module_name": "risk_forecasting",
            "materials": [
                {
                    "id": "rf_101",
                    "title": "Risk Identification Methodologies",
                    "description": "Systematic approaches to identifying risks in IPMDAR datasets",
                    "content_sections": [
                        {
                            "title": "Performance Trend Analysis",
                            "content": "Techniques for analyzing CPI and SPI trends to identify potential emerging risks, including detection of negative trends, trend inflection points, and correlation with program events."
                        },
                        {
                            "title": "Variance Analysis for Risk Identification",
                            "content": "Methodologies for using variance analysis to identify potential risk areas, including analysis of both favorable and unfavorable variances to determine the risk profile of the program."
                        },
                        {
                            "title": "Critical Path and Near-Critical Path Risk Identification",
                            "content": "Techniques for identifying schedule risks through critical path analysis, including float consumption patterns, critical path volatility, and critical path density metrics."
                        }
                    ]
                },
                {
                    "id": "rf_102",
                    "title": "Quantitative Risk Analysis Techniques",
                    "description": "Advanced methods for quantifying program risks",
                    "content_sections": [
                        {
                            "title": "Monte Carlo Simulation",
                            "content": "Implementation of Monte Carlo simulation for schedule and cost risk analysis, including input distribution selection, correlation modeling, and output interpretation."
                        },
                        {
                            "title": "Probabilistic Risk Assessment",
                            "content": "Techniques for determining probability and impact of identified risks, developing S-curves for cost and schedule outcomes, and establishing confidence levels for program estimates."
                        },
                        {
                            "title": "Integrated Cost-Schedule Risk Analysis",
                            "content": "Methods for integrating cost and schedule risk analysis to provide a more comprehensive view of program risk, including modeling the cost impact of schedule slips."
                        }
                    ]
                },
                {
                    "id": "rf_103",
                    "title": "Estimate at Completion (EAC) Forecasting",
                    "description": "Advanced techniques for accurate EAC forecasting",
                    "content_sections": [
                        {
                            "title": "Index-Based EAC Methods",
                            "content": "Various index-based EAC calculation methods, including CPI, SPI, and composite index methods, with guidelines for selecting the appropriate method based on program characteristics."
                        },
                        {
                            "title": "Regression-Based Forecasting",
                            "content": "Implementation of regression analysis techniques for EAC forecasting, including linear, non-linear, and multiple regression approaches based on historical program performance."
                        },
                        {
                            "title": "Bayesian EAC Estimation",
                            "content": "Application of Bayesian methods to EAC estimation, incorporating prior information, expert judgment, and current performance data to develop robust forecasts."
                        }
                    ]
                },
                {
                    "id": "rf_104",
                    "title": "Risk Mitigation Strategy Development",
                    "description": "Approaches to developing effective risk mitigation strategies",
                    "content_sections": [
                        {
                            "title": "Risk Response Planning",
                            "content": "Methodologies for developing appropriate risk responses (avoid, transfer, mitigate, accept) based on risk characteristics and program constraints."
                        },
                        {
                            "title": "Mitigation Effectiveness Assessment",
                            "content": "Techniques for assessing the effectiveness of risk mitigation strategies, including quantitative analysis of risk reduction potential and cost-benefit analysis of mitigation options."
                        },
                        {
                            "title": "Management Reserve Allocation",
                            "content": "Approaches to determining appropriate management reserve levels based on risk analysis, including methods for allocating reserve to specific risk areas and managing reserve consumption."
                        }
                    ]
                }
            ]
        }
    
    def _get_default_assessments(self):
        """Get default assessments if JSON data is not available."""
        return {
            "module_name": "risk_forecasting",
            "assessments": [
                {
                    "id": "rf_assessment_1",
                    "title": "Risk Identification and Analysis Assessment",
                    "description": "Assessment of risk identification and analysis capabilities",
                    "questions": [
                        {
                            "id": "q1",
                            "question": "Identify the key risk indicators in a program that has a stable CPI of 0.95, an SPI that has declined from 1.0 to 0.92 over three months, and increasing critical path float consumption.",
                            "answer": "The key risk indicators are: 1) Stable but unfavorable CPI (0.95) indicating consistent cost overruns, 2) Declining SPI trend (1.0 to 0.92) suggesting accelerating schedule slippage, 3) Increasing critical path float consumption indicating potential future schedule impacts. Together, these suggest increasing schedule pressure that may further impact cost performance if acceleration is required.",
                            "difficulty": "intermediate"
                        },
                        {
                            "id": "q2",
                            "question": "A program with a BAC of $100M is currently 40% complete with an ACWP of $45M and BCWP of $40M. Calculate the EAC using the CPI method and the CPI×SPI method, if the BCWS is $50M. Interpret the difference between these two forecasts.",
                            "answer": "CPI = BCWP/ACWP = 40/45 = 0.889. SPI = BCWP/BCWS = 40/50 = 0.8. EAC(CPI) = BAC/CPI = 100/0.889 = $112.5M. EAC(CPI×SPI) = BAC/(CPI×SPI) = 100/(0.889×0.8) = $140.6M. The difference indicates that when schedule delays are factored into the forecast, a significantly higher cost at completion is predicted, suggesting that schedule recovery efforts may add substantial cost to the program.",
                            "difficulty": "advanced"
                        }
                    ]
                },
                {
                    "id": "rf_assessment_2",
                    "title": "Risk Mitigation Strategy Assessment",
                    "description": "Assessment of risk mitigation strategy development capabilities",
                    "questions": [
                        {
                            "id": "q1",
                            "question": "Develop a comprehensive risk mitigation strategy for a program showing early signs of staffing shortage impacts (minor schedule slips in non-critical activities, some declining productivity metrics).",
                            "answer": "A comprehensive risk mitigation strategy should include: 1) Short-term actions: Implement overtime for critical resources, prioritize activities to focus available resources on critical path work, develop more detailed staffing forecasts for next 3 months. 2) Medium-term actions: Begin targeted recruitment for key positions, develop cross-training program to increase staff flexibility, evaluate subcontracting options for lower-priority work. 3) Long-term actions: Work with functional managers to develop staffing pipeline, evaluate schedule rebaselining if necessary, consider schedule replanning to better align with resource constraints. 4) Monitoring approach: Establish weekly resource utilization tracking, create staffing risk early warning metrics, integrate resource discussions into program status reviews.",
                            "difficulty": "advanced"
                        },
                        {
                            "id": "q2",
                            "question": "How should management reserve be sized for a $50M, 3-year development program with moderate technical complexity and no similar prior programs for comparison?",
                            "answer": "For a $50M program with moderate technical complexity and no historical basis, management reserve should be determined through: 1) Quantitative risk analysis using Monte Carlo simulation with subject matter expert inputs for each major work element; 2) Development of an S-curve showing probability distribution of potential costs; 3) Selection of an appropriate confidence level (typically 70-80% for moderate complexity); 4) Sizing the management reserve as the difference between the baseline budget and the selected confidence level. Without historical data, expert judgment must be heavily leveraged, typically resulting in reserve of 15-20% for moderate complexity development programs. The reserve should be allocated to specific risk areas rather than held as a general pool.",
                            "difficulty": "advanced"
                        }
                    ]
                }
            ]
        }
    
    def train_risk_identification(self, agent_id):
        """
        Specialized training on risk identification methodologies.
        
        Args:
            agent_id: Unique identifier for the agent
            
        Returns:
            dict: Training results
        """
        logger.info(f"Training agent {agent_id} on risk identification methodologies")
        
        return {
            'agent_id': agent_id,
            'module': self.name,
            'component': 'risk_identification',
            'material_ids': ['rf_101'],
            'status': 'completed'
        }
    
    def train_quantitative_risk_analysis(self, agent_id):
        """
        Specialized training on quantitative risk analysis techniques.
        
        Args:
            agent_id: Unique identifier for the agent
            
        Returns:
            dict: Training results
        """
        logger.info(f"Training agent {agent_id} on quantitative risk analysis")
        
        return {
            'agent_id': agent_id,
            'module': self.name,
            'component': 'quantitative_risk_analysis',
            'material_ids': ['rf_102'],
            'status': 'completed'
        }
    
    def train_eac_forecasting(self, agent_id):
        """
        Specialized training on EAC forecasting methods.
        
        Args:
            agent_id: Unique identifier for the agent
            
        Returns:
            dict: Training results
        """
        logger.info(f"Training agent {agent_id} on EAC forecasting methods")
        
        return {
            'agent_id': agent_id,
            'module': self.name,
            'component': 'eac_forecasting',
            'material_ids': ['rf_103'],
            'status': 'completed'
        }
    
    def train_risk_mitigation(self, agent_id):
        """
        Specialized training on risk mitigation strategy development.
        
        Args:
            agent_id: Unique identifier for the agent
            
        Returns:
            dict: Training results
        """
        logger.info(f"Training agent {agent_id} on risk mitigation strategies")
        
        return {
            'agent_id': agent_id,
            'module': self.name,
            'component': 'risk_mitigation',
            'material_ids': ['rf_104'],
            'status': 'completed'
        }
