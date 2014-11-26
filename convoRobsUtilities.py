from os import system
import speech_recognition as sr
import time

class colors:
	BLACK='\x1b[30m'
	RED = '\x1b[31m'
	GREEN = '\x1b[32m'
	YELLOW = '\x1b[33m'
	BLUE = '\x1b[34m'
	MAGENTA = '\x1b[35m'
	CYAN = '\x1b[36m'
	WHITE = '\x1b[37m'

	BLACKBG='\x1b[40m'
	REDBG = '\x1b[41m'
	GREENBG = '\x1b[42m'
	YELLOWBG = '\x1b[43m'
	BLUEBG = '\x1b[44m'
	MAGENTABG = '\x1b[45m'
	CYANBG = '\x1b[46m'
	WHITEBG = '\x1b[47m'		
	
	NOCOL = '\x1b[0m'

def returnTime():
	fatherTime = ""
	fatherTime = time.strftime("%b:%d:%H:%M:%S")
	fatherTime = fatherTime.split(":")
	return fatherTime

def buildDictionary(name,databasetype=None):
	try:
		if databasetype==None:
			fileRef=open("People/%sStuff/%sResponses.csv"%(name,name))
		else:
			fileRef=open("People/%sStuff/%s%sResponses.csv"%(name,name,databasetype))
		fileLines = fileRef.readlines()
		fileRef.close()
	except:
		return {}

	stdResponses = {}
	try:
		for lineIndex in range(len(fileLines)):
			fileLines[lineIndex]=fileLines[lineIndex].split("[")
			fileLines[lineIndex]=[fileLines[lineIndex][0],fileLines[lineIndex][1].split(",")]
			lenLast = len(fileLines[lineIndex][1][len(fileLines[lineIndex][1])-1])
			fileLines[lineIndex][1][len(fileLines[lineIndex][1])-1]=fileLines[lineIndex][1][len(fileLines[lineIndex][1])-1][:lenLast-2]
			
			fixed=[]
			for responseElement in fileLines[lineIndex][1]:
				for strIndex in range(len(responseElement)-1,-1,-1):
					if (responseElement[strIndex]=="\""):
						responseElement=responseElement[:strIndex]+responseElement[strIndex+1:]
				fixed.append(responseElement)
			fileLines[lineIndex][1]=fixed

			for strIndex in range(len(fileLines[lineIndex][0])-1,-1,-1):
				if (fileLines[lineIndex][0][strIndex]=="\"" or fileLines[lineIndex][0][strIndex]==","):
					fileLines[lineIndex][0]=fileLines[lineIndex][0][:strIndex]+fileLines[lineIndex][0][strIndex+1:]

			stdResponses.update({fileLines[lineIndex][0]:fileLines[lineIndex][1]})
	except:
		return {}
		
	return stdResponses




