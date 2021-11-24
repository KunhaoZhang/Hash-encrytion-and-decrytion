# Hash-encrytion-and-decrytion
For the python module project

Module os, argparse, and base64 are imported.

There are two mandatory arguments for the script:
  [--write] This is the file to read the message for encoding or decoding.
  
  [--read] This is the file to save the result.
    This file cannot exist on the system already, if so, the program will alert you and exit.
    
  Both arguments need to be present, or the program will alert you and exit.
    
There are two optional arguments:

  [-e] This flag indicates that the action should be encoding.
  [-d] This flag indicates that the action should be decoding.
  
  The two flags cannot exist at the same time, if so, the program will alert you and exit.
  If none of these are specified, -e will be the default action.
