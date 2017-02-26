apt-get install -y python-pip
apt-get install -y mongodb

pip install gitpython


git init
git remote add greedyMarket-aggregate https://github.com/tylerbadams/greedyMarket-aggregate.git
git fetch greedyMarket-aggregate
git checkout -f greedyMarket-aggregate/master

echo "0 0 */1 * * ${PWD}/deploy.py" | tee -a /var/spool/cron/root

sudo service mongod start
python deploy.py
