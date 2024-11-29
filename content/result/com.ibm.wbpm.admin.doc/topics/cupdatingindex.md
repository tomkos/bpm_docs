# Manually re-creating or updating the Workflow Center index

## Re-creating the index with a Rest API

```
POST /rest/bpm/wle/v1/internal/processcenter/index
```

- On containers:
/opt/ibm/wlp/output/defaultServer/searchIndex/artifact/defaultServer
- On traditional: <Node\_profile>/searchIndex/artifact for each custom
profile

```
curl -k -i --user user:password --request POST https://hostname:port/uri-prefix/rest/bpm/wle/v1/internal/processcenter/index
```

## Traditional: Re-creating the index in a network deployment environment

The index is kept in the file system of the machine that the server is running on. You do not
need to back up the profile or the database before running the
artifactIndexFullReindex or artifactIndexUpdate commands, and
you can run the commands when the server is running.

To re-create the index in a network deployment environment, complete the following steps:

1 From the command prompt, change to the deployment manager profile bin subdirectory where the command is located.
    - For a Linux or UNIX operating system:
cd install\_root/profiles/process\_center\_Dmgr\_profile/bin
    - For a Windows operating
system:cd install\_root\profiles\process\_center\_Dmgr\_profile\bin
2 Enter the following command: hostName is the hostname of the application cluster member on the node andport is the server SOAP port.

- For a Linux or UNIX operating system:
./artifactIndexFullReindex.sh -u userId -p password -host hostName -port port
- For a Windows operating
system:artifactIndexFullReindex -u userId -p password -host hostName -port port

## Traditional: Updating the index in a network deployment environment

To update the index in a network deployment environment, complete the following steps:

1 From the command prompt, change to the deployment manager profile bin subdirectory where the command is located.
    - For a Linux or UNIX operating system:
cd install\_root/profiles/process\_center\_Dmgr\_profile/bin
    - For a Windows operating
system:cd install\_root\profiles\process\_center\_Dmgr\_profile\bin
2 Enter the following command: hostName is the hostname of the application cluster member on the node andport is the server SOAP port.

- For a Linux or UNIX operating system:
./artifactIndexUpdate.sh -u userId -p password -host hostName -port port
- For a Windows operating
system:artifactIndexUpdate -u userId -p password -host hostName -port port