import re
from itertools import cycle


sentenceEnders = re.compile(r"""
    # Split sentences on whitespace between them.
    (?:               # Group for two positive lookbehinds.
      (?<=[.!?])      # Either an end of sentence punct,
    | (?<=[.!?]['"])  # or end of sentence punct and quote.
    )                 # End group of two positive lookbehinds.
    (?<!  Mr\.   )    # Don't end sentence on "Mr."
    (?<!  Mrs\.  )    # Don't end sentence on "Mrs."
    (?<!  Jr\.   )    # Don't end sentence on "Jr."
    (?<!  Dr\.   )    # Don't end sentence on "Dr."
    (?<!  Prof\. )    # Don't end sentence on "Prof."
    (?<!  M\.    )
    (?<!  Sr\.   )    # Don't end sentence on "Sr."
    \s+               # Split on whitespace between sentences.
    """, 
    re.IGNORECASE | re.VERBOSE)

with open("testLesEn.txt", "r+") as fileEng:
    linesEng = fileEng.read()
with open("testLesFr.txt", "r+") as fileFre:
    linesFre = fileFre.read()
        
linesEng = linesEng.replace("\n", " ")
linesFre = linesFre.replace("\n", " ")



sentenceListEng = sentenceEnders.split(linesEng)
sentenceListFre = sentenceEnders.split(linesFre)        

sentenceListFre = cycle(sentenceListFre)

count = 0


    #for sentenceFre in sentenceListFre:
    #    if "?" not in sentenceFre:
    #        fileFreResult.write(sentenceFre+"\n")

with open("test.fr", "w") as fileFreResult:
    with open("test.en", "w") as fileEngResult:
            for sentenceEng in sentenceListEng:
                sentenceFre = sentenceListFre.next()
                #print count
                print sentenceEng
               # print "english:"
                print sentenceEng.count(';')
                print sentenceFre
                print sentenceFre.count(';')
                #if sentenceEng.count(';') > sentenceFre.count(';'):

                count = count+1
                #if count == 200:
                    #break
                #if "?" not in sentenceEng:
                fileEngResult.write(sentenceEng+"\n")
                #if "?" not in sentenceFre:
                fileFreResult.write(sentenceFre+"\n")       