import time

def traffic_light_cycle():
    while True:
        print("🟢 GREEN - Go! (20 seconds)")
        time.sleep(20)
        
        print("🟠 AMBER - Caution! (5 seconds)")
        time.sleep(5)
        
        print("🔴 RED - Stop! (10 seconds)")
        time.sleep(10)
if __name__ == traffic_light_cycle():
    print("Traffic light cycle completed.")