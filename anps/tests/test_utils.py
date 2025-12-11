from anps.scanner.utils import threaded_scan

def test_threaded_scan():
    def worker(port):
        return {"port": port, "status": "open"}

    ports = [1, 2, 3]
    results = threaded_scan(worker, ports, 3)
    assert len(results) == 3
