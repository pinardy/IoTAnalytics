#from ubidots import ApiClient
import sys
import time
import datetime
import serial
import logging
import struct
import threading
import Queue
import sqlite3
import dwopenmqtt
import dwopenmqtt2
import dwopenmqtt3
import dwopenmqtt4
import dwopenmqtt5
import dwopenmqtt6
import dwopenmqtt7
import dwopenmqtt8
import dwopenmqtt9
import dwopenmqtt10
import dwopenmqtt11
import dwopenmqtt12
import dwopenmqtt13
import dwopenmqtt14
import dwopenmqtt15
import dwopenmqtt16
import serial
import os

from threading import Thread
from time import sleep

E_SL_MSG_READ_ATTRIBUTE_RESPONSE        =   0x8102
E_SL_MSG_SAVE_PDM_RECORD                =   0x0200
E_SL_MSG_SAVE_PDM_RECORD_RESPONSE       =   0x8200
E_SL_MSG_LOAD_PDM_RECORD_REQUEST        =   0x0201
E_SL_MSG_LOAD_PDM_RECORD_RESPONSE       =   0x8201
E_SL_MSG_DELETE_PDM_RECORD              =   0x0202
E_SL_MSG_PDM_HOST_AVAILABLE             =   0x0300
E_SL_MSG_PDM_HOST_AVAILABLE_RESPONSE    =   0x8300
E_SL_MSG_READ_ATTRIBUTE_REQUEST         =   0x0100
E_SL_MSG_WRITE_ATTRIBUTE_REQUEST        =   0x0110

# dwM2M Developer Community Assigned Tokens...
dwApiURL    = "http://api.devicewise.com/api";
dwApiHost   = "api.devicewise.com";

# dwOpen Member/Thing Assigned Tokens...
dwAppToken1  = "6jqD7avSDOyhLKiq";
dwAppToken2  = "UMYUJCOyU6UeVPxX";
dwAppToken3  = "wwTgt0aO6SiYEMh6";
dwAppToken4  = "zhP0WsnumjXQrnRD";

dwThingKey1  = "mtgrm1_s1";
dwThingKey2  = "mtgrm1_s2";
dwThingKey3  = "mtgrm2_s1";
dwThingKey4  = "mtgrm2_s2";
dwThingKey5  = "mtgrm1_sp";
dwThingKey6  = "pantry_s1";
dwThingKey7  = "wnh_s1";
dwThingKey8  = "wnh_s2";
dwThingKey9  = "wnh_office_s1";
dwThingKey10  = "mtgrm2_ms1";
dwThingKey11  = "mtgrm1_ms1";
dwThingKey12  = "pantry_ms1";
dwThingKey13  = "pantry_ms2";
dwThingKey14  = "pantry_ac1";
dwThingKey15  = "mtgrm1_ac1";
dwThingKey16  = "mtgrm2_ac1";



#define serial settings
ser = serial.Serial(
		port='/dev/ttyUSB0',
		baudrate=1000000,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS
		)


# Global flag to the threads
bRunning = True

# Create an ApiClient object

#api = ApiClient(token='jxpVAKvimQIcFEUs8lMRnCPdGAVO8V')

# Get a Ubidots Variable

# vartemp1 = api.get_variable('578edb4f7625425234b3fbb4')
# varhumd1 = api.get_variable('578edb59762542525a1e34b5')
# vartemp2 = api.get_variable('578edb60762542521568a49b')
# varhumd2 = api.get_variable('578edb6776254252cb124d86')
# varpower = api.get_variable('578edab87625424b4965af2d')
# varenergy = api.get_variable('578edaca7625424bbd435a5e')

tagA1 = 0           # timer
tagA1_count=True    # flag
stop = False        # to see if we need to stop the timer thread
# tagA1 = 0


# ----------- Timer -----------
def timerA1():
	global tagA1_count
	global tagA1
	global stop
	print "-----------------------------------------------------------"
	print "Before the timer loop================================="
	print 'Stop: ' + str(stop)
	print "-----------------------------------------------------------"
	
	# timer starts from zero at the start when the function is called
	tagA1 = 0
	
	for i in range(240):
		print 'Sleeping for a second...'
		sleep(1)
		tagA1 += 1
		# print 'tagA1: ' + str(tagA1)
		# print 'Stop: ' + str(stop)

        # stop is True if room is occupied, then we stop counting
		if stop:
			break

    # if no motion after 4 mins, turn off aircon
	if (tagA1 >= 240):
		# turn off aircon
		#oCB.oSL._WriteMessage(E_SL_MSG_WRITE_ATTRIBUTE_REQUEST,"021021010102010000000001001c3000")
		
		# reset timer
		tagA1 = 0

	print "\nCounting complete"
	print "tagA1: " + str(tagA1)

	tagA1_count = True
	print "tagA set back to True"

	return;
# ---------------------------------


# =============================================================================
# == Function: userCallBack
# == Purpose:  Handles Method Callbacks
# =============================================================================
def userCallBack( MsgID, MethodName, ParamText, thingKey):
  
	print "*** userCallBack... method = ", MethodName
	print "*** ParamText = ", ParamText
	print "*** thingKey = ", thingKey
	
	
	if( MethodName == "update" ):
				
		
		dwopen.dwMailboxAck( MsgID, 0, '', '' );
		
	
		
	if( MethodName == "on" ):
				
		thestring = "\x01\x02\x10\x92\x02\x10\x02\x16\xE2\x02\x12\xAA\xDF\x02\x11\x02\x11\x02\x11\x03"
					   

		ser.isOpen()
		ser.write(thestring);
		dwopen.dwMailboxAck( MsgID, 0, '', '' );	
		
		print " ON On On"
		
	if( MethodName == "off" ):
				
		thestring = "\x01\x02\x10\x92\x02\x10\x02\x16\xE3\x02\x12\xAA\xDF\x02\x11\x02\x11\x02\x10\x03"

		ser.isOpen()
		ser.write(thestring);
		dwopen.dwMailboxAck( MsgID, 0, '', '' );	
		
		print " off off off"
		
	if(( MethodName == "startac" )and(thingKey=="pantry_ac1")):
				

		oCB.oSL._WriteMessage(E_SL_MSG_WRITE_ATTRIBUTE_REQUEST,"02975C010102010000000001001c3001")
		dwopen14.dwMailboxAck( MsgID, 0, '', '' );	
		oCB.oSL._WriteMessage(E_SL_MSG_READ_ATTRIBUTE_REQUEST,"02975C010102010000000001001c")
		print " Request status"
		print " On the ac"
		
	if(( MethodName == "stopac" )and(thingKey=="pantry_ac1")):
				

		oCB.oSL._WriteMessage(E_SL_MSG_WRITE_ATTRIBUTE_REQUEST,"02975C010102010000000001001c3000")
		dwopen14.dwMailboxAck( MsgID, 0, '', '' );	
		oCB.oSL._WriteMessage(E_SL_MSG_READ_ATTRIBUTE_REQUEST,"02975C010102010000000001001c")
		print " Request status"
		print " Off the ac"
		
	if(( MethodName == "csp" )and(thingKey=="pantry_ac1")):
				
		print "*** ------------------------------------------------------------------------------- "
		csp = dwopen14.getFramedText(ParamText, '\"value\":', '}');		
		csp=float(csp)		
		csp=csp*100;
		csp=round(csp)
		print "*** Coolingsetpoint #1 = ",csp;
		csp=int(csp)
		print "*** Coolingsetpoint #2 = ",csp;
		csp=hex(csp);
		csp=str(csp)		
		csp=csp[2:]
		unchanged="02975C0101020100000000010011290"
		finalstring=unchanged + csp		
		oCB.oSL._WriteMessage(E_SL_MSG_WRITE_ATTRIBUTE_REQUEST,finalstring)		
		print "*** Coolingsetpoint #3 = ",csp;
		dwopen14.dwMailboxAck( MsgID, 0, '', '' );			
		print " Set"		
		oCB.oSL._WriteMessage(E_SL_MSG_READ_ATTRIBUTE_REQUEST,"02975C0101020100000000010011")
		print " Cooling Set Point has been published"
		
	if(( MethodName == "hsp" )and(thingKey=="pantry_ac1")):
		hsp = dwopen14.getFramedText(ParamText, '\"value\":', '}');		
		hsp=float(hsp)		
		hsp=hsp*100;
		hsp=round(hsp)
		print "*** Heatingsetpoint #1 = ",hsp;
		hsp=int(hsp)
		print "*** Heatingsetpoint #2 = ",hsp;
		hsp=hex(hsp);
		hsp=str(hsp)		
		hsp=hsp[2:]		
		unchanged="02975C0101020100000000010012290"
		finalstring=unchanged + hsp		
		oCB.oSL._WriteMessage(E_SL_MSG_WRITE_ATTRIBUTE_REQUEST,finalstring)		
		print "*** Coolingsetpoint #3 = ",hsp;
		dwopen14.dwMailboxAck( MsgID, 0, '', '' );		
		print " Set"	
		oCB.oSL._WriteMessage(E_SL_MSG_READ_ATTRIBUTE_REQUEST,"02975C0101020100000000010012")
		print " Heating Set Point has been published"
	
	if(( MethodName == "fancontrol" )and(thingKey=="pantry_ac1")):
		print " Fan speed is"		
		fanoption = dwopen14.getFramedText(ParamText, '\"fancontrol\":\"', '\"');
		print " Fan speed is",fanoption
		
		if( fanoption == "low" ):
			print " Fan speed is low~"
			
			changingbit="01"
					
		if( fanoption == "middle" ):
			print " Fan speed is midlle~~"
		
			changingbit="02"
					
		if( fanoption == "high" ):
			print " Fan speed is high~~~"
		
			changingbit="03"
		
		unchangedbits="02975C010102020000000001000030"
		finaloption=unchangedbits + changingbit		
		oCB.oSL._WriteMessage(E_SL_MSG_WRITE_ATTRIBUTE_REQUEST,finaloption)	
		print " Fan speed is changed"
		print "dwOpen API - Executing Set Attribute Request..."
		attribKey   = "fanmode"
		attribValue = fanoption						
		rc = dwopen.dwSetAttribute( dwThingKey14, attribKey, attribValue );
		print "dwOpen API - Set Attribute Returned... rc = ", rc
		dwopen14.dwMailboxAck( MsgID, 0, '', '' );
		
	if(( MethodName == "startac" )and(thingKey=="mtgrm1_ac1")):
				

		 oCB.oSL._WriteMessage(E_SL_MSG_WRITE_ATTRIBUTE_REQUEST,"02247C010102010000000001001c3001")
		 dwopen15.dwMailboxAck( MsgID, 0, '', '' );	
		 oCB.oSL._WriteMessage(E_SL_MSG_READ_ATTRIBUTE_REQUEST,"02247C010102010000000001001c")
		 print " Request status"
		 print " On the ac"
		
	if(( MethodName == "stopac" )and(thingKey=="mtgrm1_ac1")):
				

		oCB.oSL._WriteMessage(E_SL_MSG_WRITE_ATTRIBUTE_REQUEST,"02247C010102010000000001001c3000")
		dwopen15.dwMailboxAck( MsgID, 0, '', '' );	
		oCB.oSL._WriteMessage(E_SL_MSG_READ_ATTRIBUTE_REQUEST,"02247C010102010000000001001c")
		print " Request status"
		print " Off the ac"
		
	if(( MethodName == "csp" )and(thingKey=="mtgrm1_ac1")):
				
		print "*** ------------------------------------------------------------------------------- "
		csp = dwopen15.getFramedText(ParamText, '\"value\":', '}');		
		csp=float(csp)		
		csp=csp*100;
		csp=round(csp)
		print "*** Coolingsetpoint #1 = ",csp;
		csp=int(csp)
		print "*** Coolingsetpoint #2 = ",csp;
		csp=hex(csp);
		csp=str(csp)		
		csp=csp[2:]
		unchanged="02247C0101020100000000010011290"
		finalstring=unchanged + csp		
		oCB.oSL._WriteMessage(E_SL_MSG_WRITE_ATTRIBUTE_REQUEST,finalstring)		
		print "*** Coolingsetpoint #3 = ",csp;
		dwopen15.dwMailboxAck( MsgID, 0, '', '' );			
		print " Set"		
		oCB.oSL._WriteMessage(E_SL_MSG_READ_ATTRIBUTE_REQUEST,"02247C0101020100000000010011")
		print " Cooling Set Point has been published"
		
	if(( MethodName == "hsp" )and(thingKey=="mtgrm1_ac1")):
		hsp = dwopen15.getFramedText(ParamText, '\"value\":', '}');		
		hsp=float(hsp)		
		hsp=hsp*100;
		hsp=round(hsp)
		print "*** Heatingsetpoint #1 = ",hsp;
		hsp=int(hsp)
		print "*** Heatingsetpoint #2 = ",hsp;
		hsp=hex(hsp);
		hsp=str(hsp)		
		hsp=hsp[2:]		
		unchanged="02247C0101020100000000010012290"
		finalstring=unchanged + hsp		
		oCB.oSL._WriteMessage(E_SL_MSG_WRITE_ATTRIBUTE_REQUEST,finalstring)		
		print "*** Coolingsetpoint #3 = ",hsp;
		dwopen15.dwMailboxAck( MsgID, 0, '', '' );		
		print " Set"	
		oCB.oSL._WriteMessage(E_SL_MSG_READ_ATTRIBUTE_REQUEST,"02247C0101020100000000010012")
		print " Heating Set Point has been published"
	
	if(( MethodName == "fancontrol" )and(thingKey=="mtgrm1_ac1")):
		print " Fan speed is"		
		fanoption = dwopen15.getFramedText(ParamText, '\"fancontrol\":\"', '\"');
		print " Fan speed is",fanoption
		
		if( fanoption == "low" ):
			print " Fan speed is low~"
			
			changingbit="01"
					
		if( fanoption == "middle" ):
			print " Fan speed is midlle~~"
		
			changingbit="02"
					
		if( fanoption == "high" ):
			print " Fan speed is high~~~"
		
			changingbit="03"
		
		unchangedbits="02247C010102020000000001000030"
		finaloption=unchangedbits + changingbit		
		oCB.oSL._WriteMessage(E_SL_MSG_WRITE_ATTRIBUTE_REQUEST,finaloption)	
		print " Fan speed is changed"
		print "dwOpen API - Executing Set Attribute Request..."
		attribKey   = "fanmode"
		attribValue = fanoption						
		rc = dwopen.dwSetAttribute( dwThingKey15, attribKey, attribValue );
		print "dwOpen API - Set Attribute Returned... rc = ", rc
		dwopen15.dwMailboxAck( MsgID, 0, '', '' );
		
	if(( MethodName == "startac" )and(thingKey=="mtgrm2_ac1")):
				

		oCB.oSL._WriteMessage(E_SL_MSG_WRITE_ATTRIBUTE_REQUEST,"021021010102010000000001001c3001")
		dwopen16.dwMailboxAck( MsgID, 0, '', '' );	
		oCB.oSL._WriteMessage(E_SL_MSG_READ_ATTRIBUTE_REQUEST,"021021010102010000000001001c")
		print " Request status"
		print " On the ac"
		
	if(( MethodName == "stopac" )and(thingKey=="mtgrm2_ac1")):
				

		oCB.oSL._WriteMessage(E_SL_MSG_WRITE_ATTRIBUTE_REQUEST,"021021010102010000000001001c3000")
		dwopen16.dwMailboxAck( MsgID, 0, '', '' );	
		oCB.oSL._WriteMessage(E_SL_MSG_READ_ATTRIBUTE_REQUEST,"021021010102010000000001001c")
		print " Request status"
		print " Off the ac"
		
	if(( MethodName == "csp" )and(thingKey=="mtgrm2_ac1")):
				
		print "*** ------------------------------------------------------------------------------- "
		csp = dwopen16.getFramedText(ParamText, '\"value\":', '}');		
		csp=float(csp)		
		csp=csp*100;
		csp=round(csp)
		print "*** Coolingsetpoint #1 = ",csp;
		csp=int(csp)
		print "*** Coolingsetpoint #2 = ",csp;
		csp=hex(csp);
		csp=str(csp)		
		csp=csp[2:]
		unchanged="0210210101020100000000010011290"
		finalstring=unchanged + csp		
		oCB.oSL._WriteMessage(E_SL_MSG_WRITE_ATTRIBUTE_REQUEST,finalstring)		
		print "*** Coolingsetpoint #3 = ",csp;
		dwopen16.dwMailboxAck( MsgID, 0, '', '' );			
		print " Set"		
		oCB.oSL._WriteMessage(E_SL_MSG_READ_ATTRIBUTE_REQUEST,"0210210101020100000000010011")
		
		
	if(( MethodName == "hsp" )and(thingKey=="mtgrm2_ac1")):
		hsp = dwopen16.getFramedText(ParamText, '\"value\":', '}');		
		hsp=float(hsp)		
		hsp=hsp*100;
		hsp=round(hsp)
		print "*** Heatingsetpoint #1 = ",hsp;
		hsp=int(hsp)
		print "*** Heatingsetpoint #2 = ",hsp;
		hsp=hex(hsp);
		hsp=str(hsp)		
		hsp=hsp[2:]		
		unchanged="0210210101020100000000010012290"
		finalstring=unchanged + hsp		
		oCB.oSL._WriteMessage(E_SL_MSG_WRITE_ATTRIBUTE_REQUEST,finalstring)		
		print "*** Heatingsetpoint #3 = ",hsp;
		dwopen16.dwMailboxAck( MsgID, 0, '', '' );		
		print " Set"	
		oCB.oSL._WriteMessage(E_SL_MSG_READ_ATTRIBUTE_REQUEST,"0210210101020100000000010012")
		print " Heating Set Point has been published"
	
	if(( MethodName == "fancontrol" )and(thingKey=="mtgrm2_ac1")):
		print " Fan speed is"		
		fanoption = dwopen16.getFramedText(ParamText, '\"fancontrol\":\"', '\"');
		print " Fan speed is",fanoption
		
		if( fanoption == "low" ):
			print " Fan speed is low~"
			
			changingbit="01"
					
		if( fanoption == "middle" ):
			print " Fan speed is midlle~~"
		
			changingbit="02"
					
		if( fanoption == "high" ):
			print " Fan speed is high~~~"
		
			changingbit="03"
		
		unchangedbits="021021010102020000000001000030"
		finaloption=unchangedbits + changingbit		
		oCB.oSL._WriteMessage(E_SL_MSG_WRITE_ATTRIBUTE_REQUEST,finaloption)	
		print " Fan speed is changed"
		print "dwOpen API - Executing Set Attribute Request..."
		attribKey   = "fanmode"
		attribValue = fanoption						
		rc = dwopen.dwSetAttribute( dwThingKey16, attribKey, attribValue );
		print "dwOpen API - Set Attribute Returned... rc = ", rc
		dwopen16.dwMailboxAck( MsgID, 0, '', '' );
	
			
	return;

	



