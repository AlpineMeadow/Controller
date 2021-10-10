

#This group of functions are meant for use in the QPT.py program.  They will be used to set the
#correct form of the command to be sent to the controller.



#Bits are set to active high, that is, set or 1 indicates that the condition exists.

#Hard faults require that a reset command is sent.

#Set some Control characters.
#The escape character.  Used for when command data is the same as the one of the
               #ACK, NAK, STX or ETX characters.
ESC = 0x27

#The start of text character.
STX = 0x2

#The end of text character.
ETX = 0x3

#The acknowledge character.
ACK = 0x6

#The not acknowledge character.
NAK = 0xF

#This next set of constants are active high.  This means that if the condition exists then the
#bit is set to 1, otherwise it is set to zero.
CWSL = 0   # Clockwise Soft Limit.
CCWSL = 0  # Counter Clockwise Soft Limit.
CWHL = 0   # Clockwise Hard Limit.
CCWHL = 0  # Counter Clockwise Hard Limit.
TO = 0     # Time Out - This can be found in either Tilt or Pan status bits.
DE = 0     # Direction Error - This can be found in either Tilt or Pan status bits.
OL = 0     # Overload Error - This can be found in either Tilt or Pan status bits.
PRF = 0    # Pan Resolver Fault.
USL = 0    # Up Soft Limit.
DSL = 0    # Down Soft Limit.
UHL = 0    # Up Hard Limit.
DHL = 0    # Down Hard Limit.
TRF = 0    # Tilt Resolver Fault.
HRES = 0   # High Resolution
EXEC = 0   # Executing command.
DES = 0    # Destination. These are the coordinatates of the destination not the actual coordinates.
OSLR = 0   # Soft Limit Override.
CWM = 0    # Clockwise Moving - controller is currently moving clockwise.
CCWM = 0   # Counter Clockwise Moving - controller is currently moving counter clockwise.
UPM = 0    # Up Moving - controller is currently moving upward.
DWNM = 0   # Down Moving - controller is currently moving downward.

#Define some masks.

#Mask out the pan soft and hard limits.
maskCWSL = 128  #Clockwise Soft Limit.
maskCCWSL = 64  #Counter Clockwise Soft Limit.
maskCWHL = 32   #Clockwise Hard Limit.
maskCCWHL = 16  #Counter Clockwise Hard Limit.

#Mask out the tilt soft and hard limits.
maskUSL = 128  #Up Soft Limit.
maskDSL = 64   #Down Soft Limit.
maskUHL = 32   #Up Hard Limit.
maskDHL = 16   #Down Hard Limit.

#Mask out the moving and destination flags.
maskHRES = 128  #High Resolution.
maskEXEC = 64   #Executing command.
maskDES = 32   #The destination coordinates.
maskOSLR = 16   #Overridden Soft Limit.

#Mask out the pan and tilt motions.
maskCWM = 8    #Clockwise motion.
maskCCWM = 4  #Counter Clockwise motion.
maskUPM = 2   #Upward motion.
maskDWNM = 1  #Downard motion.

#Mask out the Error messages.
maskTO = 8     #Time Out.
maskDE = 4     #Direction Error.
maskOL = 2     #Current Overload.
maskPRF = 1    #Pan Resolver Fault.
maskTRF = 1    #Tilt Resolver Fault.

#################################################################################

#################################################################################

