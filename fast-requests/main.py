import requests
import threading


url = "https://api.countapi.xyz/hit/baun" # Your URL Here
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
