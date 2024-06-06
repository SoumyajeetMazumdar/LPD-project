import time

def consume_memory(size_in_gb):
    # Convert GB to bytes
    size_in_bytes = size_in_gb * 1024 * 1024 * 1024
    try:
        # Allocate memory
        memory_hog = bytearray(size_in_bytes)
        print(f"Allocated {size_in_gb} GB of memory.")
        # Keep the memory allocated for a while
        time.sleep(600)  # Sleep for 10 minutes
    except MemoryError:
        print("Memory allocation failed. Not enough RAM available.")
    finally:
        print("Releasing memory.")

if __name__ == "__main__":
    try:
        gb = int(input("Enter the amount of GB to consume: "))
        consume_memory(gb)
    except ValueError:
        print("Please enter a valid integer for the GB size.")
