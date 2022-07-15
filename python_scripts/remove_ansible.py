import jenkins

server = jenkins.Jenkins('http://:8080', username='', password='')

server.delete_node('ansible1')
server.delete_node('ansible2')
#server.delete_node('ansible3')
#server.delete_node('ansible4')
print ("Done!")