def MQTTCONNECT():

#------------------------------------------------
#-- Connect to m2mAIR Cloud Server
#------------------------------------------------
	print("Connect to m2mAIR Cloud Server...")

	# rc = dwopen2.mqttConnect( dwApiHost, dwThingKey2, dwAppToken1, userCallBack );
	# print "dwOpen API - MQTT Connect Returned... rc = ", rc
	# print("Waiting 3 Seconds...")
	# time.sleep( 3 )

	'''
	print "dwOpen API - Executing Log Publish Request..."
	msgText  = "Python MQTT Edge Device... Connected and Active!"
	rc = dwopen.dwLogPublish( dwThingKey2, msgText );
	print "dwOpen API - Log Publish Returned... rc = ", rc
	time.sleep( 3)
	'''
	# rc = dwopen3.mqttConnect( dwApiHost, dwThingKey3, dwAppToken1, userCallBack );
	# print "dwOpen API - MQTT Connect Returned... rc = ", rc
	# print("Waiting 3 Seconds...")
	# time.sleep( 3 )
	'''
	rc = dwopen.dwLogPublish( dwThingKey3, msgText );
	print "dwOpen API - Log Publish Returned... rc = ", rc
	time.sleep( 3)
	'''
	rc = dwopen.mqttConnect( dwApiHost, dwThingKey1, dwAppToken1, userCallBack );
	print "1dwOpen API - MQTT Connect Returned... rc = ", rc
	print("Waiting 3 Seconds...")
	time.sleep( 2 )
	
	rc = dwopen2.mqttConnect( dwApiHost, dwThingKey2, dwAppToken1, userCallBack );
	print "2dwOpen API - MQTT Connect Returned... rc = ", rc
	print("Waiting 3 Seconds...")
	time.sleep( 2 )
	
	rc = dwopen3.mqttConnect( dwApiHost, dwThingKey3, dwAppToken1, userCallBack );
	print "3dwOpen API - MQTT Connect Returned... rc = ", rc
	print("Waiting 3 Seconds...")
	time.sleep( 2 )
	
	rc = dwopen4.mqttConnect( dwApiHost, dwThingKey4, dwAppToken1, userCallBack );
	print "4dwOpen API - MQTT Connect Returned... rc = ", rc
	print("Waiting 3 Seconds...")
	time.sleep( 2 )
	
	rc = dwopen5.mqttConnect( dwApiHost, dwThingKey5, dwAppToken2, userCallBack );
	print "5dwOpen API - MQTT Connect Returned... rc = ", rc
	print("Waiting 3 Seconds...")
	time.sleep( 2 )
	
	rc = dwopen6.mqttConnect( dwApiHost, dwThingKey6, dwAppToken1, userCallBack );
	print "6dwOpen API - MQTT Connect Returned... rc = ", rc
	print("Waiting 3 Seconds...")
	time.sleep( 2 )
	
	rc = dwopen7.mqttConnect( dwApiHost, dwThingKey7, dwAppToken1, userCallBack );
	print "7dwOpen API - MQTT Connect Returned... rc = ", rc
	print("Waiting 3 Seconds...")
	time.sleep( 2 )
	
	rc = dwopen8.mqttConnect( dwApiHost, dwThingKey8, dwAppToken1, userCallBack );
	print "8dwOpen API - MQTT Connect Returned... rc = ", rc
	print("Waiting 3 Seconds...")
	time.sleep( 2 )
	
	rc = dwopen9.mqttConnect( dwApiHost, dwThingKey9, dwAppToken1, userCallBack );
	print "9dwOpen API - MQTT Connect Returned... rc = ", rc
	print("Waiting 3 Seconds...")
	time.sleep( 2 )
	
	rc = dwopen10.mqttConnect( dwApiHost, dwThingKey10, dwAppToken3, userCallBack );
	print "10dwOpen API - MQTT Connect Returned... rc = ", rc
	print("Waiting 3 Seconds...")
	time.sleep( 2 )
	
	rc = dwopen11.mqttConnect( dwApiHost, dwThingKey11, dwAppToken3, userCallBack );
	print "11dwOpen API - MQTT Connect Returned... rc = ", rc
	print("Waiting 3 Seconds...")
	time.sleep( 2 )
	
	rc = dwopen12.mqttConnect( dwApiHost, dwThingKey12, dwAppToken3, userCallBack );
	print "12dwOpen API - MQTT Connect Returned... rc = ", rc
	print("Waiting 3 Seconds...")
	time.sleep( 2 )
	
	rc = dwopen13.mqttConnect( dwApiHost, dwThingKey13, dwAppToken3, userCallBack );
	print "13dwOpen API - MQTT Connect Returned... rc = ", rc
	print("Waiting 3 Seconds...")
	time.sleep( 2 )
	
	rc = dwopen14.mqttConnect( dwApiHost, dwThingKey14, dwAppToken4, userCallBack );
	print "14dwOpen API - MQTT Connect Returned... rc = ", rc
	print("Waiting 3 Seconds...")
	time.sleep( 2 )
	
	rc = dwopen15.mqttConnect( dwApiHost, dwThingKey15, dwAppToken4, userCallBack );
	print "15dwOpen API - MQTT Connect Returned... rc = ", rc
	print("Waiting 3 Seconds...")
	time.sleep( 2 )
	
	rc = dwopen16.mqttConnect( dwApiHost, dwThingKey16, dwAppToken4, userCallBack );
	print "16dwOpen API - MQTT Connect Returned... rc = ", rc
	print("Waiting 3 Seconds...")
	time.sleep( 2 )
	
	
	'''
	rc = dwopen.dwLogPublish( dwThingKey1, msgText );
	print "dwOpen API - Log Publish Returned... rc = ", rc
	time.sleep( 2)
	'''

	print("Begin Publishing Requests to m2mAIR Cloud Server...")

