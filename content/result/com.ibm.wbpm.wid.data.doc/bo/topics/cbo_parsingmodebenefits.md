# Benefits of using lazy versus eager parsing mode

Some applications benefit from lazy XML parsing mode, while
others see improved performance with eager parsing mode. It is recommended
that you benchmark your application in both parsing modes to determine
which mode best suites the specific characteristics of your application.

Applications that parse large XML data streams are likely to see
performance improvements when the lazy XML parsing mode is used. The
performance benefits increase as the size of the XML byte stream increases,
and the amount of data from the byte stream that is accessed by the
application decreases.

- Applications that parse non-XML data streams
- Applications that use messages that are created using the BOFactory
service
- Applications that parse very small XML messages