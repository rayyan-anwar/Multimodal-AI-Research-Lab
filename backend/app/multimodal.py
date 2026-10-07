import numpy as np
from PIL import Image
from sklearn.feature_extraction.text import TfidfVectorizer
def analyze(image,text):
    a=np.asarray(image.convert("RGB"),dtype=float)/255
    tf=TfidfVectorizer(max_features=50,stop_words="english").fit_transform([text])
    return {"author":"Rayyan Anwar","image":{"width":image.width,"height":image.height,"mean_intensity":float(a.mean()),"std_intensity":float(a.std())},"text":{"nonzero_terms":int(tf.nnz),"words":len(text.split())}}
