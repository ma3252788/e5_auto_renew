import os
import time


def print_ts(message):
    print("[%s] %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), message))


def run(interval, command):
    print_ts("-" * 100)
    print_ts("Command %s" % command)
    print_ts("Starting every %s seconds." % interval)
    print_ts("-" * 100)
    while True:
        try:
            # sleep for the remaining seconds of interval
            time_remaining = interval - time.time() % interval
            print_ts("Sleeping until %s (%s seconds)..." % ((time.ctime(time.time() + time_remaining)), time_remaining))
            time.sleep(time_remaining)
            print_ts("Starting command.")
            # execute the command
            status = os.system(command)
            print_ts("-" * 100)
            print_ts("Command status = %s." % status)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    interval = 300
    command = r"/Users/mcj/anaconda3/bin/flexget execute && /Users/mcj/anaconda3/bin/python3 /Users/mcj/日常使用/GitCode/算法集合/1_自己写的/1.2_小工具类/webtest测试网站是否能打开/ipv6test_mulweb.py && /Users/mcj/anaconda3/bin/python3 /Users/mcj/日常使用/GitCode/Python_Learning/mail.py"
    # command = r"/Users/mcj/anaconda3/bin/flexget execute && /Users/mcj/anaconda3/bin/python3 /Users/mcj/日常使用/GitCode/Python_Learning/mail.py")

    run(interval, command)

