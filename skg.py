from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
import es_queries
import sys

def get_edge_for_two_nodes(nodes, search_field, indexes_to_search, depth=1, level=1):
    query_body = es_queries.find_edge(nodes[0], nodes[1], search_field)
    # print(query_body)
    result = es.search(index=indexes_to_search, body=query_body)
    print(result)
    buckets = result['aggregations']['keywords']['buckets']

    print("level: {} nodes: {} | {}".format(level, nodes[0], nodes[1]))
    for b in buckets:
        if not b['key'] in nodes:
            print("term: {} | docs: {} | bg_count: {} | score: {}%".format(b['key'], b['doc_count'],
            		b['bg_count'], int(b['score']*100)))
            if depth > 1:
                for n in nodes:
                    get_edge_for_two_nodes([n, b['key']], search_field, indexes_to_search, depth-1, level+1)

# es = Elasticsearch()

# get_edge_for_two_nodes(["yoda", "vader"], "body_text", ["scifi_posts", "scifi_comments"],  1)
# get_edge_for_two_nodes(["jean grey", "in love"], "body_text", ["scifi_posts", "scifi_comments"])
# get_edge_for_two_nodes(["marty mcfly", "time travel"], "body_text", ["scifi_posts", "scifi_comments"], 5)

# get_edge_for_two_nodes(["bruce banner", "iron man"], "entities", ["scifi_posts", "scifi_comments"], 2)
# get_edge_for_two_nodes(["yoda", "vader"], "entities", ["scifi_posts", "scifi_comments"],  1)
# get_edge_for_two_nodes(["jean grey", "in love"], "body_text", ["scifi_posts", "scifi_comments"], 2)
# get_edge_for_two_nodes(["darth vader", "luke skywalker"], "entities", ["scifi_posts"], 3)

if __name__=="__main__":
    if len(sys.argv) == 4:
        node1 = str(sys.argv[1])
        node2 = str(sys.argv[2])
        depth = int(sys.argv[3])
        es = Elasticsearch()
        get_edge_for_two_nodes([node1, node2], "entities", ["scifi_posts", "scifi_comments"], depth)
    else:
        print("Arguments insufficient")

