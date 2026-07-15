import urllib.request
url = 'https://r.jina.ai/http://127.0.0.1:8000/index.html'
try:
    with urllib.request.urlopen(url, timeout=60) as r:
        print('STATUS', r.status)
        body = r.read(400).decode('utf-8', 'ignore')
        print(body)
except Exception as e:
    print('ERROR', type(e).__name__, e)
