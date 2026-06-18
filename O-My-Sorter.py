# Github: https://github.com/SystemOfExploit

import os

print()
print("#############################################")
print("#          Welcome to o-my-sorter!          #")
print("# Coder: https://github.com/SystemOfExploit #")
print("#############################################")
print("#              VERSION: 1.0.1               #")
print("#############################################")

file = input("Enter name of your txt file (example: omysorter.txt): ").strip()

if not os.path.exists(file):
    print(f"Error: File '{file}' not found in current directory!")
    print("Please check the filename and try again.")
    exit()

aifile = "ai.txt"
csfile = "cs2_cheats.txt"
minefile = "minecraft_cheats.txt"
gamesfile = "gamelaunchers.txt"
portfile = "portforward_services.txt"
malwarefile = "malwaresites.txt"
vpnfile = "vpn.txt"
gitfile = "git_services.txt"
marketsfile = "markets.txt" 

ai_keywords = ["chatgpt.com", "gemini.google.com", "deepseek.com", "qwen.ai", "claude.ai", "cursor.com"]
cs_keywords = ["neverlose.cc", "skeet.cc", "gamesense.pub", "midnight.im", "memesense.gg", "interium.ooo", "xone.fun", "fatality.win", "nixware.cc", "iniuria.us"]
mine_keywords = ["futureclient.net", "rusherhack.org", "boze.dev", "mioclient.me"]
games_keywords = ["roblox.com", "battle.net", "epicgames.com", "steamcommunity.com"]
port_keywords = ["portmap.io", "playit.gg", "cloudpub.ru", "xtunnel.ru", "ngrok.com"]
malware_keywords = ["webrat.in", "webr.at", "webrat.uk", "webrat.eu"] 
vpn_keywords = ["mulvad.net", "protonvpn.com", "hide.mn", "nordvpn.com", "expressvpn.com"]
git_keywords = ["github.com", "gitlab.com"]
markets_keywords = ["funpay.com", "lolz.live", "lzt.market", "lolz.guru", "zelenka.guru", "lolz.market", "zelenka.market", "ggsel.net"]

ai_keywords_lower = [kw.lower() for kw in ai_keywords]
cs_keywords_lower = [kw.lower() for kw in cs_keywords]
mine_keywords_lower = [kw.lower() for kw in mine_keywords]
games_keywords_lower = [kw.lower() for kw in games_keywords]
port_keywords_lower = [kw.lower() for kw in port_keywords]
malware_keywords_lower = [kw.lower() for kw in malware_keywords]
vpn_keywords_lower = [kw.lower() for kw in vpn_keywords]
git_keywords_lower = [kw.lower() for kw in git_keywords]
markets_keywords_lower = [kw.lower() for kw in markets_keywords]

with open(file, "r", encoding="utf-8") as infile, open(aifile, "w", encoding="utf-8") as outfile:
    for line in infile:
        line_lower = line.lower()
        if any(kw in line_lower for kw in ai_keywords_lower):
            outfile.write(line)

with open(file, "r", encoding="utf-8") as infile, open(csfile, "w", encoding="utf-8") as outfile:
    for line in infile:
        line_lower = line.lower()
        if any(kw in line_lower for kw in cs_keywords_lower):
            outfile.write(line)

with open(file, "r", encoding="utf-8") as infile, open(minefile, "w", encoding="utf-8") as outfile:
    for line in infile:
        line_lower = line.lower()
        if any(kw in line_lower for kw in mine_keywords_lower):
            outfile.write(line)

with open(file, "r", encoding="utf-8") as infile, open(gamesfile, "w", encoding="utf-8") as outfile:
    for line in infile:
        line_lower = line.lower()
        if any(kw in line_lower for kw in games_keywords_lower):
            outfile.write(line)

with open(file, "r", encoding="utf-8") as infile, open(portfile, "w", encoding="utf-8") as outfile:
    for line in infile:
        line_lower = line.lower()
        if any(kw in line_lower for kw in port_keywords_lower):
            outfile.write(line)

with open(file, "r", encoding="utf-8") as infile, open(malwarefile, "w", encoding="utf-8") as outfile:
    for line in infile:
        line_lower = line.lower()
        if any(kw in line_lower for kw in malware_keywords_lower):
            outfile.write(line)

with open(file, "r", encoding="utf-8") as infile, open(vpnfile, "w", encoding="utf-8") as outfile:
    for line in infile:
        line_lower = line.lower()
        if any(kw in line_lower for kw in vpn_keywords_lower):
            outfile.write(line)

with open(file, "r", encoding="utf-8") as infile, open(gitfile, "w", encoding="utf-8") as outfile:
    for line in infile:
        line_lower = line.lower()
        if any(kw in line_lower for kw in git_keywords_lower):
            outfile.write(line)

with open(file, "r", encoding="utf-8") as infile, open(marketsfile, "w", encoding="utf-8") as outfile:
    for line in infile:
        line_lower = line.lower()
        if any(kw in line_lower for kw in markets_keywords_lower):
            outfile.write(line)

print("Sorting completed!")