def getArgs(parser) :
  """

   NAME:  getArgs
           
   PURPOSE:  Gets the command line arguments and places them in variables.
             
   CATEGORY:  Machine Command
              
   CALLING SEQUENCE: Called by main.py
  
   INPUTS:
            parser : The parser object.
  
   OPTIONAL INPUTS: None
                  
   KEYWORD PARAMETERS: None
                  
   OUTPUTS: The data class PARAMS
            Azimuth : A value the user wants to command the controller to point to.
            Elevation : A value the user wants to command the controller to point to.
            deltaAzEl : A two element list containing the delta Azimuth and delta
            Elevation values.
            Speeds :  A two element list containing the pan and tilt speed.
            StatusJogFlags : A four element list of flags to set the Resolver Units,
            the OverrideSoftLimit, Stop and Reset commands.
            Position :  A four element list indentifying the latitude, longitude,
            altitude  and location of the user.
            saveDir : The path of the directory to save the data file in.
            Command :  The command the user wants to send to the controller.
                 
   OPTIONAL OUTPUTS:  None
                   
   SIDE EFFECTS: All of these parametes are filled by the user.  
                   
   RESTRICTIONS: None
                   
   EXAMPLE: getArgs(parser)
  
   MODIFICATION HISTORY:
             Written by jdw on  October 8, 2021

  """

  CommandList = ('Possible Commands are: \n' + 'Get Status Jog, Move to Entered Coordinates, Move to Zero Zero, Move to Delta Coordinates, Move to Home, Send Stop')

  
  #Get the parameters
  parser.add_argument('-Az', '--Azimuth', default = 0.0,
                      help = 'Choose the starting Azimuth', type = float)

  parser.add_argument('-El', '--Elevation', default = 0.0,
                      help = 'Choose the starting Elevation', type = float)
  
  parser.add_argument('-dAz', '--DeltaAz', default = 0.0,
                      help = 'Choose the delta Azimuth', type = float)

  parser.add_argument('-dEl', '--DeltaEl', default = 0.0,
                      help = 'Choose the delta Elevation', type = float)
  
  parser.add_argument('-PS', '--PanSpeed', default = 0.0,
                      help = 'Choose the pan speed', type = float)

  parser.add_argument('-TS', '--TiltSpeed', default = 0.0,
                      help = 'Choose the tilt speed', type = float)
  
  parser.add_argument('-RU', '--ResolverUnits', default = 0,
                      help = 'Send Response from Controller in Resolver Units', type = int)
  
  parser.add_argument('-OSL', '--OverrideSoftLimit', default = 0,
                      help = 'Send override soft limit to the controller', type = int)

  parser.add_argument('-STOP', '--Stop', default = 0,
                      help = 'Send a stop command to the controller', type = int)

  parser.add_argument('-RES', '--Reset', default = 0,
                      help = 'Send a reset to the controller', type = int)

  parser.add_argument('-ALT', '--Altitude', default = 0.0,
                      help = 'Altitude of location ', type = float)
  
  parser.add_argument('-LAT', '--Latitude', default = 0.0,
                      help = 'Latitude of location', type = float)

  parser.add_argument('-LONG', '--Longitude', default = 0.0,
                      help = 'Longitude of location', type = float)

  parser.add_argument('-LOC', '--Location', default = 'Air Force Academy',
                      help = 'Text description of location', type = str)

  parser.add_argument('-SD', '--SaveDirectory', default = '/home/jdw/Sparc/Quickset/',
                      help = 'Directory to save data in.', type = str)

  parser.add_argument('-C','--Command', default = '',
                      help = CommandList, type = str)

  args = parser.parse_args()
  
  #Generate variables from the inputs.
  Azimuth = args.Azimuth
  Elevation = args.Elevation
  deltaAz = args.DeltaAz
  deltaEl = args.DeltaEl
  panSpeed = args.PanSpeed
  tiltSpeed = args.TiltSpeed  
  ResolverUnits = args.ResolverUnits
  OSL = args.OverrideSoftLimit
  Stop = args.Stop
  Res = args.Reset
  Altitude = args.Altitude
  Latitude = args.Latitude
  Longitude = args.Longitude
  Location = args.Location
  saveDirectory = args.SaveDirectory
  Command = args.Command
  Command = Command.lower()
  
  deltaAzEl = [deltaAz, deltaEl]
  Speeds = [panSpeed, tiltSpeed]
  StatusJogFlags = [ResolverUnits, OSL, Stop, Res]
  Position = [Altitude, Latitude, Longitude, Location]

  return [Azimuth, Elevation, deltaAzEl, Speeds, StatusJogFlags, Position,
  saveDirectory, Command]

#End of the function getArgs(parser).py

#################################################################################

#################################################################################

def getElevation(latitude, longitude) :
  """

   NAME: getElevation(latitude, longitude)
           
   PURPOSE: Use internet service to determine the elevation of a given latitude and
   longitude. 
             
   CATEGORY: Machine Control
              
   CALLING SEQUENCE: Called by QPT.py
  
   INPUTS:
           latitude : The latitude of the location.  This is of type float. 
           longitude : The longitude of the location.  This is of type float.
  
   OPTIONAL INPUTS:  None
                  
   KEYWORD PARAMETERS:  None
                  
   OUTPUTS:  Returns the elevation in meters of the given latitude and longitude.
                 
   OPTIONAL OUTPUTS:  None
                   
   SIDE EFFECTS:  None
                   
   RESTRICTIONS:  None
                   
   EXAMPLE: elevation = getElevation(latitude, longitude)
  
   MODIFICATION HISTORY:
             Written by jdw on October 8, 2021

  """

  import requests
  import pandas as pd    

  #Use the internet to find the elevation given the latitude and longitude.
  query = 'https://api.open-elevation.com/api/v1/lookup'f'?locations={latitude},{longitude}'
  r = requests.get(query).json()
  elevation = pd.json_normalize(r, 'results')['elevation'].values[0]

  return elevation

#End of the function getElevation(latitude, longitude).py

#################################################################################

#################################################################################

