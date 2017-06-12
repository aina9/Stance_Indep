import sys, re, urllib3, json

http = urllib3.PoolManager()
url = "http://localhost:2737/translate"

lines = sys.stdin.read().splitlines()
for line in lines:
    cols = line.split("\t")
    text = cols[1]

    r = http.request('POST', url, fields={'langpair': 'ca|es', 'q': text})
    s = json.loads(r.data.decode('utf-8'))['responseData']['translatedText']
    s = re.sub(r"\*", "", s)

    sys.stdout.write("{}\t{}\t{}\t{}\t{}\tspa\n".format(cols[0], s, *cols[2:]))
