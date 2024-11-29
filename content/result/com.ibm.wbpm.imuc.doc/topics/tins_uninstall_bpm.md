# Uninstalling IBM Business Automation Workflow interactively

## About this task

## Procedure

1. Close the programs that you installed
using Installation Manager.
2. Stop all running servers.
3 Display the Uninstall Packages pageof the Installation Manager.
    - Start the Installation Manager. On the Start page, click Uninstall.
    - Click Start > All Programs > IBM > IBM Business Automation Workflow > Uninstall.
4. On the Uninstall Packages page, select IBM Business Automation Workflow and
associated packages that you want to uninstall. Tip: If you started Installation Manager from
the Start menu (Start > ... > Uninstall) in the previous step,
your IBM Business Automation Workflow edition
is pre-selected for uninstallation on the Uninstall Packages page.
If you no longer need to use Db2®, or intend to reinstall IBM Business Automation Workflow, select the database option for Db2 to uninstall this database.CAUTION:Do not select the option to uninstall Db2 unless you are sure that no other
product is using Db2. Selecting
this option will delete all the Db2 databases and database assets, even if other products, including products on a remote system,
might use Db2 on this
system.
5. Click Next.
6. On the Summary page, review the list
of packages that will be uninstalled, and then click Uninstall.
After the uninstallation finishes, the Complete page
opens.
7. Click Finish to
exit the wizard.

## Results

## What to do next

- If databases were created in the previous installation, ensure
that the databases were dropped. See Reinstallation cannot create new profile.
- If you uninstalled Db2, ensure
that the BPMINST directory was deleted.
- If you uninstalled Db2 , deletethe remaining Db2 entries in the/etc/service file. This is necessary because the new installation requires thatport 50000 be available. Update the following file to remove any referencesto Db2 and port50000 . For example, remove the following line:db2c\_bpminst 50000/tcp ordb2c\_db2inst1 50000/tcp
    - /etc/services
    - C:\Windows\System32\drivers\etc\services

```
db2c\_bpminst 50000/tcp
```

```
db2c\_db2inst1 50000/tcp
```