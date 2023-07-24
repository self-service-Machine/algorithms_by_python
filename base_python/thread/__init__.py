import time

"""
** 阻塞：调用函数的当前的线程被挂起
   非阻塞：调用函数的时候，当前线程不会被挂起，而是继续执行

** 同步：指代码调用IO操作时，必须等待IO操作完成才能继续调用的方式
   异步：指代码调用IO操作时，不用等待IO操作完成也能继续调用的方式

** 并发：一段时间内，有几个程序在一个cpu上运行，但在该时间段内的一个时间点上只有一个程序在cpu上运行
   并行：在一个时间点上，有几个程序在几个cpu上同时运行


** IO多路复用：select、poll、epoll
     * select：轮询，每次都要遍历所有的fd，效率低
     * poll：轮询，每次都要遍历所有的fd，效率低
     * epoll：事件通知，只通知发生变化的fd，效率高
   通过一种机制来监听多个描述符，一个某个描述符准备就绪(可读、可写)，就能通知程序进行相应的操作,上述三种多路复用都属于同步IO；异步IO无需自己负责读写
"""


# 不安全的多线程共享变量
"""
# GIL  global interpreterer lock(全局解释器锁)， GIL使得在一个进程中的一个时间点上只有一个线程在执行python编译的字节码；
# 操作系统最小调度单元是线程,线程必选依赖进程存在

a = 0

def add():
    global a
    for i in range(1000000):
        a += 1

def sub():
    global a
    for i in range(1000000):
        a -= 1

if __name__ == '__main__':
    t1 = threading.Thread(target=add)
    t2 = threading.Thread(target=sub)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(a)

# python的GIL会在适当的时候切换线程，它并不会等到一个线程完全执行完毕才会释放。
实际上GIL会根据线程执行的任务的字节码的长度和时间片来随机释放，或者GIL在遇到IO阻塞的时候也会释放。
"""


# 子进程执行内容
def son_thread():
    print(666)
    time.sleep(3)
    print(777)


# 主进程与子进程执行结束后，整个程序才会结束
"""
if __name__ == '__main__':

    import threading
    # 主线程开启子线程
    t1 = threading.Thread(target=son_thread)
    t1.start()
    print("end")
    # 主线程结束时子线程不受影响，子线程结束后整个程序结束

"""


# 守护线程
"""
if __name__ == '__main__':
    t1 = threading.Thread(target=son_thread)
    # 设置守护线程
    t1.setDaemon(True)
    t1.start()
    print('end')
    # 当主线程结束时，守护线程（没执行完）也会结束
"""


# 阻塞等待
"""
if __name__ == '__main__':

    import threading
    t1 = threading.Thread(target=son_thread)
    t1.start()
    # 阻塞等待子线程执行完毕后主线程继续往下执行
    t1.join()
    print("end")
"""


# 线程通信 -- 使用队列通信
"""
# 线程间通信有多种方式，共享内存、网络、文件、数据库...
   * 共享内存：多个线程来对一块内存就行操作，但是这样会有线程安全的隐患(参考上面GIL随机释放的例子)，要想线程安全，就得对共享的内存进行加锁

def pop(quene):
    while True:
        data = quene.get()
        print(data)


def insert(quene):
    for i in range(20):
        # put方法向队列中插入数据（引用类型）
        quene.put(i)


if __name__ == '__main__':
    from queue import Queue
    # 实例化时通过maxsize指定队列的长度，不指定时默认为无限长；
    # Queue是线程安全的；内部使用了"deque"(线程安全的双向队列)
    quene = Queue(maxsize=20)
    t1 = threading.Thread(target=insert, args=(quene,))
    t2 = threading.Thread(target=pop, args=(quene,))
    t1.start()
    t2.start()
"""


# 线程同步

"""
# 线程同步：多个线程之间的执行顺序是无序的，但是有时候我们需要让多个线程之间有序的执行，这时候就需要线程同步

a = 0
# 声明锁
lock = threading.Lock()


def add():
    global a
    global lock
    for i in range(1000000):
        lock.acquire()
        a += 1
        lock.release()


def sub():
    global a
    global lock
    for i in range(1000000):
        lock.acquire()
        a -= 1
        lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=add)
    t2 = threading.Thread(target=sub)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(a)

# 给a赋值时必须拿到锁，拿到锁的线程的锁的资源
"""


