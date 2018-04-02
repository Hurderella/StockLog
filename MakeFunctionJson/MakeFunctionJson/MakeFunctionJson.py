
import json

if __name__ == "__main__":
	print("Hello World")

	prevLine = ""
	eleComplete = False
	eleDic = {}
	code = ""
	with open("typingHard.txt", "r") as f :
		infoDic = {}
		argCount = 0
		cmdCount = 0
		ckCmdCount = 0
		for line in f:
			line = line.strip();
			#print("{} > {}".format(line.split(" : "), len(line.split(":"))))
			cmdName = line.split(" : ");
			if len(cmdName) == 2:
				if len(infoDic) is not 0:
					#eleDic = {}
					eleDic[code] = infoDic
					#print("ckCmdCount : {0} >> {1}".format(ckCmdCount, eleDic))
					#print("-----------------------------")
					ckCmdCount += 1
					argCount = 0
					infoDic = {}

				code = cmdName[0].strip("[ ");
				nameStr = cmdName[1].strip(" ]");
				print("#{0} code {1}, name {2}".format(cmdCount, code, nameStr));
				cmdCount += 1
				
				infoDic["name"] = nameStr
				
			if "SetInputValue" in line:
				typeStr = "int"
				description = line.split("\"")[1]
				#print("description : {}".format(line.split("\"")[1]))
				if "YYYYMMDD" in prevLine :
					typeStr = "date"
					
				
				argName = "arg{}".format(argCount)
				infoDic[argName] = {"type" : typeStr, "description" : description}
				#print(infoDic)
				argCount += 1

			prevLine = line
		#eleDic = {}
		eleDic[code] = infoDic
		#print("ckCmdCount : {0} >> {1}".format(ckCmdCount, eleDic))
		#print("-----------------------------")
	
	#print(eleDic)
	print(json.dumps(eleDic, indent = '\t'))
	with open("cmd.json", 'w', encoding = "utf-8") as wf:
		#json.dumps(eleDic, wf, indent = '\t', ensure_ascii = False)
		wf.write(json.dumps(eleDic, ensure_ascii = False))