import asyncio

#async = coroutine (not sub) using asyncio
async def echo_client(message):
  # Client is basically server backwards - wait for connection then send message and read response
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)
    print(f"client sends {message!r}")
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f"client receives: {data.decode()!r}")
    writer.close()

# could make a main but it would just run the client so let's do that directly
asyncio.run(echo_client("I LOVE ASYNC!"))
