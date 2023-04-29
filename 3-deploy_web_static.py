#!/usr/bin/python3
"""
    Generates a .tgz archive from contents of
    the web_static folder of your AirBnB Clone
    repo, using the function do_pack.

    def do_pack():
    All files must be added to the final archive
    and stored in the folder "versions"

    The name of the archive created must be
    web_static_<year><month><day><hour><minute><second>.tgz

    The function do_pack must return the archive
    path if the archive has been correctly generated.
    Otherwise, it should return None

    def do_deploy():
    Files are transferred to the provided servers
    and unpacked at correct locations
    Returns True on completeion
"""

import datetime
from fabric.api import local, run, put, env
from os.path import isdir, exists
env.hosts = ['52.6.189.32', '18.206.207.55']
env.user = 'ubuntu'
env.identity = '~/.ssh/school'
env.password = None


def do_pack():
    """Compresses the web_static folder into a .tgz archive"""
    try:
        day = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_N = "versions/web_static_{}.tgz".format(day)
        local("tar -czvf {} web_static".format(file_N))
        return file_N
    except FileNotFoundError:
        return None


def do_deploy(archive_path):
    """
        Fabric function to deploy static codes to servers
        archive_path: The path to the tar.gz file to deploy
    """
    if exists(archive_path) is False:
        return False

    try:
        file_N = archive_path.split('/')[-1]
        path = "/data/web_static/releases/"
        link_path = "/data/web_static/current"
        no_ext = file_N.split('.')[0]
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_N, path, no_ext))
        run('rm /tmp/{}'.format(file_N))
        run('mv {0}{1}/web_static/* {0}{1}'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf {}'.format(link_path))
        run('ln -s {}{}/ {}'.format(path, no_ext, link_path))
        run('chmod -R 755 /data/')
        print("New version deployed!")
        return True
    except FileNotFoundError:
        return False


def deploy():
    """
        Function calls do_pack() and do_deploy()
        Returns value for do_deploy()
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
