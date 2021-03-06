#encoding=utf-8
import threading
import time

# Python2
# from Queue import Queue

import queue


class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 1000:
                for i in range(100):
                    count = count + 1
                    msg = self.name + '产品生成'+str(count)
                    queue.put(msg)
                    print(msg)
            time.sleep(0.1)


class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize()>100:
                for i in range(3):
                    msg = self.name + "spent" + queue.get()
                    print(msg)
            time.sleep(0.2)


if __name__ == '__main__':
    queue = queue.Queue()

    for i in range(500):
        queue.put('初始产品'+str(i))
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()
