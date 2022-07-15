import jenkins
import socket
import requests

server = jenkins.Jenkins('http://:8080', username='', password='')

nodeName=socket.gethostname()
hostResponce = requests.get('https://api.ipify.org')
host = hostResponce.text

credentialsId = ''


def create_node2(nodeName, host):
    params = {
        'port': '22',
        'username': 'root',
        'credentialsId': credentialsId,
        'host': host
    }
    server.create_node(
        name=nodeName,
        nodeDescription='pre',
        remoteFS='/root/jenkins',
        labels='precise',
        exclusive=False,
        launcher=jenkins.LAUNCHER_SSH,
        launcher_params=params)


create_node2(nodeName, host)
