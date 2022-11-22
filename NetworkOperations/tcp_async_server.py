import asyncio
# run this in the background and then connect to it using client

#async = coroutine (not sub) using asyncio
async def echo_handler(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    ad = writer.get_extra_info('peername')

    print(f'recieved {message!r} from {adr!r}')

    print(f'sending {message!r}')
    writer.write(data)
    await writer.drain()

    print("closing connection")
    writer.close()


async def main():
    server = await asyncio.start_server(
        echo_handler, '127.0.0.1', 8888)

    # set comprehension gets us all the sockets we are connecting to
    ads = ", ".join((str(sock.getsockname()) for sock in server.sockets))
    print(f"Serving addresses: {ads}")

    # setup server to serve forever, make sure to kill it if done
    async with server:
        await server.serve_forever()

asyncio.run(main())
