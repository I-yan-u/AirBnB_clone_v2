#!/usr/bin/python3
""" Fabric file that deploys onto webservers"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['52.6.189.32', '18.206.207.55']
env.user = 'ubuntu'
env.identity = '~/.ssh/school'
env.password = None


def do_deploy(archive_path):
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
    except:
        return False

