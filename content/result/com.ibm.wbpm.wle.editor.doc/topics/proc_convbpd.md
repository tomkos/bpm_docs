# Converting BPDs to processes

When you convert a BPD into a process, the subprocesses inside
it are also converted, and tasks and their properties are maintained.
References to linked processes and heritage human services are maintained.
However, the referenced artifacts are not converted. To convert your
user interfaces, you must separately convert your heritage human services
and coaches. See Converting deprecated functions. You can invoke
heritage humans services from a process, so you can convert your BPDs
and continue to use heritage human services and coaches until you
are ready to convert your user interfaces to responsive user interfaces.

If you have a BPD that references an external
implementation, you should convert the external implementation to an external service before you
convert the BPD to a process. When the external implementation is converted to an external service,
any references in the BPD that point to the external implementation are automatically changed to
point to the external service when the BPD is converted to a process.

- Last User in Lane
- Routing Policy
- List of Users

- Milestones
- Any icon settings on process nodes
- Simulation configuration
- KPI configuration
- Handling error events from previous releases. See Error events in models from V7.5.x and earlier.

## How to convert BPDs to processes

- This conversion is one way. After the BPD is converted to a process,
you cannot undo the operation, so take a snapshot before you convert
the BPD. You can then compare the two by opening the snapshot in the desktop Process Designer and
the process in the Process Designer.
- Conversion of  BPDs to processes is done at the process app or
toolkit level. BPDs in dependent toolkits are not converted automatically.
You must open the dependent toolkit and convert the BPDs manually.

1. Open the process app or toolkit.
2. In the library, select the BPD that you want to convert. To select
multiple BPDs, hold the Ctrl key and click the BPDs that you want.
3. Right-click, and select Convert to process.
4. Expand Processes in the library. The converted
processes now appear under Processes.

1. Open the process app or toolkit.
2. Open the Process App Settings or Toolkit
Settings editor.
3. In the BPD Conversion tab, select the processes
that you want to convert and click Convert.
4. Expand Processes  in the library to see
the converted process.