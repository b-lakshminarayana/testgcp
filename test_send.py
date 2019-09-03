import argparse
from google.cloud import pubsub


def list_topics(project_id):
	pubsub_client=pubsub.Client()
	
for topic in pubsub_client.list_topics():
	print(topic.name)


def create_topic(topic_name):
	topic_name = "test_topic1"
	pubsub_client=pubsub.Client()
	topic = pubsub_client.topic(topic_name)
	topic.create()
	print('Topic {} created: {}'.format(topic.name))
