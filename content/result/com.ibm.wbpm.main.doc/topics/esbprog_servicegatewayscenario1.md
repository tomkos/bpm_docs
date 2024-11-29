<!-- image -->

# Example scenario

- Flight booking - MQ binding
- Seat reservation - JMS binding
- Flight schedule - HTTP binding
- Food selection- web services binding

The airline company have a requirement that all messages must be audited in a single unit before
the message reaches the service provider. In the future the airline company want to be able to
associate new services without redeploying the gateway. The dynamic service gateway is used because
it has a multi protocol requirement.