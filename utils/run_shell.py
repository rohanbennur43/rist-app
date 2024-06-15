import subprocess
import threading

class ShellCommandThread(threading.Thread):
    def __init__(self, command):
        super().__init__()
        self.command = command
        self.process = None
        self.stdout = None
        self.stderr = None
        self.exception = None
        self._stop_event = threading.Event()

    def run(self):
        try:
            # Run the shell command
            self.process = subprocess.Popen(self.command)
            self.stdout, self.stderr = self.process.communicate()
        except subprocess.CalledProcessError as e:
            self.stderr = e.stderr
            self.exception = e

    def stop(self):
        # Set the stop event and terminate the process if 
        self._stop_event.set()
        if self.process and self.process.poll() is None:
            self.process.terminate()

    def stopped(self):
        # Check if the thread is stopped
        return self._stop_event.is_set()


def run_shell_command(command):
    """
    Run a shell command in a separate thread and return the thread object.
    
    :param command: The shell command to execute (list or string).
    :return: Thread object.
    """
    thread = ShellCommandThread(command)
    thread.start()
    return thread
