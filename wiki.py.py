wiki.py

import wikipedia

# choose a topic
topic = "Python (programming language)"

# search and get a short summary
result = wikipedia.summary(topic, sentences=2)

print(result)