#------------------------------------------------
#-- Log Publish
#------------------------------------------------
print("Load dwOpenMQTT Library...")
dwopen = dwopenmqtt.dwOpen();
dwopen2 = dwopenmqtt2.dwOpen();
dwopen3 = dwopenmqtt3.dwOpen();
dwopen4 = dwopenmqtt4.dwOpen();
dwopen5 = dwopenmqtt5.dwOpen();
dwopen6 = dwopenmqtt6.dwOpen();
dwopen7 = dwopenmqtt7.dwOpen();
dwopen8 = dwopenmqtt8.dwOpen();
dwopen9 = dwopenmqtt9.dwOpen();
dwopen10 = dwopenmqtt10.dwOpen();
dwopen11 = dwopenmqtt11.dwOpen();
dwopen12 = dwopenmqtt12.dwOpen();
dwopen13 = dwopenmqtt13.dwOpen();
dwopen14 = dwopenmqtt14.dwOpen();
dwopen15 = dwopenmqtt15.dwOpen();
dwopen16 = dwopenmqtt16.dwOpen();
print("dwOpenMQTT Library Loaded...")	
MQTTCONNECT();





# #------------------------------------------------
# #-- Location Publish
# #------------------------------------------------
# print "dwOpen API - Sending Location Publish Request..."
# #ILST Headquarters - GPS Detail...
# locLatitude  = "1.376825"
# locLongitude = "103.86439100000007"
# locAltitude  = "11.4"
# locSpeed     = "0.0"
# locHeading   = "18.8"
# locFixType   = "manual"

# rc = dwopen.dwLocationPublish( dwThingKey1, locLatitude, locLongitude, locAltitude, locSpeed, locHeading, locFixType );
# rc = dwopen.dwLocationPublish( dwThingKey2, locLatitude, locLongitude, locAltitude, locSpeed, locHeading, locFixType );
# rc = dwopen.dwLocationPublish( dwThingKey3, locLatitude, locLongitude, locAltitude, locSpeed, locHeading, locFixType );
# print "dwOpen API - Location Publish Returned... rc = ", rc

# time.sleep( 2 )

# #------------------------------------------------
# #-- Set Attribute
# #------------------------------------------------
# print "dwOpen API - Executing Set Attribute Request..."

# attribKey   = "Brand"
# attribValue = "Owon"

# rc = dwopen.dwSetAttribute( dwThingKey1, attribKey, attribValue );
# rc = dwopen.dwSetAttribute( dwThingKey2, attribKey, attribValue );
# rc = dwopen.dwSetAttribute( dwThingKey3, attribKey, attribValue );
# print "dwOpen API - Set Attribute Returned... rc = ", rc

# time.sleep( 2 )


	


class cSerialLinkError(Exception):
    pass



class cModuleError(cSerialLinkError):
    """ Exception class for errors that the node may send back"""
    def __init__(self, statusCode, statusMessage=""):
        self.statusCode = statusCode
        self.statusMessage = statusMessage
        
        Exception.__init__(self, repr(self))
        
    def __repr__(self):
        if (self.statusCode == 0):
            raise ValueError("Not a failure code")
        elif (self.statusCode == 1):
            r = "Incorrect Parameters"
        elif (self.statusCode == 2):
            r = "Unhandled Command"
        elif (self.statusCode == 3):
            r = "Command Failed"
        elif (self.statusCode == 4):
            r = "Busy"
        elif (self.statusCode == 5):
            r = "Stack already started"
        else:
            r = "Unknown status code %d" % self.statusCode
        
        if len(self.statusMessage):
            r = ": ".join([r, self.statusMessage])
        return r

       
