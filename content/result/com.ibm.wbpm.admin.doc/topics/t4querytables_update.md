<!-- image -->

# Updating composite and supplemental query tables

## Before you begin

- Run the script in connected mode,
that is, do not use the wsadmin -conntype none option.
- At least one cluster member must be running.
- Include the
wsadmin -user and -password options
to specify a user ID that has operator, administrator, or deployer
authority.
- If you are not working with the default
profile, use the wsadmin -profileName profile option
to specify the profile.

## About this task

## Procedure

1 Change to the Business Process Choreographersubdirectory where the administrative script is located.
    - install\_root/ProcessChoreographer/admin
    - install\_root\ProcessChoreographer\admin
2. Update the query table using either a query table definition
XML file or a JAR file that contains the definitions. If property
files are already deployed, they will be overwritten. Enter the following
command:
install\_root/bin/wsadmin.sh -f manageQueryTable.py
       -cluster clusterName
         -update definition qtdFile | jarFileEnter the following command:
install\_root\bin\wsadmin -f manageQueryTable.py
       -cluster clusterName
         -update definition qtdFile | jarFileWhere: 
-cluster clusterName
The name of the cluster where Business Process Choreographer is
configured. In a multicluster setup, you must specify the application
cluster because that is where Business Process Choreographer is configured.
-update definition qtdFile | jarFile
The file name, including the fully qualified path, of either the
query table definition XML file to be updated or a JAR file that contains
the definitions. Use this option to update an existing query table. On Windows, you must use either / or \\\\ as
the path separator. For example, to specify the file c:\temp\myQueryTable.qtd you
must specify it as c:/temp/myQueryTable.qtd or c:\\\\temp\\\\myQueryTable.qtd.If a JAR file is provided, it
can contain multiple QTD files and property files for each QTD file,
which contain display names and descriptions. Use the Query Table
Builder to export query table definitions as a JAR file.

## Example

Enter the following
command:

```
wsadmin.sh -f manageQueryTable.py -cluster myCluster 
           -update definition sample\_v2.qtd
```

Enter the following command:

```
wsadmin -f manageQueryTable.py -cluster myCluster 
        -update definition sample\_v2.qtd
```

<!-- image -->