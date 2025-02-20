from sklearn import svm
from sklearn.externals import joblib
import json

with open('../data/lang/freq.json', 'r', encoding='utf-8') as fp:
    d = json.load(fp)
    data = d[0]

clf = svm.SVC()
clf.fit(data['freqs'], data['labels'])

joblib.dump(clf, '../data/lang/freq.pkl')
print('ok')
