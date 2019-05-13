# rwnfg

- Generates RSS feed for Radio War Nerd free previews & reposts available on Patreon page
- Tested with Python 3.X

Install system requirements:
```
sudo apt-get install libxslt-dev libxml2-dev
```

Create virtual environment
```
python3 -m venv .venv
```

Activate virtual environment
```
source .venv/bin/activate
```

Install pip requirements:
```
pip install -r requirements.txt
```

Generate RSS feed:
```
python3 rwnfg.py
```

Generated file:
```
rwn.xml
```

Deactivate virtual environment
```
deactivate
```
