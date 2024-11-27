import threading
import time
import random
import requests


def downloader(thread_id,url,returns):
    start_download_time = time.time()
    requests.get(url).json()
    end_download_time = time.time()
    download_duration = end_download_time - start_download_time
    print("Thread " + str(thread_id) + ": Download time: " + str(round(download_duration, 2)) + " seconds  ")
    returns.append(thread_id)

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
    threads_returns = []
    for i, url in enumerate(urls):
        thread = threading.Thread(target=downloader, args=(i, url, threads_returns, ))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    print(threads_returns)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Total execution time: " + str(round(end - start, 2)) + " seconds")
