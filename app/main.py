import asyncio

from app.kafka.repositories.kafka_repositories import KafkaRepository
from app.gateway.gRPC.server import serve as serve_gateway
from app.post_service.gRPC.server import serve as serve_post_service

async def main():
    kf = KafkaRepository()
    await kf.wait_kafka()
    asyncio.create_task(kf.get_message("registration", "user_service"))
    asyncio.create_task(serve_gateway())
    asyncio.create_task(serve_post_service())

if __name__ == "__main__":
    asyncio.run(main())