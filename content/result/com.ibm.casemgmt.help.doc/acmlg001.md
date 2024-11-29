# Log files for the Content Platform Engine REST
API

1. Copy the
/install\_path/IBM/FileNet/ContentEngine/tools/PE/samples/fnlog4j.properties.sample
file from the Content Platform Engine
server.
2. Place the file in the jre/lib directory of the application server that is
installed on the workflow server, and rename the file to
fnlog4j.properties.
3. Edit the fnlog4j.properties file to specify your preferred logging level.
For details, see the IBM®
FileNet® P8
documentation about enabling trace logging for process clients.When the updated
fnlog4j.properties file is placed in the correct jre/lib
directory, logging is automatically enabled. You do not need to restart the application server or
the workflow server.

| Operating system   | Default file path                                                                  |
|--------------------|------------------------------------------------------------------------------------|
| AIX®               | /usr/IBM/WebSphere/AppServer/java/jre/lib/fnlog4j.properties                       |
| Linux®             | /opt/IBM/WebSphere/AppServer/java/jre/lib/fnlog4j.properties                       |
| Linux for System z | /opt/IBM/WebSphere/AppServer/java/jre/lib/fnlog4j.properties                       |
| Windows            | drive:\Program Files (x86)\IBM\WebSphere\AppServer\java\jre\lib\fnlog4j.properties |