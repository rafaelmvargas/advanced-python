import time

class Server:
    def __init__(self, servername):
        self.hostname = servername
        self.last_started = 90542

    def ping(self):
        return True

    def restart(self):
        print('{} is restarting...'.format(self.hostname))
        self.last_started = int(time.monotonic())
        time.sleep(2)
        print('done')

    def copyfile_up(self, filename):
        print('copying {} up to {}'.format(filename, self.hostname))

    def copyfile_down(self, filename):
        print('copying {} down from {}'.format(filename, self.hostname))

    def uptime(self):
        return(self.last_started)

