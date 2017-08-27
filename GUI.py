from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers import SchedulerAlreadyRunningError, SchedulerNotRunningError
import GPIOUtils
import ScannerUtils
import tkinter as tk


class Application(tk.Frame):


    def __init__(self, master, ledPin=4, buzzerPin=5):
        super(Application, self).__init__(master = master)

        self.ledPin = ledPin
        self.buzzerPin = buzzerPin

        GPIOUtils.setAsOutputPin(self.ledPin)
        GPIOUtils.setAsOutputPin(self.ledPin)
        GPIOUtils.setOutputLowOnPin(self.ledPin)
        GPIOUtils.setOutputLowOnPin(self.ledPin)

        self.receivedMacs = []
        self.validMacs = {'3C:7A:8A:F3:DB:F7 Arris Group', 'AC:37:43:A0:07:55 HTC', '76:40:29:64:AF:00 Hooli'}

        self.grid()
        self.grid_rowconfigure(5, weight=1)
        
        for i in range(1, 4):
            self.grid_columnconfigure(i, weight=1)
            
        self.pack_propagate(0)
        self.pack(fill=tk.X, expand=1)

        self.createWidgets()

        self.scanScheduler = BackgroundScheduler()
        self.scanScheduler.add_job(self.singleScan, 'interval', minutes=30)


    def createWidgets(self):

        self.startMonitorBtn = tk.Button(self, text='Start Monitoring', command=self.startMonitoring).grid(row=1, column=1, padx=2, sticky=tk.E)
        self.stopMonitorBtn = tk.Button(self, text='Stop Monitoring', command=self.stopMonitoring).grid(row=1, column=2)
        self.singleScanBtn = tk.Button(self, text='Single Scan', command=self.singleScan).grid(row=1, column=3, sticky=tk.W)

        self.validMacsLbl = tk.Label(self, text='Connected devices MAC addresses:', fg='blue').grid(row=3, column=2, pady=5, sticky=tk.NSEW)
        self.validMacsListbox = tk.Listbox(self, selectmode=tk.SINGLE)

        self.suspMacsLbl = tk.Label(self, text='Suspicious MAC addresses:', fg='red').grid(row=9, column=2, sticky=tk.NSEW)
        self.suspMacsListbox = tk.Listbox(self, selectmode=tk.SINGLE)

        self.validMacsListbox.grid(row=5, column=1, columnspan=3, padx=5, sticky=tk.NSEW)
        self.suspMacsListbox.grid(row=10, column=1, columnspan=3, padx=5, sticky=tk.NSEW)

        self.modifyTaskBtn = tk.Button(self, text="Modify Tasks", command=self.modifyTask).grid(row=7, column=3, padx=5, sticky=tk.NSEW)
        self.addBtn = tk.Button(self, text="Add to Valid", command=self.addToValidMacs).grid(row=11, column=3, padx=5, sticky=tk.NSEW)


    def populateValidInvalidListboxes(self):

        # delete everything from both listboxes
        self.validMacsListbox.delete(0, tk.END)
        self.suspMacsListbox.delete(0,tk.END)

        # iterate through MACs of all devices on network, then identify as trusted or suspicious, then display in corresponding listbox
        for mac in self.receivedMacs:
            if mac in self.validMacs:
                self.validMacsListbox.insert(tk.END, mac)
            else:
                self.suspMacsListbox.insert(tk.END, mac)


    def startMonitoring(self):
        try:
            self.scanScheduler.start()
        except SchedulerAlreadyRunningError:
            print('Already monitoring continuously')

        return


    def stopMonitoring(self):
        try:
            self.scanScheduler.pause()
        except SchedulerNotRunningError:
            print('Already not monitoring continuously')

        return


    def singleScan(self):

        print('scanning...')

        # get MACs of devices on network
        self.receivedMacs = ScannerUtils.getMacAddresses()

        # classify as safe/dangerous and populate corresponding listboxes
        self.populateValidInvalidListboxes()

        # perform appropriate actions (LED/buzzer) according to MACs present
        self.processReceivedMacs()


    def addToValidMacs(self):

        # add the selected device to valid mac addresses list
        self.validMacs.add(self.suspMacsListbox.get(tk.ACTIVE))

        # re-classify and populate listboxes
        self.populateValidInvalidListboxes()


    def processReceivedMacs(self):

        # if there are any suspicious mac addresses then turn on led and sound the buzzer
        if len(self.suspMacsListbox.get(0, tk.END)) != 0:
            GPIOUtils.setOutputHighOnPin(self.ledPin)
            GPIOUtils.setOutputHighOnPin(self.buzzerPin)

        # perform personalized task for each registered user, according to valid macs
        for mac in self.validMacsListbox.get(0, tk.END):
            print('performing tasks for', mac)
            # TODO: actually perform tasks!

    # TODO
    def modifyTask(self):
        return


if __name__=='__main__':

    root = tk.Tk()
    root.title('NetworkBuddy')
    root.geometry('500x500')
    root.resizable(width=False, height=False)

    app = Application(master=root)
    app.mainloop()