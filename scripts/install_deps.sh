#Installing dependecies in virtual enviroment
sudo apt-get update
sudo apt-get install git python3
mkdir ${PWD}/dependencies && cd ${PWD}/dependencies
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip
python3 -m pip install virtualenv
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
deactivate
