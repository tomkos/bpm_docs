<!-- image -->

# Input Response

<!-- image -->

You can set
properties for the Input Response node in the Details tab of the Properties
view.

## Properties

| Property                                          | Description                                                                                                                                            | Possible Values                                                                                                                                                                                                   |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Use dynamic endpoint if set in the message header | Determines if the address contained in the SMOHeader should be used to override the address contained in the WS-Addressing ReplyTo header, if present. | If set to True, and if the SMOHeader contains a Target address, and if the WS-Addressing ReplyTo header is present, the response message is redirected to the address contained in the SMOHeader. 	Default: false |