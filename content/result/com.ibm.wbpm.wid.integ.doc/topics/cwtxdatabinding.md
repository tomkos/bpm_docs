<!-- image -->

# WTX data handler

The WTX data handler can be used in JMS, generic JMS, MQ-JMS, MQ
and HTTP exports and imports.

The WTX map selection data handler can be used in an EIS context
for FlatFile, FTP and Email imports and exports.

WTX is used in a disconnected pattern. It does not connect to the
client (JMS queues, for example) directly to get the incoming message
or send the outgoing message. The incoming message is sent to an export/import
which then hands off the data to the WTX data handler
which converts the data by calling WTX and then hands it back to the
export/import.

- WTX data handler concepts

Several WTX concepts should be known to you.
- Designing the WTX map and related artifacts

Understanding the relationship between the complex type and its corresponding element is important.
- Configuring the WTX map selection data handler

Configuring the WTX map selection data handler with the binding configuration resource wizard is shown.
- Configuring the WTX map selection data handler properties

The properties for the WTX map selection data handler need to be set.
- Deploying the WTX map

Deploying the WTX map requires an understanding of the WTX directory in the module.