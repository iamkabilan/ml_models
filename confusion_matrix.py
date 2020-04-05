"""
Let's implement the confusion matrix without using any ML libraries.


Notations:
	No - 0
	Yes - 1
"""

actual= [1, 1, 0, 1, 0, 0, 1, 0, 0, 0]
predicted= [1, 0, 0, 1, 0, 0, 1, 1, 1, 0]

def confusion_matrix(actual,predicted):
	n=len(actual)
	TP=0
	TN=0
	FP=0
	FN=0
	conf_mat=[]
	for i in range(n):
		
		if(actual[i]==0 and predicted[i]==0): # 1) True-Negative
			TN=TN+1
		elif(actual[i]==1 and predicted[i]==0): # 2) False-Positive
			FP=FP+1
		elif(actual[i]==0 and predicted[i]==1): # 3) False-Negative
			FN=FN+1
		else:									# 4) True-Positive
			TP=TP+1
	conf_mat.append([TN,FN])
	conf_mat.append([FP,TP])

	return conf_mat

print(confusion_matrix(actual,predicted))