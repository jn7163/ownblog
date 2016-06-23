#encoding:utf-8

import psutil,time,os

class Memory:
    def __init__(self):
        self.memory=psutil.virtual_memory()
        self.check()
    def check(self):        
        self.total=self.memory.total
        self.used=self.memory.used
    def percent(self):
        return (self.used+0.0)/self.total


def showprocess():
	pids=psutil.pids()
	for pid in pids:
		process = psutil.Process(pid)
		os.stdout.write(process.name())


memory=Memory()
data=u'CPU 逻辑个数：%d \nCPU 物理个数：%d' % (psutil.cpu_count(),psutil.cpu_count(logical=False))
while 1:
    os.system('cls')
    print data
    print 'memory have used %f%%' % memory.percent()
    memory.check()
    time.sleep(1)