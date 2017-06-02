import numpy as np
import socket
import sys
import time
import RPi.GPIO as GPIO

#TCP/IP related
TCP_IP = '192.168.0.249'
TCP_PORT = 50000
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



def main():
  global s
  s.connect((TCP_IP, TCP_PORT))

  s.send('ENA')

  
  if float(sys.argv[1])>=0:
    	UV_value = float(sys.argv[1])
    	DB_value = float(sys.argv[2])
    	BL_value = float(sys.argv[3])
    	GR_value = float(sys.argv[4])
    	RE_value = float(sys.argv[5])
    	IR_value = float(sys.argv[6])

    	#print('%.4f' % UV_value+' '+'%.4f' % DB_value+' '+'%.4f' % BL_value+' '+'%.4f' % GR_value+' '+'%.4f' % RE_value+' '+'%.4f' % IR_value)

    	try:
    		
    		s.send('UVX %f'%UV_value)
		time.sleep(0.5)

    		s.send('DBL %f'%DB_value)
		time.sleep(0.5)

    		s.send('BLU %f'%BL_value)
		time.sleep(0.5)

    		s.send('GRE %f'%GR_value)
		time.sleep(0.5)

    		s.send('RED %f'%RE_value)
		time.sleep(0.5)

    		s.send('IRX %f'%IR_value)
		#time.sleep(0.5)

		print 'UVX %f'%UV_value,'DBL %f'%DB_value,'BLU %f'%BL_value,'GRE %f'%GR_value,'RED %f'%RE_value,'IRX %f'%IR_value
    	except:
    		print "problem sending"  	

  else:

    	print('shutoff')

    	s.send('UVX 0')
	#time.sleep(0.5)
    	s.send('DBL 0')
	#time.sleep(0.5)
    	s.send('BLU 0')
	#time.sleep(0.5)
    	s.send('GRE 0')
	#time.sleep(0.5)
    	s.send('RED 0')
	#time.sleep(0.5)
    	s.send('IRX 0')

    	GPIO.setmode(GPIO.BCM)
    	GPIO.setwarnings(False)

    	GPIO.setup(9, GPIO.OUT)
    	GPIO.setup(26, GPIO.OUT)
    	GPIO.setup(12, GPIO.OUT)
    	GPIO.setup(13, GPIO.OUT)
    	GPIO.setup(14, GPIO.OUT)
    	GPIO.setup(15, GPIO.OUT)

    	GPIO.output(9, 0) #UV
    	GPIO.output(26, 0) #Deep blue
    	GPIO.output(12, 0) #Blue
    	GPIO.output(13, 0) #Green
    	GPIO.output(14, 0) #Red
    	GPIO.output(15, 0) #IR

  s.send('DIS')



if __name__ == '__main__':
  main()