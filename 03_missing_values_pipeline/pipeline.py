import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
df=pd.DataFrame({"age":[21,None,35,42,None],"income":[30000,45000,None,80000,52000],"score":[70,82,91,None,76]})
features=["age","income","score"]
X=SimpleImputer(strategy="median").fit_transform(df[features])
X=StandardScaler().fit_transform(X)
print(pd.DataFrame(X,columns=features).round(2))
