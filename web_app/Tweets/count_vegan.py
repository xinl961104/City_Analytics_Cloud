import json
import time

count = 0
num_veg = 0
batch_size = 250
with open('../../../historic_data/twitter-melb.json', encoding="utf8") as f:
    next(f)
    start_time = time.time()
    keys = ["music", "film", "art"]
    for line in f:
        data = json.loads(line[:-2])['doc']['text']
        if ((any(i in data.lower() for i in keys))):
            if (json.loads(line[:-2])['doc']['coordinates'] is not None):
                print(data)
                count += 1
                print('count: ', count)
        # num_veg += any(i in data.lower() for i in keys)
        # count += 1
        # print('number of vegan tweet: ', num_veg)
        # if (count%10000 == 0):
        #     print('tweets analysed: ', count)
        #     print('number of vegan tweet: ', num_veg)
        #     time_taken = time.time()-start_time
        #     percentage = count/2500000
        #     print('time elapsed: ', int(time_taken), ' s', 'time remaining: ', int((time_taken/percentage)*(1-percentage)), ' s')

