import sys
sys.path.append('../')
import time
from ph_ads import ADS1115
ADS1115_REG_CONFIG_PGA_6_144V        = 0x00 # 6.144V range = Gain 2/3
ADS1115_REG_CONFIG_PGA_4_096V        = 0x02 # 4.096V range = Gain 1
ADS1115_REG_CONFIG_PGA_2_048V        = 0x04 # 2.048V range = Gain 2 (default)
ADS1115_REG_CONFIG_PGA_1_024V        = 0x06 # 1.024V range = Gain 4
ADS1115_REG_CONFIG_PGA_0_512V        = 0x08 # 0.512V range = Gain 8
ADS1115_REG_CONFIG_PGA_0_256V        = 0x0A # 0.256V range = Gain 16
ads1115 = ADS1115()

def ph(number):
 print(number)
 if (number <= 0):print("Ph value is:0")
 elif (285<number<=1342):print("ph value is 1")
 elif (228<number<=285):print("ph value is 2")
 elif (171<number<=228):print("ph value is 3")
 elif (114<number<=171):print("ph value is 4")
 elif (57<number<=114):print("ph value is 5")
 elif (0<number<=157):print("ph value is 6")
 elif(-57<number<=0):print("ph value is 7")
 elif(-114<number<=-57):print("ph value is 8")
 elif(-171<number<=-114):print("ph value is 9")
 elif(-228<number<=-171):print("ph value is 10")
 elif(-285<number<=-228):print("ph value is 11")
 elif(-342<number<=-285):print("ph value is 12")
 elif(-400<number<-342):print("ph value is 13")
 elif(number>-400):print("ph  value is 14")
while True :
    #Set the IIC address
 ads1115.setAddr_ADS1115(0x48)
    #Sets the gain and input voltage range.
 ads1115.setGain(ADS1115_REG_CONFIG_PGA_6_144V)
    #Get the Digital Value of Analog of selected channel
 adc0 = ads1115.readVoltage(0)
 for k,v in adc0.items():
  p=v*5/1024+0.05
  p=3.5*p+30	
  ph(p)
  time.sleep(0.2)

