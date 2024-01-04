import os
import time
import datetime
from winletoast import ToastNotifier

class Shutdown(object):
    def __init__(self, mins=0):
        self.clock = str(datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S'))
        self.mins = mins
        self.parser = ToastNotifier()

    def main(self):
        if self.mins > 0:
            print(self.popup())
            time.sleep(self.mins * 60)
            return os.system("shutdown /s /t 1")
        else:
            return os.system("shutdown /s /t 8")

    def popup(self):
        return self.parser.show_toast("Shutdown",
                                     f"Time is now: {self.clock}\nSystem will power-off in {int(self.mins)} min.",
                                     duration=50)

if __name__ == "__main__":
    try:
        mins = int(input("Enter minutes to shutdown: ")) * 60
        Shutdown(mins).main()
    except ValueError:
        Shutdown().main()
