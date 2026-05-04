from collections import Counter

# Lecture du fichier log
with open("access.log", "r") as file:
    logs = file.readlines()

suspicious_ips = []
attack_lines = []

# Analyse des lignes
for line in logs:
    ip = line.split()[0]

    # Detection SQL Injection
    if "OR '1'='1" in line or "' OR" in line:
        suspicious_ips.append(ip)
        attack_lines.append(line.strip())

# Compter les occurrences des IP
ip_count = Counter(suspicious_ips)

# Affichage des resultats
print("=== Resultats de l'analyse ===\n")

print("IP suspecte :")
for ip, count in ip_count.items():
    print(f"- {ip} (nombre de tentatives : {count})")

print("\nType d'attaque :")
print("- SQL Injection")

print("\nRequetes suspectes :")
for attack in attack_lines:
    print("-", attack)