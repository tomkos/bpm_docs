# Configuring the Workflow Center index

```
<server>
  <search-index>            
	<artifact-index-enabled merge="replace">true</artifact-index-enabled>            
<artifact-index-update-interval merge="replace">60</artifact-index-update-interval>
  </search-index>
</server>
```

For more information about the 100custom.xml file's location and how to
create, modify, and deploy it, see The 100Custom.xml file and configuration.

## Traditional: Setting the index location

To change the
index location, log in to the administrative console and select Environment
> WebSphere Variables.