def getControllerFlagsStatus(moveType, controllerOutput) :
  """

   NAME:  getControllerFlagStatus(moveType, controllerOutput)
           
   PURPOSE: Determine if any of the controller status flags are active.  This can be
   done for either the pan move or the tilt move or for just the general instrument
   parameters. 
             
   CATEGORY: Machine Control.
              
   CALLING SEQUENCE:  Called by all of the functions that send a command to the controller.
  
   INPUTS:
            moveType : A string describing which of the movement types to be looked at.
            controllerOutput : The output from the controller.  This value will be
            anded to each of the possible flags to determine which if any are
            active.  The controller sets the flags to a value of 1 to indicate that
            they are active.  
  
   OPTIONAL INPUTS: None
                  
   KEYWORD PARAMETERS: None
                  
   OUTPUTS:  All active test results are printed to the screen.  There is nothing
   returned. 
                 
   OPTIONAL OUTPUTS: None
                   
   SIDE EFFECTS: None
                   
   RESTRICTIONS: None
                   
   EXAMPLE: getControllerFlagsStatus('Pan', panStatus)
  
   MODIFICATION HISTORY:
             Written by jdw on October 8, 2021

  """

  #This function will pull the flags out of the returned controller output.

  if(moveType == 'Pan') :
    if(controllerOutput & maskCWSL == 1) :
      print('The clockwise soft limit for the pan motion is active. ')

    if(controllerOutput & maskCCWSL == 1) :
      print('The Counter Clockwise soft limit for the pan motion is active. ')
      
    if(controllerOutput & maskCWHL == 1) :
      print('The Clockwise hard limit for the pan motion is active. ')
      
    if(controllerOutput & maskCCWHL == 1) :
      print('The Counter Clockwise hard limit for the pan motion is active. ')
      
    if(controllerOutput & maskTO == 1) :
      print('The Time Out for the pan motion is active. ')
      
    if(controllerOutput & maskDE == 1) :
      print('The Direction Error for the pan motion is active. ')
      
    if(controllerOutput & maskOL == 1) :
      print('The Current Overload for the pan motion is active. ')
      
    if(controllerOutput & maskPRF == 1) :
      print('The Pan Resolver Fault is active. ')
  #End of if clause - if(moveType == 'Pan')
  
  if(moveType == 'Tilt') :
    if(controllerOutput & maskUSL == 1) :
      print('The Up soft limit for the tilt motion is active. ')
      
    if(controllerOutput & maskDSL == 1) :
      print('The Down soft limit for the tilt motion is active. ')
      
    if(controllerOutput & maskUHL == 1) :
      print('The Up hard limit for the tilt motion is active. ')
      
    if(controllerOutput & maskDHL == 1) :
      print('The Down hard limit for the tilt motion is active. ')
      
    if(controllerOutput & maskTO == 1) :
      print('The Time Out for the tilt motion is active. ')
      
    if(controllerOutput & maskDE == 1) :
      print('The Direction Error for the tilt motion is active. ')
      
    if(controllerOutput & maskOL == 1) :
      print('The Current Overload for the tilt motion is active. ')
      
    if(controllerOutput & maskTRF == 1) :
      print('The Pan Resolver Fault is active. ')
  #End of if clause - if(moveType == 'Tilt') :
  
  if(moveType == 'Gen') :  #Here Gen is short for general status.
    if(controllerOutput & maskHRES == 1) :
      print('The Up soft limit for the tilt motion is active. ')
      
    if(controllerOutput & maskEXEC == 1) :
      print('The controller is executing and command. ')
      
    if(controllerOutput & maskDES == 1) :
      print('The destination of the controller. ')
      
    if(controllerOutput & maskOSLR == 1) :
      print('The Overridden Soft Limit switch is active. ')
      
    if(controllerOutput & maskCWM == 1) :
      print('The Controller is moving in a clockwise motion. ')
      
    if(controllerOutput & maskCCWM == 1) :
      print('The Controller is moving in a counter clockwise motion. ')
      
    if(controllerOutput & maskUPM == 1) :
      print('The Controller is moving in an upward direction. ')
      
    if(controllerOutput & maskPRF == 1) :
      print('The Controller is moving in a downward direction. ')
  #End of if clause - if(moveType == 'Gen') :
    
  return
#End of the function getControllerFlags.py
#################################################################################

#################################################################################

def writePanTiltValues(PARAMS, panCoord, tiltCoord) :
  """

   NAME:  writePanTiltValues(PARAMS)
           
   PURPOSE:  Write(or append) the controller pointing values(Az and El) to a file.
             
   CATEGORY:  Machine Control.
              
   CALLING SEQUENCE:  Called by all functions that send a pan or tilt command to the
   controller. 
  
   INPUTS:
               PARAMS : The parameter data class.
               panCoord : The pan location of the controller.  This is an integer.
               tiltCoord : The tilt location of the controller.  This is an integer.
  
   OPTIONAL INPUTS: None
                  
   KEYWORD PARAMETERS: None
                  
   OUTPUTS: None
                 
   OPTIONAL OUTPUTS: None
                   
   SIDE EFFECTS: A file is written.
                   
   RESTRICTIONS: None
                   
   EXAMPLE: writePanTiltValues(PARAMS, panCoord, tiltCoord)
  
   MODIFICATION HISTORY:
             Written by jdw on October 8, 2021

  """
  import time
  
  #Get the date and time.
  timestr = time.localtime()

  yearStr = str('{0:02d}'.format(timestr[0]))
  monthStr = str('{0:02d}'.format(timestr[1]))
  dayStr = str('{0:02d}'.format(timestr[2]))
  hourStr = str('{0:02d}'.format(timestr[3]))
  minuteStr = str('{0:02d}'.format(timestr[4]))

  dateTime = yearStr + monthStr + dayStr + '_' + hourStr + ':' + minuteStr

  #Generate a filename.
  filename = PARAMS.saveDir + PARAMS.location + dateTime + '.csv'
  
  #Write the data to a file.
  if(path.exists(filename)) :
    #Append to the file.
    with open(filename, mode='a') as f :
      dataWriter = csv.writer(f, delimiter=',')
      dataWriter.writerow([datetime, pan, tilt])
      #End of the for loop - for i in range(len(LST)):
    #End of the with statement - with open(filename, mode='a') as f :

  else :
    #Write the file.
    with open(filename, mode='w') as f :
      writeDataHandle = csv.writer(f, delimiter=',')
      writeDataHandle.writerow([latitude, longitude, altitude])
      writeDataHandle.writerow([datetime, pan, tilt])
      #End of the for loop - for i in range(len(LST)):
    #End of the with statement - with open(filename, mode='w') as f :
  #End of if-else clause.
  
  return

