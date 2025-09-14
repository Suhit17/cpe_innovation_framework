#!/usr/bin/env python3
"""
Setup test script for CPE Innovation Framework
Run this to verify your environment is correctly configured
"""

import os
import sys
from pathlib import Path

def test_environment():
    """Test the development environment setup"""
    
    print("CPE Innovation Framework - Environment Test")
    print("=" * 50)
    
    # Test Python version
    python_version = sys.version_info
    print(f"Python Version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        print("❌ Python 3.8+ required")
        return False
    else:
        print("✅ Python version OK")
    
    # Test virtual environment
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Virtual environment activated")
    else:
        print("⚠️  Virtual environment not detected (recommended but not required)")
    
    # Load environment variables
    try:
        from dotenv import load_dotenv
        load_dotenv()
        print("✅ dotenv loaded successfully")
    except ImportError:
        print("❌ python-dotenv not installed - run: pip install python-dotenv")
        return False
    
    # Test OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key and api_key != "your_openai_api_key_here":
        print("✅ OpenAI API key configured")
    else:
        print("❌ OpenAI API key not set - edit your .env file")
        return False
    
    # Test required imports
    required_packages = [
        ('crewai', 'CrewAI'),
        ('langchain', 'LangChain'),
        ('langchain_openai', 'LangChain OpenAI'),
        ('pandas', 'Pandas'),
        ('numpy', 'NumPy'),
        ('sklearn', 'Scikit-learn')
    ]
    
    missing_packages = []
    
    for package, name in required_packages:
        try:
            __import__(package)
            print(f"✅ {name} imported successfully")
        except ImportError:
            print(f"❌ {name} import failed")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\nMissing packages: {', '.join(missing_packages)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    print("\n" + "=" * 50)
    print("Environment test completed!")
    
    # Test basic framework initialization
    print("\nTesting framework initialization...")
    try:
        sys.path.append('src')
        from main import CPEInnovationFramework
        
        framework = CPEInnovationFramework()
        status = framework.get_system_status()
        
        print("✅ Framework initialized successfully")
        print(f"   Agents: {status['agents_count']}")
        print(f"   Tasks: {status['tasks_count']}")
        print(f"   Status: {status['framework_status']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Framework initialization failed: {e}")
        return False

def main():
    """Main test function"""
    success = test_environment()
    
    if success:
        print("\n🎉 Setup successful! You're ready to use the CPE Innovation Framework.")
        print("\nNext steps:")
        print("1. Run: python src/main.py")
        print("2. Check the documentation in docs/")
        print("3. Try the examples in examples/")
    else:
        print("\n❌ Setup incomplete. Please fix the issues above.")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())