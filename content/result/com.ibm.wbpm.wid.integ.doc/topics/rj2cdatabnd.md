<!-- image -->

# J2C data bindings

```
public interface RecordDataBinding extends DataBinding, javax.resource.cci.Record {

}
```

If the data binding is to be used with the Java
EE Connector Architecture (J2C)-based service, it has to implement
this interface. As a record, it can be passed to the resource adapter
interaction's execute method with input and output.

If
the resource adapter supports the javax.resource.cci.Streamable interface,
as its view of the record argument passed to the execute method, the commonj.connector.runtime.StreamableDataBinding interface
presented below can be used.

```
public interface StreamableDataBinding extends RecordDataBinding, Streamable {

}
```

When this data binding is passed to the resource adapter's
execute method, it may use the Streamable interface
directly, if implemented, without going through the data object.

```
public CustomerDataObject getCustomer(CustomerDataObject customer){

		ConnectionFactory connectionFactory = getConnectionFactory();

		// Create and configure InteractionSpec
		InteractionSpec interactionSpec = new EISInteractionSpec();
		interactionSpec.setProperty1(…);
		interactionSpec.setProperty2(…);
	
		// Create instance of the Interaction
		Connection connection = connectionFactory.getConnection();
		Interaction interaction = connection.createInteraction();
		
		// Instantiate data bindings
		RecordDataBinding inputBinding = new CustomerBindingImpl();
		RecordDataBinding outputBinding = new CustomerBindingImpl();
			
		// Set service argument on the input data binding
		inputBinding.setDataObject(customer);
		
		if(supportsInputOutputExecute)		
interaction.execute(interactionSpec,inputBinding,outputBinding);
		
		return (CustomerDataObject)outputBinding.getDataObject();

	}
```

The previous RecordDataBinding interface
is not sufficient if the resource adapter supports the input only
variant of the execute method on the interaction. This is because
the execute method with only the input record argument returns the
'native' result as a Common Client Interface (CCI) record. This
record needs to be set on the data binding and then the converted
data object can be retrieved.

The required functionality is
provided by the commonj.connector.runtime.RecordHolderDataBinding interface
shown below.

```
public interface RecordHolderDataBinding extends DataBinding {
	
	public javax.resource.cci.Record getRecord() throws DataBindingException;
	public void setRecord(javax.resource.cci.Record aRecord) 
			throws DataBindingException;
}
```

If the Resource Adapter supports the input only variant
of the execute method, the Data Binding provider needs to implement
the previous interface.

```
public CustomerDataObject getCustomer(CustomerDataObject customer){

		ConnectionFactory connectionFactory = getConnectionFactory();

		// Create and configure InteractionSpec
		InteractionSpec interactionSpec = new EISInteractionSpec();
		interactionSpec.setProperty1(…);
		interactionSpec.setProperty2(…);
	
		// Create instance of the Interaction
		Connection connection = connectionFactory.getConnection();
		Interaction interaction = connection.createInteraction();
		
		// Instantiate data bindings
		RecordDataBinding inputBinding = new CustomerBindingImpl();
		RecordDataBinding outputBinding = new CustomerBindingImpl();
			
		// Set service argument on the input data binding
		inputBinding.setDataObject(customer);
		
		Record result = 	interaction.execute(interactionSpec,inputBinding);
      outputBinding.setRecord(result);
		
		return (CustomerDataObject)outputBinding.getDataObject();

	}
```

The second instance when the RecordHolderDataBinding interface
must be implemented is for the inbound J2C communication. The listener
interface is invoked by the resource adapter and the Message Driven
Bean (MDB) implementing it is passed the 'native' data. This
data needs to be set on the data binding to be able to retrieve from
its business object.  If the listener argument and return are typed
as javax.resource.cci.Record, the RecordHolderDataBinding is
sufficient. If the listener argument(s) or return type is other than
a CCI record, the following utility commonj.connector.runtime.InboundNativeDataRecord interface
is provided.

```
public interface InboundNativeDataRecord extends Record {

	public Object[] getNativeData();
	public void setNativeData(Object[] data);
}
```

An arbitrary number and types of arguments to the listener
can be set on this interface, as the object array. The implementation,
a CCI record, can then be set on the RecordHolderDataBinding interface
thus passing all the listener arguments and allowing the data binding
to retrieve arguments and create the business object. On the return,
the data binding implementation sets the return value in the symmetric
manner. The runtime then uses a get method, also returning an object
array.  The argument at index 0 is the return value to be returned
to the invoker (resource adapter).

## Related concepts

- Pattern of accessing external services with adapters
- Developing services with adapters
- Simple adapter wizard
- Migrating applications using previous adapter levels

## Related tasks

- Configuring and using adapters
- Creating a business object from a source file

## Related reference

- A closer look at business objects from data structures
- J2C imports and exports at run time
- Trade-offs when developing adapter imports and exports
- Considerations when using adapters
- Considerations when refactoring
- Contributing your own external service or data wizard plug-in
- Limitations for adapter imports and exports