#End of the function writePanTiltValues.py

#################################################################################

#################################################################################

def getLittleEndian(value, nbits) :
  """

   NAME: getLittleEndian(value, nbits)
           
   PURPOSE:  This function converts an integer value into a two component list of 16
   bit signed two's complement little endian hexadecimal values.  This function was
   extremely difficult to write and if there are any problems(bugs) with this
   program, this would be the first function I would troubleshoot.
             
   CATEGORY: Machine Control.
              
   CALLING SEQUENCE:  Called by all functions that send a move command to the controller.
  
   INPUTS:
           value : The integer value of the move command.  This can be for either the
           azimuth control or the elevation control.
           nbits : The number of bits to write the integer.  This should almost
           always be 16 but I made it a variable(instead of a parameter) for some
           unforeseen cases.                   

   OPTIONAL INPUTS: None
                  
   KEYWORD PARAMETERS: None
                  
   OUTPUTS: The 16 bit 2's complement integer of the input.
                 
   OPTIONAL OUTPUTS:  None
                   
   SIDE EFFECTS:  None
                   
   RESTRICTIONS: None
                   
   EXAMPLE:  AzBytes = getLittleEndian(value, nbits)
  
   MODIFICATION HISTORY:
             Written by jdw on October 8, 2021

  """

  #Take the integer value and turn it into a hexadecimal value of the proper format.
  #Here we are dealing with negative values.  This command forces hex() to deal with
  #the called for(nbits) length otherwise Python will assign infinite precision to
  #these values which is just confusing and gives wrong results.
  temphex = hex((value + (1 << nbits)) % (1 << nbits))  #We are moding here so that
  #we end up with the same number but of the correct size.

  #Turn the hexadecimal number into an integer.
  tempint = int(temphex, 16)

  #Generate a string that holds the hexadecimal value of the temporary integer.
  hexnum = hex(tempint)[2:]  #[2:] removes the '0x' part of the representation.

  #Determine the length of the string and find the the number of zeros to pad.
  numZeros = 4 - len(hexnum)
  zeropad = numZeros*'0'

  #Join the zeros to the hexadecimal number.
  hexnum = zeropad + hexnum

  #Now turn the string into an integer.
  byte1 = int(hexnum[2] + hexnum[3], 16)
  byte2 = int(hexnum[0] + hexnum[1], 16)

  #We need to check to see that byte1 and/or byte2 does not match a control
  #character.
  ESCAPE = 0x1B
  byteDict = {'byte1' : [], 'byte2' : []}
  
  if((byte1==STX) or (byte1==ETX) or (byte1==ACK) or (byte1==NAK) or (byte1==ESC)) :
    #The byte is the same as the control character.  We add an escape and flip the
    #seventh bit.  This will result in two bytes being returned.
    b1 = [ESCAPE, byte1^0x80]
    byteDict['byte1'] = b1
  else :
    b1 = [byte1] 
    byteDict['byte1'] = b1
  
  if((byte2==STX) or (byte2==ETX) or (byte2==ACK) or (byte2==NAK) or (byte2==ESC)) :
    #The byte is the same as the control character.  We add an escape and flip the
    #seventh bit.  This will result in two bytes being returned.
    b2 = [ESCAPE, byte2^0x80]
  else :
    b2 = [byte2] 
    byteDict['byte2'] = b2

  #Return a list of the properly ordered integers.
  return byteDict

#End of the function getLittle.py
#################################################################################

#################################################################################

#This function will calculate the check sum of all of the sub-commands used in a particular
#controller command.  The result will be returned as a hexidecimal value.
def getCheckSum(Values) :
  """

   NAME: getCheckSum(Values)
           
   PURPOSE:  Check to see that the command sent to the controller is correct.
             
   CATEGORY: Machine Control.
              
   CALLING SEQUENCE:  Called by all functions that send a command to the controller.
  
   INPUTS: 
           Values : A list of bytes that are components of the command.
           
   OPTIONAL INPUTS: None
                  
   KEYWORD PARAMETERS: None
                  
   OUTPUTS:  The result of the check sum calculation. This calculation is simply the
   OR'ing of all of the value items.
                 
   OPTIONAL OUTPUTS: None
                   
   SIDE EFFECTS:  None
                   
   RESTRICTIONS: None 
                   
   EXAMPLE:   LRC = getCheckSum(Values)
  
   MODIFICATION HISTORY:
             Written by jdw on October 9, 2021

  """

    import numpy as np

    #Find the number of sub-commands to be XORed.
    n = len(Values)

    #Get the first value to XOR.  I want to make these values into signed 8-bit integers.
    result = np.int8(Values[0])
    
    #Loop through the remaining values, XORing them to the original result.
    for i in range(n - 1) :
        result ^= np.int8(Values[i + 1])
    #End of for loop; For i in range(n - 1) :
    
    #Convert to hexidecimal and return.
    return result