class cSerialLink(threading.Thread):
    """Class implementing the binary serial protrocol to the control bridge node"""
    def __init__(self, port, baudrate=115200):
        threading.Thread.__init__(self, name="SL")
        self.logger = logging.getLogger(str(port))
        self.commslogger = logging.getLogger("Comms("+str(port)+")")
        
        # Turn this up to see traffic between node and host
        self.commslogger.setLevel(logging.WARNING)
        
        self.oPort = serial.Serial(port, baudrate)
        
        # Message queue used to pass messages between reader thread and WaitMessage()
        self.dMessageQueue = {}
        
        # Start reader thread
        self.daemon=True
        self.start()


            
    def _WriteByte(self, oByte, bSpecial=False, bAscii=False):
        """ Internal function
            Send a single byte to the serial port. Takes care of byte stuffing
        """
        if bAscii:
            if not bSpecial and oByte < 0x10:
                self.commslogger.info("Ascii Host->Node: 0x02 ESC")
                oByte = struct.pack("B", oByte ^ 0x10)
                self.oPort.write(struct.pack("B", 0x02))                
            else:
                oByte = struct.pack("B", oByte)
            self.commslogger.info("Ascii Host->Node: 0x%02x", ord(oByte))
            self.oPort.write(oByte)    
        else:
            if not bSpecial and ord(oByte) < 0x10:
                self.commslogger.info("non Ascii Host->Node: 0x02 ESC")
                oByte = struct.pack("B", ord(oByte) ^ 0x10)
                self.oPort.write(struct.pack("B", 0x02))
            self.commslogger.info("non Ascii Host->Node: 0x%02x", ord(oByte))
            self.oPort.write(oByte)    


    def _WriteMessage(self, eMessageType, sData):
        """ Internal function
            Send a complete message to the serial port. Takes care of byte stuffing
            and checksum generation. eMessageType should be a 16bit message number
            sData is a string containing the packed message data 
        """
        self.logger.info("Host->Node: Message Type 0x%04x, length %d %s", eMessageType, (len(sData)),sData)

        u8Checksum = ((eMessageType >> 8) & 0xFF) ^ ((eMessageType >> 0) & 0xFF)
        u8Checksum = u8Checksum ^ (((len(sData)/2) >> 8) & 0xFF) ^ (((len(sData)/2) >> 0) & 0xFF)
        bIn=True
        for byte in sData:
            if bIn:
                u8Byte= int(byte,16)<<4 & 0xFF
                bIn=False
            else:
                u8Byte |= int(byte,16)>>0 & 0xFF          
                u8Checksum = u8Checksum ^ u8Byte
                bIn=True
            
        u16Length = len(sData)/2
        
        self._WriteByte(struct.pack("B", 0x01), True)
        self._WriteByte(struct.pack("B", (eMessageType >> 8) & 0xFF))
        self._WriteByte(struct.pack("B", (eMessageType >> 0) & 0xFF))
        self._WriteByte(struct.pack("B", (u16Length >> 8) & 0xFF))
        self._WriteByte(struct.pack("B", (u16Length >> 0) & 0xFF))
        self._WriteByte(struct.pack("B", (u8Checksum) & 0xFF))
        bIn= True
        
        for byte in sData:
            if bIn:
                u8Byte= int(byte,16)<<4 & 0xFF
                bIn=False
            else:
                u8Byte |= int(byte,16)>>0 & 0xFF                
                self._WriteByte(u8Byte,False,True)
                bIn=True
            
        self._WriteByte(struct.pack("B", 0x03), True)


    def _ReadMessage(self):
        """ Internal function
            Read a complete message from the serial port. Takes care of byte stuffing
            Length and checksum message integrity checks.
            Return tuple of message type and buffer of data.
        """
        bInEsc = False
        
        u8Checksum = 0
        eMessageType = 0
        u16Length = 0
        sData = ""
        state = 0
        while(bRunning):
            byte = self.oPort.read(1)
            #sys.stdout.write(byte)
            if True: #len(byte) > 0:
                self.commslogger.info("Node->Host: 0x%02x", ord(byte))

                if (ord(byte) == 0x01):
                    self.commslogger.debug("Start Message")
                    u8Checksum = 0
                    eMessageType = 0
                    u16Length = 0
                    sData = ""
                    state = 0
                elif (ord(byte) == 0x02):
                    self.commslogger.debug("ESC")
                    bInEsc = True
                elif (ord(byte) == 0x03):
                    self.commslogger.debug("End Message")
                    
                    if not len(sData) == u16Length:
                        self.commslogger.warning("Length mismatch (Expected %d, got %d)", u16Length, len(sData))
                        continue
                    
                    u8MyChecksum = ((eMessageType >> 8) & 0xFF) ^ ((eMessageType >> 0) & 0xFF)
                    u8MyChecksum = u8MyChecksum ^ ((u16Length >> 8) & 0xFF) ^ ((u16Length >> 0) & 0xFF)
                    for byte in sData:
                        u8MyChecksum = (u8MyChecksum ^ ord(byte)) & 0xFF
  
                    if not u8Checksum == u8MyChecksum:
                        self.commslogger.warning("Checkum mismatch (Expected 0x%02x, got 0x%02x)", u8Checksum, u8MyChecksum)
                        continue
                    self.commslogger.debug("Checksum ok")
                    return (eMessageType, sData)
                else:
                    if bInEsc:
                        bInEsc = False
                        byte = struct.pack("B", ord(byte) ^ 0x10)
                    
                    if state == 0:
                        # Type MSB
                        eMessageType = ord(byte) << 8
                        state = state + 1
                    elif state == 1:
                        eMessageType = eMessageType + ord(byte)
                        self.commslogger.debug("Message Type: 0x%04x", eMessageType)
                        state = state + 1
                    elif state == 2:
                        # Type MSB
                        u16Length = ord(byte) << 8
                        state = state + 1
                    elif state == 3:
                        u16Length = u16Length + ord(byte)
                        self.commslogger.debug("Message Length: 0x%04x", u16Length)
                        state = state + 1
                    elif state == 4:
                        u8Checksum = ord(byte)
                        self.commslogger.debug("Message Checksum: 0x%02x", u8Checksum)
                        state = state + 1
                    else:
                        self.commslogger.debug("Message Add Data: 0x%02x", ord(byte))
                        sData = sData + byte
        return (0, "")


    def run(self):
        """ Reader thread function.
            Keep reading messages from the port.
            Log messages are sent straight to the logger.
            Everything else is queued for listers that are waiting for message types via WaitMessage().
        """
	LastTemp1= -1
	LastTemp2= -1
	LastTemp3= -1
	LastTemp4= -1
	LastTemp5= -1
	LastTemp6= -1
	LastTemp7= -1
	LastTemp8= -1
	LastTemp9= -1
	LastHumidity1= -1
	LastHumidity2= -1
	LastHumidity3=-1
	LastHumidity4=-1
	LastHumidity5=-1
	LastHumidity6=-1
	LastHumidity7=-1
	LastHumidity8=-1
	LastHumidity9=-1
	LastEnergy= -1
	LastPower= -1
	LastStatusAcPantry=-1
	LastStatusAcMeetingRoom1=-1
	LastStatusAcMeetingRoom2=-1
	LastCspAcPantry=-1
	LastCspAcMeetingRoom1=-1
	LastCspAcMeetingRoom2=-1
	
	self.logger.debug("Read thread starting")
	print "Program Running"
	print "Program Running"
	print "Program Running"
	print "Program Running"
	print "Program Running"	
		
		
        try:
            while(bRunning):
						(eMessageType, sData) = self._ReadMessage()
                #self.logger.info("Node->Host: Response 0x%04x, length %d", eMessageType, len(sData))
                
                #if ((eMessageType == E_SL_MSG_READ_ATTRIBUTE_RESPONSE)or(eMessageType == 0x8100)or(eMessageType == 0x8401)):
						stringme= (''.join(x.encode('hex') for x in sData))
						
						self.logger.warning("Unhandled message 0x%04x", eMessageType)
						self.logger.info("Read Attributes response %s", stringme)
						#self.logger.info("Read Attributes response %s", stringme)
						#time.sleep( 2 )
						
						#print "Connection state" + dwopen.client.mqtt_cs_connected ;

						if "b1750107020000" in stringme:
							start = stringme.find("b1750107020000") + 18
							smartplugenergy = stringme[start : start + 16]
							smartplugenergy = int(smartplugenergy,16)
							self.logger.info("Smart plug Energy: %s" , smartplugenergy)
							
							# file = open("/var/www/html/SPenergy.txt", "w")
							# file.write(str(smartplugenergy))
							# file.close()
							
							if smartplugenergy <> LastEnergy:
								#response = varenergy.save_value({"value": smartplugenergy})
								rc = dwopen5.dwPropertyPublish( dwThingKey5, "Smart_Plug_Energy", smartplugenergy )
								print "dwOpen API - Property Publish Returned... rc = ", rc
							LastEnergy = smartplugenergy
							
						if "b1750107020400" in stringme:
							start = stringme.find("b1750107020400") + 18
							smartplugpower = stringme[start : start + 8]
							smartplugpower = int(smartplugpower,16)
							self.logger.info("Smart plug Power: %s" , smartplugpower)
							
							# file = open("/var/www/html/SPpower.txt", "w")
							# file.write(str(smartplugpower))
							# file.close()
							
							if smartplugpower <> LastPower:
								#response = varpower.save_value({"value": smartplugpower})
								rc = dwopen5.dwPropertyPublish( dwThingKey5, "Smart_Plug_Power", smartplugpower )
								print "dwOpen API - Property Publish Returned... rc = ", rc
							LastPower = smartplugpower
							
						if "89ae010402" in stringme:
							self.logger.info("Temperature 1: %s" , stringme)
							start = stringme.find("89ae010402") + 18
							temp1 = stringme[start : start + 4]
							temp1 = float(int(temp1, 16))/100
							self.logger.info("Temperature 1: %s" , temp1)
							
							# file = open("/var/www/html/t1.txt", "w")
							# file.write(str(temp1))
							# file.close()
							
							#response = vartemp1.save_value({"value": temp1})
							rc = dwopen.dwPropertyPublish( dwThingKey1, "temperature", temp1 )
							print "dwOpen API - Property Publish Returned... rc = ", rc
							
							
								
							if temp1 <> LastTemp1:
								if temp1 < 20:
									alarmState = 0
									alarmMsg   = "Temp - Cold"
								elif temp1 < 27:
									alarmState = 1
									alarmMsg   = "Temp - Normal"
								elif temp1 < 32:
									alarmState = 2
									alarmMsg   = "Temp - Warm"
								else:
									alarmState = 3
									alarmMsg   = "Temp - Hot"
								#time.sleep( 2 )
								rc = dwopen.dwAlarmPublish( dwThingKey1, "alarm_temp", alarmState, alarmMsg );
								print "dwOpen API - Property Publish Returned... rc = ", rc
							

							LastTemp1 = temp1
						
						
						if "89ae020405" in stringme:
							self.logger.info("Humidity 1: %s" , stringme)
							start = stringme.find("89ae010405") + 21
							humidity1 = stringme[start : start + 4]
							humidity1 = float(int(humidity1, 16))/100
							self.logger.info("Humidity 1: %s" , humidity1)
							
							# file = open("/var/www/html/h1.txt", "w")
							# file.write(str(humidity1))
							# file.close()
							
							#response = varhumd1.save_value({"value": humidity1})
							rc = dwopen.dwPropertyPublish( dwThingKey1, "humidity", humidity1 )
							print "dwOpen API - Property Publish Returned... rc = ", rc
							
							if humidity1 <> LastHumidity1:
								if humidity1 < 35:
									alarmState = 0
									alarmMsg   = "Humidity - Dry"
								elif humidity1 < 80:
									alarmState = 1
									alarmMsg   = "Humidity - Normal"
								else:
									alarmState = 2
									alarmMsg   = "Humidity - Wet"
								#time.sleep( 2 )
								rc = dwopen.dwAlarmPublish( dwThingKey1, "alarm_humid", alarmState, alarmMsg );
								print "dwOpen API - Property Publish Returned... rc = ", rc
								
							LastHumidity1 = humidity1
							
						if "7800010402" in stringme:
							self.logger.info("Temperature 2: %s" , stringme)
							start = stringme.find("7800010402") + 18
							temp2 = stringme[start : start + 4]
							temp2 = float(int(temp2, 16))/100
							self.logger.info("Temperature 2: %s" , temp2)
							
							# file = open("/var/www/html/t1.txt", "w")
							# file.write(str(temp2))
							# file.close()
							
							#response = vartemp2.save_value({"value": temp2})
							rc = dwopen2.dwPropertyPublish( dwThingKey2, "temperature", temp2 )
							print "dwOpen API - Property Publish Returned... rc = ", rc
							
							
								
							if temp2 <> LastTemp2:
								if temp2 < 20:
									alarmState = 0
									alarmMsg   = "Temp - Cold"
								elif temp2 < 27:
									alarmState = 1
									alarmMsg   = "Temp - Normal"
								elif temp2 < 32:
									alarmState = 2
									alarmMsg   = "Temp - Warm"
								else:
									alarmState = 3
									alarmMsg   = "Temp - Hot"
								#time.sleep( 2 )
								rc = dwopen2.dwAlarmPublish( dwThingKey2, "alarm_temp", alarmState, alarmMsg );
								print "dwOpen API - Property Publish Returned... rc = ", rc
							

							LastTemp2 = temp2
						
						
						if "7800020405" in stringme:
							self.logger.info("Humidity 2: %s" , stringme)
							start = stringme.find("7800010405") + 21
							humidity2 = stringme[start : start + 4]
							humidity2 = float(int(humidity2, 16))/100
							self.logger.info("Humidity 2: %s" , humidity2)
							
							# file = open("/var/www/html/h1.txt", "w")
							# file.write(str(humidity2))
							# file.close()
							
							#response = varhumd2.save_value({"value": humidity2})
							rc = dwopen2.dwPropertyPublish( dwThingKey2, "humidity", humidity2 )
							print "dwOpen API - Property Publish Returned... rc = ", rc
							
							if humidity2 <> LastHumidity2:
								if humidity2 < 35:
									alarmState = 0
									alarmMsg   = "Humidity - Dry"
								elif humidity2 < 80:
									alarmState = 1
									alarmMsg   = "Humidity - Normal"
								else:
									alarmState = 2
									alarmMsg   = "Humidity - Wet"
								#time.sleep( 2 )
								rc = dwopen2.dwAlarmPublish( dwThingKey2, "alarm_humid", alarmState, alarmMsg );
								print "dwOpen API - Property Publish Returned... rc = ", rc
								
							LastHumidity2 = humidity2
							
						if "0121010402" in stringme:
							self.logger.info("Temperature 3: %s" , stringme)
							start = stringme.find("0121010402") + 18
							temp3 = stringme[start : start + 4]
							temp3 = float(int(temp3, 16))/100
							self.logger.info("Temperature 3: %s" , temp3)
							
							# file = open("/var/www/html/t1.txt", "w")
							# file.write(str(temp3))
							# file.close()
							
							#response = vartemp3.save_value({"value": temp3})
							rc = dwopen3.dwPropertyPublish( dwThingKey3, "temperature", temp3 )
							print "dwOpen API - Property Publish Returned... rc = ", rc
							
							
								
							if temp3 <> LastTemp3:
								if temp3 < 20:
									alarmState = 0
									alarmMsg   = "Temp - Cold"
								elif temp3 < 27:
									alarmState = 1
									alarmMsg   = "Temp - Normal"
								elif temp3 < 32:
									alarmState = 2
									alarmMsg   = "Temp - Warm"
								else:
									alarmState = 3
									alarmMsg   = "Temp - Hot"
								#time.sleep( 2 )
								rc = dwopen3.dwAlarmPublish( dwThingKey3, "alarm_temp", alarmState, alarmMsg );
								print "dwOpen API - Property Publish Returned... rc = ", rc
							

							LastTemp3 = temp3
						
						
						if "0121020405" in stringme:
							self.logger.info("Humidity 3: %s" , stringme)
							start = stringme.find("0121010405") + 21
							humidity3 = stringme[start : start + 4]
							humidity3 = float(int(humidity3, 16))/100
							self.logger.info("Humidity 3: %s" , humidity3)
							
							# file = open("/var/www/html/h1.txt", "w")
							# file.write(str(humidity3))
							# file.close()
							
							#response = varhumd3.save_value({"value": humidity3})
							rc = dwopen3.dwPropertyPublish( dwThingKey3, "humidity", humidity3 )
							print "dwOpen API - Property Publish Returned... rc = ", rc
							
							if humidity3 <> LastHumidity3:
								if humidity3 < 35:
									alarmState = 0
									alarmMsg   = "Humidity - Dry"
								elif humidity3 < 80:
									alarmState = 1
									alarmMsg   = "Humidity - Normal"
								else:
									alarmState = 2
									alarmMsg   = "Humidity - Wet"
								#time.sleep( 2 )
								rc = dwopen3.dwAlarmPublish( dwThingKey3, "alarm_humid", alarmState, alarmMsg );
								print "dwOpen API - Property Publish Returned... rc = ", rc
								
							LastHumidity3 = humidity3	
						
						if "c89f010402" in stringme:
							self.logger.info("Temperature 3: %s" , stringme)
							start = stringme.find("c89f010402") + 18
							temp4 = stringme[start : start + 4]
							temp4 = float(int(temp4, 16))/100
							self.logger.info("Temperature 3: %s" , temp4)
							
							# file = open("/var/www/html/t1.txt", "w")
							# file.write(str(temp4))
							# file.close()
							
							#response = vartemp4.save_value({"value": temp4})
							rc = dwopen4.dwPropertyPublish( dwThingKey4, "temperature", temp4 )
							print "dwOpen API - Property Publish Returned... rc = ", rc
							
							
								
							if temp4 <> LastTemp4:
								if temp4 < 20:
									alarmState = 0
									alarmMsg   = "Temp - Cold"
								elif temp4 < 27:
									alarmState = 1
									alarmMsg   = "Temp - Normal"
								elif temp4 < 32:
									alarmState = 2
									alarmMsg   = "Temp - Warm"
								else:
									alarmState = 3
									alarmMsg   = "Temp - Hot"
								#time.sleep( 2 )
								rc = dwopen4.dwAlarmPublish( dwThingKey4, "alarm_temp", alarmState, alarmMsg );
								print "dwOpen API - Property Publish Returned... rc = ", rc
							

							LastTemp4 = temp4
						
						
						if "c89f020405" in stringme:
							self.logger.info("Humidity 3: %s" , stringme)
							start = stringme.find("c89f010405") + 21
							humidity4 = stringme[start : start + 4]
							humidity4 = float(int(humidity4, 16))/100
							self.logger.info("Humidity 3: %s" , humidity4)
							
							# file = open("/var/www/html/h1.txt", "w")
							# file.write(str(humidity4))
							# file.close()
							
							#response = varhumd3.save_value({"value": humidity4})
							rc = dwopen4.dwPropertyPublish( dwThingKey4, "humidity", humidity4 )
							print "dwOpen API - Property Publish Returned... rc = ", rc
							
							if humidity4 <> LastHumidity4:
								if humidity4 < 35:
									alarmState = 0
									alarmMsg   = "Humidity - Dry"
								elif humidity4 < 80:
									alarmState = 1
									alarmMsg   = "Humidity - Normal"
								else:
									alarmState = 2
									alarmMsg   = "Humidity - Wet"
								#time.sleep( 2 )
								rc = dwopen4.dwAlarmPublish( dwThingKey4, "alarm_humid", alarmState, alarmMsg );
								print "dwOpen API - Property Publish Returned... rc = ", rc
								
							LastHumidity4 = humidity4						
							
						if "43b8010402" in stringme:
							self.logger.info("Temperature 3: %s" , stringme)
							start = stringme.find("43b8010402") + 18
							temp5 = stringme[start : start + 4]
							temp5 = float(int(temp5, 16))/100
							self.logger.info("Temperature 3: %s" , temp5)
							
							# file = open("/var/www/html/t1.txt", "w")
							# file.write(str(temp5))
							# file.close()
							
							#response = vartemp5.save_value({"value": temp5})
							rc = dwopen6.dwPropertyPublish( dwThingKey6, "temperature", temp5 )
							print "dwOpen API - Property Publish Returned... rc = ", rc
							
							
								
							if temp5 <> LastTemp5:
								if temp5 < 20:
									alarmState = 0
									alarmMsg   = "Temp - Cold"
								elif temp5 < 27:
									alarmState = 1
									alarmMsg   = "Temp - Normal"
								elif temp5 < 32:
									alarmState = 2
									alarmMsg   = "Temp - Warm"
								else:
									alarmState = 3
									alarmMsg   = "Temp - Hot"
								#time.sleep( 2 )
								rc = dwopen6.dwAlarmPublish( dwThingKey6, "alarm_temp", alarmState, alarmMsg );
								print "dwOpen API - Property Publish Returned... rc = ", rc
							

							LastTemp5 = temp5
						
						
						if "43b8020405" in stringme:
							self.logger.info("Humidity 3: %s" , stringme)
							start = stringme.find("43b8010405") + 21
							humidity5 = stringme[start : start + 4]
							humidity5 = float(int(humidity5, 16))/100
							self.logger.info("Humidity 3: %s" , humidity5)
							
							# file = open("/var/www/html/h1.txt", "w")
							# file.write(str(humidity5))
							# file.close()
							
							#response = varhumd3.save_value({"value": humidity5})
							rc = dwopen6.dwPropertyPublish( dwThingKey6, "humidity", humidity5 )
							print "dwOpen API - Property Publish Returned... rc = ", rc
							
							if humidity5 <> LastHumidity5:
								if humidity5 < 35:
									alarmState = 0
									alarmMsg   = "Humidity - Dry"
								elif humidity5 < 80:
									alarmState = 1
									alarmMsg   = "Humidity - Normal"
								else:
									alarmState = 2
									alarmMsg   = "Humidity - Wet"
								#time.sleep( 2 )
								rc = dwopen6.dwAlarmPublish( dwThingKey6, "alarm_humid", alarmState, alarmMsg );
								print "dwOpen API - Property Publish Returned... rc = ", rc
								
							LastHumidity5 = humidity5
						
						if "6740010402" in stringme:
							self.logger.info("Temperature 3: %s" , stringme)
							start = stringme.find("6740010402") + 18
							temp6 = stringme[start : start + 4]
							temp6 = float(int(temp6, 16))/100
							self.logger.info("Temperature 3: %s" , temp6)
							
							# file = open("/var/www/html/t1.txt", "w")
							# file.write(str(temp6))
							# file.close()
							
							#response = vartemp6.save_value({"value": temp6})
							rc = dwopen7.dwPropertyPublish( dwThingKey7, "temperature", temp6 )
							print "dwOpen API - Property Publish Returned... rc = ", rc
							
							
								
							if temp6 <> LastTemp6:
								if temp6 < 20:
									alarmState = 0
									alarmMsg   = "Temp - Cold"
								elif temp6 < 27:
									alarmState = 1
									alarmMsg   = "Temp - Normal"
								elif temp6 < 32:
									alarmState = 2
									alarmMsg   = "Temp - Warm"
								else:
									alarmState = 3
									alarmMsg   = "Temp - Hot"
								#time.sleep( 2 )
								rc = dwopen7.dwAlarmPublish( dwThingKey7, "alarm_temp", alarmState, alarmMsg );
								print "dwOpen API - Property Publish Returned... rc = ", rc
							

							LastTemp6 = temp6
						
						
						if "6740020405" in stringme:
							self.logger.info("Humidity 3: %s" , stringme)
							start = stringme.find("6740010405") + 21
							humidity6 = stringme[start : start + 4]
							humidity6 = float(int(humidity6, 16))/100
							self.logger.info("Humidity 3: %s" , humidity6)
							
							# file = open("/var/www/html/h1.txt", "w")
							# file.write(str(humidity6))
							# file.close()
							
							#response = varhumd3.save_value({"value": humidity6})
							rc = dwopen7.dwPropertyPublish( dwThingKey7, "humidity", humidity6 )
							print "dwOpen API - Property Publish Returned... rc = ", rc
							
							if humidity6 <> LastHumidity6:
								if humidity6 < 35:
									alarmState = 0
									alarmMsg   = "Humidity - Dry"
								elif humidity6 < 80:
									alarmState = 1
									alarmMsg   = "Humidity - Normal"
								else:
									alarmState = 2
									alarmMsg   = "Humidity - Wet"
								#time.sleep( 2 )
								rc = dwopen7.dwAlarmPublish( dwThingKey7, "alarm_humid", alarmState, alarmMsg );
								print "dwOpen API - Property Publish Returned... rc = ", rc
								
							LastHumidity6 = humidity6
						
						if "3704010402" in stringme:
							self.logger.info("Temperature 3: %s" , stringme)
							start = stringme.find("3704010402") + 18
							temp7 = stringme[start : start + 4]
							temp7 = float(int(temp7, 16))/100
							self.logger.info("Temperature 3: %s" , temp7)
							
							# file = open("/var/www/html/t1.txt", "w")
							# file.write(str(temp7))
							# file.close()
							
							#response = vartemp7.save_value({"value": temp7})
							rc = dwopen8.dwPropertyPublish( dwThingKey8, "temperature", temp7 )
							print "dwOpen API - Property Publish Returned... rc = ", rc
							
							
								
							if temp7 <> LastTemp7:
								if temp7 < 20:
									alarmState = 0
									alarmMsg   = "Temp - Cold"
								elif temp7 < 27:
									alarmState = 1
									alarmMsg   = "Temp - Normal"
								elif temp7 < 32:
									alarmState = 2
									alarmMsg   = "Temp - Warm"
								else:
									alarmState = 3
									alarmMsg   = "Temp - Hot"
								#time.sleep( 2 )
								rc = dwopen8.dwAlarmPublish( dwThingKey8, "alarm_temp", alarmState, alarmMsg );
								print "dwOpen API - Property Publish Returned... rc = ", rc
							

							LastTemp7 = temp7
						
						
						if "3704020405" in stringme:
							self.logger.info("Humidity 3: %s" , stringme)
							start = stringme.find("3704010405") + 21
							humidity7 = stringme[start : start + 4]
							humidity7 = float(int(humidity7, 16))/100
							self.logger.info("Humidity 3: %s" , humidity7)
							
							# file = open("/var/www/html/h1.txt", "w")
							# file.write(str(humidity7))
							# file.close()
							
							#response = varhumd3.save_value({"value": humidity7})
							rc = dwopen8.dwPropertyPublish( dwThingKey8, "humidity", humidity7 )
							print "dwOpen API - Property Publish Returned... rc = ", rc
							
							if humidity7 <> LastHumidity7:
								if humidity7 < 35:
									alarmState = 0
									alarmMsg   = "Humidity - Dry"
								elif humidity7 < 80:
									alarmState = 1
									alarmMsg   = "Humidity - Normal"
								else:
									alarmState = 2
									alarmMsg   = "Humidity - Wet"
								#time.sleep( 2 )
								rc = dwopen8.dwAlarmPublish( dwThingKey8, "alarm_humid", alarmState, alarmMsg );
								print "dwOpen API - Property Publish Returned... rc = ", rc
								
							LastHumidity7 = humidity7
							
						if "4225010402" in stringme:
							self.logger.info("Temperature 3: %s" , stringme)
							start = stringme.find("4225010402") + 18
							temp8 = stringme[start : start + 4]
							temp8 = float(int(temp8, 16))/100
							self.logger.info("Temperature 3: %s" , temp8)
							
							# file = open("/var/www/html/t1.txt", "w")
							# file.write(str(temp8))
							# file.close()
							
							#response = vartemp8.save_value({"value": temp8})
							rc = dwopen9.dwPropertyPublish( dwThingKey9, "temperature", temp8 )
							print "dwOpen API - Property Publish Returned... rc = ", rc
							
							
								
							if temp8 <> LastTemp8:
								if temp8 < 20:
									alarmState = 0
									alarmMsg   = "Temp - Cold"
								elif temp8 < 27:
									alarmState = 1
									alarmMsg   = "Temp - Normal"
								elif temp8 < 32:
									alarmState = 2
									alarmMsg   = "Temp - Warm"
								else:
									alarmState = 3
									alarmMsg   = "Temp - Hot"
								#time.sleep( 2 )
								rc = dwopen9.dwAlarmPublish( dwThingKey9, "alarm_temp", alarmState, alarmMsg );
								print "dwOpen API - Property Publish Returned... rc = ", rc
							

							LastTemp8 = temp8
						
						
						if "4225020405" in stringme:
							self.logger.info("Humidity 3: %s" , stringme)
							start = stringme.find("4225010405") + 21
							humidity8 = stringme[start : start + 4]
							humidity8 = float(int(humidity8, 16))/100
							self.logger.info("Humidity 3: %s" , humidity8)
							
							# file = open("/var/www/html/h1.txt", "w")
							# file.write(str(humidity8))
							# file.close()
							
							#response = varhumd3.save_value({"value": humidity8})
							rc = dwopen9.dwPropertyPublish( dwThingKey9, "humidity", humidity8 )
							print "dwOpen API - Property Publish Returned... rc = ", rc
							
							if humidity8 <> LastHumidity8:
								if humidity8 < 35:
									alarmState = 0
									alarmMsg   = "Humidity - Dry"
								elif humidity8 < 80:
									alarmState = 1
									alarmMsg   = "Humidity - Normal"
								else:
									alarmState = 2
									alarmMsg   = "Humidity - Wet"
								#time.sleep( 2 )
								rc = dwopen9.dwAlarmPublish( dwThingKey9, "alarm_humid", alarmState, alarmMsg );
								print "dwOpen API - Property Publish Returned... rc = ", rc
								
							LastHumidity8 = humidity8
							
							
						# if there is motion
						if "00010500026e9f002100000000" in stringme:
                                    # stop the time-counter thread
									print "=================================="
									print "=================================="
									print "=================================="
									print "=================================="

									global stop
									print 'Stop: ' + str(stop)
									stop = True
									print 'Stop: ' + str(stop)
									
									print "=================================="
									print "=================================="
									print "=================================="
									print "=================================="
                                    # reset timer to 0 because room is occupied
									tagA1 = 0

									self.logger.info("The stringme info: %s" , stringme)
									statusofhumanoccupancy=1
									#oCB.oSL._WriteMessage(E_SL_MSG_WRITE_ATTRIBUTE_REQUEST,"021021010102010000000001001c3001")
									
									
									print "AC IS ON AUTOMATICALLY on"
									rc = dwopen10.dwPropertyPublish( dwThingKey10, "Status", statusofhumanoccupancy )
									print "dwOpen API - Property Publish Returned... rc = ", rc
									#dwopen.dwMailboxAck( MsgID, 0, '', '' );

						# if there is no motion
						if "00010500026e9f002000000000" in stringme:
									self.logger.info("The stringme info: %s" , stringme)
									statusofhumanoccupancy=0
									
									# Set our flag to False so that timer thread can count
									stop = False
									
									# creates a thread that points to timerA1
									t1 = Thread(target=timerA1)

									# calls run method of thread
									try:
										t1.start() # Run timerA1, count for 240s
									except:
										print 'Thread failed to start'

                                    # Turn off aircon
									#oCB.oSL._WriteMessage(E_SL_MSG_WRITE_ATTRIBUTE_REQUEST,"021021010102010000000001001c3000")

									print "AC IS OFF AUTOMATICALLY"
									rc = dwopen10.dwPropertyPublish( dwThingKey10, "Status", statusofhumanoccupancy )
									print "dwOpen API - Property Publish Returned... rc = ", rc
									#dwopen.dwMailboxAck( MsgID, 0, '', '' );
									
						if "0001050002ca12002100010000" in stringme:
									self.logger.info("The stringme info: %s" , stringme)
									statusofhumanoccupancy=1
									rc = dwopen11.dwPropertyPublish( dwThingKey11, "Status", statusofhumanoccupancy )
									print "dwOpen API - Property Publish Returned... rc = ", rc
									#dwopen.dwMailboxAck( MsgID, 0, '', '' );		
						if "0001050002ca12002000010000" in stringme:
									self.logger.info("The stringme info: %s" , stringme)
									statusofhumanoccupancy=0
									rc = dwopen11.dwPropertyPublish( dwThingKey11, "Status", statusofhumanoccupancy )
									print "dwOpen API - Property Publish Returned... rc = ", rc
									#dwopen.dwMailboxAck( MsgID, 0, '', '' );
						if "000105000260c3002100020000" in stringme:
									self.logger.info("The stringme info: %s" , stringme)
									statusofhumanoccupancy=1
									rc = dwopen12.dwPropertyPublish( dwThingKey12, "Status", statusofhumanoccupancy )
									print "dwOpen API - Property Publish Returned... rc = ", rc
									#dwopen.dwMailboxAck( MsgID, 0, '', '' );
						if "000105000260c3002000020000" in stringme:
									self.logger.info("The stringme info: %s" , stringme)
									statusofhumanoccupancy=0
									rc = dwopen12.dwPropertyPublish( dwThingKey12, "Status", statusofhumanoccupancy )
									print "dwOpen API - Property Publish Returned... rc = ", rc
									#dwopen.dwMailboxAck( MsgID, 0, '', '' );
						if "0001050002e84b002100030000" in stringme:
									self.logger.info("The stringme info: %s" , stringme)
									statusofhumanoccupancy=1
									rc = dwopen13.dwPropertyPublish( dwThingKey13, "Status", statusofhumanoccupancy )
									print "dwOpen API - Property Publish Returned... rc = ", rc
									#dwopen.dwMailboxAck( MsgID, 0, '', '' );
						if "0001050002e84b002000030000" in stringme:
									self.logger.info("The stringme info: %s" , stringme)
									statusofhumanoccupancy=0
									rc = dwopen13.dwPropertyPublish( dwThingKey13, "Status", statusofhumanoccupancy )
									print "dwOpen API - Property Publish Returned... rc = ", rc
									#dwopen.dwMailboxAck( MsgID, 0, '', '' );

						if "975c0102010011" in stringme:
								print "dwOpen API - Executing Set Attribute Request..."
								start = stringme.find("975c0102010011") + 18
								coolingsetpoint = stringme[start : start + 4]
								temptest2 = stringme[start : start + 4]
								coolingsetpoint = float(int(coolingsetpoint, 16))/100
								self.logger.info("Temperature coolingsetpoint: %s" , stringme)
								self.logger.info("start: %s" , start)
								self.logger.info("Temperature Test 2: %s" , temptest2)
								self.logger.info("Temperature 2: %s" , coolingsetpoint)
								attribKey   = "coolingsetpoint"
								attribValue = str(coolingsetpoint) + " Degree Celsius"
								
								if coolingsetpoint <> LastCspAcPantry:
								#response = varenergy.save_value({"value": smartplugenergy})
									rc = dwopen14.dwSetAttribute( dwThingKey14, attribKey, attribValue );
									print "dwOpen API - Set Attribute Returned... rc = ", rc
									self.logger.info("Read Attributes response %s", stringme)
									time.sleep( 2 )
								
									rc = dwopen14.dwPropertyPublish( dwThingKey14, "coolingsetpoint", coolingsetpoint )
									print "dwOpen API - Property Publish Returned... rc = ", rc
								
								LastCspAcPantry = coolingsetpoint						
								
						if "975c0102010012" in stringme:
								print "dwOpen API - Executing Set Attribute Request..."
								start2 = stringme.find("975c0102010012") + 18
								heatingsetpoint = stringme[start2 : start2 + 4]
								temptest22 = stringme[start2 : start2 + 4]
								heatingsetpoint = float(int(heatingsetpoint, 16))/100
								self.logger.info("Temperature heatingsetpiont: %s" , stringme)
								self.logger.info("start2: %s" , start2)
								self.logger.info("Temperature Test 2: %s" , temptest22)
								self.logger.info("Temperature 2: %s" , heatingsetpoint)
								attribKey   = "heatingsetpoint"
								attribValue = str(heatingsetpoint)+ " Degree Celsius"
						
								rc = dwopen14.dwSetAttribute( dwThingKey14, attribKey, attribValue );
								print "dwOpen API - Set Attribute Returned... rc = ", rc
								self.logger.info("Read Attributes response %s", stringme)
								time.sleep( 2 )
						
						if "975c010201001c" in stringme:
								print "dwOpen API - Executing Set Attribute Request..."
								
								self.logger.info("Read Attributes response %s", stringme)
								
								start3 = stringme.find("975c010201001c") + 18
								workingstatus = stringme[start3 : start3 + 2]
								#statustest = stringme.find("975c010201001c") + 
								#workingstatus = float(int(workingstatus, 16))/100
								self.logger.info("Workingstatus: %s" , stringme)
								self.logger.info("start3: %s" , start3)
								#self.logger.info("statustest: %s" , statustest)
								self.logger.info("workingstatus: %s" , workingstatus)
								attribKey   = "workingstatus"
								
								
						
								if workingstatus <> LastStatusAcPantry:
							
									if( workingstatus == "01" ):
										print " The ac is on"
			
										attribValue="On"
										flag=30
					
									if( workingstatus == "00" ):
										print " The ac is off"
		
										attribValue="Off"
										flag=0
								#response = varenergy.save_value({"value": smartplugenergy})
									rc = dwopen14.dwSetAttribute( dwThingKey14, attribKey, attribValue );
									print "dwOpen API - Set Attribute Returned... rc = ", rc
									self.logger.info("Read Attributes response %s", stringme)
									time.sleep( 2 )
									rc = dwopen14.dwPropertyPublish( dwThingKey14, "workingstatus", flag )
									print "dwOpen API - Property Publish Returned... rc = ", rc
								LastStatusAcPantry = workingstatus						
								
						if "975c0102010000" in stringme:
									self.logger.info("Temperature 1: %s" , stringme)
									start = stringme.find("975c010201") + 18
									temp1 = stringme[start : start + 4]
									temptest = stringme[start : start + 4]
									temp1 = float(int(temp1, 16))/100
									self.logger.info("Temperature Test: %s" , temptest)
									self.logger.info("Temperature 1: %s" , temp1)
									rc = dwopen14.dwPropertyPublish( dwThingKey14, "temperature1", temp1 )
									print "dwOpen API - Property Publish Returned... rc = ", rc
									
						





						if "247c0102010011" in stringme:
								print "dwOpen API - Executing Set Attribute Request..."
								start247c = stringme.find("247c0102010011") + 18
								coolingsetpoint247c = stringme[start247c : start247c + 4]
								temptest2247c = stringme[start247c : start247c + 4]
								coolingsetpoint247c = float(int(coolingsetpoint247c, 16))/100
								self.logger.info("Temperature coolingsetpiont: %s" , stringme)
								self.logger.info("start: %s" , start247c)
								self.logger.info("Temperature Test 2: %s" , temptest2247c)
								self.logger.info("Temperature 2: %s" , coolingsetpoint247c)
								attribKey   = "coolingsetpoint"
								attribValue = str(coolingsetpoint247c) + " Degree Celsius"
								
								
								if coolingsetpoint247c <> LastCspAcMeetingRoom1:
								#response = varenergy.save_value({"value": smartplugenergy})
									rc = dwopen15.dwSetAttribute( dwThingKey15, attribKey, attribValue );
									print "dwOpen API - Set Attribute Returned... rc = ", rc
									self.logger.info("Read Attributes response %s", stringme)
									time.sleep( 2 )
								
									rc = dwopen15.dwPropertyPublish( dwThingKey15, "coolingsetpoint", coolingsetpoint247c )
									print "dwOpen API - Property Publish Returned... rc = ", rc
								
								LastCspAcMeetingRoom1 = coolingsetpoint247c						
								
								
						if "247c0102010012" in stringme:
								print "dwOpen API - Executing Set Attribute Request..."
								start2247c = stringme.find("247c0102010012") + 18
								heatingsetpoint247c = stringme[start2247c : start2247c + 4]
								#temptest22 = stringme[start2 : start2 + 4]
								heatingsetpoint247c = float(int(heatingsetpoint247c, 16))/100
								self.logger.info("Temperature heatingsetpiont: %s" , stringme)
								self.logger.info("start2: %s" , start2247c)
								#self.logger.info("Temperature Test 2: %s" , temptest22)
								self.logger.info("Temperature 2: %s" , heatingsetpoint247c)
								attribKey   = "heatingsetpoint"
								attribValue = str(heatingsetpoint247c) + " Degree Celsius"
						
								rc = dwopen15.dwSetAttribute( dwThingKey15, attribKey, attribValue );
								print "dwOpen API - Set Attribute Returned... rc = ", rc
								self.logger.info("Read Attributes response %s", stringme)
								time.sleep( 2 )
						
						if "247c010201001c" in stringme:
								print "dwOpen API - Executing Set Attribute Request..."
								#print "=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=- "
								#self.logger.info("Read Attributes response %s", stringme)
								#print "=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=- "
								start3247c = stringme.find("247c010201001c") + 18
								workingstatus247c = stringme[start3247c : start3247c + 2]
								#statustest = stringme.find("975c010201001c") + 
								#workingstatus = float(int(workingstatus, 16))/100
								self.logger.info("Workingstatus: %s" , stringme)
								#self.logger.info("start3: %s" , start3)
								#self.logger.info("statustest: %s" , statustest)
								self.logger.info("workingstatus: %s" , workingstatus247c)
								attribKey   = "workingstatus"
								
								
								
								if workingstatus247c <> LastStatusAcMeetingRoom1:
							
									if( workingstatus247c == "01" ):
										print " The ac is on"
			
										attribValue="On"
										flag=30
					
									if( workingstatus247c == "00" ):
										print " The ac is off"
		
										attribValue="Off"
										flag=0
								#response = varenergy.save_value({"value": smartplugenergy})
									rc = dwopen15.dwSetAttribute( dwThingKey15, attribKey, attribValue );
									print "dwOpen API - Set Attribute Returned... rc = ", rc
									self.logger.info("Read Attributes response %s", stringme)
									time.sleep( 2 )
									rc = dwopen15.dwPropertyPublish( dwThingKey15, "workingstatus", flag )
									print "dwOpen API - Property Publish Returned... rc = ", rc
								LastStatusAcMeetingRoom1 = workingstatus247c
								
								
								
						
								
						if "247c0102010000" in stringme:
									self.logger.info("Temperature 1: %s" , stringme)
									start247c = stringme.find("247c010201") + 18
									temp1247c = stringme[start247c : start247c + 4]
									#temptest = stringme[start : start + 4]
									temp1247c = float(int(temp1247c, 16))/100
									#self.logger.info("Temperature Test: %s" , temptest)
									self.logger.info("Temperature 1: %s" , temp1247c)
									rc = dwopen15.dwPropertyPublish( dwThingKey15, "temperature1", temp1247c )
									
									
								
									
									
									print "dwOpen API - Property Publish Returned... rc = ", rc
									
									
									
						if "10210102010011" in stringme:
								print "dwOpen API - Executing Set Attribute Request..."
								start1021 = stringme.find("10210102010011") + 18
								coolingsetpoint1021 = stringme[start1021 : start1021 + 4]
								#temptest2 = stringme[start : start + 4]
								coolingsetpoint1021 = float(int(coolingsetpoint1021, 16))/100
								self.logger.info("Temperature coolingsetpiont: %s" , stringme)
								#self.logger.info("start: %s" , start)
								#self.logger.info("Temperature Test 2: %s" , temptest2)
								self.logger.info("Temperature 2: %s" , coolingsetpoint1021)
								attribKey   = "coolingsetpoint"
								attribValue = str(coolingsetpoint1021) + " Degree Celsius"
								
								if coolingsetpoint1021 <> LastCspAcMeetingRoom2:
								#response = varenergy.save_value({"value": smartplugenergy})
									rc = dwopen16.dwSetAttribute( dwThingKey16, attribKey, attribValue );
									print "dwOpen API - Set Attribute Returned... rc = ", rc
									self.logger.info("Read Attributes response %s", stringme)
									time.sleep( 2 )
								
									rc = dwopen16.dwPropertyPublish( dwThingKey16, "Coolingsetpoint", coolingsetpoint1021 )
									print "dwOpen API - Property Publish Returned... rc = ", rc
								
								LastCspAcMeetingRoom2 = coolingsetpoint1021	
								
								
								
								
								
						if "10210102010012" in stringme:
								print "dwOpen API - Executing Set Attribute Request..."
								start2 = stringme.find("10210102010012") + 18
								heatingsetpoint1021 = stringme[start2 : start2 + 4]
								temptest22 = stringme[start2 : start2 + 4]
								heatingsetpoint1021 = float(int(heatingsetpoint1021, 16))/100
								self.logger.info("Temperature heatingsetpiont: %s" , stringme)
								self.logger.info("start2: %s" , start2)
								self.logger.info("Temperature Test 2: %s" , temptest22)
								self.logger.info("Temperature 2: %s" , heatingsetpoint1021)
								attribKey   = "heatingsetpoint"
								attribValue = str(heatingsetpoint1021)+ " Degree Celsius"
						
								rc = dwopen16.dwSetAttribute( dwThingKey16, attribKey, attribValue );
								print "dwOpen API - Set Attribute Returned... rc = ", rc
								self.logger.info("Read Attributes response %s", stringme)
								time.sleep( 2 )
								
								#rc = dwopen16.dwPropertyPublish( dwThingKey16, "Heatingsetpoint", heatingsetpoint1021 )
								#print "dwOpen API - Property Publish Returned... rc = ", rc	
						
						if "1021010201001c" in stringme:
								print "dwOpen API - Executing Set Attribute Request..."

								self.logger.info("Read Attributes response %s", stringme)
								
								start31021 = stringme.find("1021010201001c") + 18
								workingstatus1021 = stringme[start31021 : start31021 + 2]
								#statustest = stringme.find("975c010201001c") + 
								#workingstatus = float(int(workingstatus, 16))/100
								self.logger.info("Workingstatus: %s" , stringme)
								self.logger.info("start3: %s" , start31021)
								#self.logger.info("statustest: %s" , statustest)
								self.logger.info("workingstatus: %s" , workingstatus1021)
								attribKey   = "workingstatus"
								
								print workingstatus1021
								
								
								
						
								if workingstatus1021 <> LastStatusAcMeetingRoom2:
							
									if( workingstatus1021 == "01" ):
										print " The ac is on"
			
										attribValue="On"
										flag=30
					
									if( workingstatus1021 == "00" ):
										print " The ac is off"
		
										attribValue="Off"
										flag=0
										
								#response = varenergy.save_value({"value": smartplugenergy})
									rc = dwopen16.dwSetAttribute( dwThingKey16, attribKey, attribValue );
									print "dwOpen API - Set Attribute Returned... rc = ", rc
									self.logger.info("Read Attributes response %s", stringme)
									time.sleep( 2 )
									rc = dwopen15.dwPropertyPublish( dwThingKey16, "workingstatus", flag )
									print "dwOpen API - Property Publish Returned... rc = ", rc
								LastStatusAcMeetingRoom2 = workingstatus1021
								print "Last value",LastStatusAcMeetingRoom2
								print "Last value2",workingstatus1021
						if "10210102010000" in stringme:
									self.logger.info("Temperature 1: %s" , stringme)
									start1021 = stringme.find("1021010201") + 18
									temp11021 = stringme[start1021 : start1021 + 4]
									#temptest = stringme[start : start + 4]
									temp11021 = float(int(temp11021, 16))/100
									#self.logger.info("Temperature Test: %s" , temptest)
								
									if (temp11021<22):
										oCB.oSL._WriteMessage(E_SL_MSG_WRITE_ATTRIBUTE_REQUEST,"0210210101020100000000010011290960")
										print "Temperature has been changed quitely"
									self.logger.info("Temperature 1: %s" , temp11021)
									rc = dwopen16.dwPropertyPublish( dwThingKey16, "temperature1", temp11021 )
									print "dwOpen API - Property Publish Returned... rc = ", rc
									

									
												
									
									
									
									
							
                #else:
                    
								#print "-----------------------------------------------------------"
								#self.logger.warning("Unhandled message 0x%04x", eMessageType)
								#self.logger.info("Read Attributes response %s", stringme)
								#print "-----------------------------------------------------------"
							# try:
                      
                        # # Yield control to other thread to allow it to set up the listener
                        # if ((eMessageType == E_SL_MSG_SAVE_PDM_RECORD)or
                            # (eMessageType == E_SL_MSG_LOAD_PDM_RECORD_REQUEST) or
                            # (eMessageType == E_SL_MSG_DELETE_PDM_RECORD) or
                            # (eMessageType == E_SL_MSG_PDM_HOST_AVAILABLE)):                            
                                # self.dMessageQueue[eMessageType] = Queue.Queue(30)
                        # time.sleep(0)
                        # self.dMessageQueue[eMessageType].put(sData)
                    # except KeyError:
		
        finally:
            self.logger.debug("Read thread terminated")


    def SendMessage(self, eMessageType, sData=""):
        """ Send a message to the node amd wait for its synchronous response
            Raise cSerialLinkError or cModuleError on failure
        """
        self.logger.info("Host->Node: Command  0x%04x, length %d", eMessageType, (len(sData)/2))
        self._WriteMessage(eMessageType, sData)
        try:
            status = self.WaitMessage(E_SL_MSG_STATUS, 1)
        except cSerialLinkError:
            raise cSerialLinkError("Module did not acknowledge command 0x%04x" % eMessageType)
        
        status = struct.unpack("B", status[0])[0]
        message = "" if len(sData) == 0 else sData
        
        if status == 0:
            stringme= (':'.join(x.encode('hex') for x in sData))
            self.logger.info("Command success. %s " %message)
        else:
            # Error status code
            raise cModuleError(status, message)


    def WaitMessage(self, eMessageType, fTimeout):
        """ Wait for a message of type eMessageType for fTimeout seconds
            Raise cSerialLinkError on failure
            Many different threads can all block on this function as long
            as they are waiting on different message types.
        """
        sData = None
        try:
            # Get the message from the receiver thread, and delete the queue entry
            sData = self.dMessageQueue[eMessageType].get(True, fTimeout)
            del self.dMessageQueue[eMessageType]
        except KeyError:
            self.dMessageQueue[eMessageType] = Queue.Queue()
            try:
                # Get the message from the receiver thread, and delete the queue entry
                sData = self.dMessageQueue[eMessageType].get(True, fTimeout)
                del self.dMessageQueue[eMessageType]
            except Queue.Empty:
                # Raise exception, no data received
                raise cSerialLinkError("Message 0x%04x not received within %fs" % (eMessageType, fTimeout))
        
        self.logger.debug("Pulled message type 0x%04x from queue", eMessageType)
        return sData



