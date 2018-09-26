#Samantha Shoecraft
#7/26/17
import nltk
import operator
example = '<START> tera\'ngan legh yaS <END>'
e_words = example.split()
from transition import transition_counts
from transition import tag_counts
from emission import dict

tags = list(tag_counts.keys())
T = len(tag_counts.keys())
W = len(e_words)
score = [[0 for x in range(W)] for y in range(T)]
backP = [[0 for x in range(W)] for y in range(T)]

for t in range(1,6):
	if t != 4:
		score[t][1] = 1
		if (tags[0],tags[t]) in transition_counts.keys():
			score[t][1] = score[t][1] * transition_counts.get((tags[0], tags[t]))
		else:
			score[t][1] = score[t][1] * 0.1
		if e_words[1] in dict.keys():
			score[t][1] = score[t][1] * dict.get(e_words[1]).get(tags[t])
		else:
			score[t][1] = score[t][1] * 0.1
		backP[t][1] = 0;

for w in range(2, 5):
	for t in range(1,6):
		if t != 4:
			if e_words[w] in dict.keys():
				score[t][w] = score[t][w] * dict.get(e_words[w]).get(tags[t])
			else:
				score[t][w] = 0.1
			max = -1
			i = -1
			j_save = -1
			
			for j in range(1,6):
				if j != 4:
					if (tags[j],tags[t]) in transition_counts.keys():
						i = score[j][w - 1] * transition_counts.get((tags[j], tags[t]))
					else:
						i = score[j][w - 1] * 0.1
					if i > max:
						max = i
						j_s = j
			score[t][w] = score[t][w] * max
			backP[t][w] = j_s

max = -1
j_s = -1
for t in range(1,6):
		if t != 4:
			if score[t][4] > max:
				max = score[t][4]
				j_s = t

s_stack = []
s_stack.append(tags[ backP[j_s][4]])
s_stack.append(tags[backP[backP[j_s][4]][3]])
s_stack.append(tags[ backP[backP[ backP[j_s][4] ][3]][2]] )


print(''.join(e_words[t] + '/' + s_stack.pop() + ' ' for t in range(1,4)))




