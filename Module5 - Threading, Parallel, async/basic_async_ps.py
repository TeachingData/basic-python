import asyncio

# run external python command (cause shell) using async wrapper
async def get_processes():
    # external command to run
    command = 'ps'

    # create subprocess, requires redirect of stdout for piping
    pro = await asyncio.create_subprocess_exec(
            #sys.executable, '-c', command,
            command, stdout=asyncio.subprocess.PIPE)

    # use the redirected output (stdout) and read each line of it
    # adds each line to a list for later processing
    lines = []
    while True:
        data = await pro.stdout.readline()
        if data:
            lines.append(data.decode('ascii').strip())
        else:
            break

    # wait (think spin lock) for exit of process
    await pro.wait()
    return lines

print(*asyncio.run(get_processes()), sep="\n")
# print using splat (unpack operator) and a seperator arguement is same as:
# for p in asyncio.run(get_processes()):
#   print(p)
