#!/usr/bin/python3
"""A module for web application deployment with Fabric."""
import os
from datetime import datetime
from fabric.api import run, env, put, local, runs_once

env.hosts = ['54.144.128.232', '18.204.20.190']
def do_deploy(archive_path):
    """Deploys the static files to the host servers."""

    if os.path.exists(archive_path) is False:
        return False
    filename = archive_path.split('/')[1]
    remote_filepath = f"/data/web_static/releases/{filename.replace('.tgz', '')}/"
    put(archive_path, f"/tmp/{filename}")
    run(f"mkdir -p {remote_filepath}")
    run(f"tar -xzf /tmp/{filename} -C {remote_filepath}")
    run(f"mv {remote_filepath}/web_static/* {remote_filepath}")
    run(f"rm -rf {remote_filepath}/web_static")
    run(f"rm -rf /data/web_static/current")
    run(f"ln -s {remote_filepath} /data/web_static/current")
