#! /usr/bin/env python3


def chooseCommand(signalNum, stackFrame) :
    print('Possible Commands are: \n') 
    print('Get Status Jog')
    print('Move to Entered Coordinates')
    print('Move to Zero Zero')
    print('Move to Delta Coordinates')
    print('Move to Home')
    print('Send Stop')
    print('Read Pointing')
    Command = input()

    if(Command.lower() == 'move to entered coordinates') :

        print('Enter the Azimuth Coordinates(in degrees).')
        Az = int(input())

        print('Enter the Elevation Coordinates(in degrees).')
        El = int(input())
        
        print('The Azimuth is : ', Az,'The Elevation is : ', El)
        
    if(Command.lower() == 'move to delta coordinates') :

        print('Enter the delta Azimuth Coordinate(in degrees)')
        deltaAz = int(input())
        
        print('Enter the delta Elevation Coordinate(in degrees)')
        deltaEl = int(input())
        
        print('The delta Azimuth is : ', deltaAz,'The delta Elevation is : ', deltaEl) 

        
#    print('Signal Number : ', signalNum, 'Frame : ', stackFrame)


def main() :
  #Import the necessary modules.
  import signal
  import time
  import argparse
  import serial
  import QPTFunctions as QPTF
  import getParams as gP

  #Set up the serial port parameters.
  port = '/dev/ttyUSB1'
  baud_rate = 9600  #Standard baud rate for the controller.
  byte_size = serial.EIGHTBITS  #Set the size of the byte to be written.
  parity = serial.PARITY_NONE #Took this from the manual under the Autobaud section.
  timeout = 1  #Not sure what is the best value for this.  I might want to set this to some
  #floating point value.

  ser = serial.Serial(
      port = port,
      baudrate = baud_rate,
      bytesize = byte_size,
      parity = parity,
      timeout = timeout)
 
  #Fill in the Parameter data class values for latitude, longitude and altitude.
  PARAMS.latitude = 38.9983  #Air Force Academy
  PARAMS.longitude = -104.8613  #Air Force Academy
  PARAMS. altitude = 2068.982  #Air Force Academy. Units are meters.  This corresponds to 6788 ft.

  #Set the signal object.  The function chooseCommand is called upon receiving an interrupt. 
  signal.signal(signal.SIGINT, chooseCommand)
    
  #Lets start a loop.
  while(True) :
      
    #Write out a statement that will ask the user to send interrupt to program
    #when a new command is required.
    print('Enter Control-C to send a command to the Controller.')
    time.sleep(0.5)

    #Send continuous Get Status commands to the controller so that it stays
    #synched up with the server/computer.
    bytesWritten = ser.write(QPTF.getSimpleStatusCommand())
  #End of while loop - while(keepGoing):


        
# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()
