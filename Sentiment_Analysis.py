# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 10:37:37 2018

@author: leblanckh
"""

from textblob import TextBlob
import argparse
import codecs
#import xml.etree.cElementTree as etree

#def processMedlineFile(pubmedFile,fTitles,fHasTitlesAndAbstracts,fPubYear,fJournals):
#	for event, elem in etree.iterparse(pubmedFile, events=('start', 'end', 'start-ns', 'end-ns')):
#		if (event=='end' and elem.tag=='MedlineCitation'):
#			# Find the elements for the PubMed ID, and publication date information
#			pmid = elem.findall('./PMID')
#			journalTitleElements = elem.findall('./Article/Journal/Title')
#			journalTitleISOElements = elem.findall('./Article/Journal/ISOAbbreviation')
#			yearFields = elem.findall('./Article/Journal/JournalIssue/PubDate/Year')
#			medlineDateFields = elem.findall('./Article/Journal/JournalIssue/PubDate/MedlineDate')
#
#			# Try to extract the pmidID
#			pmidText = ''
#			if len(pmid) > 0:
#				pmidText = " ".join( [a.text.strip() for a in pmid if a.text ] )
#                # Extract the title of paper
#			titleElements = elem.findall('./Article/ArticleTitle')
#			
#			# Extract the abstract from the paper
#			abstractElements = elem.findall('./Article/Abstract/AbstractText')
#
#			title = " ".join(extractTextFromElemList(titleElements))
#			journalTitle = " ".join(extractTextFromElemList(journalTitleElements))
#			journalISOTitle = " ".join(extractTextFromElemList(journalTitleISOElements))
#
#			hasTitle = len(titleElements) > 0
#			hasAbstract = len(abstractElements) > 0
#
#			#print hasTitle, hasAbstract, pubYear, journalTitle, journalISOTitle, title
#
#			title01 = 1 if hasTitle else 0
#			abstract01 = 1 if hasAbstract else 0
#
#			fTitles.write(title + "\n")
#			fHasTitlesAndAbstracts.write("%d\t%d\n" % (title01,abstract01))
#			fJournals.write("%s\t%s\n" % (journalTitle,journalISOTitle))

if __name__ == '__main__':
	parser = argparse.ArgumentParser("Pointless tool to count the number of instances the term 'text mining' appears in a text file")
	parser.add_argument('--inFile',type=str,required=True,help='Text file to process')
	parser.add_argument('--outFile',type=str,required=True,help='File to store the count')
	args = parser.parse_args()

	with codecs.open(args.inFile,'r','utf-8') as f:
            abstract = TextBlob(f)
          

	with open(args.outFile,'a') as f:
            f.write('%d\n' % abstract.sentiment)
#testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
#testimonial.sentiment
