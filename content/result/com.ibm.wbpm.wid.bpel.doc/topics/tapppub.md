<!-- image -->

# Dealing with application publication errors

## About this task

```
Process myBPEL of application myModApp is not stopped. Stop the templates 
manually before updating or uninstalling a process application.
```

When IBM® Integration
Designer installs the WebSphere® Test Environment, it configures the server to run under development
mode, meaning that the process engine will tolerate changes to
running templates.

If you are publishing to any other server,
you simply need to configure the server with this same attribute by
following these steps:

## Procedure

1. Start the server.
2. Launch the administrative console.
3. Navigate to the application server panel and select the development mode check box.