#!/usr/bin/python3
"""
Fabric local archive packer
"""

from fabric import local
from datetime import datetime
from os.path import isdir

def do_pack():
    """
    Pack the local archive
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir('version') is False:
            local('mkdir version')
        file_name = "version/web_static_{}.tgz".format(date)
        local('tar -cvzf {} web_static'.format(file_name))
        return file_name
    except:
        return None
