import threading
import time
import random
import requests


def downloader(thread_id,text,url):
    sleep_seconds = random.randint(0, 15)
    time.sleep(sleep_seconds)
    print("Thread " + str(thread_id) + ": " + text + " slept " + str(sleep_seconds) + " seconds" )
    requests.get(url).json()

def main():
    urls = [
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/todos',
        'https://jsonplaceholder.typicode.com/users'
    ]
    threads = []
    for i, url in enumerate(urls):
        thread = threading.Thread(target=downloader, args=(i, "I", url))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
