<!-- image -->

# Adding the Details component to a JSF application

## Procedure

1. Add the Details component to the JavaServer
Pages (JSP) file. Add the bpe:details tag
to the <h:form> tag. The bpe:details tag
must contain a model attribute. You can add properties
to the Details component with the bpe:property tag. 

The following example shows how to add a Details component
to display some of the properties for a task instance.
<h:form>

   <bpe:details model="#{TaskInstanceDetails}">
      <bpe:property name="displayName" />
      <bpe:property name="owner" />
      <bpe:property name="kind" />
      <bpe:property name="state" />
      <bpe:property name="escalated" />
      <bpe:property name="suspended" />
      <bpe:property name="originator" />
      <bpe:property name="activationTime" />
      <bpe:property name="expirationTime" />
   </bpe:details>

</h:form>The model attribute refers
to a managed bean, TaskInstanceDetails. The bean provides
the properties of the Java™ object.
2. Configure the managed bean referred to in the bpe:details tag.
For the Details component, this managed bean must
be an instance of the com.ibm.bpe.jsf.handler.BPCDetailsHandler class.
This handler class wraps a Java object and exposes its public properties
to the details component.
The following example shows
how to add the TaskInstanceDetails managed bean to the
configuration file.
<managed-bean>
   <managed-bean-name>TaskInstanceDetails</managed-bean-name>
   <managed-bean-class>com.ibm.bpe.jsf.handler.BPCDetailsHandler</managed-bean-class>
   <managed-bean-scope>session</managed-bean-scope>
   <managed-property>
      <property-name>type</property-name>
      <value>com.ibm.task.clientmodel.bean.TaskInstanceBean</value>
   </managed-property>
</managed-bean>The example shows that the TaskInstanceDetails bean
has a configurable type property. The value of the type property
specifies the bean class (com.ibm.task.clientmodel.bean.TaskInstanceBean),
the properties of which are shown in the rows of the displayed details. The
bean class can be any JavaBeans class. If the bean provides
default converter and property labels, the converter and the label are used
for the rendering in the same way as for the List component.

## Results

- Details component: Tag definitions

The Business Process Choreographer Explorer Details component displays the properties of tasks, work items, activities, process instances, and process templates.