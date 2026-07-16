import time
import random
import queue

from threading import Thread

counter=0

job_queue=queue.Queue()
counter_queue=queue.Queue()