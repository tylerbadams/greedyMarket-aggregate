import git
import os
import json


with open('config/deployment.json') as deployConf:
  deployConf = json.load(deployConf)
print deployConf

repo = git.Repo(os.getcwd())
repo.remotes['greedyMarket-aggregate'].fetch( verbose = True )

commits_behind = repo.iter_commits('HEAD..greedyMarket-aggregate/{0}'.format(deployConf['branch']))

repo.git.checkout('remotes/origin/{0}'.format(deployConf['branch']))

