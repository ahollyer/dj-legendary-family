from fabric.api import run, env, sudo, cd, prefix

env.hosts = ['45.32.162.25']
env.user = 'aspen'

DIR = '/home/aspen/dj-legendary-family'
VENV = 'source /home/aspen/.virtualenvs/legendary/bin/activate && source SECRETS.ENV'

def start ():
  with cd(DIR):
    with prefix(VENV):
      run('pm2 start uwsgi -- --ini uwsgi.ini > start.log')

def stop ():
  run('pm2 stop all > stop.log')

def deploy ():
  with cd(DIR):
    run('git pull')

    with prefix(VENV):
      run('pip install -r requirements.txt  > install.log')
      run('python manage.py migrate')

    run('pm2 restart all > restart.log')

# Test if correctly installed
def hello ():
  print("Hello")
