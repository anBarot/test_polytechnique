#!/usr/bin/env python3
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv

def main():
    load_dotenv('./.env')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_polytechnique.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        print(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()