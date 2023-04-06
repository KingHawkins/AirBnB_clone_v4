#!/usr/bin/python3
"""deletes out of date archives"""
import os
from fabric.api import *

env.hosts = ['100.24.235.35', '100.26.158.195']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def local_clean(rng=0):
    """Cleans the archive files in the local machine\
            this is a helper function"""
    try:
        discard = ''
        check_no = local("ls -ltr versions/ | grep 'web_static' | wc -l")
        array = local("""ls -ltr versions | grep 'web_static'\
                      | awk '{print $9}'""", capture=True).split('\n')
        if rng == 0 or rng == 1:
            discard = array[:-1]
            for item in discard:
                item = 'versions/' + item
                os.remove(item)
            print(discard)
        else:
            discard = array[:-rng]
            for item in discard:
                item = 'versions/' + item
                os.remove(item)
            print(discard)
    except Exception:
        return False


def do_clean(number=0):
    """Cleans the archive files in the web servers\
            this is the main function"""
    try:
        discard = ''
        local_clean(number)
        check_no = run("""ls -ltr /data/web_static/releases/ \
                       | grep 'web_static' | wc -l """)
        array = run("""ls -ltr /data/web_static/releases \
                    | grep 'web_static' | awk '{ print $9 }'""")\
            .replace('\r', '').split('\n')
        if number == 0 or number == 1:
            discard = array[:-1]
            for item in discard:
                item = '/data/web_static/releases/' + item
                run(f'rm -rfv {item}')
                print(item)

            print(discard)
        else:
            discard = array[:-number]
            for item in discard:
                item = '/data/web_static/releases/' + item
                run(f'rm -rfv {item}')
                print(item)
            print(discard)
    except Exception:
        return False
