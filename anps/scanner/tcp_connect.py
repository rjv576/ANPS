import socket
import logging
from typing import Optional

'''TCP Connect Scanner Module'''

# This module provides functionality to perform TCP connect scans on specified target hosts and ports.
class TCPConnectScanner:
    def __init__(self, target: str, timeout: float = 0.5):
        self.target = target
        self.timeout = timeout
        
    # Scan a specific port on the target host
    def scan_port(self, port: int) -> Optional[dict]:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # timeout cross-platform
            sock.settimeout(self.timeout)

            result = sock.connect_ex((self.target, port))

            if result == 0:
                banner = self._grab_banner(sock)
                sock.close()

                return {
                    "port": port,
                    "status": "open",
                    "banner": banner
                }

            sock.close()
            return None

        except Exception as exc:
            logging.error(f"Error scanning port {port}: {exc}")
            return None
        
    # Grab banner from the service if available
    def _grab_banner(self, sock):
        try:
            sock.send(b"HELLO\r\n")
            return sock.recv(1024).decode(errors="ignore").strip()
        except:
            return "No banner"
