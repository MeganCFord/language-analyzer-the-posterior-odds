presentation.md

where we are: written the names of all the tests we'll be writing. we know the structure of our app, we know what we want as our input and output, and we know all the math we'll be doing in between. We're using both construction and inheritance.


input a string as the single perameter into the instantiation of our analyzer app, which inherits from a tokenizer class which in turn inherits from a domain and emotion class. the emotion class has a subclass of sentiment as well. the domain and emotion/sentiment classes then construct a behavior prediction class based on their calculations. 

we're looping through hand-built lexicon lists to assign a point to a counter variable, based on each word's appearance in the corresponding lexicon. our sentiment is going to be a positive/negative number. 

nltk
  tokenizing
  beyes equation which would allow us to greatly improve our statistics by assigning a 'likelihood of being x emotion' to each word and then multiply those relative likelihoods with the absolute ratio of the occurance of the word vs the total sentence. waterfall diagram. 
