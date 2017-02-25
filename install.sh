apt-get install python-pip
pip install gitpython

git init
git remote add greedyMarket-aggregate https://github.com/tylerbadams/greedyMarket-aggregate.git
git fetch greedyMarket-aggregate
git checkout -f greedyMarket-aggregate/master

if ! grep -Fxq "0 0 */1 * * ${PWD}/deploy.py" /var/spool/cront/root; then
   echo "0 0 */1 * * ${PWD}/deploy.py" | tee -a /var/spool/cron/root

python deploy.py
