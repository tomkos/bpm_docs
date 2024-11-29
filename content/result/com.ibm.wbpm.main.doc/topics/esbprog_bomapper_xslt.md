<!-- image -->

# Business Object Map and Mapping
 mediation primitives

1. Mapping (previously named XSL Transformation or XSLT)
 mediation primitive
2. Business Object Mapper (BO Mapper) mediation primitive

Figure 1. Hover pane showing the source and target XML message type

<!-- image -->

Both the Mapping
 and the BO Mapper mediation primitives transform the SMO. The
difference is that the Mapping
 mediation primitive changes message body content according to
an XSL style sheet or a Business Object Map (BO Map). The BO Mapper
mediation primitive changes the message body content, according to a BO Map which is created in the
Integration Designer. Both of these mediation primitives allow services that use different business
objects to communicate and exchange data.

Within the Integration Designer tools, the Mapping Editor makes populating a target XML
document with data from a source XML document a visual task. The Mapping Editor is used by both the
Mapping
 and BO Mapper mediation primitives. The source message
structure for the interface and the target message structure for the interface are within the
Mapping Editor. By drawing connections between the source and target fields, you create mappings
between the source and target elements and attributes.

Within a transformation of the entire SMO, you can store data outside of the message body, for
retrieval by downstream primitives. For example, the context of the SMO can be used to store or
retrieve data from either the transient context if it is required in the same flow (request or
response) or the correlation context if it is needed in both request and response flows.

- Comparison between the Mapping and BO Mapper mediation primitives

There is some overlap between the capabilities of the BO Mapper and the Mapping (previously called the XSL Transformation) mediation primitives. The following table summarizes the different capabilities of each.
- Example scenarios

In this scenario, a fictitious company, Personal Holidays have a holiday booking system.