import csv
import itertools

def calculate_apriori_confidence(X,Y,buckets):
	occr_X = 0
	occr_Y = 0
	for bucket in buckets:
		if type(X) is list:
			if all(val in bucket for val in X):
				occr_X = int(occr_X) + 1
		else:
			if X in bucket:
				occr_X = int(occr_X) + 1

		if type(Y) is list:
			if all(val in bucket for val in Y):
				occr_Y = int(occr_Y) + 1
		else:
			if Y in bucket:
				occr_Y = int(occr_Y) + 1
	conf  = float(occr_Y)/float(occr_X)*100
# 	print "Confidence given X implies Y: ", conf,"%"
	return conf

def pred_dis(symptomlist,buckets):
	disease_score={}
	disease_bucket = {}
	score = 0
	sure = 0
	for bucket in buckets:
		bucket_len = (float(len(bucket)))
		score = set(symptomlist) & set(bucket)
		interection_len = (float(len(score)))
		score = float(len(score))/float(len(symptomlist))*100
		score_1 = interection_len/bucket_len*100
		if(score == 100 and score_1 == 100):
			sure = 1
		if score>0:
			# print(score)
			disease = get_disease_given_bucket(bucket)
			# print(disease)
			disease_score[disease] = score
			disease_bucket[disease] = bucket
		if sure:
			print("It is most likely "+ disease)
			return
	# print(disease_score)
	top_3 = sorted(disease_score.items() , reverse=True, key=lambda x: x[1])[:3]
	score = []
	score_1 = []
	symps = {}
	symptom_new = []	
	for illness in top_3:
		symptomlist_new = symptomlist.copy()
		dif = (set(disease_bucket[illness[0]])).difference(set(symptomlist))
		# print(dif)
		symptom = "fever"
		prev_confidence = 0
		while(len(dif)>0):
			symp = dif.pop()
			if(symp == ''):
				continue
			if(calculate_apriori_confidence(disease_bucket[illness[0]],symp,buckets) > prev_confidence):
				symptom = symp
		# if(symptom not in symps.keys()):
		symptom_new.append(symptom)
	return symptom_new,top_3,symptomlist,disease_bucket

def react_out(out,top_3,symptomlist,disease_bucket):
	# out = react_inp(symptom_new)
	# out = "YYY"
	i = 0
	symps = {}
	for illness in top_3:

		symptomlist_new = symptomlist.copy()
		if(symptom not in symps.keys()):
			symptom_new.append(symptom)

			x = out[i]
			i+=1
			if(x == 'Y'):
				symptomlist_new.append(symptom)
				symps[symptom] = 1
			else:
				symps[symptom] = 0
		else:
			if(symps[symptom]==1):
				symptomlist_new.append(symptom)
				
		inters = (set(symptomlist_new) & set(disease_bucket[illness[0]]))
		score.append( float(len(inters))/float(len(symptomlist_new))*100)
		score_1.append( float(len(inters))/float(len(disease_bucket[illness[0]]))*100)
	ind = 0
	if(score[1]>score[0] or (score[1]==score[0] and score_1[1]>score_1[0])):
		ind = 1
	if(score[2]>score[ind] or (score[2]==score[ind] and score_1[2]>score_1[ind])):
		ind = 2

	print("It is most probably "+top_3[ind][0])
	return top_3[ind][0]


"""Assuming every bucket uniquely points to a disease"""
def get_disease_given_bucket(bucket):
	disease = ""
	with open("bucketmap.csv") as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			row_clean = [i for i in row if i]
			bucket_clean = [i for i in bucket if i]
			if len(row_clean) == (len(bucket_clean)+1):
				if all(values in row_clean for values in bucket_clean):
					disease = row_clean[0]
					break
#     bucket = pd.read_csv()

	return disease

def solver(symptomlist):
	buckets = []

	with open("buckets.csv") as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			buckets.append(row)

	# symptomlist=["suicidal","hallucinations auditory","irritable mood","agitation"]
	return pred_dis(symptomlist,buckets)