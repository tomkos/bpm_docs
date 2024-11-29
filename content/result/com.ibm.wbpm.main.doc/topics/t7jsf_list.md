<!-- image -->

# Adding the List component to a JSF application

## Procedure

1. Add the List component to the JavaServer Pages
(JSP) file. Add the bpe:list tag to the h:form tag.
The bpe:list tag must include a model attribute. Add bpe:column tags
to the bpe:list tag to add the properties of the objects
that are to appear in each of the rows in the list.
The
following example shows how to add a List component to
display task instances.
<h:form>

   <bpe:list model="#{TaskPool}">
      <bpe:column name="name" action="taskInstanceDetails" />
      <bpe:column name="state" />
      <bpe:column name="kind" />
      <bpe:column name="owner" />
      <bpe:column name="originator" />
   </bpe:list>

</h:form>The model attribute refers to a managed bean, TaskPool.
The managed bean provides the list of Java™ objects over which the list iterates
and then displays in individual rows.
2. Configure the managed bean referred to in the bpe:list tag.
For the List component, this managed bean must
be an instance of the com.ibm.bpe.jsf.handler.BPCListHandler class.

The following example shows how to add the TaskPool managed bean
to the configuration file.
<managed-bean>
<managed-bean-name>TaskPool</managed-bean-name>
<managed-bean-class>com.ibm.bpe.jsf.handler.BPCListHandler</managed-bean-class>
<managed-bean-scope>session</managed-bean-scope>
   <managed-property>
      <property-name>query</property-name>
      <value>#{TaskPoolQuery}</value>
   </managed-property>
   <managed-property>
      <property-name>type</property-name>
      <value>com.ibm.task.clientmodel.bean.TaskInstanceBean</value>
   </managed-property>
</managed-bean>

<managed-bean>
<managed-bean-name>TaskPoolQuery</managed-bean-name>
<managed-bean-class>sample.TaskPoolQuery</managed-bean-class>
<managed-bean-scope>session</managed-bean-scope>
   <managed-property> 
     <property-name>type</property-name>
     <value>com.ibm.task.clientmodel.bean.TaskInstanceBean</value>
   </managed-property>
</managed-bean>

<managed-bean>
<managed-bean-name>htmConnection</managed-bean-name>
<managed-bean-class>com.ibm.task.clientmodel.HTMConnection</managed-bean-class>
<managed-bean-scope>application</managed-bean-scope>
   <managed-property>
      <property-name>jndiName</property-name>
      <value>java:comp/env/ejb/LocalHumanTaskManagerEJB</value>
   </managed-property>
</managed-bean>
The example shows that TaskPool has two configurable properties: query and type.
The value of the query property refers to another managed bean, TaskPoolQuery.
The value of the type property specifies the bean class, the properties of
which are shown in the columns of the displayed list. The associated query
instance can also have a property type. If a property type is specified, it
must be the same as the type specified for the list handler.  
You can
add any type of query logic to the JSF application as long as the result of
the query can be represented as list of strongly-typed beans. For example,
the TaskPoolQuery is implemented using a list of com.ibm.task.clientmodel.bean.TaskInstanceBean objects.
3. Add the custom code for the managed bean that is referred to by
the list handler. The following example shows how to add
custom code for the TaskPool managed bean.
public class TaskPoolQuery implements Query {

  public List execute throws ClientException {

    // Examine the faces-config file for a managed bean "htmConnection". 
    //
    FacesContext ctx = FacesContext.getCurrentInstance();
    Application  app = ctx.getApplication();
    ValueBinding htmVb = app.createValueBinding("#{htmConnection}");
    htmConnection = (HTMConnection) htmVb.getValue(ctx);  
    HumanTaskManagerService taskService = 
         htmConnection.getHumanTaskManagerService();

    // Then call the actual query method on the Human Task Manager service.
    //
    // Add the database columns for all of the properties you want to show 
    // in your list to the select statement
    //
    QueryResultSet queryResult = taskService.query(
    	"DISTINCT TASK.TKIID, TASK.NAME, TASK.KIND, TASK.STATE, TASK.TYPE,"
      + "TASK.STARTER, TASK.OWNER, TASK.STARTED, TASK.ACTIVATED, TASK.DUE, 
         TASK.EXPIRES, TASK.PRIORITY",
      "TASK.KIND IN(101,102,105) AND TASK.STATE IN(2) 
        AND WORK\_ITEM.REASON IN (1)",
      (String)null,
      (Integer)null, 
      (TimeZone)null);
    List applicationObjects = transformToTaskList ( queryResult );
    return applicationObjects ;
  }

  private List transformToTaskList(QueryResultSet result) {

ArrayList array = null;
int entries = result.size();
array = new ArrayList( entries );

// Transforms each row in the QueryResultSet to a task instance beans.
	for (int i = 0; i < entries; i++) {
	  result.next();
	  array.add( new TaskInstanceBean( result, connection ));
	}
	return array ;
  }
}

The TaskPoolQuery bean queries the properties of the Java objects.
This bean must implement the com.ibm.bpc.clientcore.Query interface.
When the list handler refreshes its contents, it calls the execute method
of the query. The call returns a list of Java objects. The getType method
must return the class name of the returned Java objects.

## Results

- How lists are processed

Every instance of the List component is associated with an instance of the com.ibm.bpe.jsf.handler.BPCListHandler class.
- User-specific time zone information

The JavaServer Faces (JSF) components provide a utility for handling user-specific time zone information in the List component.
- Error handling in the List component

When you use the List component to display lists in your JSF application, you can take advantage of the error handling functions provided by the com.ibm.bpe.jsf.handler.BPCListHandler class.
- List component: Tag definitions

The Business Process Choreographer Explorer List component displays a list of objects in a table, for example, tasks, activities, process instances, process templates, work items, and escalations.