#! /usr/bin/env python3

#A program to communicate with the QPT azimuthal and elevation controller.

# A command to find the ports that are available is : python -m serial.tools.list_ports


#Gather our code in a main() function.
def main() :
  import argparse
  import serial
  import QPTFunctions as QPTF
  import getParams as gP
  from geopy.geocoders import Nominatim
  
  #Set up the serial port.
  port = '/dev/ttyUSB1'
  baud_rate = 9600  #Standard baud rate for the controller.
  byte_size = serial.EIGHTBITS  #Set the size of the byte to be written.
  parity = serial.PARITY_NONE #Took this from the manual under the Autobaud section.
  timeout = 1  #Not sure what is the best value for this.  I might want to set this to some
  #floating point value.

#  ser = serial.Serial(
#    port = port,
#    baudrate = baud_rate,
#    bytesize = byte_size,
#    parity = parity,
#    timeout = timeout)
    
  #Fill the PARAMS dataclass.
  PARAMS = gP.getParams(QPTF.getArgs(argparse.ArgumentParser()))
  
  #Get the latitude and longitude.
  locator = Nominatim(user_agent = 'QPT')
  location = locator.geocode(PARAMS.location)
  latitude = location.latitude
  longitude = location.longitude
  
  #Get the altitude.
  altitude = QPTF.getElevation(latitude, longitude)

  #Fill in the Parameter data class values for latitude, longitude and altitude.
  PARAMS.latitude = latitude
  PARAMS.longitude = longitude
  PARAMS. altitude = altitude

  breakpoint()
  
  if(Command == 'send status jog') :
    QPTF.sendStatusJog(PARAMS, ser)
  #End of if statement - if(Command == 'SendStatusJog') :
  
  if(Command == 'send stop') :
    QPTF.sendStop(PARAMS, ser)
  #End of if statement- if(Command == 'SendStatusJog') :
    
  if(Command == 'move to zero zero') :
    QPTF.moveToZeroZero(PARAMS, ser)
  #End of if statement - if(Command == 'SendStatusJog') :

  if(Command == 'move to entered coords') :
    QPTF.moveToEnteredCoords(PARAMS, ser)
  #End of if statement - if(Command == 'SendStatusJog') :
    
  if(Command == 'move to delta coords') :
    QPTF.moveToDeltaCoords(PARAMS, ser)
  #End of if statement - if(Command == 'SendStatusJog') :

  if(Command == 'move to home') :
    QPTF.moveToHome(PARAMS, ser)
  #End of if statement -  if(Command == 'MoveToHome')

  #Close the serial port.
  ser.close()
  
# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()


