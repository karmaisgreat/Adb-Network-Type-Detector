import os,platform,time
detected_os = platform.system()
if 'Windows' in detected_os:
    print('\nWindows OS Detected!\n')
    while True:
        cmd0 = "platform-tools_r29.0.5-windows\\adb.exe shell dumpsys telephony.registry > logging.txt"
        os.system(cmd0)
        fin = open('logging.txt', "r")
        data_list = fin.readlines()
        fin.close()
        fout = open("logging.txt", "w")
        fout.writelines(data_list[:5])
        fout.close()
        if 'mRilDataRadioTechnology=2(EDGE)' in open('logging.txt').read():
            print('EDGE DETECTED!')
        elif 'mRilDataRadioTechnology=3(UMTS)' in open('logging.txt').read():
            print('UMTS DETECTED!')
        elif 'mRilDataRadioTechnology=9(HSDPA)' in open('logging.txt').read():
            print('HSDPA DETECTED!')
        elif 'mRilDataRadioTechnology=11(HSPA)' in open('logging.txt').read():
            print('HSPA DETECTED!')
        elif 'mRilDataRadioTechnology=15(HSPAP)' in open('logging.txt').read():
            print('HSPAP DETECTED!')
        elif 'mRilDataRadioTechnology=14(LTE)' in open('logging.txt').read():
            print('LTE DETECTED!')
        else:
            print('UNKNOWN NETWORK!')
        time.sleep(2)
        
elif 'Linux' in detected_os:
    print('\nLinux OS Detected!\n')
    while True:
        cmd0 = "platform-tools_r29.0.5-linux\\adb dumpsys telephony.registry > logging.txt"
        os.system(cmd0)
        fin = open('logging.txt', "r")
        data_list = fin.readlines()
        fin.close()
        fout = open("logging.txt", "w")
        fout.writelines(data_list[:5])
        fout.close()
        if 'mRilDataRadioTechnology=2(EDGE)' in open('logging.txt').read():
            print('EDGE DETECTED!')
        elif 'mRilDataRadioTechnology=3(UMTS)' in open('logging.txt').read():
            print('UMTS DETECTED!')
        elif 'mRilDataRadioTechnology=11(HSPA)' in open('logging.txt').read():
            print('HSPA DETECTED!')
        elif 'mRilDataRadioTechnology=15(HSPAP)' in open('logging.txt').read():
            print('HSPAP DETECTED!')
        elif 'mRilDataRadioTechnology=14(LTE)' in open('logging.txt').read():
            print('LTE DETECTED!')
        else:
            print('UNKNOWN NETWORK!')
        time.sleep(2)
else:
    print('\nUnknown OS Detected!\n')
    exit()