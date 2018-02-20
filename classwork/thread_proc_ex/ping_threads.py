import re
import subprocess, platform
import datetime


PING_KEY = 'n' if platform.system().lower() == "windows"  else 'c'


def ping2(host):
    return subprocess.Popen(
        ["ping", host, PING_KEY, "1"],
        stdout=subprocess.PIPE).stdout.read()

def ping(host):
    return subprocess.check_output(
        f"ping -{PING_KEY} 1 {host}",
        shell=True)

def process_ping(host):
    str_result = ping(host).decode()
    match = re.search(r"Average = (\d+)",
                      str_result)
    if match is not None:
        ping_avg = float(match.group(1))
        print(f"{host}: {ping_avg}")
    else:
        print(f"Can't match ping response: {str_result}")

def run(hosts):
    for host in hosts:
        process_ping(host)

if __name__ == '__main__':
    run(hosts=['8.8.8.8', '8.8.4.4', '127.0.0.1'])
