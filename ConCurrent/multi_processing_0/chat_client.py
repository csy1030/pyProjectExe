from socket import *
import os,sys

# 服务器地址
ADDR = ('192.168.237.144',8888)

# 发送消息
def send_msg(s,name):
    while True:
        text = input("发言:")
        if text == "quit":
            msg = "Q " + name
            s.sendto(msg.encode(),ADDR)
            sys.exit("退出聊天室")
        msg = "C %s %s" % (name,text)
        s.sendto(msg.encode(),ADDR)

# 接收消息
def recv_msg(s):
    while True:
        data,addr = s.recvfrom(2048)
        if data.decode() == 'EXIT':
            sys.exit()
        print(data.decode())

# 创建网络连接
def main():
    s = socket(AF_INET,SOCK_DGRAM)
    while True:
        name = input("请输入姓名:")

        # 为了方便解析,在标识符后面加入L 空格
        msg = "L " + name
        s.sendto(msg.encode(), ADDR)
        data,addr = s.recvfrom(1024)
        if data.decode() == 'OK':
            print("您已进入聊天室")
            break
        else:
            print(data.decode())

    # 创建新的进程
    pid = os.fork()
    if pid < 0:
        sys.exit("Error")
    elif pid == 0:
        send_msg(s,name)
    else:
        recv_msg(s)
    s.close()

if __name__ == "__main__":
    main()