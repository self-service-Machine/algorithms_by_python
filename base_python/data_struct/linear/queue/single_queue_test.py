"""
单项队列实践
"""
import random

from base_python.data_struct.linear.queue import Queue


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    # 闲忙状态判断
    def busy(self):
        if self.current_task is not None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_page() * 60 / self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_page(self):
        return self.pages

    def wait_time(self, currenttime):
        return currenttime - self.timestamp


#
def simulation(num_seconds, page_per_minute):
    """

    :param num_seconds:
    :param page_per_minute:  打印每张纸耗时
    :return:
    """
    labprinter = Printer(page_per_minute)
    print_queue = Queue()
    waitingtimes = []

    for current_second in range(num_seconds):
        # 随机产生任务
        if new_print_task():
            # 将 总时间内随机时间current_second 创建任务
            task = Task(current_second)
            print_queue.enqueue(task)
        # 判断打印机闲忙和任务队列不为空
        if labprinter.busy() is False and print_queue.is_empty() is False:
            # 从任务队列取出一条
            next_task = print_queue.dequeue()
            waitingtimes.append(next_task.wait_time(current_second))
            labprinter.start_next(next_task)

    average_wait = sum(waitingtimes) / len(waitingtimes)
    print('average wait %6.2f secs %3d tasks remaing' % (average_wait, print_queue.size()))


def new_print_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


if __name__ == '__main__':
    for i in range(10):
        simulation(3600, 10)
