#!/usr/bin/python3
"""Creates an archive in a versions folder"""
from datetime import datetime
from fabric.api import local
from shlex import split


def do_pack():
    """Creates an archive file"""
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


do_pack()
