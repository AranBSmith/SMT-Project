import re





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
    (?<!  Sr\.   )    # Don't end sentence on "Sr."
    \s+               # Split on whitespace between sentences.
    """, 
    re.IGNORECASE | re.VERBOSE)


linesAll = ""
with open("hunchback_english_sample.txt", "r+") as f:
	
    lines = f.readlines()
    for line in lines:
    	linesAll = linesAll+line
        
linesAll = linesAll.replace("\n", " ")
sentenceList = sentenceEnders.split(linesAll)        

with open("hunchback_english_result.txt", "w") as f1:
	for l in sentenceList:
		f1.write(l+"\n")
print sentenceList