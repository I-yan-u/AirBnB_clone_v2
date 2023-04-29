#!/usr/bin/python3
"""
    Cleans unnecessary archives
    do_clean(number=0)
    number filter the amount of archives to remain
    based on how recent they are.
"""
from fabric.api import *
import os
env.hosts = ['52.6.189.32', '18.206.207.55']
env.user = 'ubuntu'
env.identity = '~/.ssh/school'


def do_clean(number=0):
    """ removes old archive files"""
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]