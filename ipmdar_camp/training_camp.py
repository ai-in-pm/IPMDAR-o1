import os
import json
import time
import random
import logging
from datetime import datetime
from .training_modules import (
    compliance_policy_training,
    data_analytics_training,
    project_management_training,
    risk_forecasting_training,
    systems_integration_training,
    implementation_support_training
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ipmdar_camp/logs/training.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("IPMDAR Training Camp")

class IPMDARTrainingCamp:
    """
    IPMDAR Training Camp - Comprehensive training system for AI agents to 
    achieve expert-level understanding of IPMDAR implementation.
    
    This class manages the complete training lifecycle for all IPMDAR AI agents,
    including curriculum delivery, knowledge assessment, certification, and 
    continuous learning.
    """
    
    def __init__(self, knowledge_base=None):
        """
        Initialize the IPMDAR Training Camp.
        
        Args:
            knowledge_base: Optional pre-loaded knowledge base
        """
        self.knowledge_base = knowledge_base
        self.certification_status = {}
        self.training_modules = {
            'compliance_policy': compliance_policy_training.CompliancePolicyTraining(),
            'data_analytics': data_analytics_training.DataAnalyticsTraining(),
            'project_management': project_management_training.ProjectManagementTraining(),
            'risk_forecasting': risk_forecasting_training.RiskForecastingTraining(),
            'systems_integration': systems_integration_training.SystemsIntegrationTraining(),
            'implementation_support': implementation_support_training.ImplementationSupportTraining()
        }
        
        # Load certification records if they exist
        self.certification_records_path = 'ipmdar_camp/logs/certification_records.json'
        self.load_certification_records()
    
    def load_certification_records(self):
        """Load existing certification records if available."""
        try:
            if os.path.exists(self.certification_records_path):
                with open(self.certification_records_path, 'r') as f:
                    self.certification_status = json.load(f)
                    logger.info(f"Loaded existing certification records for {len(self.certification_status)} agents")
            else:
                logger.info("No existing certification records found")
        except Exception as e:
            logger.error(f"Error loading certification records: {e}")
    
    def save_certification_records(self):
        """Save certification records to persistent storage."""
        try:
            with open(self.certification_records_path, 'w') as f:
                json.dump(self.certification_status, f, indent=2)
            logger.info(f"Saved certification records for {len(self.certification_status)} agents")
        except Exception as e:
            logger.error(f"Error saving certification records: {e}")
    
    def train_agent(self, agent_id, agent_type, force_retrain=False):
        """
        Train an AI agent through the complete IPMDAR curriculum.
        
        Args:
            agent_id: Unique identifier for the agent
            agent_type: Type of agent (e.g., 'compliance_policy', 'data_analytics')
            force_retrain: Force retraining even if already certified
            
        Returns:
            bool: True if agent is certified (either already or after training)
        """
        # Check if agent is already certified and training isn't forced
        if agent_id in self.certification_status and self.certification_status[agent_id]['certified'] and not force_retrain:
            logger.info(f"Agent {agent_id} ({agent_type}) is already certified. Skipping training.")
            return True
        
        logger.info(f"Beginning training for Agent {agent_id} ({agent_type})...")
        
        # Initialize or reset certification record
        self.certification_status[agent_id] = {
            'agent_id': agent_id,
            'agent_type': agent_type,
            'training_started': datetime.now().isoformat(),
            'training_completed': None,
            'curriculum_progress': {},
            'assessment_scores': {},
            'certified': False,
            'certification_date': None
        }
        
        try:
            # Execute core curriculum for the agent type
            core_modules = self._get_core_curriculum(agent_type)
            self._complete_core_curriculum(agent_id, agent_type, core_modules)
            
            # Execute specialized curriculum for the agent type
            specialized_modules = self._get_specialized_curriculum(agent_type)
            self._complete_specialized_curriculum(agent_id, agent_type, specialized_modules)
            
            # Execute cross-domain training for holistic understanding
            cross_domain_modules = self._get_cross_domain_curriculum(agent_type)
            self._complete_cross_domain_training(agent_id, agent_type, cross_domain_modules)
            
            # Conduct final assessment and certification
            certification_result = self._conduct_certification_assessment(agent_id, agent_type)
            
            # Update certification status
            self.certification_status[agent_id]['certified'] = certification_result
            if certification_result:
                self.certification_status[agent_id]['certification_date'] = datetime.now().isoformat()
                self.certification_status[agent_id]['training_completed'] = datetime.now().isoformat()
                logger.info(f"Agent {agent_id} ({agent_type}) successfully certified!")
            else:
                logger.warning(f"Agent {agent_id} ({agent_type}) failed certification assessment.")
            
            # Save updated certification records
            self.save_certification_records()
            
            return certification_result
            
        except Exception as e:
            logger.error(f"Error during training for Agent {agent_id}: {e}")
            return False
    
    def _get_core_curriculum(self, agent_type):
        """Get the core curriculum modules for a specific agent type."""
        # All agents need to complete these fundamental modules
        core_modules = [
            'ipmdar_fundamentals',
            'dod_acquisition_framework',
            'data_requirements_basics',
            'regulatory_compliance_overview'
        ]
        
        return core_modules
    
    def _get_specialized_curriculum(self, agent_type):
        """Get the specialized curriculum modules for a specific agent type."""
        # Each agent type has its own specialized modules
        specialized_curricula = {
            'compliance_policy': [
                'regulatory_frameworks_deep_dive',
                'policy_interpretation_techniques',
                'compliance_verification_methods',
                'acquisition_regulations_mastery',
                'cdrl_development_and_review'
            ],
            'data_analytics': [
                'evms_principles_and_practices',
                'performance_metric_analysis',
                'data_visualization_techniques',
                'statistical_analysis_for_ipmdar',
                'predictive_modeling_basics'
            ],
            'project_management': [
                'project_lifecycle_management',
                'ipmdar_tailoring_strategies',
                'wbs_development_and_management',
                'schedule_integration_techniques',
                'resource_management_best_practices'
            ],
            'risk_forecasting': [
                'risk_identification_methods',
                'quantitative_risk_analysis',
                'forecasting_techniques',
                'eac_etc_calculation_methods',
                'monte_carlo_simulation_basics'
            ],
            'systems_integration': [
                'data_schemas_and_formats',
                'system_interoperability_standards',
                'integration_architecture_design',
                'automated_data_validation',
                'legacy_system_integration'
            ],
            'implementation_support': [
                'change_management_strategies',
                'training_program_development',
                'process_documentation_techniques',
                'stakeholder_communication',
                'implementation_roadmap_design'
            ]
        }
        
        return specialized_curricula.get(agent_type, [])
    
    def _get_cross_domain_curriculum(self, agent_type):
        """Get cross-domain curriculum modules for holistic understanding."""
        # Define modules from other domains that each agent type should learn
        cross_domain_curricula = {
            'compliance_policy': [
                'data_analytics:performance_metric_basics',
                'project_management:tailoring_fundamentals',
                'systems_integration:data_format_requirements'
            ],
            'data_analytics': [
                'compliance_policy:reporting_requirements',
                'risk_forecasting:risk_analysis_basics',
                'project_management:schedule_fundamentals'
            ],
            'project_management': [
                'compliance_policy:acquisition_requirements',
                'risk_forecasting:risk_management_basics',
                'implementation_support:stakeholder_engagement'
            ],
            'risk_forecasting': [
                'data_analytics:statistical_foundations',
                'project_management:critical_path_analysis',
                'compliance_policy:contract_types_and_risks'
            ],
            'systems_integration': [
                'data_analytics:data_structure_fundamentals',
                'implementation_support:system_deployment_basics',
                'compliance_policy:data_security_requirements'
            ],
            'implementation_support': [
                'project_management:implementation_planning',
                'systems_integration:user_interface_basics',
                'compliance_policy:training_requirements'
            ]
        }
        
        return cross_domain_curricula.get(agent_type, [])
    
    def _complete_core_curriculum(self, agent_id, agent_type, modules):
        """Complete the core curriculum modules for an agent."""
        logger.info(f"Starting core curriculum for Agent {agent_id} ({agent_type})")
        
        training_module = self.training_modules.get(agent_type)
        if not training_module:
            logger.error(f"No training module found for agent type: {agent_type}")
            return
        
        # Process each core module
        for module in modules:
            logger.info(f"  - Completing core module: {module}")
            
            # Simulate training time
            time.sleep(0.5)  # Reduced for testing, would be longer in production
            
            # Record progress
            score = random.uniform(0.90, 1.0)  # Simulate high scores for core modules
            self.certification_status[agent_id]['curriculum_progress'][module] = {
                'completed': True,
                'completion_date': datetime.now().isoformat(),
                'score': score
            }
            
            logger.info(f"    Completed with score: {score:.2f}")
    
    def _complete_specialized_curriculum(self, agent_id, agent_type, modules):
        """Complete the specialized curriculum modules for an agent."""
        logger.info(f"Starting specialized curriculum for Agent {agent_id} ({agent_type})")
        
        training_module = self.training_modules.get(agent_type)
        if not training_module:
            logger.error(f"No training module found for agent type: {agent_type}")
            return
        
        # Process each specialized module
        for module in modules:
            logger.info(f"  - Completing specialized module: {module}")
            
            # Simulate training time
            time.sleep(0.7)  # Longer for specialized modules
            
            # Record progress
            score = random.uniform(0.85, 1.0)  # Slightly more variation in specialized modules
            self.certification_status[agent_id]['curriculum_progress'][module] = {
                'completed': True,
                'completion_date': datetime.now().isoformat(),
                'score': score
            }
            
            logger.info(f"    Completed with score: {score:.2f}")
    
    def _complete_cross_domain_training(self, agent_id, agent_type, modules):
        """Complete cross-domain training modules for an agent."""
        logger.info(f"Starting cross-domain training for Agent {agent_id} ({agent_type})")
        
        # Process each cross-domain module
        for module in modules:
            logger.info(f"  - Completing cross-domain module: {module}")
            
            # Simulate training time
            time.sleep(0.6)
            
            # Record progress
            score = random.uniform(0.80, 0.95)  # Lower scores expected in cross-domain areas
            self.certification_status[agent_id]['curriculum_progress'][module] = {
                'completed': True,
                'completion_date': datetime.now().isoformat(),
                'score': score
            }
            
            logger.info(f"    Completed with score: {score:.2f}")
    
    def _conduct_certification_assessment(self, agent_id, agent_type):
        """
        Conduct the final certification assessment for an agent.
        
        Returns:
            bool: True if agent passed certification, False otherwise
        """
        logger.info(f"Conducting certification assessment for Agent {agent_id} ({agent_type})")
        
        # Get the specialized training module for this agent type
        training_module = self.training_modules.get(agent_type)
        if not training_module:
            logger.error(f"No training module found for agent type: {agent_type}")
            return False
        
        # Simulate assessment process
        time.sleep(1.0)  # Comprehensive assessment takes longer
        
        # Calculate scores across different assessment areas
        assessment_areas = [
            'knowledge_comprehension',
            'practical_application',
            'problem_solving',
            'adaptability',
            'cross_domain_understanding'
        ]
        
        total_score = 0
        assessment_scores = {}
        
        for area in assessment_areas:
            # Simulate assessment scoring
            score = random.uniform(0.85, 1.0)
            assessment_scores[area] = score
            total_score += score
            logger.info(f"  - Assessment area '{area}': {score:.2f}")
        
        # Calculate average score
        average_score = total_score / len(assessment_areas)
        logger.info(f"  Assessment complete. Average score: {average_score:.2f}")
        
        # Store assessment results
        self.certification_status[agent_id]['assessment_scores'] = assessment_scores
        self.certification_status[agent_id]['final_score'] = average_score
        
        # Certification requires an average score of at least 0.85 (85%)
        certified = average_score >= 0.85
        return certified
    
    def verify_agent_certification(self, agent_id):
        """
        Verify that an agent is certified to provide IPMDAR expertise.
        
        Args:
            agent_id: Unique identifier for the agent
            
        Returns:
            bool: True if agent is certified, False otherwise
        """
        if agent_id in self.certification_status:
            return self.certification_status[agent_id]['certified']
        return False
    
    def get_certification_details(self, agent_id):
        """
        Get detailed certification information for an agent.
        
        Args:
            agent_id: Unique identifier for the agent
            
        Returns:
            dict: Certification details or None if not found
        """
        return self.certification_status.get(agent_id)
    
    def schedule_refresher_training(self, agent_id, training_date=None):
        """
        Schedule refresher training for an agent to maintain up-to-date expertise.
        
        Args:
            agent_id: Unique identifier for the agent
            training_date: Optional specific date for training, defaults to current time
            
        Returns:
            str: Scheduled training date as ISO format string
        """
        if training_date is None:
            training_date = datetime.now().isoformat()
        
        if agent_id in self.certification_status:
            self.certification_status[agent_id]['refresher_training_scheduled'] = training_date
            self.save_certification_records()
            logger.info(f"Refresher training scheduled for Agent {agent_id} on {training_date}")
            return training_date
        else:
            logger.warning(f"Cannot schedule refresher training for unknown Agent {agent_id}")
            return None
