#!/usr/bin/env python
import os
import sys
#import unittest

#from pretec.ext.script import Manager

# @manager.command
# def test():
#     """Corre los tests sin coverage"""
#     tests=unittest.TestLoader().discover('.')
#     unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pretec.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
