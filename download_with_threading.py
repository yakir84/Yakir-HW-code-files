import threading
import time
import requests

def downloader(thread_id, url, chars_list):
    chars = requests.get(url).json()
    chars_list.append(len(str(chars)))

def main():
    urls = [
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/todos',
        'https://jsonplaceholder.typicode.com/users'
    ]
    chars_list = []
    threads = []

    for i, url in enumerate(urls):
        thread = threading.Thread(target=downloader, args=(i, url, chars_list, ))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    total_chars = 0
    for i, chars in enumerate(chars_list):
        print("Thread " + str(i) + ": Downloaded " + str(chars) + " chars from " + urls[i])
        total_chars += chars

    print("Total number of downloaded chars: " + str(total_chars) + " chars")

if __name__ == "__main__":
    main()


