import sys
import time
import serial
import logging
import struct
import threading
import Queue
import sqlite3
import serial
import dwopenmqtt
import os

from threading import Thread
from time import sleep

global tagA		#set counter as global variable
global tagB
global tagC
global tagD
global tagE
global tagF
global tagG
global tagH
			
global tagA1		#set counter as global variable
global tagB1
global tagC1
global tagD1
global tagE1
global tagF1
global tagG1
global tagH1


tagA =0
tagB =0
tagC =0
tagD =0
tagE =0
tagF =0
tagG =0
tagH =0

tagA1 =0
tagB1 =0
tagC1 =0
tagD1 =0
tagE1 =0
tagF1 =0
tagG1 =0
tagH1 =0

count = 0
header=None
x=None
y=None
m=None

tagA_count=True
tagB_count=True
tagC_count=True
tagD_count=True
tagE_count=True
tagF_count=True
tagG_count=True
tagH_count=True

tagA1_count=True
tagB1_count=True
tagC1_count=True
tagD1_count=True
tagE1_count=True
tagF1_count=True
tagG1_count=True
tagH1_count=True


# dwM2M Developer Community Assigned Tokens...
dwApiURL    = "http://api.devicewise.com/api";
dwApiHost   = "api.devicewise.com";

# dwOpen Member/Thing Assigned Tokens...
dwAppToken1  = "iD5QHSS0YmcFzNXD";

dwThingKey1  = "pi_rfid";

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
)

def userCallBack( MsgID, MethodName, ParamText ):
	if( MethodName == "reset" ):
			print "*** Counter reset"
			
			tagA = 0	#reset counter to 0
			tagB = 0
			tagC = 0
			tagD = 0
			tagE = 0
			tagF = 0
			tagG = 0
			tagH = 0
			
			tagA1 = 0	#reset counter to 0
			tagB1 = 0
			tagC1 = 0
			tagD1 = 0
			tagE1 = 0
			tagF1 = 0
			tagG1 = 0
			tagH1 = 0
			
			rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_A_Counter", tagA )		#publish counter value to cloud
			rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_B_Counter", tagB )
			rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_C_Counter", tagC )
			rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_D_Counter", tagD )
			rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_E_Counter", tagE )
			rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_F_Counter", tagF )
			rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_G_Counter", tagG )
			rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_H_Counter", tagH )
			#dwopen.dwMailboxAck( MsgID, 0, '', '' );
			
			rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_A1_Counter", tagA1 )		#publish counter value to cloud
			rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_B1_Counter", tagB1 )
			rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_C1_Counter", tagC1 )
			rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_D1_Counter", tagD1 )
			rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_E1_Counter", tagE1 )
			rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_F1_Counter", tagF1 )
			rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_G1_Counter", tagG1 )
			rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_H1_Counter", tagH1 )
			dwopen.dwMailboxAck( MsgID, 0, '', '' );
	return;
	
   #timer for antenna 2
def timerA1():
   global tagA1_count
   for i in range(3):
		sleep(1)   #waits 5 seconds
   print"finish count tagA set back to True"
   tagA1_count=True
   return;
   
def timerB1():
   global tagB1_count
   for i in range(3):
		sleep(1)   #waits 5 seconds
   print"finish count tagB set back to True"
   tagB1_count=True
   return;

def timerC1():
   global tagC1_count
   for i in range(3):
		sleep(1)   #waits 5 seconds
   print"finish count tagC set back to True"
   tagC1_count=True
   return;
   
def timerD1():
   global tagD1_count
   for i in range(3):
		sleep(1)   #waits 5 seconds
   print"finish count tagD set back to True"
   tagD1_count=True
   return;
   
def timerE1():
   global tagE1_count
   for i in range(3):
		sleep(1)   #waits 5 seconds
   print"finish count tagE set back to True"
   tagE1_count=True
   return;

 def timerF1():
	global tagF1_count
   for i in range(3):
		sleep(1)   #waits 5 seconds
   print"finish count tagE set back to True"
   tagF1_count=True
   return;

def timerG1():
   global tagG1_count
   for i in range(3):
		sleep(1)   #waits 5 seconds
   print"finish count tagE set back to True"
   tagG1_count=True
   return;
   
