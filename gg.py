import subprocess
import sys

def install_packages(packages):
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# List of packages to install
packages = ["linear-tree",'xgboost','pandas','matplotlib','feature_engine']

install_packages(packages)
