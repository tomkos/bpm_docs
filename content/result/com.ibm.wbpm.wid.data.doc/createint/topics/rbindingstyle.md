<!-- image -->

# Binding style

There are several binding styles, however, they are divided into two categories. Document style,
which sends the entire XML document in a message, and Remote Procedure Call (RPC), which sends part
of a message. These categories are themselves divided into subcategories, which are explained in
detail in Which WSDL style should I use?. There are tradeoffs to each one. The default
selection in the interface editor, document literal wrapped, is sufficient for most uses. However,
if you are using an attachment in a business object, document literal non-wrapped must be used.

If you bring an interface into the
interface editor and another binding style has been used then the
editor will leave the binding style as it is. This feature is known
as toleration. The following binding styles are supported by
the interface editor:

| Binding style                                        | Interface editor support                  |
|------------------------------------------------------|-------------------------------------------|
| Document literal wrapped                             | Default                                   |
| Document literal non-wrapped (used with attachments) | Can be selected from the interface editor |
| Remote Procedure Call (RPC)                          | Tolerated if WSDL has been imported       |
| Unknown                                              | Tolerated if WSDL has been imported       |