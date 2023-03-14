import time

def ft_progress(lst):
    tm = time.time()
    for x in lst:
        tm_n = time.time() - tm
        percent = ((x + 1) / len(lst)) * 100
        print("ETA: {:.2f}s [{:3n}%][{:█>{:n}}{:.<{:n}}] {}/{} | elapsed time {:.2f}s".format((len(lst) - 1 - x) * (tm_n / (x + 1)), percent, "", percent, "", 100 - percent, x + 1, len(lst), tm_n), end="\r")
        yield x

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.01)
print()
print(ret)
