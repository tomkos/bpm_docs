<!-- image -->

# Atom feed format

The term Atom applies to two related
standards:

- The Atom Syndication Format is an XML language used for web feeds.
- The Atom Publishing Protocol (AtomPub or APP) is a simple HTTP-based
protocol for creating and updating web resources.

Web feeds allow clients to check for updates published on
a web site. To provide a web feed, a web site publishes a list of
recent articles or content in a standardized, machine-readable format.
This list is known as a feed. The feed can then be downloaded
by web sites that syndicate content from the feed or by feed-reader
programs.

The Atom feed format has a well defined schema. The
feed contains multiple entries and each entry is associated with content.
The content can either be inline or the content can be available at
the link specified. The content has associated type information which
is the mime type of the content.

There are three well-defined
types called text, "html and xhtml. A user can
provide his own types complying to the rules of Atom specification.

## Inbound data

For inbound data, the Atom
data handler converts the Atom feed into a well-defined business object.
If the feed contains inline content, then, based on the configuration
setup on the data handler, it will call the configured data handler
to convert the inline content to a business object and set that business
object in the feed. You must provide a schema for the business object
that corresponds to this inline content.

Consider the following
example. There are two entries in the feed. The content type of the
first entry is XML and the other entry is JSON. This is what the input
data would look like.

```
287	<?xml version="1.0" encoding="utf-8"?>
288	<feed xmlns="http://www.w3.org/2005/Atom">
289	 
290	 <title>Example Feed</title>
291	 <subtitle>A subtitle.</subtitle>
292	 <link href="http://example.org/feed/" rel="self"/>
293	 <link href="http://example.org/"/>
294	 <updated>2003-12-13T18:30:02Z</updated>
295	 <author>
296	   <name>John Doe</name>
297	   <email>johndoe@example.com</email>
298	 </author>
299	 <id>urn:uuid:60a76c80-d399-11d9-b91C-0003939e0af6</id>
300	 
301	 <entry>
302	   <content type="text/xml">
303	       <p:Customer xmlns:p="http://www.ibm.com/crm" xmlns="http://www.ibm.com/crm">
304	               <id>10</id>
305	       </p:Customer>
306	   </content>
307	   <title>Atom-Powered Robots Run Amok</title>
308	   <link href="http://example.org/2003/12/13/atom03"/>
309	   <id>urn:uuid:1225c695-cfb8-4ebb-aaaa-80da344efa6a</id>
310	   <updated>2003-12-13T18:30:02Z</updated>
311	   <summary>Some text.</summary>
312	 </entry> 
313	<entry>
314	   <content>
315	      <content type="text/json">
316	          {"firstName"="John","lastName"="Doe","id"="10"}
317	      </content>
318	      <type>text/json</type>
319	   </content>
320	   <title>Atom-Powered Robots Run Amok</title>
321	   <link href="http://example.org/2003/12/13/atom03"/>
322	   <id>urn:uuid:1225c695-cfb8-4ebb-aaaa-80da344efa6a</id>
323	   <updated>2003-12-13T18:30:02Z</updated>
324	   <summary>Some text.</summary>
325	 </entry> 
326	
327	</feed>
```

You would need to provide an XML schema that would
correspond to the Customer shown previously. This customer is an inline
content entry.

You would also need to provide
an XML schema that corresponds to the JSON data shown previously.
This JSON data is also an inline content entry.

- mimeType=text/xml and data handler = XMLDataHandlerConfig
- mimeType=text/json and data handler = JSONDataHandlerConfig.

## Outbound data

For outbound data, the Atom
data handler converts a well-defined business object into an Atom
feed. If the feed business object contains an inline content business
object, then, depending on the configuration of the data handler,
it will call the configured data handler to convert the business object
in the content to the inline content entry in the feed. You must provide
a schema for the business object that corresponds to this inline content.

Consider
the following example. There are two business objects corresponding
to the content entry. One of the business objects is Customer and
the business object is Order. The Customer business object has to
be serialized into XML in the Atom feed and the Order has to be serialized
as a delimited stream in the Atom feed.

The Customer business
object:

<!-- image -->

The
serialized XML for it:

```
<entry>
	<content type="text/xml">
		<p:Customer xmlns:p="http://www.ibm.com/crm" 
					xmlns="http://www.ibm.com/crm">
			<id>10</id>
			<firstName>John</firstName>
			<lastName>Doe</lastName>
		</p:Customer>
	</content>
</entry>
```

The Order business object:

<!-- image -->

The serialized delimited stream
for it:

```
<entry>
	<content type="text/delimited">
		10,Television
```

The output data would be as follows:

```
328	<?xml version="1.0" encoding="utf-8"?>
329	<feed xmlns="http://www.w3.org/2005/Atom">
330	 
331	 <title>Example Feed</title>
332	 <subtitle>A subtitle.</subtitle>
333	 <link href="http://example.org/feed/" rel="self"/>
334	 <link href="http://example.org/"/>
335	 <updated>2003-12-13T18:30:02Z</updated>
336	 <author>
337	   <name>John Doe</name>
338	   <email>johndoe@example.com</email>
339	 </author>
340	 <id>urn:uuid:60a76c80-d399-11d9-b91C-0003939e0af6</id>
341	 <entry>
342	   <content type="text/xml">
343	       <p:Customer xmlns:p="http://www.ibm.com/crm" 
344	                   xmlns="http://www.ibm.com/crm">
345	           <id>10</id>
346	           <firstName>John</firstName>
347	           <lastName>Doe</lastName>
348	       </p:Customer>
349	   </content>       
350	   <title>Atom-Powered Robots Run Amok</title>
351	   <link href="http://example.org/2003/12/13/atom03"/>
352	   <id>urn:uuid:1225c695-cfb8-4ebb-aaaa-80da344efa6a</id>
353	   <updated>2003-12-13T18:30:02Z</updated>
354	   <summary>Some text.</summary>
355	 </entry>  
356	 <entry>
357	   <content type="text/delimited">
358	       10,Television
359	   </content>        
360	   <title>Atom-Powered Robots Run Amok</title>
361	   <link href="http://example.org/2003/12/13/atom03"/>
362	   <id>urn:uuid:1225c695-cfb8-4ebb-aaaa-80da344efa6a</id>
363	   <updated>2003-12-13T18:30:02Z</updated>
364	   <summary>Some text.</summary>
365	 </entry> 
366	 <entry>
367	   <title>Atom-Powered Robots Run Amok</title>
368	   <id>urn:uuid:1225c695-cfb8-4ebb-aaaa-80da344efa6a</id>
369	   <updated>2003-12-13T18:30:02Z</updated>
370	   <summary>Some text.</summary>
371	 </entry> 
372	</feed>
```

- Atom feed format properties

The properties of the Atom feed format are described.
- Interface for Atom feed format

The interface and business objects to support the Atom feed format are discussed.

## Related reference

- Delimited format
- Fixed width format
- JavaScript Object Notation (JSON) format
- SOAP data handler