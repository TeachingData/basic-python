import asyncio

class ProcessMonitor:
    """
    This is used to check several simple measurements from the system. Including:
      - The number of processes running (ps)
      - The number of files and total size of files in a directory
      - The number of files over a set size in a directory and its subdirectories
      - The pid of a passed process based on its name
    It then logs each of these to a specific logging file (unless changed by constructor).
    """

    __logfile: str = "processlog.log"

    def __init__(self, logfile: str="processlog.log"):
        if logfile[:-4] != ".log":
            logfile += ".log"
        self.__logfile = logfile

    def totalprocesses(self) -> str:
        # list of values from ps and -1 for header and empty line at end
        return asyncio.run(self.run_command("ps -l")).count("\n")-1

    def totalfiles(self) -> str:
        # get results to file because we have to run two commands on it (get total and total)
        results = asyncio.run(self.run_command("ls -lh"))
        # not going to use an f-string here, one of the rare times where string concat is better (cause of backslash)
        return 'Total files ' + str(results.count("\n")-1) + ' with Total Memory of ' \
                + str(results[6:results.find("\n")])

    def findprocess(self, name: str="python") -> list:
        # Again we'd need a full regex here to properly check or learn grep better - this is just an example
        results = asyncio.run(self.run_command(f"ps | grep {name}")).split("\n")
        lines = []
        for line in results:
            l = line.split()
            if len(l) > 1:
                lines.append(f"Process {l[-1]} running with pid of {l[0]}")
        return lines

    def findbigfiles(self, directory: str="~") -> list:
        # using +00 is insane - it gets every file but good for testing - TODO: let pass size
        results = asyncio.run(self.run_command(f"find {directory} -size +00 -print"))

        # we can ignore the first line and any last entry which doesn't have a "." in its last 4 chars
        # cause that's not a file or is a hidden file

        files = []
        for line in results.split("\n"):
            l = line.split("/")
            if "." in l[-1][-5:]:
                # not including first part of directory because its blank
                files.append(f"filename: {l[-1]}, directory: /{'/'.join(l[1:-1])}")
        return files


    async def run_command(self, command: str):
        """
        Runs passed command in coroutine until finished and
        then passes output back to calling function for logging
        Not the best way to do this - have some .gather function after building a bundle usually
            Just for an example to teach a few concepts
        """
        proc = await asyncio.create_subprocess_shell(
                command,
                stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE)

        stdout, stderr = await proc.communicate()

        if stdout:
            return stdout.decode()
        return stderr.decode()
