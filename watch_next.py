# Import spacy module and specify which model to use
import spacy
nlp = spacy.load('en_core_web_md')

# Description of the Planet Hulk moview
sentence_to_compare = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,
the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator'''

# Open movies file with the descriptions of other movies
with open("movies.txt", "r") as f:
    sentences = f.read().splitlines()

# Function to print which movie to watch next based on highest similarity score
def watch_next(sentence_to_compare):
    model_sentence = nlp(sentence_to_compare)
    for sentence in sentences:
        similarity = nlp(sentence).similarity(model_sentence)
        print(sentence + " - ", similarity)
    highest_similarity = max(sentences, key=lambda sentence: nlp(sentence).similarity(model_sentence))
    print(f"\nThe movie to watch next is {highest_similarity}")

watch_next(sentence_to_compare)
