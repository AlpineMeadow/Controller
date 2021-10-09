#This module will set up a data class that will hold all of the parameters.

def getParams(params) :

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

    from dataclasses import dataclass

    #Create a data class that holds the parameters for communicating with the
    #controller.
    @dataclass(frozen = False)
    class PARAMS :
        Azimuth : float
        Elevation : float
        deltaAz : float
        deltaEl : float
        panJogSpeed : float
        tiltJogSpeed : float
        resolverUnits : int
        overrideSoftLimits : int
        stop : int
        reset : int
        altitude : float
        latitude : float
        longitude : float
        location : str
        command : str
    #End of the PARAMS class definition.

#    breakpoint()   

    Azimuth = params[0]
    Elevation = params[1]
    deltaAz = params[2][0]
    deltaEl = params[2][1]
    panJogSpeed = params[3][0]
    tiltJogSpeed = params[3][1]
    resolverUnits = params[4][0]
    overrideSoftLimits = params[4][1]
    stop = params[4][2]
    reset = params[4][3]
    altitude = params[5][0]
    latitude = params[5][1]
    longitude = params[5][2]
    location = params[5][3]
    command = params[6]
    
    #Fill the PARAMS class.
    Params = PARAMS(
        Azimuth,
        Elevation,
        deltaAz,
        deltaEl,
        panJogSpeed,
        tiltJogSpeed,
        resolverUnits,
        overrideSoftLimits,
        stop,
        reset,
        altitude,
        latitude,
        longitude,
        location,
        command)

    return Params
#End of the function getParams.py
        
