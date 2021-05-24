import os
import subprocess

def clean():
    try:
        subprocess.call("ipconfig /release")
        subprocess.call("ipconfig /flushdns")
        subprocess.call("ipconfig /renew")
        print("\nSuccess!")
    except:
        print("Error Occured! Please try again!")
          

clean()


