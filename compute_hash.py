#!/usr/bin/env python3
import hashlib, re, sys

path = sys.argv[1] if len(sys.argv) > 1 else 'exeglyphe_001.html'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'<script id="core"[^>]*>(.*?)</script>'
match = re.search(pattern, content, re.DOTALL)

if not match:
    print("ERREUR: section core introuvable")
    sys.exit(1)

core = match.group(1)
h = hashlib.sha256(core.encode('utf-8')).hexdigest()
print("Hash calcule:", h)

new_content = re.sub(
    r'(<meta name="hash" id="expected-hash" content=")[^"]*(")',
    r'\g<1>' + h + r'\g<2>',
    content
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Hash insere dans", path)
