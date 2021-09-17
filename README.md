# Semantic Knowledge Graph 
Implementation of Trey Grainger's Semantic Knowledge Graph in Elasticsearch 6.8

## Data preperation
Run the following command to fetch the relevant data.

`sh ./download_data.sh`

This downloads scifi stackexchange forum data.

## Data ingestion
Run the following command to ingest the data in ElasticSearch (you must have elasticsearch instance running in the background)

`python ingest_xml.py`

## Usage
`python skg.py "<entity1>" "<entity2>" <depth>`

## Reference
1. The Semantic Knowledge Graph: A compact, auto-generated model for real-time traversal and ranking of any relationship within a domain [[arxiv link](https://arxiv.org/pdf/1609.00464.pdf)]
2. Natural Language Search with Knowledge Graphs - Trey Grainger, Lucidworks [[youtube video](https://www.youtube.com/watch?v=5noi2VM9F-g)]

