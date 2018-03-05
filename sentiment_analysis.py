from textblob import TextBlob
import argparse
import codecs

if __name__ == '__main__':
	parser = argparse.ArgumentParser("Pointless tool to count the number of instances the term 'text mining' appears in a text file")
	parser.add_argument('--inFile',type=str,required=True,help='Text file to process')
	parser.add_argument('--outFile',type=str,required=True,help='File to store the count')
	args = parser.parse_args()

	with codecs.open(args.inFile,'r','utf-8') as f:
            abstract = TextBlob(f.read())
          

	with open(args.outFile,'a+') as f:
            f.write('%d\n' % abstract.sentiment)
#testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
#testimonial.sentiment
