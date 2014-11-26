from os import system
import convoRobsUtilities
from random import randrange
from convoRobsUtilities import colors

class Person:

	def __init__(self,name_param="Adam",voice_param="Tom",type_param="Extrovert",color_param="\x1b[0m"):
		self.name = name_param #Any name
		self.voice = voice_param #What voice to use
		self.type = type_param #Introvert,Extrovert
		self.responses=0
		self.active = True
		self.color=color_param

		self.greetDatabase=convoRobsUtilities.buildDictionary(self.name)
		self.conversationDatabase=convoRobsUtilities.buildDictionary(self.name,"Conversation")
		self.generalDatabase=convoRobsUtilities.buildDictionary("General","Conversation")

		for x in range(len(list(self.generalDatabase.values()))):
			for y in range(len(list(self.generalDatabase.values())[x])):
				if list(self.generalDatabase.values())[x][y] not in list(self.generalDatabase.keys()):
					print("%s\"%s\" has not been assigned to a response in the General Response Database...%s"%(colors.RED,list(self.generalDatabase.values())[x][y],colors.NOCOL))

		try:
			fileRef=open("People/%sStuff/%sResponses.csv"%(self.name,self.name))
			fileRef.close()
		except (FileNotFoundError) as e:
			print("%s is missing files"%(self.name))

	def randResponse(self,fileLines):
		try:
			respondingTo=fileLines[len(fileLines)-1][:len(fileLines[len(fileLines)-1])-1]
			if self.responses==1:
				randNum = randrange(0,len(self.greetDatabase[respondingTo])) 
				return self.greetDatabase[respondingTo][randNum]
			else:
				try:
					randNum = randrange(0,len(self.conversationDatabase[respondingTo])) 
					return self.conversationDatabase[respondingTo][randNum]
				except:
					print("\x1b[35m",self.name," is referencing the general database... \x1b[0m")
					randNum = randrange(0,len(self.generalDatabase[respondingTo])) 
					return self.generalDatabase[respondingTo][randNum]
		except (IndexError) as e:
			randNum=randrange(0,len(self.greetDatabase["Hello"]))
			return self.greetDatabase["Hello"][randNum]

	def respond(self,converseFile="conversation.txt"):
		self.responses+=1
		try:
			fileRef = open(converseFile)
			listLines = fileRef.readlines()
			fileRef.close()
		except (FileNotFoundError) as e:
			print("Conversation file not found...")
			return None

		return self.randResponse(listLines)

	def speak(self,response):
		try:
			system("say -v \"%s\" %s"%(self.voice,response))
		except:
			return


	def main(self,filename="conversation.txt"):

		active=True
		lastSaid=""

		if (self.type=="Introvert"):
			listening=True
		elif (self.type=="Extrovert"):
			listening=False

		while active:
			while listening:
				fileRef=open(filename)
				listLines=fileRef.readlines()
				fileRef.close()
				try:
					fileSays=listLines[len(listLines)-1][:len(listLines[len(listLines)-1])-1]
				except:
					fileSays=None
				if lastSaid != fileSays and lastSaid!=None:
					listening=False

			while not listening:
				response = self.respond(filename)
				lastSaid=response
				fileRef=open(filename,"a")
				fileRef.write(response+"\n")
				fileRef.close()
				self.speak(response)
				listening=True

	def carryOn(self,filename="conversation.txt"):
		response = self.respond(filename)
		print("%s%s: %s%s"%(self.color,self.name,response,colors.NOCOL))
		if response=="Goodbye" or response=="Bye" or "bye" in response.lower():
			self.active=False
		fileRef=open(filename,"a")
		if response!=None:
			fileRef.write(response+"\n")
		else:
			fileRef.write(+"\n")

		fileRef.close()
		self.speak(response)

