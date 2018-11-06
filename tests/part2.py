class part2(object):
	command="../sim-watch/sim-outorder"
	
	compilers={"gcc":"../sim-watch/benchmarks/cc1.alpha -O lstmt.i",
    "anagram":"../sim-watch/benchmarks/anagram.alpha words < ../sim-watch/benchmarks/anagram.in",
    "compress95":"../sim-watch/benchmarks/compress95.alpha < ../sim-watch/benchmarks/compress95.in",
    "go":"../sim-watch/benchmarks/go.alpha 2 8 2stone9.in"}
	commands=[]
	branches={'not-taken':"-bpred nottaken", 
    "taken":"-bpred taken", 
    "bi-modal":"-bpred bimod", 
    "2-level":"-bpred 2lev"} 
	sim=" -redir:sim ../results/p2/"

	def __init__(self):
		x=1
	
	def getCommands(self):
		return self.commands
	
	def execute(self):
		for cindex, compiler in self.compilers.iteritems():
			for bindex, branch in self.branches.iteritems():
				self.commands.append(self.command+" "+branch+" "+self.sim+cindex+"-"+bindex+" "+compiler)
		print 'We finished compiling the commands successfully in part2!'