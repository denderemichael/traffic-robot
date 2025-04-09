import time

def traffic_light_cycle():
    running = True
    try:
        while running:
            print("GREEN - Go! (20 seconds)")
            time.sleep(20)

            print(" AMBER - Caution! (5 seconds)")
            time.sleep(5)

            print(" RED - Stop! (10 seconds)")
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nTraffic light simulation stopped by user.")

if __name__ == "__main__":
    traffic_light_cycle()

