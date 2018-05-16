import os, sys

def main():
	sourceFile = './people.txt'
	inputFilePath = '~/crawlingData_2015-2017_v2.0/dir_new/'
	outputFilePath = '.'

	f = open(sourceFile, 'r')
	lines = f.readlines()
	for line in lines:
		line=line[:-1]
		line = line.replace(" ", "\ ")
		line = line.replace("(", "\(")
		line = line.replace(")", "\)")
		inputDir = inputFilePath+line
		#print(inputDir)
		cmd = 'cp -r {0} {1}'.format(inputDir, outputFilePath)
		os.popen(cmd)

main()