#End of the function getCheckSum.py
#################################################################################

#################################################################################

def sendTimeout(PARAMS, ser, timeLength, Query = 0) :
  """
  
   NAME: sendTimeout(PARAMS, ser, timeLength, Query = 0) :
           
   PURPOSE:  Send a timeout to the controller.
             
   CATEGORY:  Machine Control.
              
   CALLING SEQUENCE:  As of this writing,this command is implemented but is not called.
  
   INPUTS:
           PARAMS : The parameter data class.
           ser : The serial port object.
           Timelength : The length of time (in seconds) to set the timeout.
           Query : Whether or not to set the LSB to 1 or not.  If not then we set the
           timeout value. 
  
   OPTIONAL INPUTS: None
                  
   KEYWORD PARAMETERS: None
                  
   OUTPUTS:  None
                 
   OPTIONAL OUTPUTS: None
                   
   SIDE EFFECTS: The timeout value is set on the controller.
                   
   RESTRICTIONS:  None
                   
   EXAMPLE: 
  
   MODIFICATION HISTORY:
             Written by jdw on  October 9, 2021

  """

    import numpy as np

    #The Query variable is essentially a flag.  If set to 1, the controller will return the
    #current value of the timeout without changing it.  If set to 0, the controller will send
    #the timelength value to the controller.  Since we will call this function with the express
    #purpose of changing the timeout value we will set Query to zero automatically.
    
    #Normally a communication timeout is considered a fault of sufficient weight to stop any
    #automated movement of the controller.
    #Setting the timeout value to zero will result in the controller operating autonomously.
    #This setting defeats any stop due to a communication fault.
    CommandNumber = 0x96

    if(Query) :
      #We change the 0th bit to 1.
      Timeout = 0x1
    else :
      numbits = 16
      Timeout = getLittleEndian(timelength, numbits)
    #End of if-else clause.

    #Generate the LRC checksum.  
    Values = [CommandNumber, Timeout[0], Timeout[1]]
    LRC = getCheckSum(Values)

    Command = bytearray()
    Command.append(STX)
    Command.append(CommandNumber)
    Command.append(Timeout)
    Command.append(LRC)
    Command.append(ETX)

    sendCommand(ser, Command)
    return 

#End of the function sendTimeout.py

#################################################################################

#################################################################################


def getSimpleStatusCommand() :
  """

   NAME: getSimpleStatusCommand
           
   PURPOSE:  Generate a bytearray containing the proper commands to get a simple
   status command.  This function will be used to ensure that communications between
   controller and server stay synched.
             
   CATEGORY: Machine Controller.
              
   CALLING SEQUENCE:  Called by any function that will ultimately send a control
   command to the controller.
  
   INPUTS:  None
  
   OPTIONAL INPUTS: None
                  
   KEYWORD PARAMETERS: None
                  
   OUTPUTS:  Returns the get status command.
                  
   OPTIONAL OUTPUTS: None
                   
   SIDE EFFECTS: None
                   
   RESTRICTIONS: None
                   
   EXAMPLE: getSimpleStatusCommand()
  
   MODIFICATION HISTORY:
             Written by jdw on October 8, 2021

  """

  simpleStatusCommand = bytearray()

  simpleStatusCommand.append(STX)
  simpleStatusCommand.append(0x31)
  simpleStatusCommand.append(0x31)
  simpleStatusCommand.append(ETX)
  
  return simpleStatusCommand
#End of getSimpleStatusCommand.py

#################################################################################

#################################################################################

def sendStop(PARAMS, ser) :
  """

   NAME: sendStop(PARAMS, ser) :
           
   PURPOSE: Send a stop command to the controller.
             
   CATEGORY:  Machine Control.
              
   CALLING SEQUENCE:  Can be called by any function that is sending a command to the
   controller. However, I have not implemented this because doing so would require
   setting up some kind of interrupt and I have not done so nor do I really know
   how.  
  
   INPUTS:
            PARAMS : The parameter data class.
            ser : The serial port object.
  
   OPTIONAL INPUTS: None
                  
   KEYWORD PARAMETERS: None
                  
   OUTPUTS: None
                 
   OPTIONAL OUTPUTS: None
                   
   SIDE EFFECTS:  The controller motion is stopped.
                   
   RESTRICTIONS: None
                   
   EXAMPLE:
  
   MODIFICATION HISTORY:
             Written by jdw on October 9, 2021

  """

  #This function will stop the controller.  It will do so by setting the speed of the tilt and
  #pan motors to zero.  What I do not understand is how to interrupt the motion in real time.  I
  #suspect that I will be able to do this through the getStatus/Jog command but I haven't worked
  #out the details.

    CommandNumber = 0x31

    #Set the stopByte of the CommandByte to an integer value of 2(00000010).
    RES = 0  #00000000 in binary.
    OverrideSoftLimit = 0  #00000000 in binary.
    StopByte = 2 #00000010 in binary.
    RU = 0 #00000000 in binary.
    CmdByte = RU + OverrideSoftLimit + StopByte + RES

    JogPanSpeed = 0x0  #Setting this to zero will stop the controller from panning.
    JogTiltSpeed = 0x0  #Setting this to zero will stop the controller from tilting.

    #If the stop bit is set, then it must be unset in order to get the controller to move.  In
    #principle this should be set to : StopByte = 0.

    #Generate the LRC checksum.  
    Values = [CommandNumber, Command, JogPanSpeed, JogTiltSpeed]
    LRC = getCheckSum(Values)

    #Generate the command.
    Command = bytearray()
    Command.append(STX)
    Command.append(CommandNumber)
    Command.append(Command) 
    Command.append(JogPanSpeed)
    Command.append(JogTiltSpeed)
    Command.append(LRC)
    Command.append(ETX)

    #Send the command to the controller.
    sendCommand(PARAMS, ser, Command)
    
    return

