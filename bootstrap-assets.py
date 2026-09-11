import json, hashlib
from pathlib import Path
for asset in json.loads(Path('asset-manifest.json').read_text()):
 p=Path('site')/asset['path']
 assert hashlib.sha256(p.read_bytes()).hexdigest()==asset['sha256'], str(p)
print('All public illustrations verified from repository')
