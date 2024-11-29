# WSDL and XSD cache algorithm for web service integration (deprecated)

At run time, Business Automation Workflow retrieves the
            files from the cache and parses the files before connecting with the web service server.
            Depending on how the cache is configured and the application version in which the
            integration service was developed, Business Automation Workflow determines the algorithm to
            use.

## Cache files while creating integration services

- When desktop Process Designer V8.5.6.0 was used
to develop or update the integration service.
- During the development process, the web service configuration was specified by using the
Discover Scheme step for WSDL discovery.
- The use-pre856-wsdl-cache property in the 99Local.xml or
100Custom.xml file is not set or it is set to false. The
default value is false.

## Cache the files before you call the integration service for the first time each
                time the server restarts

Business Automation Workflow caches the WSDL and XSD
files from the web service provider in the server memory before the first time the integration
service is called each time the server restarts because the use-pre856-wsdl-cache
property in the 99Local.xml or 100Custom.xml file is set
to the deprecated value true.

```
<common merge="mergeChildren">
    <webservices merge="mergeChildren">
        <use-pre856-wsdl-cache merge="replace">true</use-pre856-wsdl-cache>
    </webservices>
</common>
```

This method is the default approach for migrated process applications.

```
<common merge="mergeChildren">
      <wsdl-cache-size merge="replace">25</wsdl-cache-size>
</common>
```