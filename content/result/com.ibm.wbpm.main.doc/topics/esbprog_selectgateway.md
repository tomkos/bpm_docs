<!-- image -->

# Selecting service gateway patterns

- Web service based service gateway - If a web service only service gateway is required,
then use the proxy gateway pattern. A proxy gateway provides built-in routing capabilities and
client side WSDL resolution. The other patterns, such as the dynamic service gateway, will need
extensive user code to provide similar functionality.
- Messaging or HTTP based service gateway with XML data encoding  - If the encoding style
of the messaging and HTTP service gateways is XML serialization of business objects, then use the
dynamic service gateway. IBM® Workflow
Server provides an option to automatically
parse incoming messages to the gateway. Therefore, access to the body of the message can be achieved
using the dynamic service gateway pattern.
- Messaging or HTTP based service gateway with non-XML data encoding - If access to the
body of the message is not required, use the dynamic service gateway. If access to the body of the
message is required, use the static service gateway.
- Protocol switching service gateway with XML data encoding - When a multi-protocol service
gateway is required and message encoding on all protocols is XML serialization of business objects,
use the dynamic service gateway. Workflow Server provides an option to automatically
parse incoming messages to the gateway. Therefore if access to the body of the message is required,
use the static service gateway.
- Protocol switching service gateway with non-XML data encoding  - If access to the body of
the message is not required, use the dynamic service gateway. If access to the body of the message
is required, use the static service gateway.