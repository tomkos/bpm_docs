<!-- image -->

# Example scenario

A fictitious car insurance comparison web site provides quotes to customers from 3 different car
insurance providers. Each car insurance provider service has a different security configuration.

The comparison web site must audit the body of the message before it is forwarded on to the
relevant service providers. The static service gateway is used because, only a section of the
message is audited. Since each service provider has a different security configuration, a different
SCA import is needed for each service provider, which is provided using the static service gateway
pattern.