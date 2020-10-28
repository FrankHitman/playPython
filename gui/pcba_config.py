# coding=utf-8

from tkinter import *
from tkinter.scrolledtext import *
import serial.tools.list_ports
import json
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename


# import crc16


class Ser(object):
    def __init__(self, port, baudrate, parity):
        # self.port = serial.Serial(port=port, baudrate=9600, bytesize=8, parity="E", stopbits=1, timeout=2)
        self.port = serial.Serial(port=port, baudrate=baudrate, bytesize=8, parity=parity, stopbits=1, timeout=10)

    # 发送指令的完整流程
    def send_cmd(self, cmd):

        if type(cmd) == dict:
            cmd = json.dumps(cmd).encode()
        elif type(cmd) == str:
            cmd = str.encode(cmd)
        if type(cmd) != bytes:
            print("command is not validate")
            return None
        print("cmd is ", cmd)

        length = self.port.write(cmd)
        print("cmd length is ", length)

        response = self.port.readall()
        print("response is ", response)

        if type(response) == bytes:
            response = response.decode()
        try:
            response = json.loads(response)
        except Exception as e:
            print("convert json string to dict error: ", e)
            response = ""

        return response

    def close(self):
        self.port.close()


class Application:
    def __init__(self, master=None, ser=None, port_devices=None):
        self.master = master
        self.ser = ser

        self.text = ScrolledText(master, height=30, width=100)
        self.text.grid(row=0, column=0, columnspan=2)

        self.get_vars_btn = Button(master, text="Get Variables", command=self.get_vars, state=DISABLED)
        self.get_vars_btn.grid(row=1, column=1, sticky=W + E)

        self.set_vars_btn = Button(master, text="Set Variables", command=self.set_vars, state=DISABLED)
        self.set_vars_btn.grid(row=1, column=0, sticky=W + E)

        self.enter_cfg_btn = Button(master, text="Enter Config", command=self.enter_cfg, state=DISABLED)
        self.exit_cfg_btn = Button(master, text="Exit Config", command=self.exit_cfg, state=DISABLED)
        self.enter_cfg_btn.grid(row=2, column=0, sticky=W + E)
        self.exit_cfg_btn.grid(row=2, column=1, sticky=W + E)

        self.set_wan_btn = Button(master, text="Set WAN", command=self.set_wan, state=DISABLED)
        self.get_wan_btn = Button(master, text="Get WAN", command=self.get_wan, state=DISABLED)
        self.set_wan_btn.grid(row=3, column=0, sticky=W + E)
        self.get_wan_btn.grid(row=3, column=1, sticky=W + E)

        self.load_cacert_btn = Button(master, text="Load Ca Cert", command=self.load_ca, state=DISABLED)
        self.load_cacert_btn.grid(row=4, column=0, columnspan=2, sticky=W + E)

        self.get_debug_btn = Button(master, text="Get Debug Info", command=self.get_debug_info, state=DISABLED)
        self.get_debug_btn.grid(row=5, columnspan=2, sticky=W + E)

        self.set_meter_btn = Button(master, text="Set Meter Calibration", command=self.set_meter_cal, state=DISABLED)
        self.get_meter_btn = Button(master, text="Get Meter Calibration", command=self.get_meter_cal, state=DISABLED)
        self.set_meter_btn.grid(row=6, column=0, sticky=W + E)
        self.get_meter_btn.grid(row=6, column=1, sticky=W + E)

        self.child_frame = Frame(master)
        self.child_frame.grid(row=7, column=0, columnspan=2)

        self.port_label = Label(self.child_frame, text="port:")
        self.port_combobox = Combobox(self.child_frame)
        self.port_combobox["value"] = port_devices
        self.port_label.grid(row=0, column=0, sticky=W + E)
        self.port_combobox.grid(row=0, column=1, sticky=W + E)

        self.baudrate_lable = Label(self.child_frame, text="baudrate:")
        self.baudrate_combobox = Combobox(self.child_frame)
        self.baudrate_combobox["value"] = (50, 75, 110, 134, 150, 200, 300, 600, 1200, 1800, 2400, 4800,
                                           9600, 19200, 38400, 57600, 115200, 230400, 460800, 500000,
                                           576000, 921600, 1000000, 1152000, 1500000, 2000000, 2500000,
                                           3000000, 3500000, 4000000)
        self.baudrate_combobox.current(12)
        self.baudrate_lable.grid(row=0, column=2, sticky=W + E)
        self.baudrate_combobox.grid(row=0, column=3, sticky=W + E)

        self.parity_lable = Label(self.child_frame, text="parity:")
        self.parity_combobox = Combobox(self.child_frame)
        self.parity_combobox["value"] = ("N", "E", "O")
        self.parity_combobox.current(1)
        self.parity_lable.grid(row=0, column=4, sticky=W + E)
        self.parity_combobox.grid(row=0, column=5, sticky=W + E)

        self.open_btn = Button(self.child_frame, text="open", command=self.open)
        self.close_btn = Button(self.child_frame, text="close", command=self.close)
        self.send_btn = Button(self.child_frame, text="send", command=self.send, state=DISABLED)
        self.open_btn.grid(row=1, column=0, columnspan=2, sticky=W + E)
        self.close_btn.grid(row=1, column=2, columnspan=2, sticky=W + E)
        self.send_btn.grid(row=1, column=4, columnspan=2, sticky=W + E)

    def get_vars(self):
        cmd = {
            "Action": "Config",
            "Command": "VarsGet",
            "MessageType": 1,
        }
        cmd = json.dumps(cmd)
        self.text.delete(1.0, END)
        self.text.insert(END, cmd)

        # resp = self.ser.send_cmd(cmd)
        # if "Payload" in resp:
        #     self.text.delete(1.0, END)
        #     self.text.insert(END, resp["Payload"]["Data"])

    def set_vars(self):
        # data = self.text.get(1.0, END)
        # try:
        #     data = json.loads(data)
        # except Exception as e:
        #     print("convert json string to dict error", e)
        #     return
        cmd = {
            "Action": "Config",
            "Command": "VarsSet",
            "MessageType": 1,
            "Payload": {
                "data": {
                    "StandardType": "GB",
                    "PhaseNum": 3,
                    "PowerPercentage": 100,
                    "UnderVoltsThr": 260,
                    "OverVoltsThr": 176,
                    "OverAmpsThr": 32,
                    "PlugerLifeRecord": 0,
                    "TempOffset": 0,
                    "PcbaOverTempShedThr": 55,
                    "PcbaOverTempStopThr": 75,
                    "PeDetection": "Enable",
                    "RFID": "Enable",
                    "LTE": "Enable",
                    "PanelLock": "Disable",
                    "PCBALock": "Disable",
                    "RS485": "Disable",
                    "PbHwRevision": 2,
                    "CbHwRevision": 2,
                    "TraceabilityNo": "WAAB000101",
                    "CatalogNo": "8EM1310-3DJ05-0GA1",
                    "ConfigDate": 1578990200
                }

            }
        }
        cmd = json.dumps(cmd)
        self.text.delete(1.0, END)
        self.text.insert(END, cmd)

        # resp = self.ser.send_cmd(cmd)
        # if "Payload" in resp:
        #     showinfo(title="Result", message=resp["Payload"])

    def enter_cfg(self):
        cmd = {
            "Action": "Config",
            "Command": "CfgEnter",
            "MessageType": 1,
            "Payload": {
                "Key": "Null"
            }
        }
        cmd = json.dumps(cmd)
        self.text.delete(1.0, END)
        self.text.insert(END, cmd)

    def exit_cfg(self):
        cmd = {
            "Action": "Config",
            "Command": "CfgExit",
            "MessageType": 1,
            "Payload": {
                "Key": "Null"
            }
        }

        cmd = json.dumps(cmd)
        self.text.delete(1.0, END)
        self.text.insert(END, cmd)

    def set_wan(self):
        cmd = {
            "Action": "Config",
            "Command": "WanVarsSet",
            "MessageType": 1,
            "Payload": {
                "Mqtt": {
                    "DomainName": "example.com.cn",
                    "Port": 8883,
                    "CnctEnableSta": "Enable",
                    "TopicSub": "evsecloud/v0.1/tocharger/WAAB000101",
                    "TopicPub": "evsecloud/v0.1/tocloud/WAAB000101"
                }

            }
        }
        cmd = json.dumps(cmd)
        self.text.delete(1.0, END)
        self.text.insert(END, cmd)

    def get_wan(self):
        cmd = {
            "Action": "Config",
            "Command": "WanVarsGet",
            "MessageType": 1,
        }
        cmd = json.dumps(cmd)
        self.text.delete(1.0, END)
        self.text.insert(END, cmd)

    def load_ca(self):

        filename = askopenfilename(initialdir="/", title="Select ca file",
                                   filetypes=(("cert files", "*.cert"), ("pem files", "*.pem"), ("all files", "*.*")))
        with open(filename) as f:

            data = f.read()
            if type(data) == str:
                data = data.encode()
            # crc = crc16.crc16xmodem(data)
            length = len(data)
            cmd = {
                "Action": "Config",
                "Command": "CacertLoad",
                "MessageType": 1,
                "Payload": {
                    "CacertSize": length,
                    "CacertCrc16": "crc"
                    # "CacertCrc16": crc
                }
            }
            self.text.delete(1.0, END)
            self.text.insert(END, cmd)

            resp = self.ser.send_cmd(cmd)

            if "MessageType" in resp and resp["MessageType"] == "3":
                try:
                    if resp["Payload"]["Status"] == "Accepted":
                        resp2 = self.ser.send_cmd(data)
                        if "Payload" in resp2:
                            showinfo(title="Result", message=resp2["Payload"])
                except Exception as e:
                    print("load ca cert error", e)
            else:
                print("load ca cert failed")
        return

    def get_debug_info(self):
        cmd = {
            "Action": "Config",
            "Command": "DebugInfoGet",
            "MessageType": 1,
        }
        cmd = json.dumps(cmd)
        self.text.delete(1.0, END)
        self.text.insert(END, cmd)

    def set_meter_cal(self):
        cmd = {
            "Action": "Config",
            "Command": "MeterCalSet",
            "MessageType": 1,
            "Payload": {
                "CaliVar0": 0,
                "CaliVar1": 0,
                "CaliVar2": 0,
                "CaliVar3": 0,
                "CaliVar4": 0,
                "CaliVar5": 0,
                "CaliVar6": 0,
                "CaliVar7": 0
            }

        }
        cmd = json.dumps(cmd)
        self.text.delete(1.0, END)
        self.text.insert(END, cmd)

    def get_meter_cal(self):
        cmd = {
            "Action": "Config",
            "Command": "MeterCalGet",
            "MessageType": 1,
        }
        cmd = json.dumps(cmd)
        self.text.delete(1.0, END)
        self.text.insert(END, cmd)

    def open(self):
        port = self.port_combobox.get()
        baudrate = self.baudrate_combobox.get()
        parity = self.parity_combobox.get()

        if port and baudrate and parity:
            ser = Ser(port=port, baudrate=baudrate, parity=parity)
            self.ser = ser

            self.get_meter_btn.config(state=NORMAL)
            self.set_meter_btn.config(state=NORMAL)
            self.get_vars_btn.config(state=NORMAL)
            self.set_vars_btn.config(state=NORMAL)
            self.get_debug_btn.config(state=NORMAL)
            self.load_cacert_btn.config(state=NORMAL)
            self.get_wan_btn.config(state=NORMAL)
            self.set_wan_btn.config(state=NORMAL)
            self.exit_cfg_btn.config(state=NORMAL)
            self.enter_cfg_btn.config(state=NORMAL)
            self.send_btn.config(state=NORMAL)

    def close(self):
        if self.ser:
            self.ser.close()
            self.get_meter_btn.config(state=DISABLED)
            self.set_meter_btn.config(state=DISABLED)
            self.get_vars_btn.config(state=DISABLED)
            self.set_vars_btn.config(state=DISABLED)
            self.get_debug_btn.config(state=DISABLED)
            self.load_cacert_btn.config(state=DISABLED)
            self.get_wan_btn.config(state=DISABLED)
            self.set_wan_btn.config(state=DISABLED)
            self.exit_cfg_btn.config(state=DISABLED)
            self.enter_cfg_btn.config(state=DISABLED)
            self.send_btn.config(state=DISABLED)

    def send(self):
        data = self.text.get(1.0, END)
        try:
            data = json.loads(data)
        except Exception as e:
            print("convert json string to dict error", e)
            return

        resp = self.ser.send_cmd(data)
        self.text.delete(1.0, END)
        self.text.insert(END, resp)

        # if "Payload" in resp:
        #     showinfo(title="Result", message=resp["Payload"])


if __name__ == "__main__":

    port_list = list(serial.tools.list_ports.comports())
    print(port_list)
    if len(port_list) == 0:
        print("无可用串口")
    else:
        port_devices = []
        for i in port_list:
            port_devices.append(i.device)

        print(port_devices)
        # ser = Ser(port_list[0].device)
        # ser.close()

        root = Tk()
        app = Application(root, None, port_devices)
        app.master.title("PCBA Configuration APP V0.1")

        root.mainloop()
