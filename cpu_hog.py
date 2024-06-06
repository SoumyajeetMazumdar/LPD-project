# # import threading
# # import time

# # def cpu_hog():
# #     while True:
# #         pass  # Busy-wait loop to consume CPU cycles

# # if __name__ == "__main__":
# #     num_threads = int(input("Enter the number of threads to create (typically up to your number of logical processors, which is 12 in your case): "))
    
# #     threads = []
# #     for _ in range(num_threads):
# #         thread = threading.Thread(target=cpu_hog)
# #         thread.daemon = True  # Daemonize thread to exit when the main program exits
# #         threads.append(thread)
# #         thread.start()
    
# #     print(f"Started {num_threads} threads. Press Ctrl+C to stop.")
    
# #     try:
# #         while True:
# #             time.sleep(1)  # Keep the main thread alive
# #     except KeyboardInterrupt:
# #         print("Stopping the script.")

# import threading
# import multiprocessing
# import time

# def cpu_hog():
#     while True:
#         pass  # Busy-wait loop to consume CPU cycles

# if __name__ == "__main__":
#     num_logical_processors = multiprocessing.cpu_count()
#     print(f"Number of logical processors detected: {num_logical_processors}")

#     num_threads = int(input(f"Enter the number of threads to create (up to {num_logical_processors}): "))
#     if num_threads > num_logical_processors:
#         print(f"Warning: You are creating more threads ({num_threads}) than logical processors ({num_logical_processors}).")
    
#     threads = []
#     for _ in range(num_threads):
#         thread = threading.Thread(target=cpu_hog)
#         thread.daemon = True  # Daemonize thread to exit when the main program exits
#         threads.append(thread)
#         thread.start()
    
#     print(f"Started {num_threads} threads. Press Ctrl+C to stop.")
    
#     try:
#         while True:
#             time.sleep(1)  # Keep the main thread alive
#     except KeyboardInterrupt:
#         print("Stopping the script.")

import multiprocessing
import time

def cpu_hog():
    # Perform arithmetic calculations to keep the CPU busy
    while True:
        x = 0
        for i in range(1000000):
            x += i

if __name__ == "__main__":
    num_logical_processors = multiprocessing.cpu_count()
    print(f"Number of logical processors detected: {num_logical_processors}")

    num_processes = int(input(f"Enter the number of processes to create (up to {num_logical_processors}): "))
    if num_processes > num_logical_processors:
        print(f"Warning: You are creating more processes ({num_processes}) than logical processors ({num_logical_processors}).")
    
    processes = []
    for _ in range(num_processes):
        process = multiprocessing.Process(target=cpu_hog)
        processes.append(process)
        process.start()
    
    print(f"Started {num_processes} processes. Press Ctrl+C to stop.")
    
    try:
        while True:
            time.sleep(1)  # Keep the main process alive
    except KeyboardInterrupt:
        print("Stopping the script.")
        for process in processes:
            process.terminate()
        for process in processes:
            process.join()
