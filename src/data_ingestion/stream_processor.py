"""Real-time streaming processor using Redis Streams."""
import json
import logging
from typing import Callable, Dict

import redis

logger = logging.getLogger(__name__)


class StreamProcessor:
    def __init__(self, redis_host: str = "localhost", redis_port: int = 6379):
        self.redis_client = redis.Redis(
            host=redis_host, port=redis_port, decode_responses=True
        )
        self.stream_name = "financial_news_stream"
        self.consumer_group = "news_processors"

    def publish(self, article: Dict):
        """Publish article to stream."""
        try:
            self.redis_client.xadd(
                self.stream_name,
                {"data": json.dumps(article)},
                maxlen=10000,
            )
            logger.info(f"Published article: {article.get('title', '')}")
        except Exception as e:
            logger.error(f"Error publishing to stream: {e}")

    def create_consumer_group(self):
        """Create consumer group if it doesn't exist."""
        try:
            self.redis_client.xgroup_create(
                self.stream_name, self.consumer_group, id="0", mkstream=True
            )
        except redis.ResponseError as e:
            if "BUSYGROUP" not in str(e):
                raise

    def consume(self, callback: Callable, consumer_name: str = "consumer1"):
        """Consume messages from stream."""
        self.create_consumer_group()
        while True:
            try:
                messages = self.redis_client.xreadgroup(
                    groupname=self.consumer_group,
                    consumername=consumer_name,
                    streams={self.stream_name: ">"},
                    count=10,
                    block=1000,
                )
                for stream, message_list in messages:
                    for message_id, message_data in message_list:
                        article = json.loads(message_data["data"])
                        callback(article)
                        self.redis_client.xack(
                            self.stream_name, self.consumer_group, message_id
                        )
            except Exception as e:
                logger.error(f"Error consuming from stream: {e}")
