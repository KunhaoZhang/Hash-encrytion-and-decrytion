import base64
import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--read', required=True)
parser.add_argument('--write', required=True)
parser.add_argument('-e', action='store_true')
parser.add_argument('-d', action='store_true')
args = parser.parse_args()

if os.path.isfile(args.write):
    print("The file to write already exists, use another file path please.")
    quit()
elif os.path.isfile(args.read) == False:
    print("The file to read does not exist or is a directory, use another file path please")
    quit()



if args.e and args.d:
    print("You cannot have both encrypting and decrypting option at the same time")
    quit()
elif args.e:
    data = open(args.read, "r").read()
    dataAfter = base64.b64encode(bytes(data, 'utf-8'))
    fileToWrite = open(args.write, "wb")
elif args.d:
    data = open(args.read, "rb").read()
    dataAfter = base64.b64decode(data)
    fileToWrite = open(args.write, "wb")
else:
    data = open(args.read, "r").read()
    dataAfter = base64.b64encode(data)
    fileToWrite = open(args.write, "wb")


    

fileToWrite.write(dataAfter)
fileToWrite.close()