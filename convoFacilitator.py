import personalityClasses
from os import system
from convoRobsUtilities import returnTime

def main(v1="Tom",v2="Samantha",filename="conversation.txt",order=0,p1_color="\x1b[36m",p2_color="\x1b[35m"):
	fileRef=open(filename,"a")
	fileRef.close()
	p1=personalityClasses.Person("Adam",v1,color_param=p1_color)
	p2=personalityClasses.Person("Eve",v2,color_param=p2_color)

	try:
		while p1.active and p2.active:
			if order==0:
				p1.carryOn()
				p2.carryOn()
			if order==1:
				p2.carryOn()
				p1.carryOn()
	except (KeyError) as e:
		print("Some one did not know how to respond...")


	fileRef=open(filename)
	listLines=fileRef.readlines()
	fileRef.close()

	timeList=returnTime()

	fileRef=open("archive/%s%s%s%s%s%s"%(timeList[0],timeList[1],timeList[2],timeList[3],timeList[4],filename),"a")
	fileRef.writelines(listLines)
	fileRef.close()
	system("rm %s"%(filename))