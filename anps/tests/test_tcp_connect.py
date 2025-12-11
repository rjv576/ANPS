import socket
from anps.scanner.tcp_connect import TCPConnectScanner

'''Tests for TCP Connect Scanner Module'''
def test_scan_closed_port():
    scanner = TCPConnectScanner("127.0.0.1")
    result = scanner.scan_port(9999)
    assert result is None
