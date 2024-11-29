# MTOM attachments: top-level message parts

By sending or receiving a referenced attachment in a SOAP message,
the binary data that makes up the attachment (which is often quite
large) is held separately from the SOAP message body so that it does
not need to be parsed as XML. This results in more efficient processing
than if the binary data were held within an XML element.

```
… other transport headers ... 
Content-Type: multipart/related; boundary=MIMEBoundaryurn\_uuid\_0FE43E4D025F0BF3DC11582467646812; 
type="application/xop+xml"; start="
<0.urn:uuid:0FE43E4D025F0BF3DC11582467646813@apache.org>"; start-info="text/xml"; charset=UTF-8

--MIMEBoundaryurn\_uuid\_0FE43E4D025F0BF3DC11582467646812
content-type: application/xop+xml; charset=UTF-8; type="text/xml";
content-transfer-encoding: binary
content-id: 
   <0.urn:uuid:0FE43E4D025F0BF3DC11582467646813@apache.org>

<?xml version="1.0" encoding="UTF-8"?>
   <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
      <soapenv:Header/>
      <soapenv:Body>
         <sendImage xmlns="http://org/apache/axis2/jaxws/sample/mtom">
            <input>
            <imageData><xop:Include xmlns:xop="http://www.w3.org/2004/08/xop/include" 
            href="cid:1.urn:uuid:0FE43E4D025F0BF3DC11582467646811@apache.org"/></imageData>
            </input>
         </sendImage>
      </soapenv:Body>
   </soapenv:Envelope>
--MIMEBoundaryurn\_uuid\_0FE43E4D025F0BF3DC11582467646812
content-type: text/plain
content-transfer-encoding: binary
content-id: 
         <1.urn:uuid:0FE43E4D025F0BF3DC11582467646811@apache.org>

… binary data goes here …
--MIMEBoundaryurn\_uuid\_0FE43E4D025F0BF3DC11582467646812--
```

```
<xop:Include xmlns:xop="http://www.w3.org/2004/08/xop/include" 
href="cid:1.urn:uuid:0FE43E4D025F0BF3DC11582467646811@apache.org"/>
```

## Inbound processing of referenced attachments

Figure 1. How the web service (JAX-WS)
export binding processes a SOAP message with a referenced attachment

<!-- image -->

## MTOM attachment attributes

- MTOM can support attachment elements within nested structures.
- MTOM is only available for the base64Binary type.
- MTOM can support attachment elements within nested structuresmeaning that the bodyPath for MTOM attachments arethe xpath location for the element where the MTOMattachment is held. The computing logic for bodyPath is strictly following the schema to generate the xpath locationas shown in the examples below:
    - For a non-array type (maxOccurs is 1):  /sendImage/input/imageData
    - For a array type (maxOccurs  > 1):  /sendImage/input/imageData[1]
- Mixed attachment types are not supported, meaning that if MTOM
is enabled on the import binding, the MTOM attachment will be generated.
If MTOM is disabled or if the MTOM configuration value is left as
the default value on the export binding, the incoming MTOM message
is not supported.

## Related information

- How to choose the appropriate attachment style
- Referenced attachments: swaRef-typed elements
- Referenced attachments: top-level message parts
- Unreferenced attachments