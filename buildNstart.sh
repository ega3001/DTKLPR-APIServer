sudo apt-get update
sudo apt-get install supervisor
sudo systemctl enable supervisor --now
sh scripts/install_deps.sh
cp supervisor.cfg /etc/supervisor/conf.d/api-rest-car-number.cfg
supervisorctl reload
