#! /usr/bin/python3
#Utility to change the class feature column to first column on the dataset.

import pandas as pd
import argparse


def parse_args():
	parser = argparse.ArgumentParser(description="csv switch feature's position")
	parser.add_argument("-csv",type=str,help="csv file to discretize",required=True)
	parser.add_argument("-feature",default="class",type=str,help="name of the feature to switch (default \"class\"")
	parser.add_argument("-position",default=0,type=int,help="target position of the feature (starting from 0)")	
	return parser.parse_args()

if __name__ == "__main__":

	parser = parse_args()
	df = pd.read_csv(parser.csv,sep=",")

	target_column = parser.feature
	columns = df.columns.tolist()

	for index,column in enumerate(columns):
		if column == target_column:
			target_index= index

	aux = df.iloc[:,parser.position]
	aux_column = columns[parser.position]
	to_switch = df.iloc[:,target_index]
	to_switch_column = columns[target_index]

	df.iloc[:,parser.position] = to_switch
	df.iloc[:,target_index] = aux

	columns[parser.position] = to_switch_column
	columns[target_index] =aux_column

	new_df = pd.DataFrame(data=df.values,columns=columns)
	new_df.to_csv(f"{parser.csv}.switched",index=False)

	print(f"feature {target_column} switched to position 0 and file saved to {parser.csv}.switched")
