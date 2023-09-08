#!/usr/bin/python3
"""A module for web application deployment with Fabric."""
import os
from datetime import datetime
from fabric.api import run, env, put, local, runs_once

env.hosts = ['54.144.128.232', '18.204.20.190']

@runs_once
def do_pack():
    """Archives the static files."""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    cur_time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        cur_time.year,
        cur_time.month,
        cur_time.day,
        cur_time.hour,
        cur_time.minute,
        cur_time.second
    )
    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        archize_size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, archize_size))
    except Exception:
        output = None
    return output


def do_deploy(archive_path):
    """Deploys the static files to the host servers."""

    if os.path.exists(archive_path) is False:
        return False
    filename = archive_path.split('/')[1]
    filepath = f"/data/web_static/releases/{filename.replace('.tgz', '')}"
    put(archive_path, f"/tmp/{filename}")
    run(f"mkdir -p {filepath}")
    run(f"tar -xzf /tmp/{filename} -C {filepath}/")
    run(f"mv {filepath}/web_static/* {filepath}/")
    run(f"rm -rf {filepath}/web_static")
    run(f"rm -rf /data/web_static/current")
    run(f"ln -s {filepath}/ /data/web_static/current")
    print('New version deployed!')
