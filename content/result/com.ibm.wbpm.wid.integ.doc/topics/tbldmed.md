<!-- image -->

# Building mediation flows

- Mediation flows overview

Mediation flows intercept and modify messages that are passed between existing services (providers) and clients (requesters) that want to use those services. They are most commonly used for transforming data and accessing header information, such as JMS, MQ or SOAP headers.
- Creating a mediation flow

A mediation flow consists of a sequence of processing steps that are run by mediation primitives when an input message is received. Mediation flows be contained in modules or in mediation modules.
- Type propagation in mediation flows

Messages in mediation flows are represented as service message objects (SMOs). Service message objects are enhanced business objects that include the business objects which contain the application data or payload, in addition to header and contextual information. When mediation primitives are wired together in a flow, the message is propagated from one primitive to the next. The input and output terminals of mediation primitives in a flow are configured to accept messages of a certain type, based on the validation rules of the mediation flow editor.
- Reusing mediation logic

You can reuse mediation logic for common tasks by creating mediation subflows. A subflow can be reused by mediation flows in the same module. If a subflow is placed in a library, it can be reused by mediation flows in multiple modules.
- Transforming messages

When you are integrating services, you almost always need to transform the data into a format that the receiving service can process. In mediation flows, you can use different mediation primitives to transform message formats.
- Storing and using elements in the message context

Store an element in the message context so that it is available for use later in the mediation flow. First, add the element as an empty business object in the message context. Then, initialize it by using a mediation primitive such as Message Element Setter to add a value to the business object field.
- Invoking a service

Invoking refers to the ability to call an operation of a referenced service in the mediation flow. This can be done either at the end of a request flow using a Callout primitive or inline using the Service Invoke primitive.
- Aggregating and broadcasting messages

When you aggregate messages, you combine a number of response messages from the invocation of one or more services into a single message. When you broadcast messages you send notification to the service and do not expect a response.
- Selecting endpoints dynamically

You can configure your mediation flow component to route messages to endpoints that are determined dynamically at run time. Since these service endpoints are not statically defined in the mediation flow, you can change service endpoints without the need to update and redeploy the mediation flow.
- Logging messages during a mediation flow

You can use the Message Logger mediation primitive to store messages that you can process later. The logged messages can be used for various purposes. For example, you could use the logged messages for data mining or for auditing.
- Emitting common base events

You can emit a common base event at a significant point in a mediation flow by using an Event Emitter mediation primitive. You can also define the parts of the message that should be contained in the event. Common base events are emitted to the CEI server which can be accessed by many different applications that consume the events.
- Implementing custom mediation logic

Custom mediation primitives allow you to implement your own mediation logic by using Java™ code.
- Changing the value of mediation flow properties at run time

When you develop a mediation flow, you can identify promoted properties, which are properties whose value the administrator can change at run time; without restarting the server or redeploying the mediation module.
- Working with Microsoft ADO.NET services

ADO.Net clients and servers use diffgrams in their schemas to transfer and update data. Diffgrams are not compatible with the W3C XML 1.0 schema that IBM Integration Designer requires. Learn how to use mediation flows to create, manipulate and consume  .NET messages that contain diffgrams, with no changes required to the original service WSDL.
- Changing the format of mediation flows

You can save your mediation flows in an XML format that is easy to read, thus simplifying team development and compare and merge of the mediation flows. By default, new mediation flows are saved in the XML format.
- Optimizing a mediation flow for team development

If a team of developers want to work concurrently on a mediation flow component, you can choose to save the mediation flow as multiple files to make synchronizing changes easier. A file is generated for each operation that has a flow. If each developer is assigned to implement a distinct set of operations, then each developer is only responsible for synchronizing his own files. Chances of conflicting changes are reduced, and developers can easily synchronize their work daily.
- Error handling in the mediation flow

This topic provides information on various ways to deal with errors in the mediation flow, including ways to use the Stop and Fail mediation primitives, where to look for fail information in the message, and how to handle WSDL faults.
- Contributing your own mediation primitive plug-in

You can develop your own mediation primitives, and contribute them to the Mediation Flow editor palette. Integration developers can then use these mediation primitives in the same way that you use the supplied mediation primitives, for example Message Filter.
- Mediation primitive property group schema definition

The property group schema definition. Use this schema when you are creating your own custom mediation primitives and contributing them to the mediation flow editor. The properties of your mediation primitives must conform to the schema defined here.
- Mediation primitives and nodes

Mediation primitives accept and process messages to let you change their format, content or the target service provider. Mediation primitives have properties that determine how a message will be processed. When you wire a flow in the Mediation Flow editor, you can modify the properties of nodes and mediation primitives.
- Deleting primitives that use XSLT and Business object maps

If you choose to delete a Mapping primitive or a Business object map primitives in the mediation flow editor and the selected primitive is referenced by any mapping artifacts, a Confirm Delete window will enable you to delete the primitive as well as any directly associated mapping artifacts.