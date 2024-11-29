# Upgrading IBM Business Automation Workflow

You can install upgrades to IBM Business Automation Workflow when
they are available. You can also upgrade your configuration,
perform a rolling upgrade, or make other changes.

BPM ESB is a special version of BPM which only contains the ESB features of the full BPM product.
So you can only create AdvancedOnly environments and it doesn't include the BPEL features. ESB
supports upgrade only from 22.0.2.

## Before you begin

- IBM Business Automation Workflow 24.x does
not support the z/OS operating system and does not support 32-bit operating systems. If you are
running on a 32-bit system and want to upgrade, you must either perform artifact migration as
described in Migrating artifacts to IBM Business Automation Workflow or contact IBM service for help to migrate to
IBM Business Automation Workflow 24.x on a
64-bit operating system.

1. Define the servers again in the fix pack version of the Heritage Process Portal application.
2. Create a snapshot.
3. Activate the snapshot on Workflow Center.
4. Install the snapshot on Workflow Server.

- Upgrading a product installation from Express to Enterprise

You can upgrade an installation of IBM Business Automation Workflow Express to IBM Business Automation Workflow Enterprise by using Installation Manager to install the new edition over the previously installed edition in the same package group.
- Upgrading a deployment environment from Standard to Advanced

If you are working with an existing Standard deployment environment, you can upgrade it to an Advanced deployment environment using the BPMConfig command. This enables you to take advantage of the additional capabilities that are provided in an Advanced deployment environment.
- Upgrading to IBM Business Automation Workflow 24.x

Follow the instructions for your specific configuration to install the upgrade to 24.x.
- Installing fix packs and interim fixes

Before you install a fix pack or interim fix to IBM Business Automation Workflow, prepare your environment.
- Updating desktop IBM Process Designer (deprecated)

After you update your Workflow Center with a fix pack, refresh pack, or interim fix, you must update desktop Process Designer to the same level. To do so, download the desktop Process Designer file again and run the installation. Only the fixes or changes will be applied.
- Changing Workflow Server use between Production and Non-production

When you install IBM Workflow Server, you select either Production (the default) for production use or Non-production to use Workflow Server only for development, test, or staging.
- Upgrading IBM Integration Designer

You can install upgrades to IBM Integration Designer when they are available. After you upgrade to a new version, import your projects into a new Integration Designer workspace so that version-specific artifacts, such as servers in the Servers view, can reflect the new run time environment.

## Related information

- IBM Installation Manager documentation