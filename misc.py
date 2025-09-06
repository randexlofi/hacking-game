import time, random, json # system
from colorama import init, Fore, Style
init() # init colorama

# Data load/save
def load_quests():
    with open(".venv/quests.json", 'r') as f:
        return json.load(f)

def save_quests(data):
    quests = json.dumps(data, indent=4)
    with open(".venv/quests.json", 'w') as f:
        f.write(quests)

def load_player():
    with open(".venv/player.json", 'r') as f:
        return json.load(f)

def save_player(data):
    player = json.dumps(data, indent=4)
    with open(".venv/player.json", 'w') as f:
        f.write(player)

player = load_player()


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

        if random.random() < 0.1 or target not in adresses:
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


def scan(command):
    if len(command) < 2:
        print("Please specify an IP. Usage: scan <address>\n")
        return
    
    target = command[1]
    print(f"Scanning {target}...")
    time.sleep(1)

    services = {
        21: "FTP",
        22: "SSH",
        25: "SMTP",
        80: "HTTP",
        139: "NetBIOS",
        443: "HTTPS",
        3306: "MySQL",
        8080: "HTTP-Proxy",
    }
    
    quests = load_quests()
    for quest in quests:
        if quest['action'] == "scan" and quest['target'] == target and not quest["completed"]:
            open_ports = random.sample(list(services.items()), k=random.randint(1, 4))

            for port, service in open_ports:
                time.sleep(0.5)
                print(f"{service} - port: {port} {Fore.GREEN}(open)" + Style.RESET_ALL)

            print(f"\n{Fore.GREEN}{target} scanned successfully.\n{Style.RESET_ALL}")

            # update data
            quest['completed'] = True
            player['money'] += quest['reward']
            # save updated data
            save_quests(quests)
            save_player(player)

            return

    print(f"\n{Fore.RED}{target} could not be scanned.\n{Style.RESET_ALL}")  


def show_quests():
    quests = load_quests()
    for quest in quests:
        status = "Completed" if quest["completed"] else "Active"
        print(f"""[{quest["id"]}]  {quest["title"]} ({status})
    - Objective: {quest['objective']}
    - Reward: ${quest['reward']}""")

