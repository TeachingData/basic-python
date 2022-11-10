import asyncio
import sys

# run external python command (cause shell) using async wrapper
async def get_date():
    # external command to run
    command = 'import datetime; print(f"date = {datetime.datetime.now()}")'

    # create subprocess, requires redirect of stdout for piping
    pro = await asyncio.create_subprocess_exec(
            sys.executable, '-c', command,
            stdout=asyncio.subprocess.PIPE)

    # use the redirected output (stdout) and read each line of it
    data = await pro.stdout.readline()
    line = data.decode('ascii').strip()

    # wait (think spin lock) for exit of process
    await pro.wait()
    return line

print(asyncio.run(get_date()))
