#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy:
"""
from datetime import datetime
from fabric.api import *
import os

env.hosts = ['54.209.136.208', '54.146.59.67']


def do_deploy(archive_path):
    """
    distributes an archive to your web servers, using the function do_deploy:
    """
    if archive_path:
        try:
            put(archive_path, '/tmp/')
            with cd('/tmp'):
                parent_path, filename = os.path.split(archive_path)
                dest_folder = "/data/web_static/releases/{}".format(
                    filename.split(".tgz")[0])
                run("tar -xzcf -C {} {}").format(archive_path, dest_folder)
                run("rm {}".format(archive_path))
                run("rm -rf /data/web_static/current")
                run("ln -s {} /data/web_static/current".format(dest_folder))
            return True
        except Exception as e:
            print("Erros occured: ", e)
            return False
    else:
        return False
