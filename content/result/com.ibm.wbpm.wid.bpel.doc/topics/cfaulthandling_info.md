<!-- image -->

# Retrieval of fault data for BPEL processes

- The getCurrentFaultAsException method You can use
the getCurrentFaultAsException method in a fault handler
to retrieve data for runtime faults, BPEL standard faults, and
business faults. This mechanism is useful in combination with a catch-all
fault handler because this type of fault handler does not have an associated
variable to capture fault data, or if you are catching the runtimeFailure
fault. 
The getCurrentFaultAsException method can
be called in a Java snippet activity. The method returns the fault as an exception
object of the com.ibm.bpe.api.BpelException type. The BpelException
object provides several operations to get more information about the fault,
such as the fault name. The BpelException object wraps the exception instance.
You can therefore access the fault message and the root exception, as the
following example shows: 
com.ibm.bpe.api.BpelException bpelexception = 
getCurrentFaultAsException();
System.out.println("Fault  Name" + 
bpelexception.getFaultName())
bpelexception.printStackTrace( System.out);
Throwable rootCause = bpelexception.getRootCause()
- A typed fault variable for the fault handler or fault
link For runtime faults and BPEL standard faults, you can define a typed
fault variable for your fault handler or fault link to capture the fault data.
The fault variable must be typed by the StandardFaultType complex type.