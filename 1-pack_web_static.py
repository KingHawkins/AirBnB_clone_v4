#!/usr/bin/python3
"""Creates an archive in a versions folder"""
from datetime import datetime
from fabric.api import local
from shlex import split


def do_pack():
    """Inside the fabric.api package.
    The library enables one to interact with the shell using python\
            One can be able to run shell commands remotely using\
            the `run` command and locally using the `local` command.
            Datetime library is used to get the time by which will be\
            used to get the archive filename.
            Shlex is used as a helper function to get the archive filename.
    """
    try:
        """Under surveillance\
                might fail"""
        result = split(str(datetime.now()))
        (yr, mon, day) = result[0].split('-')
        (hr, mn, sec) = result[1].split('.')[0].split(':')
        file = f'web_static_{yr}{mon}{day}{hr}{mn}{sec}.tgz'
        local('mkdir -p versions')
        local(f'tar -czf versions/{file} web_static')
        return 'versions/' + file
    except Exception:
        return None
