# Adding custom format types in a heritage coach (deprecated)

The predefined character formats for Input Text and Output Text
controls are defined by the <formatting-templates> section
in the PROFILE\_HOME\config\cells\cell\_name\nodes\node\_name\servers\server\_name\process-center\config\system\99Local.xml file.

```
<formatting-templates> <formatting-template comment="Currency" template="$ ###,###,###.##" /> <formatting-template comment="Currency" template="###,###,###.## €" /> <formatting-template comment="Currency" template="€ ###,###,###.##" /> <formatting-template comment="Integer" template="###,###,###" /> <formatting-template comment="Decimal" template="###,###,###.##" /> <formatting-template comment="US phone" template="(###) 000-0000" /> <formatting-template comment="US SSN" template="000-00-0000" /> </formatting-templates>
```