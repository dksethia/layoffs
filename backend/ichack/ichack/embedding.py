import yake
from gensim.utils import tokenize
	
kw_extractor = yake.KeywordExtractor(lan="en", n=1, dedupLim=0.9, dedupFunc='seqm', windowsSize=1, top=10, features=None)
kw_extractor_n2 = yake.KeywordExtractor(lan="en", n=2, dedupLim=0.9, dedupFunc='seqm', windowsSize=1, top=10, features=None)

def create_embedding(text):

	text = text.lower()
	words = list(tokenize(text, lowercase=True, deacc=True, errors='ignore'))
	text = " ".join(words)
	keywords_n1 = list(map((lambda x: x[0]), kw_extractor.extract_keywords(text)))
	keywords_n2 = list(map((lambda x: x[0]), kw_extractor_n2.extract_keywords(text)))
	
	return ";".join(keywords_n1)+'@'+";".join(keywords_n2)