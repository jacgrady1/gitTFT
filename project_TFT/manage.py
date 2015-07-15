#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_TFT.settings")

    from django.core.management import execute_from_command_line
    
    sys.dont_write_bytecode = True
    
    execute_from_command_line(sys.argv)
