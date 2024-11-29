# serviceDeploy command-line utility

## Roles

- Administrator
- Deployer

## Syntax

```
serviceDeploy
inputarchive
-classpath jarpathname 
-cleanStagingModules
-freeform
-ignoreErrors
-keep
-novalidate
-outputApplication inputarchive
-uniqueCellID
-workingDirectory temppath
```

## Parameters

## Inputs

## Examples

- Creates an application file called MyValueModule.ear from the
MyValueModule.jar file.
- Specifies that the resources reside in the directories
c:\java\myvaluemoduleres.rar and
c:\java\commonres.jar.
- Enables the Java subdirectory within the .jar file as
free-form.
- Keeps the temporary files generated during deployment.

```
servicedeploy MyValueModule.jar 
-classpath "c:\java\myvaluemoduleres.rar;c:\java\commonres.jar"
-freeform true -keep
```