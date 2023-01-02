#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init, after


use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")


name = "most_active_cookie"
default_task = "publish"

executable_dir = "build/"

executable = [name]

def install_dependencies(project):
    project.build_depends_on('pyinstaller')

@init
def set_properties(project):
    project.set_property("dir_source_main_python", "src/main")
    project.set_property("dir_source_unittest_python", "src/unittest")
    project.set_property("dir_source_main_scripts", "src/scripts")

@after("publish")
def publish(project, logger):
    import os

    # Creating the executable file
    from PyInstaller.__main__ import run
    os.chdir('src/main')
    run(['--name=%s' % project.name, '--onefile', '--clean', '--distpath=../../', 'most_active_cookie.py'])