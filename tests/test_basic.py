"""Basic tests for CPE Innovation Framework"""
import unittest
import sys
import os

# Add src to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import CPEInnovationFramework
from dotenv import load_dotenv

class TestCPEFramework(unittest.TestCase):
    """Basic test cases for the framework"""
    
    def setUp(self):
        """Set up test environment"""
        load_dotenv()
        if os.getenv("OPENAI_API_KEY"):
            self.framework = CPEInnovationFramework()
        else:
            self.skipTest("OpenAI API key not configured")
    
    def test_framework_initialization(self):
        """Test that framework initializes correctly"""
        self.assertIsNotNone(self.framework)
        self.assertIsNotNone(self.framework.llm)
    
    def test_system_status(self):
        """Test system status reporting"""
        status = self.framework.get_system_status()
        self.assertIn('framework_status', status)
        self.assertEqual(status['framework_status'], 'Active')
    
    def test_agent_setup(self):
        """Test agent creation"""
        self.framework.setup_agents()
        expected_agents = [
            'network_optimizer',
            'maintenance_engineer',
            'deployment_orchestrator', 
            'knowledge_curator',
            'ecosystem_coordinator'
        ]
        for agent_name in expected_agents:
            self.assertIn(agent_name, self.framework.agents)

if __name__ == '__main__':
    unittest.main()