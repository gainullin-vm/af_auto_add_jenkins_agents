import jenkins

server = jenkins.Jenkins('http://:8080', username='', password='')


nodeList = [
    'ansible3'
]

hostList = [
    ''
]

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
        exclusive=True,
        launcher=jenkins.LAUNCHER_SSH,
        launcher_params=params)
    print(server.get_node_info(nodeName))


i = 0
for nodeName in nodeList:
    host = hostList[i]
    create_node2(nodeName, host)
    print("Node " + nodeName + "successfully created!")
    i = i+1
