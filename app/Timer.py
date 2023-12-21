import time


class Timer:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.start_time = None
        self.end_time = None

    def start(self):
        """Starts the timer."""
        self.start_time = (
            time.perf_counter_ns()
        )  # Use perf_counter_ns for high precision

    def stop(self):
        """Stops the timer and returns the elapsed time in seconds."""
        if self.start_time is None:
            raise RuntimeError("Timer is not running")
        self.end_time = time.perf_counter_ns()

    def get_duration(self):
        return (self.end_time - self.start_time) / 1e9  # Convert nanoseconds to seconds

    def __enter__(self):
        """Starts the timer when entering a `with` block."""
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Stops the timer and optionally prints the elapsed time when exiting a `with` block."""
        self.stop()
        elapsed_time = self.get_duration()
        if exc_type is None and self.verbose:
            print(f"Elapsed time: {elapsed_time:.6f} seconds \n")
