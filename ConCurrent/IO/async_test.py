import asyncio
import time

now = lambda : time.time()

async def do_work(x):
    print("Waiting:",x)
    await asyncio.sleep(x)
    return "Done after %s s" % x
start = now()

# 生成协程对象
cor1 = do_work(1)
cor2 = do_work(2)
cor3 = do_work(3)
# 将协程对象生成一个可轮寻操作的对象列表
task = [
    asyncio.ensure_future(cor1),
    asyncio.ensure_future(cor2),
    asyncio.ensure_future(cor3),
]

# 得到轮寻对象调用run启动协程执行
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.)