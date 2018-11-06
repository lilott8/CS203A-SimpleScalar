import matplotlib as mpl
#Suppress error, as per: http://stackoverflow.com/questions/13336823/matplotlib-python-error
mpl.use('Agg')
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt

class grapher(object):
	
	x=1
	
	def __init__(self):
		self.x=1