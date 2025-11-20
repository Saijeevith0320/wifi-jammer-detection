
#!/usr/bin/env python3
# WiFi Jammer Detection Simulation (Deauth Attack Monitor)

import time
import random

def detect_jammer():
    print("=== WiFi Jammer Detection System ===")
    time.sleep(1)
    print("Monitoring WiFi for Deauthentication Attacks...
")
    time.sleep(1)

    # Random deauth packet simulation
    for i in range(10):
        deauth_packets = random.randint(0, 50)
        print(f"Scan {i+1}: Detected {deauth_packets} deauth packets")

        if deauth_packets > 25:
            print("⚠️  ALERT! Possible WiFi Jammer Detected!
")
            log_attack(deauth_packets)
        time.sleep(0.5)

def log_attack(count):
    with open("jammer_log.txt", "a") as f:
        f.write(f"High Deauth Count: {count}
")

if __name__ == "__main__":
    detect_jammer()
