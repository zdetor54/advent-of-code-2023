import multiprocessing

def worker_function(value):
    result = value * value
    print(f"Processed {value}, result: {result}")

if __name__ == "__main__":
    # List of values to process
    values_to_process = [1, 2, 3, 4, 5]

    # Create a pool of processes
    with multiprocessing.Pool() as pool:
        # Use the pool to parallelize the execution of the worker function
        pool.map(worker_function, values_to_process)