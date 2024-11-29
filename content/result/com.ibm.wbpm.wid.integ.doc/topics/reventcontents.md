<!-- image -->

# Content of the Event Emitter primitive's event

## Event Emitter properties displayed in a generated
event definition

- The label property of the primitive becomes the name of the generated
event
- The mediation module name is the ModuleName of extendedDataElement
- The primitive name is the MediationName of extendedDataElement
- The primitive's root property, for example /body, is in the Root
of extendedDataElemetn
- The value of the elements in the message is contained in the Message
of extendedData

<!-- image -->

## When no message data is included in the event

| Event Emitter property       | Event Emitter property value            | Common base event element                               | Common base event element value   |
|------------------------------|-----------------------------------------|---------------------------------------------------------|-----------------------------------|
| label                        | OrderReceived                           | extensionName or event/eventPointData/EventEmitterLabel | OrderReceived                     |
| Mediation module name        | ReceiveOrderMediationModule             | event/eventPointData/ModuleName                         | ReceiveOrderMediationModule       |
| Event Emitter primitive name | OrderReceivedEvent                      | event/eventPointData/MediationName                      | OrderReceivedEvent                |
| Root                         | exclude message content from event data | none                                                    | none                              |

## When a single root element is included in the event

| Event Emitter primitive property   | Event Emitter property value         | Common base event element                               | Common base event element value      |
|------------------------------------|--------------------------------------|---------------------------------------------------------|--------------------------------------|
| label                              | OrderReceived                        | extensionName or event/eventPointData/EventEmitterLabel | OrderReceived                        |
| Mediation module name              | ReceiveOrderMediationModule          | event/eventPointData/ModuleName                         | ReceiveOrderMediationModule          |
| Event Emitter primitive name       | OrderReceivedEvent                   | event/eventPointData/MediationName                      | OrderReceivedEvent                   |
| Root                               | /body/getOrderInfo/argAccount/region | event/eventPointData/Root                               | /body/getOrderInfo/argAccount/region |
|                                    |                                      | event/applicationData/content/value                     | Asia Pacific                         |

## When a complex root element is included in the event

| Event Emitter primitive property   | Event Emitter property value   | Common base event element                               | Common base event element value   |
|------------------------------------|--------------------------------|---------------------------------------------------------|-----------------------------------|
| label                              | OrderReceived                  | extensionName or event/eventPointData/EventEmitterLabel | OrderReceived                     |
| Mediation module name              | ReceiveOrderMediationModule    | extendedDataElement/MediationName                       | ReceiveOrderMediationModule       |
| Event Emitter primitive name       | OrderReceivedEvent             | event/eventPointData/MediationName                      | OrderReceivedEvent                |
| Root                               | /body/getOrderInfo/argAccount  | event/eventPointData/Root                               | /body/getOrderInfo/argAccount/    |
|                                    |                                | event/applicationData/content/value/accountID           | 049728                            |
|                                    |                                | event/applicationData/content/value/region              | Asia Pacific                      |
|                                    |                                | event/applicationData/content/value/termsDescription    | 90 days                           |
|                                    |                                | event/applicationData/content/value/companyName         | Favourite Customer                |
|                                    |                                | event/applicationData/content/value/creditLimit         | 50000                             |