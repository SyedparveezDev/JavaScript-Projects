#!/usr/bin/env python3
"""
Development management script for the IPO Django application.
This script provides easy commands for development tasks.
"""

import os
import sys
import subprocess
from pathlib import Path

def print_banner():
    """Print application banner."""
    print("=" * 60)
    print("🚀 IPO Web Application - Development Manager")
    print("=" * 60)

def check_django_installed():
    """Check if Django is installed."""
    try:
        import django
        return True, django.get_version()
    except ImportError:
        return False, None

def run_command(command, description=""):
    """Run a shell command with description."""
    if description:
        print(f"\n📋 {description}")
    print(f"💻 Running: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        if e.stderr:
            print(f"Error details: {e.stderr}")
        return False

def install_dependencies():
    """Install Python dependencies."""
    print("\n🔧 Installing Dependencies...")
    commands = [
        ("pip install -r requirements.txt", "Installing Python packages"),
    ]
    
    for command, desc in commands:
        if not run_command(command, desc):
            print("❌ Failed to install dependencies")
            return False
    
    print("✅ Dependencies installed successfully!")
    return True

def setup_database():
    """Set up the database."""
    django_installed, version = check_django_installed()
    if not django_installed:
        print("❌ Django is not installed. Please run 'install' first.")
        return False
    
    print(f"\n🗄️  Setting up database (Django {version})...")
    commands = [
        ("python manage.py makemigrations", "Creating migrations"),
        ("python manage.py migrate", "Applying migrations"),
    ]
    
    for command, desc in commands:
        if not run_command(command, desc):
            print("❌ Failed to setup database")
            return False
    
    print("✅ Database setup completed!")
    return True

def create_superuser():
    """Create Django superuser."""
    django_installed, _ = check_django_installed()
    if not django_installed:
        print("❌ Django is not installed. Please run 'install' first.")
        return False
    
    print("\n👤 Creating superuser...")
    print("💡 You'll be prompted for username, email, and password")
    
    try:
        subprocess.run("python manage.py createsuperuser", shell=True, check=True)
        print("✅ Superuser created successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to create superuser")
        return False

def load_sample_data():
    """Load sample IPO data."""
    django_installed, _ = check_django_installed()
    if not django_installed:
        print("❌ Django is not installed. Please run 'install' first.")
        return False
    
    if not Path("sample_data.json").exists():
        print("❌ Sample data file not found")
        return False
    
    return run_command("python manage.py loaddata sample_data.json", "Loading sample IPO data")

def run_tests():
    """Run the test suite."""
    django_installed, _ = check_django_installed()
    if not django_installed:
        print("❌ Django is not installed. Please run 'install' first.")
        return False
    
    return run_command("python manage.py test", "Running test suite")

def run_django_server():
    """Run Django development server."""
    django_installed, version = check_django_installed()
    if not django_installed:
        print("❌ Django is not installed. Please run 'install' first.")
        return False
    
    print(f"\n🚀 Starting Django development server (Django {version})...")
    print("📝 Access the application at: http://localhost:8000")
    print("🔧 Access admin panel at: http://localhost:8000/admin/")
    print("📡 Access API at: http://localhost:8000/api/")
    print("⚠️  Press Ctrl+C to stop the server")
    
    try:
        subprocess.run("python manage.py runserver", shell=True, check=True)
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to start server: {e}")

def run_simple_server():
    """Run simple development server."""
    print("\n🚀 Starting simple development server...")
    print("📝 Access the application at: http://localhost:8000")
    print("⚠️  This is a basic server. Install Django for full functionality.")
    print("⚠️  Press Ctrl+C to stop the server")
    
    try:
        subprocess.run("python3 simple_server.py", shell=True, check=True)
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to start server: {e}")

def show_status():
    """Show current project status."""
    print("\n📊 Project Status:")
    print("-" * 40)
    
    # Check Django installation
    django_installed, version = check_django_installed()
    if django_installed:
        print(f"✅ Django: {version}")
    else:
        print("❌ Django: Not installed")
    
    # Check required files
    files_to_check = [
        ("manage.py", "Django management script"),
        ("requirements.txt", "Dependencies file"),
        ("ipo_project/settings.py", "Django settings"),
        ("ipo_app/models.py", "IPO models"),
        ("templates/base.html", "Base template"),
    ]
    
    for file_path, description in files_to_check:
        if Path(file_path).exists():
            print(f"✅ {description}")
        else:
            print(f"❌ {description}")
    
    print("\n📋 Available Commands:")
    print("  install     - Install dependencies")
    print("  setup       - Setup database")
    print("  superuser   - Create admin user")
    print("  sample      - Load sample data")
    print("  test        - Run tests")
    print("  runserver   - Start Django server")
    print("  simple      - Start simple server")
    print("  status      - Show this status")

def main():
    """Main function to handle commands."""
    print_banner()
    
    if len(sys.argv) < 2:
        show_status()
        return
    
    command = sys.argv[1].lower()
    
    if command == "install":
        install_dependencies()
    elif command == "setup":
        setup_database()
    elif command == "superuser":
        create_superuser()
    elif command == "sample":
        load_sample_data()
    elif command == "test":
        run_tests()
    elif command == "runserver":
        run_django_server()
    elif command == "simple":
        run_simple_server()
    elif command == "status":
        show_status()
    elif command == "full-setup":
        print("🚀 Running full setup...")
        if (install_dependencies() and 
            setup_database() and 
            load_sample_data()):
            print("\n🎉 Full setup completed successfully!")
            print("💡 Run 'python dev.py superuser' to create an admin user")
            print("💡 Run 'python dev.py runserver' to start the Django server")
        else:
            print("❌ Setup failed. Please check the errors above.")
    else:
        print(f"❌ Unknown command: {command}")
        show_status()

if __name__ == "__main__":
    main()
