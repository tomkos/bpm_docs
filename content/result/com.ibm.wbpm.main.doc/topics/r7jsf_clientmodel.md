<!-- image -->

# Default converters and labels for client model objects

```
static public String getLabel(String property,Locale locale);
static public com.ibm.bpc.clientcore.converter.SimpleConverter 
       getConverter(String property);
```

The following table shows the client model objects that implement
the corresponding Business Flow Manager and Human Task Manager API classes
and provide default labels and converter for their properties. This wrapping
of the interfaces provides locale-sensitive labels and converters for a set
of properties. The following table shows the mapping of the Business Process
Choreographer interfaces to the corresponding client model objects.

| Business Process Choreographer interface    | Client model object class                                |
|---------------------------------------------|----------------------------------------------------------|
| com.ibm.bpe.api.ActivityInstanceData        | com.ibm.bpe.clientmodel.bean.ActivityInstanceBean        |
| com.ibm.bpe.api.ActivityServiceTemplateData | com.ibm.bpe.clientmodel.bean.ActivityServiceTemplateBean |
| com.ibm.bpe.api.ProcessInstanceData         | com.ibm.bpe.clientmodel.bean.ProcessInstanceBean         |
| com.ibm.bpe.api.ProcessTemplateData         | com.ibm.bpe.clientmodel.bean.ProcessTemplateBean         |
| com.ibm.task.api.Escalation                 | com.ibm.task.clientmodel.bean.EscalationBean             |
| com.ibm.task.api.Task                       | com.ibm.task.clientmodel.bean.TaskInstanceBean           |
| com.ibm.task.api.TaskTemplate               | com.ibm.task.clientmodel.bean.TaskTemplateBean           |