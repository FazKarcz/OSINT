import re
from collections import Counter

with open("dump.txt", "r", encoding="utf-8") as file:
    data = file.read()

email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
hash_pattern = r'\b[a-f0-9]{32,64}\b'
domain_pattern = r'(?<=@)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(email_pattern, data)
hashes = re.findall(hash_pattern, data)
domains = re.findall(domain_pattern, data)

# Podsumowanie
print(f"Znalezione e-maile ({len(emails)}):")
for email in emails:
    print("  -", email)

print(f"\nZnalezione potencjalne hashe ({len(hashes)}):")
for h in hashes:
    print("  -", h)

print(f"\nNajczęstsze domeny ({len(domains)}):")
for domain, count in Counter(domains).most_common():
    print(f"  - {domain} ({count})")
