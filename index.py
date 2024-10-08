import elasticsearch
from elasticsearch_dsl import Search
import pathlib

INDEX_NAME = 'index-1'
ELASTIC_HOST = 'http://localhost:9200/'
client = elasticsearch.Elasticsearch(hosts=[ELASTIC_HOST])

# data_1 = {
#     'id': 1,
#     'name': 'Python Arabia',
#     'tag': 'Python',
# }

# data_2 = {
#     'id': 2,
#     'name': 'Java for learn',
#     'tag': 'Java',
# }
# data_3 = {
#     'id': 3,
#     'name': 'Elasticsearch',
#     'tag': pathlib.Path('es.txt').read_text()
# }


# add_data_1 = client.index(index=INDEX_NAME, body=data_1)
# print(add_data_1)
# add_data_2 = client.index(index=INDEX_NAME, body=data_2)
# print(add_data_2)
# add_data_3 = client.index(index= INDEX_NAME, body= data_3)
# print(add_data_3)

if __name__ == "__main__":
    q = input("what do you want? ")
    fields = ['name', 'tag']
    results = Search(index=INDEX_NAME).using(client).query("multi_match", fields=fields, fuzziness='AUTO', query=q)

    for hit in results:
        print(hit)
        print(hit.id)
        print(hit.name)
        print("#"*30)
