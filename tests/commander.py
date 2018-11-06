import subprocess as sp
import sys

class commander(object):
	counters={"run":0, "formed":0}
	runnable=0
	command=[]
	result=None
	debug=False
	
	def __init__(self, r=False, d=False):
		self.initCommand()
		self.runnable=r
		self.debug=d
		
	def executeStatus(self):
		if self.runnable:
			return "We are running commands."
		else:
			return "We are not running commands."
			
	#def appendCommand(self, a):
	#	self.command.append(a)
		
	def initCommand(self):
		self.command=[]
		
	def issueCommand(self, c):
		self.command = c
		if(isinstance(c, basestring)):
			command = c.split()
		else:
			command = c
		if(self.debug):
			print str(self.command)
			
		if(sys.version_info < (2,7)):
			self.run26Command(command)
		else:
			self.run27Command(command)

	#Aliases of issueCommand	
	def execute(self, c):
		self.issueCommand(c)
	#Aliases of issueCommand
	def runCommand(self, command):
		self.issueCommand(command)
		
	def getResult(self):
		return self.result
		
	def getCommand(self):
		return self.command
		
	def run26Command(self, command):
		try:
			if(self.runnable):
				#This is the fix for python < 2.7
				self.result=sp.Popen(command,stdout=sp.PIPE)
				self.counters["run"] += 1
				print "Command executed successfully!"
			else:
				if(self.debug):
					print "Command not run, we are not runnable"
		except RuntimeError:
			print "Something went wrong executing: "+str(command)		
	
	def run27Command(self, command):
		try:
			if(self.runnable):
				#This is the fix for python < 2.7
				self.result=sp.check_call(command,stdout=sp.PIPE)
				self.counters["run"] += 1
				print "Command executed successfully!"
			else:
				if(self.debug):
					print "Command not run, we are not runnable"
		except RuntimeError:
			print "Something went wrong executing: "+str(command)