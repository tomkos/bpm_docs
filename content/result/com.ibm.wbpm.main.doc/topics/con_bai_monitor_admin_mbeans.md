# Monitoring and administering with MBeans

You can monitor and administer a running server through its JMX MBeans to gather
information, detect issues, and perform actions without having to restart the server.

- Monitoring and administering indexers with MBeans

A JMX MBean is registered for each indexer on the Liberty server when the indexer is initialized, and is unregistered when the indexer stops.
- Monitoring and administering retrievers with MBeans

A JMX MBean is registered for each retriever on the Liberty server when the retriever is initialized, and is unregistered when the server stops.
- Using JConsole to access the MBeans

You can use the JConsole tool to view the MBean attributes, modify the indexers and retrievers MBean attributes that are not in read-only mode, and invoke operations.