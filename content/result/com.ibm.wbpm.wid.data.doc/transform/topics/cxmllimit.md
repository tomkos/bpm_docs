<!-- image -->

# XML map: Troubleshooting and limitations

- Limitation: Conflicting namespace prefixes between the XML map input and the XML map definition

XML maps require that there not be any conflicting namespace prefix definitions between the map input and the definition.
- Troubleshooting: Empty expression when running custom XSLT

When you run your xslt map, you get the error "Empty expression" or "A location path was expected,  but the end of the XPath expression was found instead." No output is produced.
- Unsupported EXSLT functions

Some EXSLT functions are not supported at run time. If you have maps from previous versions that use these functions, you will see an error in the XML map and problems view for each unsupported function. For example, "The add function is not available". You must use a different function or transform to achieve the required result.