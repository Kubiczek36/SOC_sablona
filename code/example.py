import numpy as np


def s(t):
    return (1 / 2 * 9.81 * t ** 2)


t = np.linspace(0, 10, 1000)
s = s(t)

for i in s:
    if s > 10:
        print("docela daleko")
    else:
        print("nic moc")
