import threading
from queue import Queue

''' def threaded_scan(worker_fn, ports: list, thread_count: int = 100):
    A utility function to perform threaded scanning of ports using a worker function.

    Args:
        worker_fn: A function that takes a port as an argument and performs scanning.
        ports (list): A list of ports to scan.
        thread_count (int): The number of threads to use for scanning.

    Returns:
        list: A list of results returned by the worker function.
    '''
def threaded_scan(worker_fn, ports: list, thread_count: int = 100):
    queue = Queue()
    results = []

    for port in ports:
        queue.put(port)

    def worker():
        while not queue.empty():
            port = queue.get()
            result = worker_fn(port)
            if result:
                results.append(result)
            queue.task_done()

    threads = []

    for _ in range(thread_count):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    return results
