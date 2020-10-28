# coding=utf-8

from tkinter import *
from tkinter.ttk import Combobox
import serial.tools.list_ports
from tkinter.scrolledtext import ScrolledText
import json
import time
import threading
from tkinter.messagebox import showinfo, askokcancel
from functools import wraps


def retry(times):
    def wrapper_fn(f):
        @wraps(f)
        def new_wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    print('try %s' % (i + 1))
                    return f(*args, **kwargs)
                except Exception as e:
                    if i < 50:
                        time.sleep(1)
                    else:
                        time.sleep(3)
                    error = e
            raise error

        return new_wrapper

    return wrapper_fn


class Ser(object):
    def __init__(self, port, baudrate, parity):
        # self.port = serial.Serial(port=port, baudrate=9600, bytesize=8, parity="E", stopbits=1, timeout=2)
        self.port = serial.Serial(port=port, baudrate=baudrate, bytesize=8, parity=parity, stopbits=1, timeout=2)

    # 发送指令的完整流程
    def send_cmd(self, cmd):
        if type(cmd) == dict:
            cmd = json.dumps(cmd).encode()
        elif type(cmd) == str:
            cmd = str.encode(cmd)
        if type(cmd) != bytes:
            print("command is not validate")
            return None
        print("cmd is: ", cmd)

        length = self.port.write(cmd)
        print("cmd length is: ", length)

        response = self.port.readall()
        print("response is: ", response)

        if type(response) == bytes:
            response = response.decode()
        try:
            response = json.loads(response)
        except Exception as e:
            response = {}
            print("convert json string to dict error: ", e)

        return response

    def send_only(self, cmd):
        if type(cmd) == dict:
            cmd = json.dumps(cmd).encode()
        elif type(cmd) == str:
            cmd = str.encode(cmd)
        if type(cmd) != bytes:
            print("command is not validate")
            return None
        print("cmd is: ", cmd)

        length = self.port.write(cmd)
        print("cmd length is: ", length)

    @retry(100)
    def read_next(self):
        response = self.port.read_until(terminator=b"\r\n")
        print("response is: ", response)
        if response == '':
            raise Exception("response is none")

        if type(response) == bytes:
            response = response.decode()

        try:
            response = response[:-2]
            response = json.loads(response)
        except Exception as e:
            print("convert json string to dict error: ", e)
            raise e

        print("real response is: ", response)
        return response

    def close(self):
        self.port.close()


