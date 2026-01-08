in mini_rag:
1. first i tried chunking with differnet chunk sizes. its not determinsitic and that too in case of financial terms, the response is not a safe response. 12.5 % adn 12.7 % are coming as profits.
2. then tried sentence chunking. But then sentences are split at every period becuase decimals are present in the context.
3. Now i am trying to chunk using nltk.