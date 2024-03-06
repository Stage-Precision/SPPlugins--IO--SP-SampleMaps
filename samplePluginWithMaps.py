import sp
import os


#Sample SP IO Structure

class SampleModuleMaps(sp.BaseModule):

	#plugin info used 
	pluginInfo = {
		"name" : "Sample Plugin Maps",
		"category" : "Plugins",
		"description" : "show how to create SP Plugin IO \r ",
		"author" : "SP",
		"version" : (1, 0),
		"spVersion" : (1, 0, 142),
		"helpPath" : os.path.join(os.path.dirname(os.path.abspath(__file__)),"help.md")
	}

	def __init__(self):
		sp.BaseModule.__init__(self)
		
	# run function on our main tick
	def onTick(self):
		#print("onTick")
		pass

	# run function that provide pos data into the map pipeline
	def mapIn(self, type):
		print("MapIn " + type)
		ob = {"pos" : [0, math.sin(time.time()), 0],
			"time" : time.time()}
		self.setConnectionStatus((time.time() % 2.0) > 1.0)
		return ob

	# run function that provide pos data into the map pipeline Output
	def mapOut(self, data, cc, type):
		#print("MapOut " + cc.name + " " + str(data))
		pass


if __name__ == "__main__":
	sp.registerPlugin(SampleModuleMaps)