class Application(object):
    def __init__(self, master=None, ser=None, port_devices=None):
        self.master = master
        self.ser = ser
        self.rs485_ser = None

        self.left_frame = Frame(master, height=40, width=50)
        self.right_frame = Frame(master, height=400, width=250)
        self.rs485_frame = Frame(master)
        self.left_frame.grid(row=0, column=0)
        self.right_frame.grid(row=0, column=1)
        # self.right_frame.grid_propagate(0)
        self.rs485_frame.grid(row=0, column=2)

        self.port_label = Label(self.left_frame, text="IR port:")
        self.port_combobox = Combobox(self.left_frame)
        self.port_combobox["value"] = port_devices
        self.port_label.grid(row=0, column=0, sticky=W + E)
        self.port_combobox.grid(row=0, column=1, sticky=W + E)
        self.open_btn = Button(self.left_frame, text="open", command=self.open)
        self.close_btn = Button(self.left_frame, text="close", command=self.close)
        self.open_btn.grid(columnspan=2, sticky=W + E)
        self.close_btn.grid(columnspan=2, sticky=W + E)

        self.traceability_num_label = Label(self.left_frame, text='Traceability Num')
        self.traceability_num_entry = Entry(self.left_frame, text='WC02')
        self.traceability_num_label.grid(row=3, column=0, sticky=W + E)
        self.traceability_num_entry.grid(row=3, column=1, sticky=W + E)

        self.identify_btn = Button(self.left_frame, text="identify type", command=self.identify, state=DISABLED)
        self.identify_btn.grid(columnspan=2, sticky=W + E)

        self.identify_v = StringVar()
        self.cr817295_rdbtn = Radiobutton(self.left_frame, text='cr817295', variable=self.identify_v,
                                          value='cr817295', state=DISABLED)
        self.cr817295_rdbtn.grid(row=5, column=0, sticky=W + E)
        self.cr817296_rdbtn = Radiobutton(self.left_frame, text='cr817296', variable=self.identify_v,
                                          value='cr817296', state=DISABLED)
        self.cr817296_rdbtn.grid(row=5, column=1, sticky=W + E)

        self.interval_lable = Label(self.left_frame, text="Interval Time:")
        self.interval_combobox = Combobox(self.left_frame)
        self.interval_combobox["value"] = (2, 3, 5, 8, 10)
        self.interval_combobox.current(2)
        self.interval_lable.grid(row=6, column=0, sticky=W + E)
        self.interval_combobox.grid(row=6, column=1, sticky=W + E)

        self.start_test_btn = Button(self.left_frame, text='Start Self Test', command=self.start_test_thread,
                                     state=DISABLED)
        self.start_test_btn.grid(column=0, columnspan=2, sticky=W + E)

        self.stop_test_btn = Button(self.left_frame, text='Stop Self Test', command=self.stop_test, state=DISABLED)
        self.stop_test_btn.grid(column=0, columnspan=2, sticky=W + E)

        self.save_btn = Button(self.left_frame, text='Save', command=self.save, )
        self.save_btn.grid(column=0, columnspan=2, sticky=W + E)

        self.info_text = ScrolledText(master, height=30, width=95)
        self.info_text.grid(row=1, columnspan=3)

        self.test_item_label = Label(self.right_frame, text='Test Item')
        self.pass_label = Label(self.right_frame, text="OK")
        self.not_pass_label = Label(self.right_frame, text="NOK")
        self.test_item_label.grid(row=0, column=0, sticky=W + E)
        self.pass_label.grid(row=0, column=1, sticky=W + E)
        self.not_pass_label.grid(row=0, column=2, sticky=W + E)

        self.white_led_v = StringVar()
        self.white_led_label = Label(self.right_frame, text='White Led Test')
        self.white_led_pass = Radiobutton(self.right_frame, value="Success", variable=self.white_led_v)
        self.white_led_fail = Radiobutton(self.right_frame, value="Fail", variable=self.white_led_v)
        self.white_led_label.grid(row=1, column=0)
        self.white_led_pass.grid(row=1, column=1)
        self.white_led_fail.grid(row=1, column=2)

        self.red_led_v = StringVar()
        self.red_led_label = Label(self.right_frame, text='Red Led Test')
        self.red_led_pass = Radiobutton(self.right_frame, value="Success", variable=self.red_led_v)
        self.red_led_fail = Radiobutton(self.right_frame, value="Fail", variable=self.red_led_v)
        self.red_led_label.grid(row=2, column=0)
        self.red_led_pass.grid(row=2, column=1)
        self.red_led_fail.grid(row=2, column=2)

        self.buzzer_v = StringVar()
        self.buzzer_label = Label(self.right_frame, text='Buzzer Test')
        self.buzzer_pass = Radiobutton(self.right_frame, value="Success", variable=self.buzzer_v)
        self.buzzer_fail = Radiobutton(self.right_frame, value="Fail", variable=self.buzzer_v)
        self.buzzer_label.grid(row=3, column=0)
        self.buzzer_pass.grid(row=3, column=1)
        self.buzzer_fail.grid(row=3, column=2)

        self.button_v = StringVar()
        self.button_label = Label(self.right_frame, text='Button Test')
        self.button_pass = Radiobutton(self.right_frame, value="Success", variable=self.button_v)
        self.button_fail = Radiobutton(self.right_frame, value="Fail", variable=self.button_v)
        self.button_label.grid(row=4, column=0)
        self.button_pass.grid(row=4, column=1)
        self.button_fail.grid(row=4, column=2)

        self.remote_output_v = StringVar()
        self.remote_output_label = Label(self.right_frame, text='Remote Output Test')
        self.remote_output_pass = Radiobutton(self.right_frame, value="Success", variable=self.remote_output_v)
        self.remote_output_fail = Radiobutton(self.right_frame, value="Fail", variable=self.remote_output_v)
        self.remote_output_label.grid(row=5, column=0)
        self.remote_output_pass.grid(row=5, column=1)
        self.remote_output_fail.grid(row=5, column=2)

        self.rfid_v = StringVar()
        self.rfid_label = Label(self.right_frame, text='RFID Test')
        self.rfid_pass = Radiobutton(self.right_frame, value="Success", variable=self.rfid_v)
        self.rfid_fail = Radiobutton(self.right_frame, value="Fail", variable=self.rfid_v)
        self.rfid_label.grid(row=6, column=0)
        self.rfid_pass.grid(row=6, column=1)
        self.rfid_fail.grid(row=6, column=2)

        self.eeprom_v = StringVar()
        self.eeprom_label = Label(self.right_frame, text='EEPROM Test')
        self.eeprom_pass = Radiobutton(self.right_frame, value="Success", variable=self.eeprom_v)
        self.eeprom_fail = Radiobutton(self.right_frame, value="Fail", variable=self.eeprom_v)
        self.eeprom_label.grid(row=7, column=0)
        self.eeprom_pass.grid(row=7, column=1)
        self.eeprom_fail.grid(row=7, column=2)

        self.fram_v = StringVar()
        self.fram_label = Label(self.right_frame, text='FRAM Test')
        self.fram_pass = Radiobutton(self.right_frame, value="Success", variable=self.fram_v)
        self.fram_fail = Radiobutton(self.right_frame, value="Fail", variable=self.fram_v)
        self.fram_label.grid(row=8, column=0)
        self.fram_pass.grid(row=8, column=1)
        self.fram_fail.grid(row=8, column=2)

        self.modbus_v = StringVar()
        self.modbus_label = Label(self.right_frame, text='Internal Modbus Test')
        self.modbus_pass = Radiobutton(self.right_frame, value="Success", variable=self.modbus_v)
        self.modbus_fail = Radiobutton(self.right_frame, value="Fail", variable=self.modbus_v)
        self.modbus_label.grid(row=9, column=0)
        self.modbus_pass.grid(row=9, column=1)
        self.modbus_fail.grid(row=9, column=2)

        self.rs485_v = StringVar()
        self.rs485_label = Label(self.right_frame, text='RS485 Test')
        self.rs485_pass = Radiobutton(self.right_frame, value="Success", variable=self.rs485_v)
        self.rs485_fail = Radiobutton(self.right_frame, value="Fail", variable=self.rs485_v)
        self.rs485_label.grid(row=10, column=0)
        self.rs485_pass.grid(row=10, column=1)
        self.rs485_fail.grid(row=10, column=2)

        self.lte_v = StringVar()
        self.lte_label = Label(self.right_frame, text='4G Test')
        self.lte_pass = Radiobutton(self.right_frame, value="Success", variable=self.lte_v)
        self.lte_fail = Radiobutton(self.right_frame, value="Fail", variable=self.lte_v)
        self.lte_label.grid(row=11, column=0)
        self.lte_pass.grid(row=11, column=1)
        self.lte_fail.grid(row=11, column=2)

        self.remote_input_v = StringVar()
        self.remote_input_lable = Label(self.right_frame, text="Remote Input Test")
        self.remote_input_pass = Radiobutton(self.right_frame, value="Success", variable=self.remote_input_v)
        self.remote_input_fail = Radiobutton(self.right_frame, value="Fail", variable=self.remote_input_v)
        self.remote_input_lable.grid(row=12, column=0)
        self.remote_input_pass.grid(row=12, column=1)
        self.remote_input_fail.grid(row=12, column=2)

        self.rs485_port_label = Label(self.rs485_frame, text="RS485 port:")
        self.rs485_port_combobox = Combobox(self.rs485_frame)
        self.rs485_port_combobox["value"] = port_devices
        self.rs485_port_label.grid(row=0, column=0, sticky=W + E)
        self.rs485_port_combobox.grid(row=0, column=1, sticky=W + E)
        self.rs485_open_btn = Button(self.rs485_frame, text="RS485 open", command=self.rs485_open)
        self.rs485_close_btn = Button(self.rs485_frame, text="RS485 close", command=self.rs485_close)
        self.rs485_open_btn.grid(columnspan=2, sticky=W + E)
        self.rs485_close_btn.grid(columnspan=2, sticky=W + E)
        # self.rs485_send_btn = Button(self.rs485_frame, text="RS485 send", command=self.rs485_send_thread,
        #                              state=DISABLED)
        # self.rs485_send_btn.grid(columnspan=2, sticky=W + E)

    def save(self):
        traceability_num = self.traceability_num_entry.get()
        log_file_name = traceability_num + '.log'
        info_text = self.info_text.get(1.0, END)
        with open(log_file_name, mode='at') as f:
            f.write(info_text)

        title = '#traceability_num,type,white_led,red_led,buzzer,button,remote_output,' \
                'RFID,EEPROM,FRAM,internal_modbus,RS485,LTE,remote_input\n'
        content = traceability_num + ',' + \
                  self.identify_v.get() + ',' + \
                  self.white_led_v.get() + ',' + \
                  self.red_led_v.get() + ',' + \
                  self.buzzer_v.get() + ',' + \
                  self.button_v.get() + ',' + \
                  self.remote_output_v.get() + ',' + \
                  self.rfid_v.get() + ',' + \
                  self.eeprom_v.get() + ',' + \
                  self.fram_v.get() + ',' + \
                  self.modbus_v.get() + ',' + \
                  self.rs485_v.get() + ',' + \
                  self.lte_v.get() + ',' + \
                  self.remote_input_v.get() + '\n'
        csv_file_name = traceability_num + '.csv'
        with open(csv_file_name, mode='at') as f:
            f.write(title)
            f.write(content)
        showinfo(title="save file ok", message="file name as traceability_num.csv, traceability_num.log")
        self.info_text.delete(1.0, END)
        self.white_led_v.set("")
        self.red_led_v.set("")
        self.buzzer_v.set('')
        self.button_v.set('')
        self.remote_output_v.set('')
        self.rfid_v.set('')
        self.eeprom_v.set('')
        self.fram_v.set('')
        self.modbus_v.set('')
        self.rs485_v.set('')
        self.lte_v.set('')
        self.remote_input_v.set('')

    def start_test_thread(self):
        th = threading.Thread(target=self.start_test, args=())
        th.setDaemon(True)
        th.start()

    def start_test(self):
        traceability_num = self.traceability_num_entry.get()
        cmd = {
            "Action": "Config",
            "Command": "CfgEnter",
            "MessageType": 1,
            "Payload": {
                "Key": traceability_num
            }
        }
        resp = self.ser.send_cmd(cmd)
        if resp["Payload"]["Status"] != "Accepted":
            print("enter cfg fail")
            self.info_text.insert(END, "enter cfg fail\n")
            return

        # begin self test and check
        interval_time = self.interval_combobox.get()
        interval_time = int(interval_time)
        led_blk_cycle = 2
        buzzer_beeps = 2
        t_button_cnt = 2
        ro_cycle = 2
        ri_actcnt = 3

        self_test = {
            "Action": "Config",
            "Command": "SelfTest",
            "MessageType": 1,
            "Parameter": {
                "IntervalTime": interval_time,
                "LED_BLK_Cycle": led_blk_cycle,
                "Buzzer_Beeps": buzzer_beeps,
                "T_Button_Cnt": t_button_cnt,
                "RO_Cycle": ro_cycle,
                "RI_ActCnt": ri_actcnt
            }
        }

        self.ser.send_only(self_test)

        while True:
            time.sleep(1)
            self.info_text.see(END)
            try:
                resp = self.ser.read_next()
            except Exception as e:
                break
            if "MessageType" in resp:
                if resp["MessageType"] == "2":
                    if "Payload" in resp and resp["Payload"]["Result"] == "Success":
                        print("self test begin")
                        self.info_text.insert(END, "self test begin\n")
                    else:
                        print("self test end")
                        self.info_text.insert(END, "self test end\n")
                        break

                elif resp["MessageType"] == "3":
                    if "Payload" in resp:
                        payload = resp["Payload"]
                        self.info_text.insert(END, str(payload) + '\n')
                        if "Result" in resp["Payload"] and resp["Payload"]["Item"] == "T_Button":
                            print("T_Button test result: ", resp["Payload"]["Result"])
                            self.button_v.set(resp["Payload"]["Result"])
                        if "Result" in resp["Payload"] and resp["Payload"]["Item"] == "RFID":
                            print("RFID test result: ", resp["Payload"]["Result"])
                            self.rfid_v.set(resp["Payload"]["Result"])
                        if "Result" in resp["Payload"] and resp["Payload"]["Item"] == "EEPROM":
                            print("EEPROM test result: ", resp["Payload"]["Result"])
                            self.eeprom_v.set(resp["Payload"]["Result"])
                        if "Result" in resp["Payload"] and resp["Payload"]["Item"] == "FRAM":
                            print("FRAM test result: ", resp["Payload"]["Result"])
                            self.fram_v.set(resp["Payload"]["Result"])
                        if "Result" in resp["Payload"] and resp["Payload"]["Item"] == "InternalModbus":
                            print("Internal Modbus test result: ", resp["Payload"]["Result"])
                            self.modbus_v.set(resp["Payload"]["Result"])
                        if "Result" in resp["Payload"] and resp["Payload"]["Item"] == "RS485":
                            print("RS485 test result: ", resp["Payload"]["Result"])
                            self.rs485_v.set(resp["Payload"]["Result"])
                        if "Result" in resp["Payload"] and resp["Payload"]["Item"] == "LTE":
                            print("LTE test result: ", resp["Payload"]["Result"])
                            self.lte_v.set(resp["Payload"]["Result"])
                        if "Result" in resp["Payload"] and resp["Payload"]["Item"] == "RemoteInput":
                            print("Remote Input test result: ", resp["Payload"]["Result"])
                            self.remote_input_v.set(resp["Payload"]["Result"])

                        if resp["Payload"]["Item"] == "RS485" and resp['Payload']['Status'] == 'Start':
                            self.rs485_send_thread()

                elif resp["MessageType"] == 2:
                    print("self test end")
                    self.info_text.insert(END, "self test end\n")
                    break

    def stop_test(self):
        self.exit_cfg()
        self.start_test_btn.config(state=DISABLED)
        self.stop_test_btn.config(state=DISABLED)

    def open(self):
        port = self.port_combobox.get()
        if port:
            try:
                ser = Ser(port=port, baudrate=9600, parity='N')
                self.ser = ser
                self.identify_btn.config(state=NORMAL)

            except Exception as e:
                print('open serial error: ', e)
                self.info_text.insert(END, 'open serial error\n')

    def close(self):
        if self.ser:
            self.ser.close()
            self.start_test_btn.config(state=DISABLED)
            self.stop_test_btn.config(state=DISABLED)
            self.identify_btn.config(state=DISABLED)

    def identify(self):
        traceability_num = self.traceability_num_entry.get()
        # get if cr817295(RFID+4G) or cr817296(RS485/Modbus)
        # to justify identify by traceability_num WC0250
        if traceability_num[1:4] == 'C02':
            self.identify_v.set('cr817295')
            self.rs485_label.config(state=DISABLED)
            self.rs485_pass.config(state=DISABLED)
            self.rs485_fail.config(state=DISABLED)
            self.remote_input_lable.config(state=DISABLED)
            self.remote_input_pass.config(state=DISABLED)
            self.remote_input_fail.config(state=DISABLED)
            self.rfid_label.config(state=NORMAL)
            self.rfid_pass.config(state=NORMAL)
            self.rfid_fail.config(state=NORMAL)
            self.lte_label.config(state=NORMAL)
            self.lte_pass.config(state=NORMAL)
            self.lte_fail.config(state=NORMAL)
        elif traceability_num[1:4] == "C03":
            self.identify_v.set('cr817296')
            self.rs485_label.config(state=NORMAL)
            self.rs485_pass.config(state=NORMAL)
            self.rs485_fail.config(state=NORMAL)
            self.remote_input_lable.config(state=NORMAL)
            self.remote_input_pass.config(state=NORMAL)
            self.remote_input_fail.config(state=NORMAL)
            self.rfid_label.config(state=DISABLED)
            self.rfid_pass.config(state=DISABLED)
            self.rfid_fail.config(state=DISABLED)
            self.lte_label.config(state=DISABLED)
            self.lte_pass.config(state=DISABLED)
            self.lte_fail.config(state=DISABLED)
        else:
            print('wrong traceability number')
            self.info_text.insert(END, 'wrong traceability number\n')
            self.start_test_btn.config(state=DISABLED)
            self.stop_test_btn.config(state=DISABLED)
            return
        cmd = {
            "Action": "Config",
            "Command": "CfgEnter",
            "MessageType": 1,
            "Payload": {
                "Key": traceability_num
            }
        }
        resp = self.ser.send_cmd(cmd)

        if "Payload" not in resp or resp["Payload"]["Status"] != "Accepted":
            print("enter cfg fail")
            self.info_text.insert(END, "enter cfg fail\n")
            self.exit_cfg()
            self.start_test_btn.config(state=DISABLED)
            self.stop_test_btn.config(state=DISABLED)
            return

        if self.identify_v.get() == 'cr817295':
            vars_set = {
                "Action": "Config",
                "Command": "VarsSet",
                "MessageType": 1,
                "Payload": {
                    "data": {
                        "StandardType": "GB",
                        "PhaseNum": 1,
                        "PowerPercentage": 100,
                        "UnderVoltsThr": 170,
                        "OverVoltsThr": 260,
                        "OverAmpsThr": 32,
                        "PlugerLifeRecord": 0,
                        "TempOffset": 0,
                        "PcbaOverTempShedThr": 88,
                        "PcbaOverTempStopThr": 98,
                        "PeDetection": "Enable",
                        "RFID": "Enable",
                        "LTE": "Enable",
                        "PanelLock": "Disable",
                        "PCBALock": "Disable",
                        "RS485": "Disable",
                        "PbHwRevision": 2,
                        "CbHwRevision": 2,
                        "TraceabilityNo": "WAAB000104",
                        "CatalogNo": "8EM1310-3DJ05-0GA1",
                        "ConfigDate": 1578990200,
                        "ExModbusAddr": 2
                    }
                }
            }

        elif self.identify_v.get() == 'cr817296':
            vars_set = {
                "Action": "Config",
                "Command": "VarsSet",
                "MessageType": 1,
                "Payload": {
                    "data": {
                        "StandardType": "GB",
                        "PhaseNum": 1,
                        "PowerPercentage": 100,
                        "UnderVoltsThr": 170,
                        "OverVoltsThr": 260,
                        "OverAmpsThr": 32,
                        "PlugerLifeRecord": 0,
                        "TempOffset": 0,
                        "PcbaOverTempShedThr": 88,
                        "PcbaOverTempStopThr": 98,
                        "PeDetection": "Enable",
                        "RFID": "Disable",
                        "LTE": "Disable",
                        "PanelLock": "Disable",
                        "PCBALock": "Disable",
                        "RS485": "Enable",
                        "PbHwRevision": 2,
                        "CbHwRevision": 2,
                        "TraceabilityNo": "WAAB000104",
                        "CatalogNo": "8EM1310-3DJ05-0GA1",
                        "ConfigDate": 1578990200,
                        "ExModbusAddr": 2
                    }
                }
            }

        else:
            print('wrong traceability number')
            self.info_text.insert(END, 'wrong traceability number\n')
            self.exit_cfg()
            self.start_test_btn.config(state=DISABLED)
            self.stop_test_btn.config(state=DISABLED)
            return
        resp = self.ser.send_cmd(vars_set)
        if "Payload" not in resp or resp["Payload"]["Result"] != "Success":
            print("vars set fail")
            self.info_text.insert(END, "vars set fail\n")

        self.exit_cfg()
        self.start_test_btn.config(state=NORMAL)
        self.stop_test_btn.config(state=NORMAL)

    def exit_cfg(self):
        exit_cfg = {
            "Action": "Config",
            "Command": "CfgExit",
            "MessageType": 1,
        }
        resp = self.ser.send_cmd(exit_cfg)
        print('exit cfg response: ', str(resp) + '\n')
        # if resp["Payload"]["Status"] != "Accepted":
        #     print("exit cfg fail")
        #     self.info_text.insert(END, "exit cfg fail\n")
        #     return

    def rs485_open(self):
        port = self.rs485_port_combobox.get()
        if port:
            try:
                ser = Ser(port=port, baudrate=9600, parity='N')
                self.rs485_ser = ser
                # self.rs485_send_btn.config(state=NORMAL)

            except Exception as e:
                print('open rs485 serial error: ', e)
                self.info_text.insert(END, 'open rs485 serial error\n')

    def rs485_close(self):
        if self.rs485_ser:
            self.rs485_ser.close()
            # self.rs485_send_btn.config(state=DISABLED)

    def rs485_send(self):
        """
        >>> y=bytes.fromhex('02100fa500020400000004769f')
        >>> y
        b'\x02\x10\x0f\xa5\x00\x02\x04\x00\x00\x00\x04v\x9f'
        >>> y.hex()
        '02100fa500020400000004769f'
        """
        if self.rs485_ser:
            length = self.rs485_ser.port.write(bytes.fromhex('02100fa500020400000004769f'))
            print("cmd length is: ", length)

            response = self.rs485_ser.port.readall()
            print("response is: ", response)
            if response.hex() == '02100fa5000252cc' or response.hex() == '00100FA5000252CC':
                print('rs485 response correct')
                self.info_text.insert(END, 'rs485 response correct\n')
            else:
                print('rs485 response incorrect')
                self.info_text.insert(END, 'rs485 response incorrect\n')
            self.info_text.see(END)

    def rs485_send_thread(self):
        th = threading.Thread(target=self.rs485_send, args=())
        th.setDaemon(True)
        th.start()

    def on_closing(self):
        if askokcancel("Quit", "Do you want to quit?"):
            print('close serials')
            self.close()
            self.rs485_close()
            self.master.destroy()


if __name__ == '__main__':
    port_list = list(serial.tools.list_ports.comports())
    print(port_list)
    if len(port_list) == 0:
        print("无可用串口")
    else:
        port_devices = []
        for i in port_list:
            port_devices.append(i.device)
        print(port_devices)

        root = Tk()
        app = Application(root, None, port_devices)
        app.master.title("Control Board Self Test APP V1.0")

        root.protocol("WM_DELETE_WINDOW", app.on_closing)
        root.mainloop()
