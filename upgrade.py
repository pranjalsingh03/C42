import subprocess
import time
try:
    print("[❅] Update process start.")
    git4 = subprocess.check_output('git pull')
    if 'Already up to date.' in str(git4):
        print("[❅] Project is at latest version.")
    else:
        print("[❅] Downloading latest files Pleasue wait ....")
        time.sleep(3)
        print("[❅] Latest version files downloaded.")
except:
    pass
print("[❅] Project Migration Start.")
time.sleep(4)
makemig = subprocess.check_output('python manage.py makemigrations')
mig = subprocess.check_output('python manage.py migrate')
print("[❅] Project Migration Complete.")
os.system('cls')
print('\n\t\t[❅]Project Update Complete.\n')
time.sleep(3)
print("[❅] Starting project server .....")
time.sleep(3)
os.system('python manage.py runserver')
