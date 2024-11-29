# Exposed automation service events

The event types emitted for exposed automation service are described in the following table.

| Event type                                    | Event description                            | Required elements                                                                                                                                                                                                                                                                                                                                      |
|-----------------------------------------------|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| wle:REST\_EXPOSED\_AUTOMATION\_SERVICE\_ACTIVE    | An exposed automation service is active.     | The mon:model mon:type="wle: RESTExposedAutomationService" element describes the exposed automation service model that emitted the event. The <wle:operation> element identifies the operation of the exposed automation service that is invoked. The <mon:instance> identifies the instance of the exposed automation service that emitted the event. |
| wle:REST\_EXPOSED\_AUTOMATION\_SERVICE\_COMPLETED | An exposed automation service has completed. | The mon:model mon:type="wle: RESTExposedAutomationService" element describes the exposed automation service model that emitted the event. The <wle:operation> element identifies the operation of the exposed automation service that is invoked. The <mon:instance> identifies the instance of the exposed automation service that emitted the event. |
| wle:REST\_EXPOSED\_AUTOMATION\_SERVICE\_FAILED    | An exposed automation service has failed.    | In addition to the required elements described for the other  exposed automation service events, <mon:instance> contains a <mon:fault> element, which is described in Common fault elements for all FAILED events.                                                                                                                                     |

## Common fault elements for all FAILED events

- In case of a business error, for example, that is raised by an error event, the
<mon:fault> element includes a mon:name attribute which
contains the error code. The content of the <mon:fault> element contains
optional additional diagnostic information. For
example:<mon:fault mon:name="ERR\_123">The customer ID is invalid.</mon:fault>
- In case of an unexpected or system error, the mon:name attribute contains an
IBM product error message. For
example:<mon:fault mon:name="GXSD1037E: The required parameter value is missing."></mon:fault>