# Enforcing the scope of private variables when using the executeServiceByName
JavaScript         API

## About this task

```
VariableDoesNotExistException: CWTBG0543E: The variable variableName does not exist.
```

## Procedure

1. Stop the server for Workflow Server      
              or Workflow Center.
2. Locate each 100Custom.xml file in
your topology. For more information about the location
of the 100Custom.xml file that must be updated,
see the topic Location of 100Custom configuration files.
3. Add the following code to the file: 
<server>
    <service-engine>            
        <enforce-private-variable-scope merge="replace">true</enforce-private-variable-scope>
    </service-engine>
</server>
4. Save your changes to each 100Custom.xml file.
5. Start the server for Workflow Server or Workflow Center.