class cControlBridge():
    """Class implementing commands to the control bridge node"""
    def __init__(self, port, baudrate=115200):
        self.oSL = cSerialLink(port, baudrate)
        #self.oPdm = cPDMFunctionality(port)
        #self.oSL._WriteMessage(E_SL_MSG_PDM_HOST_AVAILABLE_RESPONSE,"00")

    def parseCommand(self,IncCommand):
        """parse commands"""
        command=str.split(IncCommand,",")          
        if command[0] == 'EXIT':
            return False
        if command[0] == 'EXP':
            self.SetExtendedPANID(command[1])
        if command[0] == 'GTV':            
            print "Node Version: 0x%08x" % self.GetVersion()
        if command[0] == 'RST':
            self.SendSwReset()
        if command[0] == 'LQI':
            self.SendLqiRequest(command[1],command[2])
        if command[0] == 'DEV':
            self.SetDeviceType(command[1])
        if command[0] == 'SIS':
            self.SetInitialSecurity(command[1],command[2],command[3],command[4])
        if command[0] == 'EPD':
            self.ErasePersistentData()
        if command[0] == 'ZFN':
            self.ZLLFactoryNewPersistentData()
        if command[0] == 'TLK':
            if(command[1] == '0'):
                self.InitiateTouchLink()
            else:
                self.InitiateTouchLinkFactoryReset()
        if command[0] == 'START':
            self.StartNetwork()
        if command[0] == 'SCAN':
            self.StartScan()
        if command[0] == 'ONFT':
           self.SendOnOffToggle(command[1],command[2],command[3],command[4],command[5])
        if command[0] == 'M2HS':
            self.SendMoveToHue(command[1],command[2],command[3],command[4],command[5],command[6])
        if command[0] == 'CHL':
            self.SetChannelMask(command[1])
        if command[0] == 'DEFAULTC':
            self.ErasePersistentData()            
            self.SendSwReset()
            time.sleep(5)
            self.SetDeviceType('00')
            time.sleep(1)
            self.SetChannelMask('0000000B') 
            time.sleep(1)
            self.SetExtendedPANID('ABCDEFABCDEFABCD')
            time.sleep(1)
            self.StartNetwork()

        if command[0] == 'DEFAULTRZLL1':
            self.ErasePersistentData()
            self.SendSwReset()
            time.sleep(5)
            self.SetDeviceType('01')
            time.sleep(1)
            self.SetChannelMask('0000000B') 
            time.sleep(1)
            self.SetExtendedPANID('ABCDEFABCDEFABCD')
            time.sleep(1)
            self.StartNetwork()

        if command[0] == 'DEFAULTRZLL2':
            self.ErasePersistentData()
            self.SendSwReset()
            time.sleep(5)
            self.SetDeviceType('01')
            time.sleep(1)
            self.SetInitialSecurity('03','00','01','5A6967426565416C6C69616E63653039')
            time.sleep(1)
            self.SetInitialSecurity('04','00','01','D0D1D2D3D4D5D6D7D8D9DADBDCDDDEDF')
            time.sleep(1)
            self.SetChannelMask('00000014') 
            time.sleep(1)
            self.SetExtendedPANID('ABCDEFABCDEFABCD')
            time.sleep(1)
            self.StartDeviceScan()

        if command[0] == 'DEFAULTRZLLHA':
            self.ErasePersistentData()
            self.SendSwReset()
            time.sleep(5)
            self.SetDeviceType('02')
            time.sleep(1)
            self.SetChannelMask('0000000F') 
            time.sleep(1)
            self.SetExtendedPANID('ABCDEFABCDEFABCD')
            time.sleep(1)
            self.StartNetwork()       

        if command[0] == 'MDR':
            self.SendMatchDescriptor(command[1],command[2],command[3],command[4],command[5],command[6])

        if command[0] == 'LOF':
            self.SendLevelOnff(command[1],command[2],command[3],command[4],command[5],command[6])

        if command[0] == 'SDR':
            self.SendSimpleDescriptor(command[1],command[2])

        if command[0] == 'LQI':
            self.SendLqiRequest(command[1],command[2])            

        if command[0] == 'SPJ':
            self.SetPermitJoiningOnTarget(command[1],command[2],command[3])

        if command[0] == 'RDR':
            self.ReadAttributeRequest(command[1],command[2],command[3],command[4],command[5],command[6],command[7],command[8],command[9],command[10])

        if command[0] == 'GGM':
            self.GetGroupMembership(command[1],command[2],command[3],command[4],command[5])

        if command[0] == 'ADG':
            self.AddGroup(command[1],command[2],command[3],command[4],command[5])


        if command[0] == 'CLOOP':
            self.ColourControlLoop(command[1],command[2],command[3],command[4],command[5],command[6],command[7],command[8],command[9])

        if command[0] == 'MCT':
            self.MoveColourTemperature(command[1],command[2],command[3],command[4],command[5],command[6],command[7],command[8],command[9])

        if command[0] == 'M2CT':
            self.MoveToColourTemperature(command[1],command[2],command[3],command[4],command[5],command[6])

        if command[0] == 'DISREP':
            self.SendMatchDescriptor('FFFD','C05E','01','0006','00','0000')
            self.SendMatchDescriptor('FFFD','0104','01','0006','00','0000')

        if command[0] == 'PDMDUMP':        
            conn = sqlite3.connect('pdm.db')
            c = conn.cursor()
            conn.close()
            
        print ''
        return True
    
    def GetVersion(self):
        """Get the version of the connected node"""
        self.oSL.SendMessage(E_SL_MSG_GET_VERSION)
        version = self.oSL.WaitMessage(E_SL_MSG_VERSION_LIST, 0.5)
        return struct.unpack(">I", version)[0]

    def SetExtendedPANID(self,extPanid):
        """Set Extended PANID"""
        self.oSL.SendMessage(E_SL_MSG_SET_EXT_PANID,str(extPanid))
        

    def SendSwReset(self):
        """Send SW Reset"""
        self.oSL.SendMessage(E_SL_MSG_RESET)
            

    def SetDeviceType(self,device):
        """Set device type"""
        self.oSL.SendMessage(E_SL_MSG_SET_DEVICETYPE,str(device))


    def StartDeviceScan(self):
        """Start scan on the device"""
        self.oSL.SendMessage(E_SL_MSG_START_SCAN)

    def DeviceStartNetwork(self):
        """Start network"""
        self.oSL.SendMessage(E_SL_MSG_START_NETWORK)

    def SetInitialSecurity(self,KeyState,KeySeq,KeyType,sKey):
        """Set Initial Security state and key"""
        self.oSL.SendMessage(E_SL_MSG_SET_SECURITY,(str(KeyState)+str(KeySeq)+str(KeyType)+str(sKey)))

    def ErasePersistentData(self):
        """Erase persistent data"""
        self.oSL._WriteMessage(E_SL_MSG_ERASE_PERSISTENT_DATA,"")

    def ZLLFactoryNewPersistentData(self):
        """Erase persistent data"""
        self.oSL._WriteMessage(E_SL_MSG_ZLL_FACTORY_NEW,"")
        

    def InitiateTouchLink(self):
        """Initiate Touch Link"""
        self.oSL.SendMessage(E_SL_MSG_INITIATE_TOUCHLINK)


    def SetChannelMask(self,channel):
        """Start Network"""
        self.oSL.SendMessage(E_SL_MSG_SET_CHANNELMASK,str(channel))

    def StartNetwork(self):
        """Start Network"""
        self.oSL.SendMessage(E_SL_MSG_START_NETWORK)

    def StartScan(self):
        """Start Network"""
        self.oSL.SendMessage(E_SL_MSG_START_SCAN)

    def SendOnOffToggle(self,addressmode,TargetAddress,srcEp,DstEp,EffectsCommandId):
        """Send on Off or Toggle command"""
        self.oSL.SendMessage(E_SL_MSG_ONOFF_NOEFFECTS,(str(addressmode)+str(TargetAddress)+str(srcEp)+str(DstEp)+str(EffectsCommandId)))

    def SendMoveToHue(self,addressmode,TargetAddress,srcEp,DstEp,Hue,Saturation,TransitionTime):
        """Send move to hue command"""
        self.oSL.SendMessage(E_SL_MSG_MOVE_TO_HUE_SATURATION,(str(addressmode)+str(TargetAddress)+str(srcEp)+str(DstEp)+str(Hue)+str(Saturation)+str(TransitionTime)))
        
    def SendMatchDescriptor(self,TargetAddress,profile,InputClusterCount,InputClusterList,OutputClusterCount,OutputClusterList):
         """Send match descriptor command"""
         self.oSL.SendMessage(E_SL_MSG_MATCH_DESCRIPTOR_REQUEST,(str(TargetAddress)+str(profile)+str(InputClusterCount)+str(InputClusterList)+str(OutputClusterCount)+str(OutputClusterList)))

    def SendLevelOnff(self,TargetAddress,srcEp,DstEp,bOnOff,level,time):
         """Send match descriptor command"""
         self.oSL.SendMessage(E_SL_MSG_MOVE_TO_LEVEL_ONOFF,(str(addressmode)+str(TargetAddress)+str(srcEp)+str(DstEp)+str(bOnOff)+str(level)+str(time)))

    def SendSimpleDescriptor(self,TargetAddress,endpoint):
         """Send match descriptor command"""
         self.oSL.SendMessage(E_SL_MSG_SIMPLE_DESCRIPTOR_REQUEST,(str(TargetAddress)+str(endpoint)))

    def SendLqiRequest(self,TargetAddress,startidx):
         """Send LQI command"""
         self.oSL.SendMessage(E_SL_MSG_MANAGEMENT_LQI_REQUEST,(str(TargetAddress)+str(startidx)))
         
    def InitiateTouchLinkFactoryReset(self):
        """Initiate Touch Link factory reset"""
        self.oSL.SendMessage(E_SL_MSG_TOUCHLINK_FACTORY_RESET)


    def SetPermitJoiningOnTarget(self,targetAddress,pemitDuration,TcOverride):
        """Initiate Touch Link factory reset"""
        self.oSL.SendMessage(E_SL_MSG_PERMIT_JOINING_REQUEST,(str(targetAddress)+str(pemitDuration)+str(TcOverride)))


    def ReadAttributeRequest(self,addressmode,TargetAddress,srcEp,dstEp,clusterid,bServer,bManufactuer,ManId,numberOfAttributes,attributelist):
         """Send Read Attributes Request"""
         self.oSL.SendMessage(E_SL_MSG_READ_ATTRIBUTE_REQUEST,(str(addressmode)+str(TargetAddress)+str(srcEp)+str(dstEp)+str(clusterid)+str(bServer)+str(bManufactuer)+str(ManId)+str(numberOfAttributes)+str(attributelist)))

    def GetGroupMembership(self,addressmode,targetAddress,srcEp,DstEp,GroupCount,GroupList):
        """Get group membership"""
        self.oSL.SendMessage(E_SL_MSG_GET_GROUP_MEMBERSHIP,(str(addressmode)+str(targetAddress)+str(srcEp)+ str(DstEp)+str(GroupCount)+str(GroupList)))

    def AddGroup(self,addressmode,targetAddress,srcEp,DstEp,GroupId):
        """Add Group"""
        self.oSL.SendMessage(E_SL_MSG_ADD_GROUP,(str(addressmode)+str(targetAddress)+str(srcEp)+ str(DstEp)+str(GroupId)))


    def ColourControlLoop(self,addressmode,targetAddress,srcEp,DstEp,updatedFlags,Actions,direction,time,startHue):
        """start colour control loop"""
        self.oSL.SendMessage(E_SL_MSG_COLOUR_LOOP_SET,(str(addressmode)+str(targetAddress)+str(srcEp)+ str(DstEp)+str(updatedFlags)+str(Actions)+str(direction)+str(time)+str(startHue)))

    def MoveColourTemperature(self,addressmode,targetAddress,srcEp,DstEp,mode, rate,minTemp,maxTemp,transitionTime):
        """move temperature"""
        self.oSL.SendMessage(E_SL_MSG_MOVE_COLOUR_TEMPERATURE,(str(addressmode)+str(targetAddress)+str(srcEp)+ str(DstEp)+str(mode)+str(rate)+str(minTemp)+str(maxTemp)+str(transitionTime)))

    def MoveToColourTemperature(self,addressmode,targetAddress,srcEp,DstEp,colourtemp,transitionTime):
        """move to temperature"""
        self.oSL.SendMessage(E_SL_MSG_MOVE_TO_COLOUR_TEMPERATURE,(str(addressmode)+str(targetAddress)+str(srcEp)+ str(DstEp)+str(colourtemp)+str(transitionTime)))

    def vPDMSendFunc(self,sData):
        """ Internal function
        """
        #print "PDMSend"
        conn = sqlite3.connect('pdm.db')
        c = conn.cursor()
        conn.text_factory = str
        RecordId = (''.join(x.encode('hex') for x in sData))
        #print RecordId
        c.execute("SELECT * FROM PdmData WHERE PdmRecId = ?", (RecordId,))
        data=c.fetchone()                        
        status='00'
        if data is None:
            #print "None"
            TotalBlocks = 0
            BlockId = 0
            size =0
            self.oSL.SendMessage(E_SL_MSG_LOAD_PDM_RECORD_RESPONSE, (status+RecordId+str(size).zfill(8)+str(TotalBlocks).zfill(8)+str(BlockId).zfill(8))+str(size).zfill(8))
        else:
            status='02'
            #print "found entry"
            persistedData = data[2]
            size = data[1]
            TotalBlocks = (long(size,16)/128)
            if((long(size,16)%128)>0):
                NumberOfWrites = TotalBlocks + 1
            else:
                NumberOfWrites = TotalBlocks
            #print size
            #print persistedData
            #print TotalBlocks
            #print NumberOfWrites
            #print long(size,16)
            bMoreData=True
            count =0
            lowerbound = 0
            upperbound = 0
            while(bMoreData):
                u32Size = long(size,16) - (count*128)
                if(u32Size>128):
                    u32Size = 256
                else:
                    bMoreData = False
                    u32Size = u32Size*2
                 
                upperbound =upperbound + u32Size
                DataStrip = persistedData[lowerbound:upperbound]
                count = count+1
                self.oSL.SendMessage(E_SL_MSG_LOAD_PDM_RECORD_RESPONSE,(status+RecordId+size+(hex(NumberOfWrites).strip('0x')).strip('L').zfill(8)+(hex(count).strip('0x')).strip('L').zfill(8)+(hex(u32Size/2).strip('0x')).strip('L').zfill(8)+DataStrip))                
                lowerbound = lowerbound+u32Size                
                
        conn.commit()
        conn.close()
        
