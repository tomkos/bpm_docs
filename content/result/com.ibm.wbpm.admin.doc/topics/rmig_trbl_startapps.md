# Errors when starting application cluster after migrating

```
[12/17/14 17:59:49:094 CST] 000000ad CompositionUn E   WSVR0194E: Composition unit WebSphere:cuname=HTM\_PredefinedTaskMsg\_V8000\_MyTopPS8011.AppTarget in BLA WebSphere:blaname=HTM\_PredefinedTaskMsg\_V8000\_MyTopPS8011.AppTarget failed to start.

[12/17/14 17:59:58:282 CST] 000000ae CompositionUn E   WSVR0194E: Composition unit WebSphere:cuname=STPJM01-BBMA-PublishedAssertManagementApp in BLA WebSphere:blaname=STPJM01-BBMA failed to start.
[12/17/14 18:00:12:782 CST] 000000ad CompositionUn E   WSVR0194E: Composition unit WebSphere:cuname=STPJM01-BBMA-Media\_Service\_Toolkit\_ImplementationApp in BLA WebSphere:blaname=STPJM01-BBMA failed to start.
[12/17/14 18:00:13:891 CST] 000000ad CompositionUn E   WSVR0194E: Composition unit WebSphere:cuname=HTM\_PredefinedTasks\_V8000\_MyTopPS8011.AppTarget in BLA WebSphere:blaname=HTM\_PredefinedTasks\_V8000\_MyTopPS8011.AppTarget failed to start.
[12/17/14 18:05:56:094 CST] 00000001 ContainerHelp E   WSVR0501E: Error creating component com.ibm.ws.runtime.component.CompositionUnitMgrImpl@27b43375
com.ibm.ws.exception.RuntimeWarning: com.ibm.ws.webcontainer.exception.WebAppNotLoadedException: Failed to load webapp: MyTopPS8011.Proxy\_host
at com.ibm.ws.webcontainer.component.WebContainerImpl.install(WebContainerImpl.java:432)
...
```

To solve the problem, apply the same proxy or
HTTP server configurations that were present in your source environment,
and also update the virtual host configuration as needed. See the WebSphere® Application
Server documentation
for information about Setting up the proxy server and Configuring virtual hosts.

If you have
any related customization in 100Custom.xml files,
such as URL prefixes, they are automatically migrated to the IBM BPM
virtual host during migration. See  Security configuration properties for more information.