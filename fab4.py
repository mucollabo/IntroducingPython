from fabric.api import run
from fabric.context_managers import env

env.password = "0901"

def iso():
    run('date -u')