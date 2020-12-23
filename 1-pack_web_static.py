#!/usr/bin/python3
"""Compress before sending."""
from fabric.api import *
import datetime
from os import path


def do_pack():
    """Generates a .tgz archive."""
    _datetime_ = datetime.now().strftime("%Y%m%d%H%M%S")
    _path_ = "versions/web_static_" + _datetime_ + ".tgz"

    if path.exists("versions") is False:
        run("mkdir versions")
    local("tar -zcvf {} web_static".format(_path_))
    return _path_
    else:
        return None
