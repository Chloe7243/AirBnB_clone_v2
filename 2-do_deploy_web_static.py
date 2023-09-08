#!/usr/bin/python3
"""A module for web application deployment with Fabric."""
import os
from datetime import datetime
from fabric.api import run, env, put, local

env.hosts = ['54.144.128.232', '18.204.20.190']


def do_deploy(archive_path):
    """Deploys the static files to the host servers."""

    if os.path.exists(archive_path) is False:
        return False
    filename = archive_path.split('/')[1]
    filepath = f"/data/web_static/releases/{filename.replace('.tgz', '')}/"
    try:
        put(archive_path, f"/tmp/{filename}")
        run(f"mkdir -p {filepath}")
        run(f"tar -xzf /tmp/{filename} -C {filepath}")
        run(f"rm /tmp/{filename}")
        run(f"mv {filepath}web_static/* {filepath}")
        run(f"rm -rf {filepath}web_static")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s {filepath} /data/web_static/current")
        print('New version deployed!')
        success = True
    except Exception:
        success = False
    return success
