import time


def getSnowFlake():
    tick = time.time();
    tick = '0{tick}'.format(tick= tick).replace('.','');
    return tick;
    return 1


print(getSnowFlake())
