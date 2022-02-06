import os
from types import TracebackType
from paramiko import SSHClient, AutoAddPolicy
from rich import print, pretty, inspect

pretty.install()
client = SSHClient()
# Load Host Keys
known_hosts = os.path.expanduser(os.path.join("~", ".ssh", "known_hosts"))
client.load_host_keys(known_hosts)
client.load_system_host_keys()

# Known hosts Policy
client.set_missing_host_key_policy(AutoAddPolicy())

client.connect(".0.0.1", username="root")
inspect(client, methods=True)
