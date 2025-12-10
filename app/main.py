import asyncio

from app.kafka.repositories.kafka_repositories import KafkaRepository
from app.gateway.gRPC.server import serve as serve_gateway
from app.post_service.gRPC.server import serve as serve_post_service
from app.core.db.db_hellper import db_helper

async def main():
    kf = KafkaRepository()
    await kf.wait_kafka()
    migrations_task =  asyncio.create_task(db_helper.run_migrations())
    kafka_task = asyncio.create_task(kf.get_message("registration", "user_service"))
    gateway_task = asyncio.create_task(serve_gateway())
    post_task = asyncio.create_task(serve_post_service())
    await asyncio.gather(migrations_task,kafka_task, gateway_task, post_task)

if __name__ == "__main__":
    asyncio.run(main())