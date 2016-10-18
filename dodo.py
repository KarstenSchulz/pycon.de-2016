"""
doit file to compile slides and pdf for „pro:dfl Gewinnspiele Online“
"""
import os
import re
import subprocess
import time
from glob import glob
from pathlib import Path
from shutil import copyfile, copytree
from subprocess import check_call

# noinspection PyPackageRequirements
from fabric.colors import red

DOIT_CONFIG = {
    # 'verbosity': 2,
    # 'num_process': 2,
}


def get_file_deps():
    """
    Return list of all sourcefiles, which should trigger a build, when changed.
    """
    file_list = list()
    suffixes = ['.css', '.html', '.jpg', '.js', '.pdf', '.png', '.puml', '.py', '.rst']
    for dirpath, dirnames, filenames in os.walk('.'):
        for f in filenames:
            if os.path.splitext(f)[1] in suffixes:
                file_list.append(os.path.join(dirpath, f))
    return file_list


global_conf = {
    'outformat': 'slides',
    'builddir': '_build',
    'srcdir': ".",
    'sphinx_options': "-W",
    'src_files': glob('*.rst') + glob('**/*.rst') + glob('**/*.puml'),
    'presentation_user_dir': '/Users/presentation/Public/Drop Box/',
    'lshs_volume': '/Volumes/karsten/Dokumente/dfl/',
}


def compile_doc(local_conf=None, **kwargs):
    """
    Create command string for compiling slide docs with sphinx.

    :param local_conf: config of this run. If not given, use global_config.
    :param kwargs: set a particular arguments to the config, like 'srcdir'
    :return: the command string to execute
    :raise: CalledProcessError if build fails
    """
    if local_conf is not None:
        conf = local_conf
    else:
        conf = global_conf
    if len(kwargs) > 0:
        conf.update(kwargs)
    cmd = [
        'sphinx-build',
        '{sphinx_options}'.format(**conf),
        '-b',
        '{outformat}'.format(**conf),
        '{srcdir}'.format(**conf),
        '{builddir}/{outformat}'.format(**conf)
    ]
    check_call(cmd)
    return True


def compile_slides():
    """
    Func to call compile_doc to make doit happy.
    """
    conf = global_conf
    conf['outformat'] = 'slides'
    compile_doc(conf)


def compile_pdf():
    """
    Func to call compile_doc to make doit happy.
    """
    conf = global_conf
    conf['outformat'] = 'latex'
    compile_doc(conf)


def list_urls():
    """
    List all urls in project
    :return: sorted list of urls
    """
    url_list = []
    for file in global_conf['src_files']:
        with open(file) as f:
            url_list.extend(re.findall(r'(https?://\S+)', f.read()))
    return sorted(url_list)


def task_slides():
    """
    Compile slides to html.
    """
    conf = global_conf
    conf['outformat'] = 'slides'
    target_file = os.path.join(conf['builddir'], conf['outformat'], 'index.html')
    return {
        'actions': [compile_slides],
        'file_dep': get_file_deps(),
        'targets': [target_file],
        'clean': True,
    }


def task_pdf():
    """
    Compile slides to pdf handout.
    """
    conf = global_conf
    conf['outformat'] = 'latex'
    target_file = os.path.join(conf['builddir'], conf['outformat'], 'eu-dsgvo.pdf')
    return {
        'actions': [compile_pdf, 'make -C {builddir}/{outformat} all-pdf'.format(**conf)],
        'file_dep': get_file_deps(),
        'targets': [target_file],
        'clean': True,
    }

