import os
import time

print("""
1) Metasploit Yükle

2) Zphisher Yükle



""")
a = input("Kurulumunuzu Yapınız : ")
os.system("apt install figlet -y ")
os.system("clear ")
os.system("figlet SEZER ")
print("Kurulum Başlıyor.... ")
time.sleep(4)

if(a=="1") :
	os.system("apt install git -y ")
	os.system("clear")
	os.system("apt install wget -y ")
	os.system("wget https://github.com/gushmazuko/metasploit_in_termux/raw/master/metasploit.sh ")
	time.sleep(3)
	os.system("chmod +x metasploit.sh ")
	time.sleep(3)
	os.system("./metasploit.sh ")
	time.sleep(3)
	os.system("cd metasploit-framework ")
	time.sleep(3)
	print("Kurulum Tamamlandı..... ")
	os.system("clear ")
	print("Kurulum Bitti Hayırlı İşler... ")
	time.sleep(3)
	os.system("msfconsole ")

	
elif(a=="2") :
	os.system("apt install figlet ")
	os.system("clear ")
	os.system("figlet Sezer")
	print("Kurulum Başlıyor....")
	time.sleep(3)
	os.system("apt install git -y ")
	os.system("clear ")
	time.sleep(2)
	os.system("git clone --depth=1 https://github.com/htr-tech/zphisher.git ")
	time.sleep(3)
	os.system("clear ")
	time.sleep(3)
	os.system("cd zphisher ")
	time.sleep(3)

	
else :
	print("Lutfen Doğru Seçim Yapînîz")

	