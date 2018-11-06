class part3(object):
	command="../sim-watch/sim-outorder"
	
	compilers={"gcc":"../sim-watch/benchmarks/cc1.alpha -O lstmt.i",
    "anagram":"../sim-watch/benchmarks/anagram.alpha words < ../sim-watch/benchmarks/anagram.in",
    "compress95":"../sim-watch/benchmarks/compress95.alpha < ../sim-watch/benchmarks/compress95.in",
    "go":"../sim-watch/benchmarks/go.alpha 2 8 2stone9.in"}
	commands=[]
	cacheSize={32:32, 64:64, 128:128, 256:256}
	cacheReplacementPolicy = {"fifo":"f", "lifo":"l", "random":"r"}
	cacheAssociativity={1:"1", 4:"4", 8:"8", 64:"64"}
	cache="-cache:dl2 ul2:1024:"
	sim=" -redir:sim ../results/p3/"
	"""
	<name>:<nsets>:<bsize>:<assoc>:<repl>
	"""
	def __init__(self):
		x=1
		
	def getCommands(self):
		return self.commands
		
	def execute(self):
		temp=""
		for cindex, compiler in self.compilers.iteritems():
			for sindex, size in self.cacheSize.iteritems():
				for aindex, associativity in self.cacheAssociativity.iteritems():
					for rpindex, replacement in self.cacheReplacementPolicy.iteritems():
						"""
						Generate our files
						"""
						file=self.sim+str(cindex)+"-"+str(sindex)+"-"
						file+=str(aindex)+"-"+str(rpindex)
						"""
						Generate our commands
						"""
						temp=self.command+" "+self.cache
						temp+=str(size)+":"+str(aindex)+":"+str(replacement)+" "
						temp+=file+" "+compiler
						self.commands.append(temp)
		print 'We finished compiling the commands successfully in part3!'