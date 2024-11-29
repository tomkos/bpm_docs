# Starting a new process

## Parameters

```
var inputs = new tw.object.Map();
inputs.put("parm1", "parm1 value");
inputs.put("parm2", "parm2 value");
tw.system.startProcessByName("StartProcess2", inputs);
```

## Thread hung exceptions

- You have defined an undercover agent (UCA) message event with
an attached service.
- In the attached service you are starting a new process instance
using the tw.system.startProcessByName() function.
- The process you are starting has variables defined that are exposed
to Business Data Search, and the process creation hangs.

The recommended solution is to use the BPMN (Business
Process Model and Notation) best practice, and model the process with
a start message event. The UCA message event will then be attached
to this start message event.