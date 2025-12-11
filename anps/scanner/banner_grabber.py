import socket
'''Banner Grabber Module - This module provides functionality to grab banners from services running on specified target hosts and ports.'''
class BannerGrabber:
    def grab(self, target: str, port: int, timeout: float = 0.5):
        try:
            s = socket.socket()
            s.settimeout(timeout)
            s.connect((target, port))
            s.send(b"HELLO\r\n")
            banner = s.recv(1024).decode(errors="ignore").strip()
            s.close()
            return banner
        except:
            return None
