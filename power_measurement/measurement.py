#! /usr/bin/python3
import argparse
import os
import sys
import time
import subprocess
def parseOpt():
	parser = argparse.ArgumentParser(description="Power measurement")
	#parser.add_argument("-raw",action="store_true")
	parser.add_argument("-output",required=True,type=str)
	parser.add_argument("-count",required=True,type=str)
	parser.add_argument("-measure",required=True,type=str)
	parser.add_argument("-samples",required=True,type=int)
	parser.add_argument("-workload",required=True,type=str)
	parser.add_argument("-startWorkload",required=True,type=int)
	parser.add_argument("-input",required=False,type=str)

	return parser.parse_args()


if __name__ =="__main__":
	parser = parseOpt()
	if parser.startWorkload > parser.samples:
		print("Number of samples cannot be lower than the start time of workload")
		exit()
	
	startedWorkload = False
	with open(parser.output,"w") as output,open(os.devnull,"w") as devnull:
		proc = subprocess.Popen(parser.measure.split(" "),stdout=output,shell=True)
		prev_samples=0
		print("")
		while True:
			stream = os.popen(f"{parser.count}")
			samples =int(stream.read())

			if samples >= parser.startWorkload and not startedWorkload:
				if(parser.input):
					input = open(parser.input,"r")
				else:
					input = subprocess.PIPE
				workload = subprocess.Popen(parser.workload.split(" "),stdout=devnull,stdin=input,shell=True)
				startedWorkload =True

			if prev_samples != samples:
				sys.stdout.write(f"\r{samples}/{parser.samples} measurements...")
				sys.stdout.flush()
				prev_samples = samples
				
			if samples  >= parser.samples:
				proc.kill()
				workload.kill()
				output.close()
				print(f"\nMeasurement finished. Results saved at {parser.output}")
				exit(0)
			

			time.sleep(0.5)