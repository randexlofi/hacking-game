import time, random # system
from colorama import init, Fore
init() # init colorama

def help_file():
    with open(".venv/commands.txt", "r") as f:
            print(f.read()+"\n")


def ping(command):
    if len(command) < 2:
        print("Please specify an IP. Usage: ping <address>\n")
        return
        
    target = command[1]
    ping_times = []

    sent = 4

    print(f"Pinging {target} with 32 bytes of data.")
    for i in range(sent):
        time.sleep(1)

        if random.random() < 0.1:
            print("Request timed out.")
        else:
            rand_time = random.randint(1, 100)
            print(f"Reply from {target}: bytes=32 time={rand_time}ms TTL=64")
            ping_times.append(rand_time)

    received = len(ping_times)
    lost = sent-received
    loss_pct = int((lost/sent) * 100)

    if ping_times:
        print(f"\nmin: {min(ping_times)}ms, max: {max(ping_times)}ms, avg: {round(sum(ping_times) / len(ping_times))}ms\n")

    print(f"\nPing stats: {sent} packets sent, {lost} lost ({loss_pct}% loss)")

