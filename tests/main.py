import part1 as p1
import part2 as p2
import part3 as p3
import part4 as p4
import commander as c

"""
	Array for our commands that are generated from our executed parts
"""
commands = {'p1':[], 'p2':[], 'p3':[]}
"""
	Whether or not we can issue the commands. This is a per part basis
"""
issuable = {'p1':True, 'p2':False, 'p3':False}

"""
	Our command prompt access to issue commands
	Runnable is set to False; this is a global setting.
	Debugging is set to False; this will dump the command issued to the screen
"""
commander = c.commander(False, False)

print commander.executeStatus()
print "==========================================="

def runCommands(com):
	for command in com:
		commander.runCommand(command)
"""
	This is our part1 parser with the information that is useful to us
	parsers["p1"] = p.parser(["sim_cpi","sim_ipc","sim_cycle","sim_num_insn","sim_num_refs","sim_num_loads",
	"sim_num_stores","mem.page_count","sim_total_loads","sim_total_stores","sim_total_branches","sim_elapsed_time"])
"""
print "==========================================="
#=============================================================#
#Part 1 stuff
#=============================================================#
"""
	1)Instantiate a new part1 object
"""
part1 = p1.part1()
"""
	2)Run our simulation given the above parameters
"""
part1.execute()
"""
	3)get the commands we need from our p1 simulation
"""
commands['p1'] = part1.getCommands()
"""
	4)run our commands
"""
if issuable['p1']:
	print "running commands from p1."
	runCommands(commands['p1'])
else:
	print "Not able to run commands from p1."
	
print "==========================================="

#=============================================================#
#Part 2 stuff
#=============================================================#
"""
	1)Instantiate a new part2 object
"""
part2 = p2.part2()
"""
	2)Run our simulation given the above parameters
"""
part2.execute()
"""
	3)get the commands we need from our p1 simulation
"""
commands['p2'] = part2.getCommands()
"""
	4)run our commands
"""
if issuable['p2']:
	print "running commands from p2."
	runCommands(commands['p2'])
else:
	print "Not able to run commands from p2."
print "==========================================="

#=============================================================#
#Part 3 stuff
#=============================================================#
"""
	1)Instantiate a new part3 object
"""
part3 = p3.part3()
"""
	2)Run our simulation given the above parameters
"""
part3.execute()
"""
	3)get the commands we need from our p1 simulation
"""
commands['p3'] = part3.getCommands()
"""
	4)run our commands
"""
if issuable['p3']:
	print "running commands from p3."
	runCommands(commands['p3'])
else:
	print "Not able to run commands from p3."
print "==========================================="