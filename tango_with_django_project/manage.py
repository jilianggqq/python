#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import logging
logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tango_with_django_project.settings")

    from django.core.management import execute_from_command_line

    # test the parameter
    logging.debug("the parameter is {0}".format(sys.argv))
    execute_from_command_line(sys.argv)