# 可重用锁
"""
import threading

a = 0
# 声明使用重入锁
lock = threading.RLock()


def add():
    global a
    global lock
    for i in range(1000000):
        lock.acquire()
        # 使用Lock这里会阻塞,Rlock并不会
        lock.acquire()
        lock.release()
        a += 1
        lock.release()


def sub():
    global a
    global lock
    for i in range(1000000):
        lock.acquire()
        a -= 1
        lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=add)
    t2 = threading.Thread(target=sub)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(a)
"""


# 使用锁控制执行进度
"""
lock = threading.Lock()


def func1():
    global lock
    lock.acquire()
    print(1)
    lock.release()
    lock.acquire()
    print(3)
    lock.release()


def func2():
    global lock
    lock.acquire()
    print(2)
    lock.release()
    lock.acquire()
    print(4)
    lock.release()


# 执行结果：1 3 2 4，
if __name__ == '__main__':
    t1 = threading.Thread(target=func1)
    t2 = threading.Thread(target=func2)
    t1.start()
    t2.start()
    
# 使用Condition控制多线程执行进度
lock = threading.Condition()


def func1():
    global lock
    lock.acquire()
    print(1)
    lock.notify()
    print('func1 notify')
    print('func1 wait')
    lock.wait()
    print(3)
    lock.notify()
    print('func1 notify')
    lock.release()


def func2():
    global lock
    lock.acquire()
    print('func2 wait')
    lock.wait()
    print(2)
    lock.notify()
    print('func2 notify')
    print('func2 wait')
    lock.wait()
    print(4)
    lock.release()


# 执行结果：1，
# 原因：t1线程线运行，t2后运行，在t1开始时，运行notify，这时候t2的wait还没执行到，但t1已经运行了notify,t2在阻塞的时候没有notify来通知它，所以会阻塞，使用Condition时，应该让阻塞的线程先运行
if __name__ == '__main__':
    t1 = threading.Thread(target=func1)
    t2 = threading.Thread(target=func2)
    t1.start()
    t2.start()
"""


# 控制线程的运行量  Semaphore
"""
# 接受一个最大线程数的参数，当线程数达到最大值时，阻塞等待，直到有线程执行完毕，释放资源，再继续执行
"""


# 线程池
"""
from concurrent.futures import ThreadPoolExecutor
import time

# 传入线程池容量，默认为机器CPU核心数
executor = ThreadPoolExecutor(max_workers=2)


def test():
    time.sleep(3)
    print("test done")
    return "test"


def done_callback(response):
    print(response)


if __name__ == '__main__':
    # 通过submit返回Future对象，可以获取线程的状态，是否完成，是否在运行，是否取消，获取返回值（线程池执行结果需一个个获取）
    task = executor.submit(test)
    task.add_done_callback(done_callback)
    print(task.done()) # False
    print(task.running()) # True
    print(task.result()) # test
    print(task.done()) # True
    print(task.cancel()) # False

**********************************************************************************************************************
# 批量获取线程池执行结果

from concurrent.futures import ThreadPoolExecutor, as_completed

executor = ThreadPoolExecutor(max_workers=2)


def test(s_time: int):
    time.sleep(s_time)
    return f"test sleep {s_time}s"


if __name__ == '__main__':
    tasks = (executor.submit(test, i) for i in range(4))
    # as_completed() 获取线程池中的任务的返回结果,按完成先后返回结果
    for future in as_completed(tasks):
        data = future.result()
        print(data)

**********************************************************************************************************************
# 按照传入顺序获取线程池返回结果
from concurrent.futures import ThreadPoolExecutor
import time

executor = ThreadPoolExecutor(max_workers=2)

def test(s_time: int):
    time.sleep(s_time)
    return f"test sleep {s_time}s"

if __name__ == '__main__':
    for data in executor.map(test, range(4)):
        print(data)
**********************************************************************************************************************

# 主线程阻塞
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, ALL_COMPLETED

executor = ThreadPoolExecutor(max_workers=2)


def test(s_time: int):
    time.sleep(s_time)
    return f"test sleep {s_time}s"


if __name__ == '__main__':
    tasks = [executor.submit(test, i) for i in range(4)]
    # wait()方法设置超时时间、指定某个task完成后解除阻塞状态
    wait(tasks, return_when=ALL_COMPLETED)
    for future in as_completed(tasks):
        data = future.result()
        print(data)
"""


# 多进程
"""
# 进程是操作系统资源分配的单元。一个进程的所有线程可以空享其进程的资源，不同进程的资源是相互隔离的；
# python中存在GIL锁，所以多线程无法发挥多cpu的优势，多进程可以

from multiprocessing import Process
import time


def test(n):
    time.sleep(n)
    print("test over")


if __name__ == '__main__':

    process = Process(target=test, args=(2,))
    process.start()
    print("main over")
"""


