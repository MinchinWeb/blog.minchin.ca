from invoke import run, task
from pathlib import Path

# from fabric.api import *
# import fabric.contrib.project as project
# import os

# Local path configuration (can be absolute or relative to fabfile)
#env.deploy_path = '../minchinweb.github.io-master'
#DEPLOY_PATH = env.deploy_path

# Remote server configuration
#production = 'root@localhost:22'
#dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
#env.cloudfiles_username = 'my_rackspace_username'
#env.cloudfiles_api_key = 'my_rackspace_api_key'
#env.cloudfiles_container = 'my_cloudfiles_container'

p = Path.cwd()
deploy_path = p.parents[0] / 'blog.minchin.ca-master'


def clean(ctx):
    print("You'll have to manually delete the output folder")
    #if os.path.isdir(DEPLOY_PATH):
    #    local('rm -rf {deploy_path}'.format(**env))
    #    local('mkdir {deploy_path}'.format(**env))


@task
def build(ctx):
    ctx.run('pelican -s pelicanconf.py', shell="C:\Windows\system32\cmd.EXE")


@task
def rebuild(ctx):
    clean(ctx)
    build(ctx)


@task
def regenerate(ctx):
    ctx.run('start pelican -r -s pelicanconf.py', shell="C:\Windows\system32\cmd.EXE")


@task
def serve(ctx):
    # local('cd {deploy_path} && start python -m SimpleHTTPServer'.format(**env))
    # in Python3000, use  python -m http.server
    ctx.run('cd {} && start python -m http.server'.format(deploy_path), shell="C:\Windows\system32\cmd.EXE")


@task
def serve_on(ctx, port):
    # local('cd {deploy_path} && start python -m SimpleHTTPServer'.format(**env))
    # in Python3000, use  python -m http.server
    ctx.run('cd {} && start python -m http.server {}'.format(deploy_path, port), shell="C:\Windows\system32\cmd.EXE")

@task
def reserve(ctx):
    build(ctx)
    serve(ctx)


@task
def preview(ctx):
    ctx.run('pelican -s publishconf.py', shell="C:\Windows\system32\cmd.EXE")


@task
def upload(ctx):
    publish(ctx)
    ctx.run('cd {deploy_path}', shell="C:\Windows\system32\cmd.EXE")
    ctx.run('git add -A', shell="C:\Windows\system32\cmd.EXE")
    ctx.run('git commit', shell="C:\Windows\system32\cmd.EXE")
    ctx.run('git push', shell="C:\Windows\system32\cmd.EXE")


@task
def publish(ctx):
    ctx.run('pelican -s publishconf.py', shell="C:\Windows\system32\cmd.EXE")


# Add devsever
# only works on Windows
#  need to kill the second window manually
@task
def devserver(ctx):
    regenerate(ctx)
    serve(ctx)

@task
def less(ctx):
    #run('lessc theme\\burst-energy\\less\\bootstrap.burst-energy.less > ' +
    #    env_deploy_path + '\\css\\style.css')
    #   lessc themes\pelican-minchin-ca\static\less\bootstrap.minchin-ca.min.less > themes\pelican-minchin-ca\static\css\bootstrap.minchin-ca.min.css
    source = p / '..' / 'minchinweb.github.io-pelican/themes\pelican-minchin-ca\static\less\\bootstrap.minchin-ca.min.less'
    dest = p / '..' / 'minchinweb.github.io-pelican/themes\pelican-minchin-ca\static\css\\bootstrap.minchin-ca.min.css'
    ctx.run('lessc {} > {}'.format(source, dest), shell="C:\Windows\system32\cmd.EXE")

@task
def test(ctx):
    #print(ctx)
    print(run)
    ctx.run('dir', shell="C:\Windows\system32\cmd.EXE")
    #run('dir', shell="C:\Windows\system32\cmd.EXE")
