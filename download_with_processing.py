import multiprocessing
import time
import requests

def downloader(url, chars_list, index, lock):
    chars = requests.get(url).json()
    with lock:
        chars_list[index] = len(str(chars))

def main():
    urls = [
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/todos',
        'https://jsonplaceholder.typicode.com/users'
    ]
    
    chars_list = multiprocessing.Array('i', len(urls))
    processes = []
    lock = multiprocessing.Lock()

    for i, url in enumerate(urls):
        process = multiprocessing.Process(target=downloader, args=(url, chars_list, i, lock))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()


    total_chars = 0
    for i, chars in enumerate(chars_list):
        print("Process " + str(i) + ": Downloaded " + str(chars) + " chars from " + urls[i])
        total_chars += chars

    print("Total number of downloaded chars: " + str(total_chars) + " chars")

if __name__ == "__main__":
    main()
