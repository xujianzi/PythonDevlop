# -*- coding: utf-8 -*-

__author__ = "Jian"

## This module serves to upgrade all the outdated module

import pip
from subprocess import call
from pip._internal.utils.misc import get_installed_distributions

def update_allpack():
    """
    Code below will require you to confirm updating action for each module
    pip-review --local --interactive 
    """
    for dist in get_installed_distributions():
        call("pip install --upgrade " + dist.project_name, shell = True)

def update_pack(packname):
    call("pip install --upgrade " + packname)

def update_pip():
    """
    TO update the pip module
    """
    call("python -m pip install --upgrade pip")

def install_pack(packname):
    call("pip install "+packname)

def update_pack_custom(packname, version_num):
    call("pip install "+ packname + "==" + version_num)

def list_pack():
    call("pip list")

def list_outdatedpack():
    call("pip list --outdated")

def delete_pack(packname):
    """
    failed! require interactive action in output
    """
    call("pip uninstall " + packname)



