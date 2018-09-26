#Samantha Shoecraft
#7/26/17
import nltk
myfile = open('Klingon_Train.txt', 'r')
line = myfile.readline()
sentances = []

while line:
	if (len(line) > 1):
		sentances.append(('<START>/<START> ' + line.strip('\n') + ' <END>/<END>').split())
	line = myfile.readline()

tags = [nltk.tag.str2tuple(word)[1] for sent in sentances for word in sent]
bigrams = list(nltk.bigrams(tags))

tag_counts = {}
transition_counts = {}

for tag in tags:
	if tag in tag_counts:
		tag_counts[tag] = tag_counts.get(tag) + 1
	else:
		tag_counts[tag] = 1
		
for tupl in bigrams:
	if tupl in transition_counts:
		transition_counts[tupl] = transition_counts.get(tupl) + 1
	else:
		transition_counts[tupl] = 1;

for t1 in tag_counts.keys():
	if t1 != '<END>':
		for t2 in tag_counts.keys():
			if t2 != '<START>':
				if (t1,t2) in transition_counts:
					transition_counts[(t1,t2)] = transition_counts.get((t1,t2)) / tag_counts.get(t1) + 0.1
				else:
					transition_counts[(t1,t2)] = 0.1
transition_counts.pop(('<START>', '<END>'), 0);
transition_counts.pop(('<END>', '<START>'), 0);
myfile.close()


