<!-- image -->

# Retry

- Retry On , determines whether, and how, fault responses cause a retry. The followingvalues are valid: Modelled faults are those that are explicitly listed in a WSDL file, any other fault is anunmodeled fault. This property is only applicable to request-response operations.
    - Never - operation call is never retried, no matter the type of fault
    - Any fault - operation call is retried on both modelled and unmodeled faults
    - Modelled fault - operation call is retried only when a modelled fault is received
    - Unmodeled fault - operation call is retried only when an unmodeled fault is received
- Retry Count, determines how many times a service call should be retried before an output
terminal is fired. The output terminal that is fired can be of the following types: modelled fault,
timeout or fail. If Try Alternate Endpoints is false or if there are no alternate
endpoints specified in the SMO headers, all attempts will retry the original service.
- Retry Delay is the number of seconds to wait between retry attempts. If it is equal to 0,
there will be no delay between retry attempts meaning they will run as fast as the server can
process them.
- Try Alternate Endpoints. If the SMO Header contains alternate endpoints, retry calls will
be made to them in the order they appear. Use Dynamic Endpoint must also be set for
this function to be available.
- Async Timeout specifies the time to wait for responses when performing an asynchronous
with deferred response invocation. If this timeout occurs and the Retry Count has
not been reached, it is treated as an unmodeled fault and retry will be performed. The retry delay
will take place following the Async Timeout. If the Retry Count has been reached,
then the Timeout terminal of the Service Invoke primitive, or the fail terminal of the Callout
Response node is fired.