<!-- image -->

# Creating a client application for BPEL processes and human
tasks (Java web services)

## Before you begin

## About this task

- HTTP transport layer
- JMS transport layer

## Procedure

1. Create a new client application project.
2. Generate the web service proxy.
3. Code your client application.
4. Build the project.
5. Run the client application.

## Examples for the HTTP and JMS transport layers

The
following examples show how to use the Business Flow Manager web service
API for the supported transport layers. The examples differ in how
the web service proxy is
generated.

```
try {
    // create bfm proxy
    BFMJAXWSPortType bfm = new BFMJAXWSService().getBFMJAXWSPort();

    // call getProcessTemplate
    ProcessTemplateType ptt = 
      bfm.getProcessTemplate("MY\_PROCESS\_TEMPLATE\_NAME");

    // handle return value
    System.out.println("Process template '" + ptt.getName() + 
        "' found, details following:");
    System.out.println("Execution mode: " + 
        ptt.getExecutionMode());
    System.out.println("Schema version: " + 
        ptt.getSchemaVersion());
  } catch (Exception e) {
    if ( e instanceof ProcessFaultMsg )
    {
      ProcessFaultMsg pfm = (ProcessFaultMsg) e;
      List<FaultStackType> list = 
          ( pfm.getFaultInfo() ).getFaultStack();
      FaultStackType fault = list.get( 0 );
      System.out.println( "ProcessFaultMessage: " + 
          fault.getMessage() );
    }
    else
    {
      e.printStackTrace( System.out );
    }  
  }
```

```
try {
    // create bfm proxy
    BFMJAXWSPortType bfm = new BFMJMSService().getBFMJMSPort();

    // call getProcessTemplate
    ProcessTemplateType ptt = 
      bfm.getProcessTemplate("MY\_PROCESS\_TEMPLATE\_NAME");

    // handle return value
    System.out.println("Process template '" + ptt.getName() + 
        "' found, details following:");
    System.out.println("Execution mode: " + 
        ptt.getExecutionMode());
    System.out.println("Schema version: " + 
        ptt.getSchemaVersion());
  } catch (Exception e) {
    if ( e instanceof ProcessFaultMsg )
    {
      ProcessFaultMsg pfm = (ProcessFaultMsg) e;
      List<FaultStackType> list = 
          ( pfm.getFaultInfo() ).getFaultStack();
      FaultStackType fault = list.get( 0 );
      System.out.println( "ProcessFaultMessage: " + 
          fault.getMessage() );
    }
    else
    {
      e.printStackTrace( System.out );
    }  
  }
```