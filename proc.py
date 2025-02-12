import subprocess


def task1():
    try:
        cmd = "ls -l /var/log"
        p = subprocess.run(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if p.returncode == 0:
            print(p.stdout.decode())
        else:
            print("The command had an error")
            print(p.stderr.decode())
    except FileNotFoundError:
        print("The command does not exist")
    except PermissionError:
        print("Please use sudo")


def task2():
    try:
        cmd = "wsl cat /root/nginx"
        p = subprocess.run(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = p.stdout.decode()
        running = "(running)" in output
        if running:
            time_running = output.splitlines()[2].split(";")[1].strip()
            print(f"Running!!!! {time_running}")
        else:
            cmd = "systemctl restart nginx"
            p = subprocess.run(cmd.split())
            if p.returncode:
                print("Nginx Started!!!!")
            else:
                print("Nginx failed to start")
    except PermissionError:
        print("Please use sudo")