if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser()
    
    parser.add_option("-p", "--port", dest="port",
                      help="Serial port device name to use", default="/dev/ttyUSB0")
                      
    parser.add_option("-b", "--baudrate", dest="baudrate",
                      help="Baudrate", default=1000000)

    (options, args) = parser.parse_args()
    
    logging.basicConfig(format="%(asctime)-15s %(levelname)s:%(name)s:%(message)s")
    logging.getLogger().setLevel(logging.INFO)
                    
    if options.port is None:
        #print "Please specify serial port with --port"
        parser.print_help()
        sys.exit(1)
		
	
	
   

    oCB = cControlBridge(options.port, options.baudrate)
    continueToRun = True
    #bRunning = True
    oCB.oSL._WriteMessage(E_SL_MSG_PDM_HOST_AVAILABLE_RESPONSE,"00")
    useString = str(options.port)+ ""
    while continueToRun:                    
        # command = raw_input(useString+'$ ')
        # if(command == ""):
            # continueToRun = True
        # else:
            # continueToRun = oCB.parseCommand(command.strip())
			
		try:
			command = raw_input(useString+'$ ')
			continueToRun = oCB.parseCommand(command.strip())
		except (EOFError):
			continueToRun = True
			
		
    print "Terminating current session...."
    sys.exit(1)


    
