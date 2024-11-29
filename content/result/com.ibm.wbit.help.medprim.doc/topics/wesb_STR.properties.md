# Synchronous Transformation Rollback mediation primitive properties

## Sample XML code

```
<node name="SynchronousTransactionRollback1" type="SynchronousTransactionRollback">
  <inputTerminal/>
	<outputTerminal>
		<wire targetNode="Fail1"/>
	</outputTerminal>
	<failTerminal/>
</node>
```