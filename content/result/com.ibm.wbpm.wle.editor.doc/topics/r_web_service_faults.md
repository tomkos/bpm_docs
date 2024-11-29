# Web service faults

To catch and handle faults, attach an error intermediate
event to the web service integration. By default, configure the error
intermediate event with the Catch All Errors option
to catch faults which are modeled in WSDL, as well as other faults
such as system or connectivity exceptions. For more information on
handling faults, see Handling
errors in services.

Figure 1. An outbound web service
integration with attached error intermediate event

<!-- image -->

If you want to catch specific WSDL faults (those that match
a particular fault name or fault type), use the Catch Specific
Errors option in the error intermediate event.

- Specify a value for the name that begins with either an alphabetical
character or the underscore (\_) character.
Valid values can include alphabetical characters, numbers, and the
underscore. Names cannot contain words that are used within IBM Business
Process Manager (for example, arrayOf or listOf).
- When defining wsdl:part entries for the fault, use the element attribute
in order to comply with the WS-I Basic Profile specification.

<!-- image -->

```
<wsdl:operation name="multiCFault">
	    <wsdl:input message="tns:multiCFaultRequestMsg" name="multiCFaultRequest"/>
    <wsdl:output message="tns:multiCFaultResponseMsg" name="multiCFaultResponse"/>
    <wsdl:fault message="tns:multiCFault\_multiCFaultFault1Msg" name="multiCFaultFault1"/>
    <wsdl:fault message="tns:multiCFault\_multiCFaultFault2Msg" name="multiCFaultFault2"/>
</wsdl:operation>
```

After the web service integration
discovers the WSDL file and generates the types (the input and output
variables needed for the service), the specified faults can be caught
when the web service runs.