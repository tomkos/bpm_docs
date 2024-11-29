<!-- image -->

# validateSCAImportExportInformation command

- All selector export bindings point to valid exports on the bus
- All SCA imports point to valid exports on the bus

<!-- image -->

## Prerequisites

Run the command in connected
mode. You must connect as a cell administrator that is assigned the
CellAdmin role, or a deployment environment administrator that is
assigned the DEAdmin role.

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
validateSCAImportExportInformation
-earFilePath earFile
```

## Required parameters

## Command output

```
LFCOR1003I: SCA export information validated successfully. No errors were found
```

```
LFCOR1001W: No matching export was found for selector target with module name moduleName and export name exportName in selector component selectorComponentName.

LFCOR1002W: No matching export was found for SCA import importName with module name moduleName and export name exportName.
```

- If the targeted module is not installed, install it now.
- If the unknown binding is for a selector component, install the
EAR and then use the administrative console or commands to update
the targets.
- If the unknown binding is an SCA import binding, install the EAR
and then use the administrative console or commands to update the
binding manually.

## Example

```
AdminTask.validateSCAImportExportInformation('[-earFilePath C:\WPS62\profiles\Profile03\installedApps\server01node01Cell\billingProcess.ear]')
```