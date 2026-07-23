import queue
import threading
import time

with open("source/sample.txt", "r") as file:
    full_file=file.read()
    print(full_file)
    file.seek(0)
    print("---------------------------")
    lines=file.readlines()
    print(lines)
    file.seek(0)
    print("---------------------------")
    first_line=file.readline()
    second_line=file.readline()
    print(first_line)
    print(second_line)
# Open a file in write mode and write some text to it
with open("source/output.txt", "w") as file:
    file.write("This is a sample text written to the file.\n")
    file.write("This is the second line of the text.\n")
    file.write("This is the third line of the text.\n")

# Open a file in append mode and add more text to it
with open("source/output.txt", "a") as file:
    file.write("This line is appended to the file.\n")
    file.write("This is another appended line.\n")

#Handling two or more files at the same time
with open("source/input1.log", "r") as file1, \
     open("source/input2.log", "r") as file2, \
     open("source/output.log", "w") as file_out:
    content1 = file1.read()
    content2 = file2.read()
    file_out.write(content1)
    file_out.write(content2)
    


# Create a thread-safe FIFO queue
#FIFO fist in first out
#? flag value to signal the write theread to shut down safetely
log_queue = queue.Queue()
SHUTDOWN_SIGNAL="None"

#Dedicated file writer worker/thread
def file_writer(filepath='source/output.log'):
    print("File writer thread started. Writing logs")
          
    with open(filepath, "a") as file:
        while True:
            queue_size=log_queue.qsize()
            print(f"Queue size: {queue_size}")

            log_entry = log_queue.get()

            #Checj if we received the shutdown signal to stop
            if log_entry == SHUTDOWN_SIGNAL:
                print("Shutdown signal received. Stopping file writer thread.")
                log_queue.task_done()
                break

            #Write the data and inmediately flush the file to ensure it saves
            file.write(log_entry + "\n")
            file.flush()
            #Tell the queue that the processing of the log entry is done
            log_queue.task_done()

def worker(worker_id):
    print(f"Worker {worker_id} started.")
    for i in range(3):
        time.sleep(0.5)  # Simulate some work being done
        log_message = f"Worker {worker_id} log entry {i} completed."

        #Thread-safe put: multiple workers can call this simultaneously
        log_queue.put(log_message)
    print(f"[WORKER] {worker_id} Finished all work")

if __name__ == "__main__":
    print("[Main] stating writer thread")

    writer_thread = threading.Thread(target=file_writer, daemon=True)
    writer_thread.start()
    print("[Main] Staring worker threads...")
    workers = []

    for i in range(3):
        t=threading.Thread(target=worker, args=(i,))
        workers.append(t)
        t.start()
    print("[Main] Waiting for workers threads to finish...")
    for t in workers:
        t.join()
    print("[Main] All workers thread have finished processing.")

    # 1. Wait for real log entries to be fully written to the file
    print("[Main] Waiting for the queue to completely empty out")
    log_queue.join()
    print("[Main] All logs processed")

    # 2. Now that the queue is empty, safely send the shutdown signal
    print("[Main] Sending shutdown signal to the writer thread...")
    log_queue.put(SHUTDOWN_SIGNAL)

    # 3. Wait for the writer thread to detect the signal, exit its loop, and terminate
    print("[Main] Waiting for writer thread exit...")
    writer_thread.join()
    print("[Main] All logs successfully written to output.log and threads safely closed!")