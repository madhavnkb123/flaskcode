import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
X=np.array([[2,10,3],[3,12,4],[4,15,5],[8,30,9],[9,32,10],[10,35,11]])
X=StandardScaler().fit_transform(X)
p=PCA(n_components=2).fit(X)
print("Explained variance:",p.explained_variance_ratio_.round(3))
print("Components:\n",p.components_.round(3))