def timerH1():
   global tagH1_count
   for i in range(3):
		sleep(1)   #waits 5 seconds
   print"finish count tagE set back to True"
   tagH1_count=True
   return;
   
   
   #timer for antenna 4
def timerA():
   global tagA_count
   for i in range(3):
		sleep(1)   #waits 5 seconds
   print"finish count tagA set back to True"
   tagA_count=True
   return;
   
def timerB():
   global tagB_count
   for i in range(3):
		sleep(1)   #waits 5 seconds
   print"finish count tagB set back to True"
   tagB_count=True
   return;

def timerC():
   global tagC_count
   for i in range(3):
		sleep(1)   #waits 5 seconds
   print"finish count tagC set back to True"
   tagC_count=True
   return;
   
def timerD():
   global tagD_count
   for i in range(3):
		sleep(1)   #waits 5 seconds
   print"finish count tagD set back to True"
   tagD_count=True
   return;
   
def timerE():
   global tagE_count
   for i in range(3):
		sleep(1)   #waits 5 seconds
   print"finish count tagE set back to True"
   tagE_count=True
   return;
   
 def timerF():
	global tagF_count
   for i in range(3):
		sleep(1)   #waits 5 seconds
   print"finish count tagE set back to True"
   tagF_count=True
   return;

def timerG():
   global tagG_count
   for i in range(3):
		sleep(1)   #waits 5 seconds
   print"finish count tagE set back to True"
   tagG_count=True
   return;
   
def timerH():
   global tagH_count
   for i in range(3):
		sleep(1)   #waits 5 seconds
   print"finish count tagE set back to True"
   tagH_count=True
   return;
    	
   

def MQTTCONNECT():

#------------------------------------------------
#-- Connect to m2mAIR Cloud Server
#------------------------------------------------
	print("Connect to m2mAIR Cloud Server...")


	msgText  = "Python MQTT Edge Device... Connected and Active!"


	rc = dwopen.mqttConnect( dwApiHost, dwThingKey1, dwAppToken1, userCallBack);
	print "dwOpen API - MQTT Connect Returned... rc = ", rc
	print("Waiting 3 Seconds...")
	time.sleep( 3 )

	rc = dwopen.dwLogPublish( dwThingKey1, msgText );
	print "dwOpen API - Log Publish Returned... rc = ", rc
	time.sleep( 2 )


	print("Begin Publishing Requests to m2mAIR Cloud Server...")
	
#------------------------------------------------
#-- Log Publish
#------------------------------------------------
print("Load dwOpenMQTT Library...")
dwopen = dwopenmqtt.dwOpen();
print("dwOpenMQTT Library Loaded...")	
MQTTCONNECT();


bytesToRead = ser.inWaiting()
#ser.read(bytesToRead)
print(str(ser.read(bytesToRead)).encode('hex'))


#start antenna 1-4
print("starting antenna 1-4")
thestring = "\x00\x04\x82\x00\x07\x01\xBB\xD9"
ser.isOpen()
ser.write(thestring);
bytesReturn = ser.inWaiting()
print(str(ser.read(bytesReturn)).encode('hex')) 

'''
sleep(2)
#start antenna 1-4
print("starting antenna 1-4")
thestring1 = "\x00\x04\x82\x00\x07\x01\xbb\xd9"
print(thestring1)
ser.isOpen()
ser.write(thestring1);
bytesReturn1 = ser.inWaiting()
print(str(ser.read(bytesReturn1)).encode('hex')) 
'''

