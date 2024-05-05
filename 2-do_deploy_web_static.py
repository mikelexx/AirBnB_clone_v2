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
    temp = archive_path.split(".tgz")
    arch_file_path = "".join(temp)
    b_list = arch_file_path.split("versions/")
    arch_file = "".join(b_list)
    c_list = archive_path.split("versions/")
    archive_wo_ver = "".join(c_list)
    if archive_path:
        put(archive_path, '/tmp/')
        run("mkdir -p /data/web_static/releases/{}/".
            format(arch_file))
        run("tar -zxf /tmp/{} -C /data/web_static/releases/{}/"
            .format(archive_wo_ver, arch_file))
        run("rm -r /tmp/{}".format(archive_wo_ver))
        run("mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}/".format(arch_file,
                                              arch_file))
        run("rm -rf /data/web_static/releases/{}/web_static".
            format(arch_file))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
            format(arch_file))
        print("New version deployed!")
        return True
    else:
        return False
