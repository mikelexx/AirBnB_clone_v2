#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy:
"""
from fabric.api import *
import os

env.user = "ubuntu"
env.hosts = ['54.209.136.208', '54.146.59.67']


def do_deploy(archive_path):
    """
    distributes an archive to your web servers, using the function do_deploy:
    """
    if not os.path.exists(archive_path):
        return False
    arch_file = os.path.basename(archive_path)
    arch_folder = arch_file.replace(".tgz", "")
    dest_folder = "/data/web_static/releases/{}/".format(arch_folder)
    status = False
    try:
        put(archive_path, "/tmp/{}".format(arch_file))
        run("mkdir -p {}".format(dest_folder))
        run("tar -xzf /tmp/{} -C {}".format(arch_file, dest_folder))
        run("rm -rf /tmp/{}".format(arch_file))
        run("mv {}web_static/* {}".format(dest_folder, dest_folder))
        run("rm -rf {}web_static".format(dest_folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(dest_folder))
        print('New version deployed!')
        status = True
    except Exception:
        status = False
    return status
