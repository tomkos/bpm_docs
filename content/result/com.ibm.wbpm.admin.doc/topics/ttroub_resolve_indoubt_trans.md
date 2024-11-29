# Resolving indoubt transactions

## Before you begin

Use the procedure to resolve indoubt transactions only
if you have tried other procedures (such as restarting the server
in recovery mode), unsuccessfully.

## About this task

When a transaction is stuck in the indoubt state, it must
either be committed or rolled back so that normal processing by the
affected messaging engine can continue.

You can use the administrative
console to display the messages causing the problem by Listing messages on a message point.

- Using the server's transaction management panels
- Using methods on the messaging engine's MBean

You should first attempt to resolve the indoubt transaction using the application server
transaction management panels. If this does not work, then use methods on the messaging engine's
MBean. These are described in the following section.

## Procedure

1 Using the application server transaction managementpanels to resolve indoubt transactions
    1. Navigate to the transaction management panels in the
administrative console Click Servers > Application servers  > [Content Pane]  > server-name  > [Container
Settings] Container Services  > Transaction Service  > Runtime > Imported prepared transactions
- Review
    2. If the transaction identity appears in the resulting
panel, you can commit or roll back the transaction Choose
the option to roll back the transaction 
If the transaction
identity does not appear in the panel, the transaction identity was
not enlisted with the Transaction Service on the server. In this case
only, you should use methods on the MBean (as described in the next
step) to display a list of the identities of the indoubt transactions
managed directly by the messaging engine.
2 Using methods on the messaging engine's MBean to resolveindoubt transactions CAUTION: Only performthis step if you were unable to display the transaction identity byusing the server's transaction management panels

1 The following methods on the messaging engine's MBeancan be used to get a list of transaction identities (xid) and to commitand roll back transactions:
    - getPreparedTransactions()
    - commitPreparedTransaction(String xid)
    - rollbackPreparedTransaction(String xid)
2. To invoke the methods, you can use a wsadmin command,
for example, you can use a command of the following form to obtain
a list of the indoubt transaction identities from a messaging engine's
MBean:  wsadmin> $AdminControl invoke [$AdminControl queryNames type=SIBMessagingEngine,*] getPreparedTransactionsAlternatively,
you can use a script such as the following to invoke the methods on
the MBean:foreach mbean [$AdminControl queryNames type=SIBMessagingEngine,*] {
  set input 0

  while {$input >=0} {
    set xidList [$AdminControl invoke $mbean getPreparedTransactions]

    set meCfgId [$AdminControl getConfigId $mbean]
    set endIdx [expr {[string first "(" $meCfgId]  - 1}]
    set me [string range ${meCfgId} 0 $endIdx]

    puts "----Prepared Transactions for ME $me ----"
    set index 0
    foreach xid $xidList {
      puts "  Index=$index XID=$xid"
      incr index
    }
    puts "------- End of list ---------"
    puts "Select index of XID to commit/rollback (-1 to continue) :"
    set input [gets stdin]

    if {$input < 0 } {
puts "No index selected, going to continue."
    } else {
      set xid [lindex $xidList $input]
      puts "Enter c to commit or r to rollback XID $xid"
      set input [gets stdin]
      if {$input == "c"} {
        puts "Committing xid=$xid"
        $AdminControl invoke $mbean commitPreparedTransaction $xid
      }
      if {$input == "r"} {
        puts "Rolling back xid=$xid"
        $AdminControl invoke $mbean rollbackPreparedTransaction $xid
      }
    }
    puts ""
  }
}
This script lists the transaction identities of
the transactions together with an index. You can then select an index
and commit or roll back the transaction corresponding to that index.

## Results

1. Use the administrative console to find the transaction identity
of indoubt transactions.
2. If a transaction identity appears in the transaction management
panel, commit or roll back the transactions as required.
3 If a transaction identity does not appear in the transaction managementpanel, use the methods on the messaging engine's MBean. For example,use a script to display a list of transaction identities for indoubttransactions. For each transaction:
    1. Enter the index of the transaction identity of the transaction.
    2. Enter c to commit the transaction
    3. Enter r to roll back the transaction.
4. To check that transactions are no longer indoubt, restart the
server and use the transaction management panel, or methods on the
messaging engine's MBean.