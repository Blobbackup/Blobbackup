from threading import BoundedSemaphore
from concurrent.futures import ThreadPoolExecutor


class BoundedThreadPoolExecutor(object):
    def __init__(self, bound, max_workers):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self.semaphore = BoundedSemaphore(bound + max_workers)

    def future_done(self, future):
        self.semaphore.release()
        exception = future.exception()
        if exception is not None:
            raise exception

    def submit(self, fn, *args, **kwargs):
        self.semaphore.acquire()
        try:
            future = self.executor.submit(fn, *args, **kwargs)
        except ValueError:
            self.semaphore.release()
            raise
        else:
            future.add_done_callback(lambda x: self.future_done(future))
            return future

    def shutdown(self, wait=True):
        self.executor.shutdown(wait)