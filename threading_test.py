import json
import sys

# number_threads = int(sys.argv[1].strip())
#
# multiple_ids = []
#
#
# def main_func(key, data, results, index):
#     print("test" + str(index))
#
#
# organized_data = {}
# with open("test_series_with_id.json", "r") as f:
#     try:
#         organized_data = json.load(f)
#     except:
#         organized_data = {}
# i = 0
# max_i = len(organized_data)
# keys = list(organized_data.keys())
# while i < max_i:
#     threads = []
#     updated = []
#     results = []
#     if i + number_threads > max_i:
#         number_threads = max_i - i
#     for j in range(number_threads):
#         key = keys[i + j]
#         threads.append(
#             threading.Thread(
#                 target=main_func, args=(key, organized_data[key], results, j)
#             )
#         )
#         threads[j].start()
#         updated.append(key)
#
#     for j in range(number_threads):
#         threads[j].join()
#         # organized_data[updated[j]] = results[j]
#
#     i += number_threads
import threading
import time


def mythread():
    time.sleep(1000)


def main():
    threads = 0  # thread counter
    y = 1000000  # a MILLION of 'em!
    for i in range(y):
        try:
            x = threading.Thread(target=mythread, daemon=True)
            threads += 1  # thread counter
            x.start()  # start each thread
        except RuntimeError:  # too many throws a RuntimeError
            break
    print("{} threads created.\n".format(threads))


if __name__ == "__main__":
    main()
