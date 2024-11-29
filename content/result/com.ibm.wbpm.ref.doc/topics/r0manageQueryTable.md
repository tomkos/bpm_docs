<!-- image -->

# manageQueryTable.py administrative script

## Prerequisites

- Run the script in the connected mode, that is,
do not use the wsadmin -conntype none option.
- Run the script on the deployment manager
node.
- Include the wsadmin -user and -password options
to specify a user ID that has administrator or deployer authority.

## Location

```
install\_root\ProcessChoreographer\admin
install\_root/ProcessChoreographer/admin
```

## Syntax

```
install\_root/bin/wsadmin.sh 
install\_root\bin\wsadmin

-f manageQueryTable.py
     -cluster clusterName
     ( ( -deploy (qtdFile | jarFile)) |
     (-undeploy queryTableName)  |
     (-update definition (qtdFile | jarFile)) |
     (-query names -kind (composite | predefined | supplemental)) |
     (-query definition -name queryTableName))
```

## Parameters

<!-- image -->

<!-- image -->

If a JAR file is provided, it
can contain multiple QTD files and property files for each QTD file,
which contain display names and descriptions. Use the Query Table
Builder to export query table definitions as a JAR file.

## Examples

Deploy composite and supplemental
query tables:

Enter the following
command:

```
wsadmin.sh -f manageQueryTable.py -cluster myCluster -deploy sample.qtd
```

Enter the following command:

```
wsadmin -f manageQueryTable.py -cluster myCluster -deploy sample.qtd
```

Undeploy composite and supplemental query
tables:

Enter the following
command:

```
wsadmin.sh -f manageQueryTable.py -cluster myCluster -undeploy COMPANY.SAMPLE
```

Enter the following command:

```
wsadmin -f manageQueryTable.py -cluster myCluster -undeploy COMPANY.SAMPLE
```

Update composite and supplemental query
tables:

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

Retrieve a list of query tables:

Enter the following
command:

```
wsadmin.sh -f manageQueryTable.py -cluster myCluster 
           -query names -kind composite
```

Enter the following command:

```
wsadmin -f manageQueryTable.py -cluster myCluster 
        -query names -kind composite
```

Retrieve the XML definitions of query
tables:

Enter the following
command:

```
wsadmin.sh -f manageQueryTable.py -cluster myCluster 
           -query definition -name COMPANY.SAMPLE
```

Enter the following command:

```
wsadmin -f manageQueryTable.py -cluster myCluster 
        -query definition -name COMPANY.SAMPLE
```