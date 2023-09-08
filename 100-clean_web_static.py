#!/usr/bin/python3
"""A module for web application deployment with Fabric."""
import os
from datetime import datetime
from fabric.api import run, env, put, local

env.hosts = ['54.144.128.232', '18.204.20.190']


def do_clean(number=0):
    """Deletes files from directory"""

    archives = os.listdir('versions/')
    archives.sort(reverse=True)
    try:
        for archive in archives[int(number):]:
            local(f"rm versions/{archive}")
            run(f"rm /data/web_static/releases/{archive}")
        success = True
    except Exception:
        success = False
    return success
