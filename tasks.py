import time
from pathlib import Path

from invoke import run, task

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
deploy_path = p.parents[0] / 'blog.minchin.ca-temp'  # used for local testing
# used for the version to be put on the wider internet
publish_path = p.parents[0] / 'blog.minchin.ca-master'


def clean(ctx):
    print("You'll have to manually delete the output folder")
    #if os.path.isdir(DEPLOY_PATH):
    #    local('rm -rf {deploy_path}'.format(**env))
    #    local('mkdir {deploy_path}'.format(**env))


@task
def build(ctx):
    """Build a local version of the blog."""
    ctx.run('pelican -s pelicanconf.py')


@task
def build_debug(ctx):
    """Use debug output to build a local version of the blog."""
    ctx.run('pelican -s pelicanconf.py --debug')


@task
def rebuild(ctx):
    """clean and build."""
    clean(ctx)
    build(ctx)


@task
def regenerate(ctx):
    """Rebuild a local version of the blog if files change."""
    ctx.run('start pelican -r -s pelicanconf.py')


@task
def serve(ctx):
    """Serve the local blog output on port 8000."""
    ctx.run('cd {} && start python -m http.server'.format(deploy_path))


@task
def serve_on(ctx, port):
    """Serve the local blog output on a port of your choosing."""
    ctx.run('cd {} && start python -m http.server {}'.format(deploy_path, port))

@task
def reserve(ctx):
    """build and serve."""
    build(ctx)
    serve(ctx)


@task
def upload(ctx):
    """publish and then push the result to GitHub."""
    publish(ctx)
    ctx.run('cd {} && git add -A && git commit -m "[Generated] {}" && git push'\
            .format(publish_path, time.strftime("%Y-%m-%d")))


@task
def publish(ctx):
    """Build a publication version of the blog."""
    ctx.run('pelican -s publishconf.py')


@task
def publish_carefully(ctx):
    """(Carefully) Build a publication version of the blog.

    i.e. fail on any warnings from pelican."""
    ctx.run('pelican -s publishconf.py --fatal=warnings')


# Add devsever
# only works on Windows
#  need to kill the second window manually
@task
def devserver(ctx):
    """regneration and serve."""
    regenerate(ctx)
    serve(ctx)


@task
def test(ctx):
    """Test invoke is working."""
    #print(ctx)
    print(run)
    ctx.run('dir')
    #run('dir', shell=INVOKE_SHELL)
