<!-- image -->

# Mediation flow components

- One or more interfaces that describe how to invoke this mediation
flow. These interfaces have to match those of the exports that will
be wired to this mediation flow.Note: The business objects specified
in the data section of the interfaces must have a non-null namespace.
If you use a null namespace you may encounter this type of error at
run time. [16/05/12 13:39:36:516 EDT] 00000066 WSDLMessageEC E   CWSXM2007E:      
Error: multiple type or message definitions for                         
{http://Stockquote/GetQuote}SearchBy
CustomerIDMsg                                                
If you print the service message object to the log, you
can see the context and headers but the body is empty.
- Zero or more named references that specify the interfaces of partners
that this flow wants to invoke. The actual partners are not known
by the flow, only their interfaces. These references are wired to
actual partners, that are imports or Java™ components,
with matching interfaces.
- Mediation flows, which define the implementation of the component.