# Extracting a managed file

```
var managedFile = tw.system.model.findManagedFileByPath("lsw-services.jar",
TWManagedFile.Types.Server);
log.error("Got the managed file!: " + managedFile);
managedFile.writeDataToFile("C:\\lsw-services.jar");
```