#End of the function sendStop.py

#################################################################################

#################################################################################

def sendStatusJog(PARAMS, ser, StatusJogFlags, panJogSpeed, tiltJogSpeed):
  """

   NAME:  sendStatusJog(PARAMS, ser, StatusJogFlags, PanJogSpeed, TiltJogSpeed) 
           
   PURPOSE:  Send a get status/jog command to the controller.  This command can be
   used to determine the controller parameters as well as causing the controller to
   stop moving by setting the PanJogSpeed and TiltJogSpeed to zero.
             
   CATEGORY: Machine Control
              
   CALLING SEQUENCE:  Called by QPT.py
  
   INPUTS:
           PARAMS : The parameter data class.
           ser : The serial port object. 
           StatusJogFlags : A set of integer flags used to set machine parameters.
           panJogSpeed : The value of the pan speed.  This is an integer.
           tiltJogSpeed : The value of the tilt speed.  This is an integer.
  
   OPTIONAL INPUTS: None
                  
   KEYWORD PARAMETERS: None
                  
   OUTPUTS: None
                 
   OPTIONAL OUTPUTS: None
                   
   SIDE EFFECTS: The controller may be caused to stop moving.
                   
   RESTRICTIONS: None
                   
   EXAMPLE: sendStatusJog(PARAMS, ser, StatusJogFlags, PanJogSpeed, TiltJogSpeed)
  
   MODIFICATION HISTORY:
             Written by jdw on October 9, 2021

  """

  #This function gets the status of the controller and it can also be used to ensure that
  #the controller stays awake.

  #There are four bits that can be set for the command byte.

  #If RU = 00000001 then the controller returns resolver units for both pan and tilt instead
  #of angles.
  if(PARAMS.resolverUnits) :
    RU = 1
  else :
    RU = 0
  #End of if-else clause.
  
  #If OSL = 00000010 then we override the soft limits during jog.  This could result in
  #damage to the controller.
  if(PARAMS.overrideSoftLimits) :
    OSL = 2
  else :
    OSL = 0
  #End of if-else clause.

  #If STOP = 00000100 then the controller stops.  In order for the controller to continue
  #this bit must be reset to zero.
  if(PARAMS.stop) :
    STOP = 4
  else :
    STOP = 0
  #End of if-else clause.
    
  #If RES = 00001000 then all hard faults are cleared.
  if(PARAMS.reset) :
    RES = 8
  else :
    RES = 0
  #End of if-else clause.

  #Start text value.
  STX = 0x2

  #Calculate the pan and tilt integers.
  nbits = 16
  panJogCommand = getLittleEndian(panJogSpeed)
  tiltJogCommand = getLittleEndian(tiltJogSpeed)
  
  CommandNumber = 0x31
  Command = RU + OSL + STOP + RES
  Aux1Command = 0x0  #This command is not used.
  Aux2Command = 0x0  #This command is not used.
  ETX = 0x3
  
  #Generate the LRC checksum.  
  Values = [CommandNumber, Command, panJogCommand[0], panJogCommand[1],
            tiltJogCommand[0], tiltJogCommand[1]]
  LRC = getCheckSum(Values)

  #Fill the command array.
  Command = bytearray()
  Command.append(STX)
  Command.append(CommandNumber)
  Command.append(Command)
  Command.append(panJogCommand[0])
  Command.append(panJogCommand[1])
  Command.append(tiltJogCommand[0])
  Command.append(tiltJogCommand[1])
  Command.append(LRC)
  Command.append(ETX)

  sendCommand(PARAMS, ser, Command)

  return 

#End of the function sendStatusJog.py

#################################################################################

#################################################################################

