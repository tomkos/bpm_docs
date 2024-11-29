<!-- image -->

# Binding-specific headers in a Service Message Object (SMO)

The sections below list all the header
information that is in the system today for each protocol. The highlighted
sections indicate the sections that are common and should be available
to the data handler in a generic manner.

- JMS header
- MQ header
- HTTP header
- EIS headers in a Service Message Object (SMO)
- EIS Email header
- EIS FTP header
- EIS Flat File header

## JMS header

The JMS user properties
will be added to the properties section shown below.

<!-- image -->

## MQ header

The MQ rfh2 user folder
will be added to the properties section.

<!-- image -->

Folder
is equal to the usr folder in the diagram.

## HTTP header

The HTTP custom
headers will be added to the properties section in the SMO header.

<!-- image -->

## EIS headers in a Service Message Object
(SMO)

The data object that will be set in the EISConnectionSpec
and EISInterationSpec classes at run time for the Email, FTP and Flat
File adapters is shown below.

The data structure
is as follows:

```
EISHeader EISHeaderType
	EISConnectionSpec anyType
	EISInteractionSpec anyType
```

## EIS Flat File header

The
ConnectionSpec properties are not required. The InteractionSpec properties
for inbound and outbound processing are shown.

<!-- image -->

## EIS Email header

The ConnectionSpec
properties are userid and password. The InteractionSpec properties
for inbound and outbound processing are shown.

<!-- image -->

## EIS FTP header

The ConnectionSpec
properties are userid and password. The InteractionSpec properties
for inbound and outbound processing are shown.

<!-- image -->