# 进程池
"""
from multiprocessing import Pool
import time


def test(n):
    time.sleep(n)
    return f"test slept {n}s"


if __name__ == '__main__':

    pool = Pool()
    task = pool.apply_async(test, args=(2,))
    pool.close()
    # 调用join之前，一定要将进程池关闭
    pool.join()
    # get会阻塞到结果返回
    print(task.get())
    print("main over")
    

**********************************************************************************************************************

# 按顺序返回进程池执行结果
from multiprocessing import Pool
import time


def test(n):

    time.sleep(n)
    return f"test slept {n}s"


if __name__ == '__main__':

    pool = Pool()
    for result in pool.map(test, range(3)):
        print(result)

    # imap()和imap_unordered()方法，可以按照进程池中进程的顺序返回结果，也可以按照进程结束的顺序返回结果
    for result in pool.imap(test, range(3)):
        print(result)

    for result in pool.imap_unordered(test, range(3)):
        print(result)

**********************************************************************************************************************
# 不同执行器创建进程池
from concurrent.futures import ProcessPoolExecutor
import time


def test(n):

    time.sleep(n)
    return f"test slept {n}s"


if __name__ == '__main__':

    executor = ProcessPoolExecutor()
    for data in executor.map(test, range(4)):
        print(data)
"""

# 进程间通信
"""
from multiprocessing import Queue, Process
import time


def test1(q):
    q.put("args")


def test2(q):
    time.sleep(3)
    print(q.get())


if __name__ == '__main__':
    # 使用进程间通信的队列;但不能用于进程池间通信
    queue = Queue()
    # 创建进程
    t1 = Process(target=test1, args=(queue,))
    t2 = Process(target=test2, args=(queue,))
    t1.start()
    t2.start()
"""


# 进程池间通信
"""
# 通过使用Manager()创建的进程间通信的队列，可以用于进程池间通信

from multiprocessing import Manager, Pool
import time


def test1(q):
    q.put("args")


def test2(q):
    time.sleep(3)
    print(q.get())


if __name__ == '__main__':

    queue = Manager().Queue()
    pool = Pool()
    t1 = pool.apply_async(test1, args=(queue,))
    t2 = pool.apply_async(test2, args=(queue,))
    pool.close()
    pool.join()
    
**********************************************************************************************************************

# 通过管道实现进程间通信
from multiprocessing import Manager, Pipe
if __name__ == '__main__':
    share_dict = Manager().dict()
    pipe = Pipe()
"""


# 协程
"""

# 协程是编译器级的，线程和进程是操作系统级
# 

import asyncio


async def test1():
    await asyncio.sleep(3)
    return "test1 done"


if __name__ == '__main__':

    # 事件循环
    loop = asyncio.get_event_loop()
    # 给事件循环添加任务，返回Feature对象
    task = loop.create_task(test1())
    # 阻塞的方法，直到所有的任务全部完成!
    loop.run_until_complete(task)
    # 获取返回结果
    print(task.result())

**********************************************************************************************************************
# 批量注册
import asyncio


async def test1():
    await asyncio.sleep(3)
    return "test1 done"


if __name__ == '__main__':

    # 事件循环
    loop = asyncio.get_event_loop()
    # 给事件循环添加任务
    tasks = [test1() for i in range(10)]
    # 阻塞的方法，直到所有的任务全部完成!
    loop.run_until_complete(asyncio.wait(tasks))

"""


# 协程中设置阻塞IO
"""

from concurrent.futures import ThreadPoolExecutor
import asyncio
import time


def get_html(url):
    time.sleep(2)
    return f'get html from {url} success'


if __name__ == '__main__':

    start = time.time()
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor()
    # 单个任务
    tasks = loop.run_in_executor(executor, get_html, 'https://www.baidu.com')
    # 多个任务
    results = []
    for i in range(5):

        task = loop.run_in_executor(executor, get_html, 'https://www.baidu.com')
        results.append(task)

    loop.run_until_complete(asyncio.wait(results))
    print(time.time() - start)
"""


# 协程的同步和通信
"""
import asyncio

lock = asyncio.Lock()
results = []


async def put():

    global lock, results
    await lock.acquire()
    results.append(1)
    await asyncio.sleep(3)
    lock.release()


async def get():
    global lock, results
    async with lock:
        item = results.pop()
        print(item)


if __name__ == '__main__':
    tasks = [put(), get(), ]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
"""