def moveToEnteredCoords(PARAMS, ser) :
  """

   NAME: moveToEnteredCoords(PARAMS, ser)
           
   PURPOSE:  Send a command to the controller to move to a set of entered coordinates.
             
   CATEGORY: Machine Control.
              
   CALLING SEQUENCE:  Called by QPT.py
  
   INPUTS:
           PARAMS : the parameter data class.
           ser : The serial port object
  
   OPTIONAL INPUTS: None
                  
   KEYWORD PARAMETERS: None
                  
   OUTPUTS: None
                 
   OPTIONAL OUTPUTS: None
                   
   SIDE EFFECTS: The controller moves to the entered coordinates.
                   
   RESTRICTIONS: None
                   
   EXAMPLE: moveToEnteredCoords(PARAMS, ser)
  
   MODIFICATION HISTORY:
             Written by jdw on October 9, 2021

  """

  #First multiply the values by 10 in order to get the proper precision.
  Azimuth = PARAMS.Azimuth*10.0
  Elevation = PARAMS.Elevation*10.0

  #Now convert the resulting angle coordinates into integers.
  Az = int(Azimuth)
  El = int(Elevation)

  #Check to see that the Azimuth and Elevation values are within appropriate ranges.
  if ((Az > 3600) or (Az < -3600)) :
    sys.exit('Azimuth range exceeds allowable values.  Exiting')
  #End of if statement - if ((Az > 3600) or (Az < -3600)) :
  
  if ((El > 1800) or (El < -1800)) :
    sys.exit('Elevation range exceeds allowable values. Exiting')
  #End of if statement - if((El > 1800) or (El < -1800)) :
  
  CommandNumber = 0x33
    
  #Convert the Azimuth and Elevation values into 16-bit signed two's-complement little endian
  #integers.
  numbits = 16
  AzBytes = getLittleEndian(Az, numbits)
  ElBytes = getLittleEndian(El, numbits)
    
  #Generate the checksum(Longitudinal reduncancy check).
  Values = [CommandNumber, AzBytes[0], AzBytes[1], ElBytes[0], ElBytes[1]]
  LRC = getCheckSum(Values)

  #Set up the command array.
  Command = bytearray()
  Command.append(STX)
  Command.append(CommandNumber)
  Command.append(AzBytes[0])
  Command.append(AzBytes[1])
  Command.append(ELBytes[0])
  Command.append(ElBytes[1])
  Command.append(LRC)
  Command.append(ETX)
  
  #Send the command to the controller.
  sendCommand(PARAMS, ser, Command)
  
  return

#End of the function moveToEnteredCoordinates.py

#################################################################################

#################################################################################


def moveToZeroZero(PARAMS, ser) :
  """

   NAME:
           
   PURPOSE:
             
   CATEGORY:
              
   CALLING SEQUENCE:
  
   INPUTS:
                   : 
                   : 
                   : 
                   : 
  
   OPTIONAL INPUTS:
                  
   KEYWORD PARAMETERS:
                  
   OUTPUTS:
                 
   OPTIONAL OUTPUTS:
                   
   SIDE EFFECTS:
                   
   RESTRICTIONS:
                   
   EXAMPLE:
  
   MODIFICATION HISTORY:
             Written by jdw on 

  """

    CommandNumber = 0x35
    STX = 0x2
    ETX = 0x3

    #Get the check sum value.
    Values = [CommandNumber]
    LRC = getCheckSum(Values)

    #Set up the command array.
    Command = bytearray()
    Command.append(STX)
    Command.append(CommandNumber)
    Command.append(LRC)
    Command.append(ETX)

    #Send the command to the controller.
    sendCommand(PARAMS, ser, Command)
    
    return 

#End of the function moveToZeroZero.py

#################################################################################

#################################################################################


def moveToDeltaCoords(PARAMS, ser) :
  """

   NAME: moveToDeltaCoords(PARAMS, ser)
           
   PURPOSE: Send a move to delta(pan) and delta(tilt) command to the controller.
             
   CATEGORY: Machine Control
              
   CALLING SEQUENCE: Called by QPT.py
  
   INPUTS:
          PARAMS : The parameter data class.
          sers : The serial port object.
  
   OPTIONAL INPUTS: None
                  
   KEYWORD PARAMETERS: None
                  
   OUTPUTS: None
                 
   OPTIONAL OUTPUTS: None
                   
   SIDE EFFECTS: The controller is sent a command to more to delta(pan) and
   delta(tilt). 
                   
   RESTRICTIONS: None
                   
   EXAMPLE: moveToDeltaCoords(PARAMS, ser)
  
   MODIFICATION HISTORY:
             Written by jdw on October 9, 2021

  """

  
  sendCommand(PARAMS, ser, Command)
  
  return Command

#End of the function MoveToDeltaCoordinates.py

#################################################################################

#################################################################################

def moveToHome(PARAMS, ser) :
  """

   NAME: moveToHome(PARAMS, ser) 
           
   PURPOSE:  Send the move to home command to the controller.
             
   CATEGORY: Machine Control.
              
   CALLING SEQUENCE:  Called by QPT.py
  
   INPUTS:
           PARAMS : The parameter data class.
           ser : The serial port object.
  
   OPTIONAL INPUTS: None
                  
   KEYWORD PARAMETERS: None
                  
   OUTPUTS: None
                 
   OPTIONAL OUTPUTS: None
                   
   SIDE EFFECTS: The controller gets the home command.
                   
   RESTRICTIONS: None
                   
   EXAMPLE: moveToHome(PARAMS, ser)
  
   MODIFICATION HISTORY:
             Written by jdw on October 9, 2021

  """

  #The command number for moving to controller home position.
  CommandNumber = 0x36

  #Generate the checksum(Longitudinal reduncancy check).
  Values = [CommandNumber]
  LRC = getCheckSum(Values)
  
  #Set up the command array.
  Command = bytearray()
  Command.append(STX)
  Command.append(CommandNumber)
  Command.append(LRC)
  Command.append(ETX)

  #Send the command to the controller.
  sendCommand(PARAMS, ser, Command)
  
  return 

#End of the function MoveToHome.py

#################################################################################

#################################################################################

