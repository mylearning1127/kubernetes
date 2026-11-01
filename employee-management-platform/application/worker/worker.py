import os, socket, time
print("Employee background worker started on", socket.gethostname(), flush=True)
while True:
    print("Checking notification queue (demo task)", flush=True)
    time.sleep(int(os.getenv("WORK_INTERVAL_SECONDS", "30")))
