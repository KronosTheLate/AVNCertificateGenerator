#!/usr/bin/env python3
import os, sys, subprocess, platform

# helper to run commands
run = subprocess.check_call

def main():
    root = os.path.dirname(os.path.abspath(__file__))
    venv = os.path.join(root, "venv")
    
    if not os.path.isdir(venv):
        print(f"Creating new virtual environment {venv}...")
        run([sys.executable, "-m", "venv", venv])
    else:
        print(f"Using existing virtual environment {venv}")

    # locate python and pip in venv
    bin_folder = "Scripts"
    py = os.path.join(venv, bin_folder, "python")
    pip = os.path.join(venv, bin_folder, "pip")

    # upgrade pip: if want to. maybe not.
    # print("upgrading pip...")
    # try:
    #     run([pip, "install", "--upgrade", "pip"])
    # except subprocess.CalledProcessError:
    #     run([pip, "install", "--user", "--upgrade", "pip"])

    # install dependencies
    req = os.path.join(root, "requirements.txt")
    if os.path.isfile(req):
        print("installing deps...")
        try:
            run([pip, "install", "-r", req])
        except subprocess.CalledProcessError:
            print("warn: some deps failed")
    
    
    run([py, "main.py"])
            
if __name__ == "__main__":
    main()
