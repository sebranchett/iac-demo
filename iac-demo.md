1. Open https://pluto-dev.tud-testing.link in a browser
1. Log in with NetId and wait 2 minutes
1. Open terminal window in JupyterLab
```
git config --global user.email "you@example.com"
git config --global user.name "Your Name"

mkdir iac-dcc
cd iac-dcc/

cdk init app --language=python

git status  # under version control

source .venv/bin/activate  # start virtual environment
pip install -r requirements.txt

cdk synth
```
1. In environment with account
```
aws ec2 describe-key-pairs --query KeyPairs[*].KeyPairId --output text

aws ssm get-parameter --name /ec2/keypair/key-???:1 --with-decryption --query Parameter.Value --output text > dcc-key-pair.pem

aws ec2 describe-instances --output text | grep compute  # gives ec2-3-68-216-65.eu-central-1.compute.amazonaws.com

ssh -i "dcc-key-pair.pem" ec2-user@ec2-???.eu-central-1.compute.amazonaws.com
```
