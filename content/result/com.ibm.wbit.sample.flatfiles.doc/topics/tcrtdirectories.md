<!-- image -->

# Create the directories and input file

## About this task

Create the following directories on your file system
(assuming a Windows operating system):

## Procedure

1. Create a c:\flatfiles directory.
2 Create the following subdirectories in the flat files directory. Linux® users: Createa similar file structure using the Linux filesystem.
    1. c:\flatfiles\inboundevents
    2. c:\flatfiles\inboundarchive
    3. c:\flatfiles\outputdir

Linux® users: Create
a similar file structure using the Linux file
system.

3. Create the following customer.txt file
and add it to the c:\flatfiles directory. When
you test the application, you can copy it to the c:\flatfiles\inboundevents directory.
 The application will delete it from this directory when it processes
it. Note that the namespace value SeparateCustomers must
match the module name you will create in the next section.
<?xml version="1.0" encoding="UTF-8"?>
<p:Customer xsi:type="p:Customer"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
xmlns:p="http://SeparateCustomers">
  <customerName>John Doe</customerName>
  <Address>170 Baseline Ave</Address>
  <City>Ottawa</City>
  <State>ON</State>
</p:Customer>
####
<p:Customer xsi:type="p:Customer"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
xmlns:p="http://SeparateCustomers">
  <customerName>Susan Kidman</customerName>
  <Address>104 Candlestick Park</Address>
  <City>Ottawa</City>
  <State>ON</State>
</p:Customer>
####
<p:Customer xsi:type="p:Customer"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
xmlns:p="http://SeparateCustomers">
  <customerName>Katheleen Black</customerName>
  <Address>530 Chanticler Road</Address>
  <City>Ottawa</City>
  <State>ON</State>
</p:Customer>
####
<p:Customer xsi:type="p:Customer"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
xmlns:p="http://SeparateCustomers">
  <customerName>Gary White</customerName>
  <Address>793 Morin Street</Address>
  <City>Ottawa</City>
  <State>ON</State>
</p:Customer>
####