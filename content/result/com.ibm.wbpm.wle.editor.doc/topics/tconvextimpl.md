# Converting external implementations

## About this task

- Conversion is one way. After the service is converted, you cannot undo the operation, so take a
snapshot before you convert the external implementation in case you need to revert to the original.
- Conversion of an external implementation is done at the process app or toolkit level. Artifacts
in dependent toolkits are not converted automatically. You must open the dependent toolkit and
convert the artifacts manually. A dependent toolkit with converted artifacts can be easily added to
your process application. In the Toolkits library navigation, find the
toolkit and select the option to upgrade the dependency.
- After you convert an external implementation, you can continue to reference the converted
external service from a task in a BPD. However, to edit the external service, you must use the
web-based Process Designer. Consider converting the
BPD to a process to make your work easier by working in a single Process Designer environment. See Converting BPDs to processes.

## Procedure

1. Open the process app or toolkit.
2. Open the Process App Settings or Toolkit Settings
editor.
3. In the Service Conversion tab, select the external implementations that
you want to convert and click Convert.
4. Optional: 
Select Convert into a single service.
5. Click Convert. 
The external service editor opens showing the converted service. If the conversion was
one-to-one, the new external service has a single operation. If the conversion was many-to-one, you
see an operation for each converted external implementation.

## What to do next