print("Initialising message cleared. Start reading!")	
while (1):
	#time.sleep(0.5)
	header = str(ser.read(1).encode('hex'))
	#print(header)
	if header == "55":	
		x = str(ser.read(4).encode('hex')) #read before antenna number 04
		#print x
		y=ser.read(1)
		#print y.encode('hex')
		antennaNumber=ord(y)
		#print antennaNumber
		z = str(ser.read(12).encode('hex')) #read antenna number
		#print z
		
		if antennaNumber==4:
		
			if z == "e2801130200028ee7c820212":
				if tagA_count==False:
					print"tagA_count is false"
				else:   
					tagA +=1
					os.system("sudo aplay /home/pi/beep-06_short.wav")
					if tagA==101:
						tagA=1
						print ("Tag A Counter= "+(str(tagA)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_A_Counter", tagA )
						print "dwOpen API - Property Publish Returned... rc = ", rc

						
					else:	
						print ("Tag A Counter= "+(str(tagA)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_A_Counter", tagA )
						print "dwOpen API - Property Publish Returned... rc = ", rc
					
				tagA_count=False
				print"Timer starts counting"
				t1 = Thread(target=timerA) #starts counting
				t1.start() #Calls first function, counte for 3s 
			
			
			
			if z == "e2801130200024ae7c750212":
				if tagB_count==False:
					print"tagB_count is false"
				else:
					tagB +=1
					os.system("sudo aplay /home/pi/beep-06_short.wav")
					if tagB==101:
						tagB=1
						print ("Tag B Counter= "+(str(tagB)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_B_Counter", tagB )
						print "dwOpen API - Property Publish Returned... rc = ", rc
					
					else:	
						print ("Tag B Counter= "+(str(tagB)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_B_Counter", tagB )
						print "dwOpen API - Property Publish Returned... rc = ", rc
					
				tagB_count=False
				print"Timer starts counting"
				t2 = Thread(target=timerB) #starts counting
				t2.start() #Calls first function, counte for 3s 
				
					
						
			if z == "e2801130200020cd7c920212":
				if tagC_count==False: 
					print"tagC_count is false"
				else:
					tagC +=1
					os.system("sudo aplay /home/pi/beep-06_short.wav")
					if tagC==101:
						tagC=1
						print ("Tag C Counter= "+(str(tagC)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_C_Counter", tagC )
						print "dwOpen API - Property Publish Returned... rc = ", rc
						
					else:	
						print ("Tag C Counter= "+(str(tagC)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_C_Counter", tagC )
						print "dwOpen API - Property Publish Returned... rc = ", rc
						
				tagC_count=False
				print"Timer starts counting"
				t3 = Thread(target=timerC) #starts counting 
				t3.start() #Calls first function, counte for 3s 
				
			if z == "e2801130200024be7c750212":
				if tagD_count==False: 
					print"tagD_count is false"
				else:
					tagD +=1
					os.system("sudo aplay /home/pi/beep-06_short.wav")
					if tagD==101:
						tagD=1
						print ("Tag D Counter= "+(str(tagD)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_D_Counter", tagD )
						print "dwOpen API - Property Publish Returned... rc = ", rc
						
					else:	
						print ("Tag D Counter= "+(str(tagD)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_D_Counter", tagD )
						print "dwOpen API - Property Publish Returned... rc = ", rc
					
				tagD_count=False
				print"Timer starts counting"
				t4 = Thread(target=timerD) #starts counting 
				t4.start() #Calls first function, counte for 3s 
					
			if z == "e28011302000289d7c820212":
				if tagE_count==False:
					print"tagE_count is false"
				else:
					tagE +=1
					os.system("sudo aplay /home/pi/beep-06_short.wav")
					if tagE==101:
						tagE=1
						print ("Tag E Counter= "+(str(tagE)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_E_Counter", tagE )
						print "dwOpen API - Property Publish Returned... rc = ", rc
						
					else:	
						print ("Tag E Counter= "+(str(tagE)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_E_Counter", tagE )
						print "dwOpen API - Property Publish Returned... rc = ", rc
					
				tagE_count=False
				print"Timer starts counting"
				t5 = Thread(target=timerE) #starts counting
				t5.start() #Calls first function, counte for 3s
				
				
			if z == "e28011302000281D7CB80212E95F":
				if tagF_count==False:
					print"tagF_count is false"
				else:
					tagF +=1
					os.system("sudo aplay /home/pi/beep-06_short.wav")
					if tagF==101:
						tagF=1
						print ("Tag F Counter= "+(str(tagF)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_F_Counter", tagF )
						print "dwOpen API - Property Publish Returned... rc = ", rc
						
					else:	
						print ("Tag F Counter= "+(str(tagF)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_F_Counter", tagF )
						print "dwOpen API - Property Publish Returned... rc = ", rc
					
				tagF_count=False
				print"Timer starts counting"
				t6 = Thread(target=timerE) #starts counting
				t6.start() #Calls first function, counte for 3s
				
			if z == "e2801130200020ED7C92021201DD":
				if tagG_count==False:
					print"tagG_count is false"
				else:
					tagG +=1
					os.system("sudo aplay /home/pi/beep-06_short.wav")
					if tagG==101:
						tagG=1
						print ("Tag G Counter= "+(str(tagG)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_G_Counter", tagG )
						print "dwOpen API - Property Publish Returned... rc = ", rc
						
					else:	
						print ("Tag G Counter= "+(str(tagG)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_G_Counter", tagG )
						print "dwOpen API - Property Publish Returned... rc = ", rc
					
				tagG_count=False
				print"Timer starts counting"
				t7 = Thread(target=timerG) #starts counting
				t7.start() #Calls first function, counte for 3s
				
			if z == "E28011302000280D7CBB02126EDC":
				if tagH_count==False:
					print"tagH_count is false"
				else:
					tagH +=1
					os.system("sudo aplay /home/pi/beep-06_short.wav")
					if tagH==101:
						tagH=1
						print ("Tag H Counter= "+(str(tagH)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_H_Counter", tagH )
						print "dwOpen API - Property Publish Returned... rc = ", rc
						
					else:	
						print ("Tag H Counter= "+(str(tagH)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_H_Counter", tagH )
						print "dwOpen API - Property Publish Returned... rc = ", rc
					
				tagH_count=False
				print"Timer starts counting"
				t8 = Thread(target=timerE) #starts counting
				t8.start() #Calls first function, counte for 3s
				
				
	if antennaNumber==2:
		
			if z == "e2801130200028ee7c820212":
				if tagA1_count==False:
					print"tagA1_count is false"
				else:   
					tagA1 +=1
					os.system("sudo aplay /home/pi/beep-06_short.wav")
					if tagA1==101:
						tagA1=1
						print ("Tag A1 Counter= "+(str(tagA1)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_A1_Counter", tagA1 )
						print "dwOpen API - Property Publish Returned... rc = ", rc

						
					else:	
						print ("Tag A1 Counter= "+(str(tagA1)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_A1_Counter", tagA1 )
						print "dwOpen API - Property Publish Returned... rc = ", rc
					
				tagA1_count=False
				print"Timer starts counting"
				t9 = Thread(target=timerA1) #starts counting
				t9.start() #Calls first function, counte for 3s 
			
			
			
			if z == "e2801130200024ae7c750212":
				if tagB1_count==False:
					print"tagB1_count is false"
				else:
					tagB1 +=1
					os.system("sudo aplay /home/pi/beep-06_short.wav")
					if tagB1==101:
						tagB1=1
						print ("Tag B1 Counter= "+(str(tagB1)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_B1_Counter", tagB1 )
						print "dwOpen API - Property Publish Returned... rc = ", rc
					
					else:	
						print ("Tag B1 Counter= "+(str(tagB1)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_B1_Counter", tagB1 )
						print "dwOpen API - Property Publish Returned... rc = ", rc
					
				tagB1_count=False
				print"Timer starts counting"
				t10 = Thread(target=timerB1) #starts counting
				t10.start() #Calls first function, counte for 3s 
				
					
						
			if z == "e2801130200020cd7c920212":
				if tagC1_count==False: 
					print"tagC1_count is false"
				else:
					tagC1 +=1
					os.system("sudo aplay /home/pi/beep-06_short.wav")
					if tagC1==101:
						tagC1=1
						print ("Tag C1 Counter= "+(str(tagC1)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_C_Counter", tagC1 )
						print "dwOpen API - Property Publish Returned... rc = ", rc
						
					else:	
						print ("Tag C1 Counter= "+(str(tagC1)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_C1_Counter", tagC1 )
						print "dwOpen API - Property Publish Returned... rc = ", rc
						
				tagC1_count=False
				print"Timer starts counting"
				t11 = Thread(target=timerC1) #starts counting 
				t11.start() #Calls first function, counte for 3s 
				
			if z == "e2801130200024be7c750212":
				if tagD1_count==False: 
					print"tagD_count is false"
				else:
					tagD1 +=1
					os.system("sudo aplay /home/pi/beep-06_short.wav")
					if tagD1==101:
						tagD1=1
						print ("Tag D1 Counter= "+(str(tagD1)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_D_Counter", tagD1 )
						print "dwOpen API - Property Publish Returned... rc = ", rc
						
					else:	
						print ("Tag D1 Counter= "+(str(tagD1)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_D1_Counter", tagD1 )
						print "dwOpen API - Property Publish Returned... rc = ", rc
					
				tagD1_count=False
				print"Timer starts counting"
				t12 = Thread(target=timerD1) #starts counting 
				t12.start() #Calls first function, counte for 3s 
					
			if z == "e28011302000289d7c820212":
				if tagE1_count==False:
					print"tagE1_count is false"
				else:
					tagE1 +=1
					os.system("sudo aplay /home/pi/beep-06_short.wav")
					if tagE1==101:
						tagE1=1
						print ("Tag E1 Counter= "+(str(tagE1)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_E1_Counter", tagE1 )
						print "dwOpen API - Property Publish Returned... rc = ", rc
						
					else:	
						print ("Tag E1 Counter= "+(str(tagE1)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_E1_Counter", tagE1 )
						print "dwOpen API - Property Publish Returned... rc = ", rc
					
				tagE1_count=False
				print"Timer starts counting"
				t13 = Thread(target=timerE1) #starts counting
				t13.start() #Calls first function, counte for 3s
				
				
			if z == "E28011302000281D7CB80212E95F":
				if tagF1_count==False:
					print"tagF1_count is false"
				else:
					tagF1 +=1
					os.system("sudo aplay /home/pi/beep-06_short.wav")
					if tagF1==101:
						tagF1=1
						print ("Tag E1 Counter= "+(str(tagF1)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_F1_Counter", tagF1 )
						print "dwOpen API - Property Publish Returned... rc = ", rc
						
					else:	
						print ("Tag F1 Counter= "+(str(tagF1)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_F1_Counter", tagF1 )
						print "dwOpen API - Property Publish Returned... rc = ", rc
					
				tagF1_count=False
				print"Timer starts counting"
				t14 = Thread(target=timerF1) #starts counting
				t14.start() #Calls first function, counte for 3s
				
				
				
				
			if z == "E2801130200020ED7C92021201DD":
				if tagG1_count==False: 
					print"tagG1_count is false"
				else:
					tagG1 +=1
					os.system("sudo aplay /home/pi/beep-06_short.wav")
					if tagG1==101:
						tagG1=1
						print ("Tag G1 Counter= "+(str(tagG1)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_G1_Counter", tagG1 )
						print "dwOpen API - Property Publish Returned... rc = ", rc
						
					else:	
						print ("Tag G1 Counter= "+(str(tagG1)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_G1_Counter", tagG1 )
						print "dwOpen API - Property Publish Returned... rc = ", rc
						
				tagG1_count=False
				print"Timer starts counting"
				t15 = Thread(target=timerG1) #starts counting 
				t15.start() #Calls first function, counte for 3s 
				
				
			if z == "E28011302000280D7CBB02126EDC":
				if tagH1_count==False:
					print"tagH1_count is false"
				else:   
					tagH1 +=1
					os.system("sudo aplay /home/pi/beep-06_short.wav")
					if tagH1==101:
						tagH1=1
						print ("Tag H1 Counter= "+(str(tagH1)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_H1_Counter", tagH1 )
						print "dwOpen API - Property Publish Returned... rc = ", rc

						
					else:	
						print ("Tag H1 Counter= "+(str(tagH1)))
						rc = dwopen.dwPropertyPublish( dwThingKey1, "Tag_H1_Counter", tagH1 )
						print "dwOpen API - Property Publish Returned... rc = ", rc
					
				tagH1_count=False
				print"Timer starts counting"
				t16 = Thread(target=timerH1) #starts counting
				t16.start() #Calls first function, counte for 3s 