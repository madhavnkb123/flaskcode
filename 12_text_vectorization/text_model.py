from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
docs=["python data science course","flask web development course","machine learning with python"]
v=TfidfVectorizer(stop_words="english"); X=v.fit_transform(docs)
q=v.transform(["python programming course"])
print("Similarity:",cosine_similarity(q,X).round(3).tolist()[0])
print("Vocabulary:",v.get_feature_names_out().tolist())
