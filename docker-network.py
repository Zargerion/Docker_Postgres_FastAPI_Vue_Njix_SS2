import docker

client = docker.from_env()

# Get the "app" container from the network
network_name = "sabter-site-2_custom"
container_name = "app"
network = client.networks.get(network_name)
container = network.containers.get(container_name)

# Get the IP address of the container
ip_address = container.attrs['NetworkSettings']['Networks'][network_name]['IPAddress']

print("IP address of the app container:", ip_address)

import psutil

# Find the Docker daemon process
for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
    if proc.info['name'] == 'dockerd':
        cmdline = proc.info['cmdline']
        break

# Extract the port number from the command line arguments
port = None
for arg in cmdline:
    if arg.startswith('-H'):
        parts = arg.split(':')
        if len(parts) == 2 and parts[1].isdigit():
            port = int(parts[1])
            break

# Use the port number to construct the Docker host URL
if port is not None:
    docker_host = f'tcp://localhost:{port}'
    print(f"Doker host is {docker_host}")
else:
    raise ValueError('Could not determine Docker daemon port number')

