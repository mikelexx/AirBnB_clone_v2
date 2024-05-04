#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
def do_pack():
    """
    this function performs the above stated requirements
    """
    local("mkdir -p versions")
    arch_path = ("versions/web_static_{}.tgz"
            .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    result = local("tar -cvzf {} web_static"
                   .format(arch_path))

    if result.failed:
        return None
    return arch_path
