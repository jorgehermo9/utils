#! /bin/python3
import pandas as pd
import argparse

def parseOpt():
	parser = argparse.ArgumentParser(description="Plot Graph")
	parser.add_argument("xls",type=str,
		help="xls file to read")
	#parser.add_argument("-raw",action="store_true")
	parser.add_argument("-output",required=False,type=str)

	return parser.parse_args()

def get_xls(xls):
	VOLTAGE_COLUMN = "Unnamed: 1"
	CURRENT_COLUMN = "Unnamed: 2"
	sheet = pd.read_excel(xls)

	data = pd.DataFrame(sheet,columns=[VOLTAGE_COLUMN,CURRENT_COLUMN]).iloc[1:]
	#Slicing to exclude first row
	watts = data[VOLTAGE_COLUMN].values * data[CURRENT_COLUMN].values
	return watts

if __name__ =="__main__":
	watts = [] 
	parser = parseOpt()

	file = parser.xls
	watts = get_xls(file)
	output = pd.DataFrame(watts,columns=["W"])
	file_path = "".join(parser.xls.rsplit(".",1)[0])+".csv"
	if not parser.output:
		output.to_csv(f"csv/{file_path}")
	else:
		output.to_csv(f"csv/{parser.output}")
	print(output)

		
