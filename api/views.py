from .models import Product
from copydetect import CopyDetector
from .apps import VectorizeConfig
from opensearchpy import OpenSearch

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import ForumSearchSerializer

@api_view(['GET'])
def check(request, id):
    ref_product = Product.objects.filter(id = id).first()
    test_products = Product.objects.filter(status = 3).exclude(id = id)
  
    for product in test_products:
        try:
            detector = CopyDetector(code1=ref_product.file, code2=product.file, extension="php", display_t=0.5)
            detector = detector.run()
        except:
            detector = 0

        if(detector != 0):
            return Response(product.name, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    return Response("There is no any plagiarism", status=status.HTTP_200_OK)

@api_view(['POST'])
def vectorize(request):
    data = request.POST["data"]
    preprocess = VectorizeConfig.reprocess(data)
    vector = VectorizeConfig.get_vec(preprocess)
    return Response(vector)

@api_view(['GET'])
def search(request, query):
    page = request.GET.get('from', 0)
    tags = request.GET.get('tags', None)
    type = request.GET.get('type', None)
    must_not = request.GET.get('must_not', None)
    
    preprocess = VectorizeConfig.reprocess(query)
    vector = VectorizeConfig.get_vec(preprocess)

    host = 'search-abysshub-j3qdpacyhclsugmt4pt74f635e.us-east-2.es.amazonaws.com'
    port = '443'
    auth = ('Abyss', '888Ceyhun2001@') 
    ca_certs_path = '/home/abyss/Desktop/Abysshub/root-ca.pem' 

    client = OpenSearch(
        hosts = [{'host': host, 'port': port}],
        http_compress = True, 
        http_auth = auth,
        use_ssl = True,
        verify_certs = False,
        ssl_assert_hostname = False,
        ssl_show_warn = False,
        ca_certs = ca_certs_path
    )
    
    query = {
        "size": 10,
        "from": page,
        "query": {
            "bool" : {
                "must": {
                    "knn": {
                        "vector": {
                            "vector": vector.tolist(),
                            "k": 2
                        }
                    }
                }
            }
        }
    }
    if(tags != None):
        query["query"]["bool"]["should"] = []
        query["query"]["bool"]["minimum_should_match"] = 1
        query["query"]["bool"]["boost"] = 1.00
        for tag in tags.split(","):
            query["query"]["bool"]["should"].append({ "term" : { "tags" : tag }})

    if(must_not != None):
        query["query"]["bool"]["must_not"] = []
        for tag in must_not.split(","):
            query["query"]["bool"]["must_not"].append({ "term" : { "tags" : tag }})

    if(type != None):
        query["query"]["bool"]["filter"] = [{ "term" : { "type" : type }}]

    response = client.search(
        body = query,
        index = 'threads'
    )

    return Response({
        "data" : {
            "total"  : response["hits"]["total"]["value"],
            "from"   : page,
            "results": ForumSearchSerializer(response["hits"]["hits"], many=True).data
        },
        "message" : None,
        "errors"  : None
    })
