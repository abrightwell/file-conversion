from optparse import OptionParser
import csv

if __name__=="__main__":
	parser = OptionParser()
	parser.add_option("-i", "--input", action="store", type="string", dest="input")
	parser.add_option("-o", "--output", action="store", type="string", dest="output", default="output.csv")

	(options, args) = parser.parse_args()

	with open(options.input, 'rb') as tab_delim_file:
		tab_file = csv.reader(tab_delim_file, delimiter="\t")
		file_contents = [line for line in tab_file]

	# write comma-delimited file (comma is the default delimiter)
	with open(options.output,'wb') as comma_delim_file:
		csv_file = csv.writer(comma_delim_file, quotechar='', quoting=csv.QUOTE_NONE)
		csv_file.writerows(file_contents)
