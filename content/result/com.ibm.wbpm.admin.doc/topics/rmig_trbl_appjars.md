# java.lang.ClassNotFoundException during or after migration

1. Move the custom application JAR files out of the
install\_root/lib/ext directory into another directory.
2. Update the classpath parameter to point to the directory that contains the JAR files. To update
the classpath in the administrative console, go to Servers > Server Types > WebSphere application servers  and click the name of your server. Under Server Infrastructure, open Java
and Process Management and click  Process Definition. Under
Additional Information, click Java Virtual Machine. Add your directory to the
classpath.

You must update the classpath for each JVM that is affected, including the deployment manager and
each of the application cluster members.