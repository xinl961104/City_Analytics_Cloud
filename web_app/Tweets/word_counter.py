import json
import time
from collections import Counter


count = 0
cnt = Counter()
try:
    with open('../../../historic_data/twitter-melb.json', encoding="utf8") as f:
        next(f)
        start_time = time.time()
        keys = []
        for line in f:
            data = json.loads(line[:-2])['doc']['text']
            data = ''.join((e.lower() for e in data if e.isalnum() or e == " ")).split()
            for word in data:
                cnt[word] += 1
            # if ((any(i in data.lower() for i in keys))):
            #     if (json.loads(line[:-2])['doc']['coordinates'] is not None):
            count += 1
            # print('count: ', count)
except Exception as e:
    print(cnt.most_common(100))