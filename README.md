# be-tourist-map
API Back-end for Tourist Map App

Up ES:
 - docker pull docker.elastic.co/elasticsearch/elasticsearch:5.3.0
 - docker run --name elasticsearch -p 9200:9200 -e "http.host=0.0.0.0" -e 'xpack.security.enabled=false' -e "transport.host=127.0.0.1" docker.elastic.co/elasticsearch/elasticsearch:5.3.0