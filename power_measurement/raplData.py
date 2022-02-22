#! /bin/python3
import pandas as pd
import argparse

def parseOpt():
	parser = argparse.ArgumentParser(description="Plot Graph")
	parser.add_argument("csv",type=str,
		help="csv file to read")
	#parser.add_argument("-raw",action="store_true")
	parser.add_argument("-output",required=False,type=str)

	return parser.parse_args()


if __name__ =="__main__":
	watts = [] 
	parser = parseOpt()

	file = parser.csv
	df = pd.read_csv(file,sep=",")
	packages = [column for column in df.columns if column.startswith("Package")]

	total_watts = sum([df[package].values for package in packages])
	output = pd.DataFrame(total_watts,columns=["W"])
	if not parser.output:
		output.to_csv(f"csv/{parser.csv}")
	else:
		output.to_csv(f"csv/{parser.output}")
	print(output)

		
