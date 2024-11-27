import multiprocessing
import time
import requests

def downloader(lock, thread_id, url, chars_list):
    with lock:
        chars = requests.get(url).json()
        chars_list[thread_id] = len(str(chars))

def main():
    urls = [
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/todos',
        'https://jsonplaceholder.typicode.com/users'
    ]
    chars_list = [0] * len(urls)
    lock = multiprocessing.Lock()
    processes = []

    for i, url in enumerate(urls):
        process = multiprocessing.Process(target=downloader, args=(lock, i, url, chars_list))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    total_chars = 0
    for i, chars in enumerate(chars_list):
        print(f"Process {i}: Downloaded {chars} chars from {urls[i]}")
        total_chars += chars

    print(f"Total number of downloaded chars: {total_chars} chars")

if __name__ == "__main__":
    main()
