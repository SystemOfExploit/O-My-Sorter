# Github: https://github.com/SystemOfExploit

print()
print("#############################################")
print("#          Welcome to o-my-sorter!          #")
print("# Coder: https://github.com/SystemOfExploit #")
print("#############################################")
print()
file = str(input("Enter name of your txt file (example: omysorter.txt): "))
ofile = str(input("Enter name of your txt file (example: omysorter.txt): "))

keywords = ["chatgpt.com", "gemini.google.com", "neverlose.cc", "skeet.cc", "gamesense.pub", "midnight.im", "memesense.gg", "interium.ooo", "xone.fun", "fatality.win", "nixware.cc", "iniuria.us", "futureclient.net", "rusherhack.org", "boze.dev", "mioclient.me", "roblox.com", "battle.net", "epicgames.com", "steamcommunity.com", "portmap.io", "playit.gg", "cloudpub.ru", "xtunnel.ru", "ngrok.com", "webrat.in", "webr.at", "webrat.uk", "webrat.eu", "mulvad.net", "protonvpn.com", "hide.mn", "nordvpn.com", "expressvpn.com", "github.com", "gitlab.com", "deepseek.com", "qwen.ai", "claude.ai", "cursor.com"]
keywords_lower = [kw.lower() for kw in keywords]

with open(file, "r", encoding="utf-8") as infile, open(ofile, "w", encoding="utf-8") as outfile:
    for line in infile:
        line_lower = line.lower()

        if any(kw in line_lower for kw in keywords_lower):
            outfile.write(line)

print("Sorting completed!")