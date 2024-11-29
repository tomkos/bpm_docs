# Storage area types

- Database and file storage areas
- Fixed storage areas
- Advanced storage areas

For more information, see Storing content.

## Database and file storage areas

## Fixed storage areas

This storage type uses fixed content devices that store content that is created by IBM®
FileNet® P8 applications. A fixed content device is a content
repository with an independent API for accessing content. Fixed content devices have a large storage
capacity and the ability to enforce content retention. There are several kinds of fixed content
devices, as follows.

## Advanced storage areas

An advanced storage area provides high-availability content storage and disaster recovery through
use of replication and replica repair. This capability is accomplished without relying on any
special features of the underlying storage devices, so advanced storage areas can be applied to
commodity storage. An advanced storage area leverages the Content Platform Engine sweep and server communication services for
replication, content deletion, and abandoned content backout. For more information, see Advantages of advanced storage areas.

An advanced storage area supports heterogeneous storage devices. OpenStack Cloud Storage and File
System Storage can be used in an advanced storage area. If you are running Content Platform Engine V5.2.1.3-P8CPE-FP003 or later, Hadoop storage
devices can also be used in an advanced storage area (if the Hadoop Storage Device add-on is
installed).

OpenStack-conforming Cloud Storage, Hadoop, S3, and File System Storage are all advanced storage
devices.