def readControllerOutput(ser, chunkSize=200):
  """

   NAME: readControllerOuput(ser, chunck_size = 200)
           
   PURPOSE:  Read the controller output.
             
   CATEGORY: Machine Control
              
   CALLING SEQUENCE: Called by all of the following functions : sendStatusJog,
   sendStop, moveToZeroZero, moveToEnteredCoords, moveToDeltaCoords, moveToHome.
  
   INPUTS:
          ser : The serial port object
          chunckSize : The size in bytes of the data to be read.  In general a size
          of two hundred will be more than large enough to get the entire controller
          output. 
  
   OPTIONAL INPUTS: None
                  
   KEYWORD PARAMETERS: None
                  
   OUTPUTS: None
                 
   OPTIONAL OUTPUTS: None
                   
   SIDE EFFECTS: None
                   
   RESTRICTIONS: None
                   
   EXAMPLE: readControllerOutput(ser, chunckSize)
  
   MODIFICATION HISTORY:
             Written by jdw on October 9, 2021

  """

  if not ser.timeout:
    raise TypeError('Port needs to have a timeout set!')

  read_buffer = b''

  while True:
    # Read in chunks. Each chunk will wait as long as specified by
    # timeout. Increase chunk_size to fail quicker
    byte_chunk = ser.read(size=chunk_size)
    read_buffer += byte_chunk
    if not len(byte_chunk) == chunk_size:
      break
  #End of while clause - while True :
  
  return read_buffer
#End of the function readControllerOutput.py

###################################################################################

###################################################################################

def parseControllerOutput(PARAMS, bufferOutput) :

  """

   NAME:  parseControllerOutput(PARAMS, BufferOutput)
           
   PURPOSE:  Abstract the information from the return output of the controller.
             
   CATEGORY : Machine Control.
              
   CALLING SEQUENCE:  called by sendCommand.py
  
   INPUTS:
           PARAMS : The parameter data class.
           bufferOutput : The output obtained from the controller.
  
   OPTIONAL INPUTS: None
                  
   KEYWORD PARAMETERS: None
                  
   OUTPUTS: None
                 
   OPTIONAL OUTPUTS: None
                   
   SIDE EFFECTS: The controller output is written by the function
   writePanTiltValues.py which is called from this function.
                   
   RESTRICTIONS: None
                   
   EXAMPLE: parseBuffer = QPTF.parseControllerOutput(PARAMS, readBufferCoordinates)
  
   MODIFICATION HISTORY:
             Written by jdw on October 10, 2021

  """

  #Separate out the various bytes of information returned by the controller.
  ackByte = bufferOutput[0]
  Command = bufferOutput[1]
  panCoord = bufferOutput[2]
  tiltCoord = bufferOutput[3]
  panStatus = bufferOutput[4]
  tiltStatus = bufferOutput[5]
  genStatus = bufferOutput[6]
  LRC = bufferOutput[7]
  ETX = bufferOutput[8]
  
  #Check to see if any of the controller Status flags are active.
  getControllerFlagsStatus('Pan', panStatus)
  getControllerFlagsStatus('Tilt', tiltStatus)
  getControllerFlagsStatus('Gen', genStatus)

  #Write returned pan and tilt values to a file.
  writePanTiltValues(PARAMS, panCoord, tiltCoord)

  return

#End of the function parseControllerOutput.py  
###################################################################################

###################################################################################

def sendCommand(PARAMS, ser, Command) :
  """

   NAME:  sendCommand(PARAMS, ser, Command)
           
   PURPOSE: This function actually sends the desired command to the controller.
             
   CATEGORY: Machine Control.
              
   CALLING SEQUENCE:  Called by the following functions: moveToHome,
   moveToDeltaCoords, moveToZeroZero, moveToEnteredCoords, sendStop, SendStatusJog
  
   INPUTS:
           PARAMS : The parameter data class.
           ser : The serial port object.
           Command : The command (byte array) to be sent to the controller.
  
   OPTIONAL INPUTS: None
                  
   KEYWORD PARAMETERS: None
                  
   OUTPUTS: None
                 
   OPTIONAL OUTPUTS: None
                   
   SIDE EFFECTS:  The controller is sent a command.
                   
   RESTRICTIONS: None
                   
   EXAMPLE: sendCommand(PARAMS, ser, Command)
  
   MODIFICATION HISTORY:
             Written by jdw on October 9, 2021

  """

  #Set a truth value.
  keepSending = 1
  
  #Loop to get the server synched with the controller.  Once it is synched then send the
  #command. 
  while(keepSending) :

    #Send the simplest Get Status/Jog command to snych up with the controller.
    bytesWritten = ser.write(getSimpleStatusCommand())
    
    if(bytesWritten != 0) :
      
      #The server is snyched up with the controller so lets send the command.
      StatusWritten = ser.write(Command)

      #Read the information sent from the controller to the server.
      readBufferCoordinates = QPTF.readControllerOutput(ser, chunk_size = 200)

      #Parse that information and communicate to the user any errors.
      parseBuffer = QPTF.parseControllerOutput(PARAMS, readBufferCoordinates)
      
      keepSending = 0  #Change flag so as to stop the while loop.
    #End of if statement - if(bytesWritten != 0) :
    
  #End of while statement - while(keepSending) :

  return

#End of the function sendCommand.py
###################################################################################

###################################################################################

