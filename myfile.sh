#!/bin/bash
clear
cd
mkdir logs
echo "The script starts now."
sudo systemctl start zookeeper >> ~/logs/zookeper.log
sudo systemctl start redis.service
export KAFKA_HOME="/opt/Kafka/kafka_2.12-2.2.1"
sudo $KAFKA_HOME/bin/kafka-server-start.sh $KAFKA_HOME/config/server.properties >> ~/logs/kafka.log &
cd Downloads/scrapy-cluster/kafka-monitor/
python kafka_monitor.py run >> ~/logs/kafkamonitor.log
cd ..
cd redis-monitor
python redis_monitor.py >> ~/logs/redislog.log
cd ..
cd crawler
scrapy runspider crawling/spiders/link_spider.py
cd ..
cd rest
python rest_service.py
cd kafka-monitor
python kafkadump.py dump -t demo.crawled_firehose >> ~/logs/crawled
python kafkadump.py dump -t demo.outbound_firehose >> ~/logs/kafkaoutput

