import json
from collections import OrderedDict

if __name__ == "__main__" :
	print("Hello World")
	data = open("cmdlist.json").read()
	d = json.loads(data)
	#print(d["opt10001"])
	od = OrderedDict(sorted(d.items()));

	subCount = 0;
	for k, v in od.items() :
		print("#{0} {1} {2}".format(subCount, k, v))
		subCount += 1
		print("------------------")
	