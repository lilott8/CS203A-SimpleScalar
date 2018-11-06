class part1(object):
    #Class Variables
    commit={1:1,2:2,4:4,8:8}
    fetch={1:1,2:2,4:4,8:8}
    decode={1:1,2:2,4:4,8:8}
    issue={1:1,2:2,4:4,8:8}
    
    count=0
    command="../sim-watch/sim-outorder"
    args=""
    sim=" -redir:sim ../results/p1/"
    prog=" -redir:prog ../results/p1/prog"
    endCommand=" /home/ott/cs203a/sim-watch/benchmarks/cc1.alpha -O lstmt.i "
    compilers={"gcc":"../sim-watch/benchmarks/cc1.alpha -O lstmt.i",
    "anagram":"../sim-watch/benchmarks/anagram.alpha words < ../sim-watch/benchmarks/anagram.in",
    "compress95":"../sim-watch/benchmarks/compress95.alpha < ../sim-watch/benchmarks/compress95.in",
    "go":"../sim-watch/benchmarks/go.alpha 2 8 2stone9.in"} 
    #List 1 is simFileName, list 2 is progFileName
    fileLists=[[], []]
    commands=[]
        
    def __init__(self):
        #init function
        self.initArgs()
    
    def appendArgs(self, c):
        self.args=self.args+''+c
    
    def initArgs(self):
        self.args=""
    
    def getArgs(self):
        return self.args
        
    def getProg(self, args):
        return self.prog+'-'+args
        
    def getSim(self, args):             
        return self.sim+args
        
    def getFiles(self):
        return self.fileLists
        
    def getCommands(self):
        return self.commands
            
    def execute(self):
        for index, command in self.compilers.iteritems():
            for findex, fetch in self.fetch.iteritems():
                for cindex, commit in self.commit.iteritems():
                    for dindex, decode in self.decode.iteritems():
                        for iindex, issue in self.issue.iteritems():
                            self.appendArgs(" -fetch:ifqsize "+str(findex))
                            self.appendArgs(" -commit:width "+str(cindex))
                            self.appendArgs(" -decode:width "+str(dindex))
                            self.appendArgs(" -issue:width "+str(iindex))
                            #Generic numbers to save so we only have to compute once
                            fileName=index+"-"+str(fetch)+'-'+str(commit)+'-'+str(decode)+'-'+str(issue)
                            #Append those to our lists
                            """
                            self.fileLists[0].append(index+"-"+fileName)
                            self.fileLists[1].append("prog-"+fileName)
                            self.getProg(fileName)
                            """
                            #self.commands.append(self.command+self.getArgs()+self.getSim(fileName)+self.getProg(fileName)+command)
                            self.commands.append(self.command+self.getArgs()+self.getSim(fileName)+" "+command)
                            #issue/save our command
                            self.count+=1
                            self.initArgs()
  	print 'We finished compiling the commands successfully in part1!'