import jenkins

server = jenkins.Jenkins('http://localhost:8080', username='v_gaynullin', password='0225DE92E41128C3')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))

#server.create_node('slave1')
nodes = server.get_nodes()
print (nodes)
#node_config = server.get_node_info('slave1')
#print (node_config)
#server.disable_node('slave1')
#server.enable_node('slave1')

# create node with parameters
params = {
    'port': '22',
    'username': 'root',
    'credentialsId': 'c20932c0-4121-476f-b079-e9d100c99c41',
    'host': '195.133.146.165'
}
server.create_node(
    'slave1',
    nodeDescription='my test slave',
    remoteFS='/root/jenkins',
    labels='precise',
    exclusive=True,
    launcher=jenkins.LAUNCHER_SSH,
    launcher_params=params)
