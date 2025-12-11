"""
OS detector.
"""

import subprocess
import platform

class OSDetector:

    def detect(self, target: str):
        try:
            if platform.system().lower() == "windows":
                cmd = ["ping", "-n", "1", target]
            else:
                cmd = ["ping", "-c", "1", target]

            result = subprocess.check_output(cmd).decode()
            
            if "TTL=64" in result:
                return "Linux/Unix"
            elif "TTL=128" in result:
                return "Windows"
            else:
                return "Unknown OS"

        except:
            return "No was detected"
