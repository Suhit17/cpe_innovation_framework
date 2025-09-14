"""Basic usage example for CPE Innovation Framework"""
import sys
import os

# Add src to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import CPEInnovationFramework
from dotenv import load_dotenv

def main():
    """Run basic framework example with full analysis"""
    
    print("CPE Innovation Framework - Full Analysis Test")
    print("=" * 50)
    
    try:
        # Load environment variables
        load_dotenv()
        
        # Initialize framework
        framework = CPEInnovationFramework()
        print("Framework initialized successfully")
        
        # Display system status
        status = framework.get_system_status()
        print("\nInitial System Status:")
        for key, value in status.items():
            print(f"  {key}: {value}")
        
        # Sample input data
        sample_data = {
            "network_config": "Enterprise CPE network with 50 devices - Cisco routers, Juniper switches, Arista APs",
            "sensor_data": "Temperature: 18-45C, CPU: 25-85%, Memory: 40-90%, vibration normal", 
            "service_specs": "Deploy security monitoring service v3.2 with threat detection",
            "community_contributions": "New mesh optimization algorithm, enhanced NAPALM drivers",
            "analysis_type": "comprehensive_ecosystem_analysis"
        }
        
        print(f"\nSample data prepared for analysis")
        
        # Run the full analysis
        print("\nStarting full analysis with all 5 agents...")
        print("This may take 2-3 minutes as agents process data...")
        
        result = framework.run_analysis(sample_data)
        
        if result:
            print("\n" + "="*50)
            print("ANALYSIS COMPLETED SUCCESSFULLY!")
            print("="*50)
            
            # Check final status
            final_status = framework.get_system_status()
            print(f"\nFinal System Status:")
            for key, value in final_status.items():
                print(f"  {key}: {value}")
            
            print(f"\nAll 5 agents have been created and executed their tasks!")
            print(f"Your CPE Innovation Framework is fully operational!")
        else:
            print("Analysis completed but returned no result")
        
    except Exception as e:
        print(f"Error: {e}")
        print("Check your OpenAI API key and network connection")

if __name__ == "__main__":
    main()