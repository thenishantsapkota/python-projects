import requests
import threading
import time 


url = "https://api.countapi.xyz/hit/baun" # Your URL Here
original_time = time.time()
def do_request():
    while True:
        response = requests.get(url)
        print(response)
        

threads = []

for i in range(150):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)


for i in range(150):
    threads[i].start()


for i in range(150):
    threads[i].join()
