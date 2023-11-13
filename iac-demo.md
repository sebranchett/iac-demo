1. Open https://pluto-dev.tud-testing.link in a browser
1. Log in with NetId and wait 2 minutes
1. Open terminal window in JupyterLab
```
export PATH=$PATH:/opt/conda/bin
apt install python3.10-venv

git config --global user.email "you@example.com"
git config --global user.name "Your Name"

mkdir iac-dcc
cd iac-dcc/

cdk init app --language=python

git status  # under version control

source .venv/bin/activate or source .venv/Scripts/activate
pip install -r requirements.txt
```