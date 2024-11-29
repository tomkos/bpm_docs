<!-- image -->

# createVersionedSCAModule command

Use the createVersionedSCAModule command
to create a new instance of an SCA module when you want to deploy
the same versioned module across multiple clusters in a cell. You
must use this command once for each additional instance of the module
you want to deploy. The new instance is created in a new EAR file;
the new EAR file name contains the module version value and the specified
unique cell ID.

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
createVersionedSCAModule
-archiveAbsolutePath input\_archive\_dir
-workingDirectory working\_dir
[-uniqueCellID unique\_cell\_ID]
```

## Required parameters

## Optional parameters

## Command output

The createVersionedSCAModule returns
a uniquely named instance of the SCA module to the same directory
that contains the original module (input\_archive\_dir).

## Example

The following example illustrates
how to create a new instance of a previously installed versioned SCA
module named billingProcess. In this example, the
original module is version 1.0.1 and it is stored in c:/myDir/billingProcess\_v1\_0\_1.ear.

```
$AdminTask createVersionedSCAModule {
   -archiveAbsolutePath C:/myDir/billingProcess\_v1\_0\_1.ear 
   -workingDirectory C:/tempAppDirectory 
   -uniqueCellID CellA1}
```