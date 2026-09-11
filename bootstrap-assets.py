import json,hashlib,urllib.request
from pathlib import Path
for asset in json.loads(Path('asset-manifest.json').read_text()):
 p=Path('site')/asset['path']
 if p.exists() and hashlib.sha256(p.read_bytes()).hexdigest()==asset['sha256']:continue
 data=urllib.request.urlopen('https://sailinglabs-brief.garyxuejingzhou.chatgpt.site/'+asset['path'],timeout=60).read()
 if hashlib.sha256(data).hexdigest()!=asset['sha256']:raise ValueError('Asset checksum mismatch: '+asset['path'])
 p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
