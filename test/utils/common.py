import time


def iterate_timeout(max_seconds, purpose, interval=2):
    start = time.time()
    count = 0
    while (time.time() < start + max_seconds):
        count += 1
        yield count
        time.sleep(interval)
    raise Exception(f"Timeout waiting for {purpose}")
