import json
import typer
from anps.scanner.tcp_connect import TCPConnectScanner
from anps.scanner.utils import threaded_scan
''' def scan(target: str, ports: str = "1-1024", threads: int = 100, output: str = None):
    A CLI command to perform a TCP connect scan on a target host.

    Args:
        target (str): The target host to scan.
        ports (str): A range of ports to scan, e.g., "1-1024".
        threads (int): The number of threads to use for scanning.
        output (str): Optional output file to save results in JSON format.
    '''
app = typer.Typer()

@app.command()
def scan(target: str, ports: str = "1-1024", threads: int = 100, output: str = None):
    start, end = map(int, ports.split("-"))
    port_list = list(range(start, end + 1))

    scanner = TCPConnectScanner(target)
    results = threaded_scan(scanner.scan_port, port_list, threads)

    if output:
        with open(output, "w") as f:
            json.dump(results, f, indent=4)
        typer.echo(f"[+] Saving in {output}")
    else:
        typer.echo(json.dumps(results, indent=4))

if __name__ == "__main__":
    app()
