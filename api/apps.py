from django.apps import AppConfig
from sentence_transformers import SentenceTransformer

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
import re

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

class VectorizeConfig(AppConfig):
    global model 
    model = SentenceTransformer("/home/ubuntu/django_abysshub/api/sbert1")
    # model = SentenceTransformer("/home/abyss/Desktop/Abysshub/sbert1")
    def get_vec(query):
        return model.encode(query)

    def reprocess(query):
        stop_words = set(stopwords.words('english')) - set(['what', 'why', 'where', 'which', 'when', 'how'])
        question = re.sub(r'[^A-Za-z]+', ' ', query)
        words = word_tokenize(str(question.lower()))
        stemmer = SnowballStemmer("english")
        question = ' '.join(str(stemmer.stem(j)) for j in words if j not in stop_words and (len(j) != 1 or j == 'c'))
        return question
