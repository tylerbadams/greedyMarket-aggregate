import git
import os
import json


with open('config/deployment.json') as deployConf:
  deployConf = json.load(deployConf)
print deployConf

repo = git.Repo(os.getcwd())
repo.remotes['greedyMarket-aggregate'].fetch( verbose = True )

commits_behind = repo.iter_commits('HEAD..origin/{0}'.format(deployConf['branch']))

if len([1 for c in commits_behind]) > 0:
  repo.git.checkout('remotes/origin/{0}'.format(deployConf['branch']))
  print 'updated on {0}'.format(deployConf['branch'])
