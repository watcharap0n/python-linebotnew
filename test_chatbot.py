from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn import svm
from attacut import tokenize
from numpy import random


test = 'ตอนนี้มีโปรโมชั่นอะไรบ้างค่ะ'
print(tokenize(test))




# embedding = [0, 1]
# answers = [['สวัสดีจ้า', 'สวัสดีครับ'], ['แมงโก้จ้า', 'แมงโก้ไง']]
# xtrain = ['สวัสดี ทักทาย', 'ชื่ออะไร ชื่อ']
#
# count_vect = CountVectorizer(tokenizer=tokenize)
# Xtrain_count = count_vect.fit_transform(xtrain)
# tf_transformer = TfidfTransformer(use_idf=False)
# tf_transformer.fit(Xtrain_count)
# Xtrain_tf = tf_transformer.transform(Xtrain_count)
# SVM = svm.SVC(C=1.0, kernel='linear', degree=3,
#               gamma='auto', probability=True)
# SVM.fit(Xtrain_tf, embedding)
# msg = ['ชื่อ']
# Xtest_count = count_vect.transform(msg)
# Xtest_tf = tf_transformer.transform(Xtest_count)
# label = SVM.predict(Xtest_tf)
# prop = SVM.predict_proba(Xtest_tf)[0][label]
# confidence = (0.35 / ((len(embedding) * prop) ** 0.5)) ** 2
#
# label = int(label)
# print(answers[label])
# print(random.choice(answers[label]))

