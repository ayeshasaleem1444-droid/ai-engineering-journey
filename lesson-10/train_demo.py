import time
for epoch in range(1, 101):
    print(f"epoch {epoch} loss: {1/epoch:.4f}", flush=True)
    time.sleep(1)
