<!-- image -->

# Exposing an XPath function JAR file to the runtime environment

## Before you begin

## About this task

## Procedure

1. In the WebSphere® Application
Server administrative
console, go to the cluster where Business Process Choreographer is configured.
lick Servers > Clusters > WebSphere application server clusters > cluster\_name.
2. Under Business Process Manager,
click Business Process Choreographer > Business Flow Manager > Custom properties > New.
3. Under Name, enter com.ibm.bpc.spi.xpath.path, and under Value, enter the path of the directory
that contains your XPath function JAR file.
4. Click OK to save your changes.
5. Restart the cluster.