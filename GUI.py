import GPIOcontrol
import MacScanner
import tkinter as tk

class Application(tk.Frame):

    def __init__(self, master):
        super(Application, self).__init__(master = master)

        self.receivedMacs = []
        self.validMacs = {'3C:7A:8A:F3:DB:F7 Arris Group', 'AC:37:43:A0:07:55 HTC', '76:40:29:64:AF:00 Hooli'}

        self.grid()
        self.grid_rowconfigure(5, weight=1)
        for i in range(1, 4):
            self.grid_columnconfigure(i, weight=1)
        self.pack_propagate(0)
        self.pack(fill=tk.X, expand=1)

        self.createWidgets()


    def createWidgets(self):
        self.startmBtn = tk.Button(self, text='Start Monitoring', command=self.startMonitoring).grid(row=1, column=1, padx=2, sticky=tk.E)
        self.stopmBtn = tk.Button(self, text='Stop Monitoring', command=self.stopMonitoring).grid(row=1, column=2)
        self.singleScanBtn = tk.Button(self, text='Single Scan', command=self.singleScan).grid(row=1, column=3, sticky=tk.W)

        self.validMacsLbl = tk.Label(self, text='Connected devices MAC addresses:', fg='blue').grid(row=3, column=2, pady=5, sticky=tk.NSEW)
        self.validMacsListbox = tk.Listbox(self, selectmode=tk.SINGLE)

        self.suspMacsLbl = tk.Label(self, text='Suspicious MAC addresses:', fg='red').grid(row=9, column=2, sticky=tk.NSEW)
        self.suspMacsListbox = tk.Listbox(self, selectmode=tk.SINGLE)

        # self.populateValidInvalidListboxes()

        self.validMacsListbox.grid(row=5, column=1, columnspan=3, padx=5, sticky=tk.NSEW)
        self.suspMacsListbox.grid(row=10, column=1, columnspan=3, padx=5, sticky=tk.NSEW)

        self.modifyTaskBtn = tk.Button(self, text="Modify Tasks", command=self.modifyTask).grid(row=7, column=3, padx=5, sticky=tk.NSEW)
        self.addBtn = tk.Button(self, text="Add to Valid", command=self.addToValidMacs).grid(row=11, column=3, padx=5, sticky=tk.NSEW)


    def populateValidInvalidListboxes(self):
        self.validMacsListbox.delete(0, tk.END)
        self.suspMacsListbox.delete(0,tk.END)
        for mac in self.receivedMacs:
            if mac in self.validMacs:
                self.validMacsListbox.insert(tk.END, mac)
            else:
                self.suspMacsListbox.insert(tk.END, mac)


    def startMonitoring(self):
        return


    def stopMonitoring(self):
        return


    def singleScan(self):
        self.receivedMacs = MacScanner.getMacAddresses()
        self.populateValidInvalidListboxes()
        GPIOcontrol.processPresentMacs(self.validMacsListbox.get(0, tk.END))
        return


    def addToValidMacs(self):
        self.validMacs.add(self.suspMacsListbox.get(tk.ACTIVE))
        self.populateValidInvalidListboxes()


    def modifyTask(self):
        return





root = tk.Tk()
root.title('NetworkBuddy')
root.geometry('500x500')    #500x250
root.resizable(width=False, height=False)

app = Application(master=root)
app.mainloop()