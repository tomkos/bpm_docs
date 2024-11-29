# Migrating existing Elasticsearch 6.x federated data repository indices to upgrade to IBM® Process Federation
Server
24.0.0.0

## About this task

```
<ibmPfs\_federatedSystem
    [...]
    indexName="myFederatedSystemIndex"
    index.number\_of\_shards="3"
    index.number\_of\_replicas="2"
    [...]
/>
```

- http://existing.es6.cluster:9200 as the URL to reach the
existing Elasticsearch 6.x cluster.
- http[s]://new.es8.cluster:9200
					as the URL to reach the new Elasticsearch 8.x cluster.

## Procedure

1. Add your existing Elasticsearch 6.x cluster to the reindex whitelist of your
					new Elasticsearch 8.x cluster, by adding the following line to the elasticsearch.yml
					configuration file of your new Elasticsearch 8.x cluster:
reindex.remote.whitelist: existing.es6.cluster:9200For
					more information about the reindex.remote.whitelist
					configuration property, see
						Reindex from remote
2. Stop all the Process Federation Server
servers.
3. Create a new index
						@myFederatedSystemIndex with alias
							myFederatedSystemIndex in the
					new Elasticsearch 8.x
					cluster, using the settings and default mappings required by Process Federation Server.
Issue an HTTP PUT request to
							http[s]://new.es8.cluster:9200/@myFederatedSystemIndex
					by using the following JSON payload as a template (replacing the
						number\_of\_shards value by the actual value defined for the
					federated system property index.number\_of\_shards in
						server.xml, and replacing the alias name
							myFederatedSystemIndex by the value
					defined for the federated system property indexName in
						server.xml):Important:
The number\_of\_replicas is set to 0 in
							order to speed up the reindexing process, and the actual
								number\_of\_replicas defined in the federated system
							configuration in server.xml will be set later in
							the procedure. For the same reason, the index refresh interval is
							initially set to -1 and will be reverted to its default
							value later in the procedure. See
								Reindex from a remote cluster
							for more details.For more information about the Elasticsearch Create
							Index REST API, see Create Index REST API

{
	"settings": {
		"index": {
			"number\_of\_shards": 3,
			"number\_of\_replicas": 0,
			"refresh\_interval": -1
		},
		"analysis": {
			"normalizer": {
				"lowercase\_normalizer": {
					"filter": ["lowercase",
					"asciifolding"],
					"char\_filter": [],
					"type": "custom"
				}
			}
		}
	},
	"mappings": {
		"dynamic\_templates": [{
			"string\_field": {
				"path\_match": "*.*.string",
				"mapping": {
					"copy\_to": "all\_fields",
					"type": "text",
					"fields": {
						"alphabeticalSort": {
							"normalizer": "lowercase\_normalizer",
							"type": "keyword"
						},
						"keyword": {
							"ignore\_above": 256,
							"type": "keyword"
						}
					}
				}
			}
		},
		{
			"key\_field": {
				"path\_match": "*.*.key",
				"mapping": {
					"copy\_to": "all\_fields",
					"type": "text",
					"fields": {
						"alphabeticalSort": {
							"normalizer": "lowercase\_normalizer",
							"type": "keyword"
						},
						"keyword": {
							"ignore\_above": 256,
							"type": "keyword"
						}
					}
				}
			}
		},
		{
			"boolean\_field": {
				"path\_match": "*.*.boolean",
				"mapping": {
					"copy\_to": "all\_fields",
					"type": "boolean"
				}
			}
		},
		{
			"date\_field": {
				"path\_match": "*.*.date",
				"mapping": {
					"copy\_to": "all\_fields",
					"type": "date"
				}
			}
		},
		{
			"long\_field": {
				"path\_match": "*.*.long",
				"mapping": {
					"copy\_to": "all\_fields",
					"type": "long"
				}
			}
		},
		{
			"double\_field": {
				"path\_match": "*.*.double",
				"mapping": {
					"copy\_to": "all\_fields",
					"type": "double"
				}
			}
		}],
		"properties": {
			"all\_fields": {
				"type": "text"
			},
			"instance": {
				"properties": {
					"duetime": {
						"properties": {
							"date": {
								"copy\_to": "all\_fields",
								"type": "date"
							}
						}
					}
				}
			}
		}
	},
	"aliases": {
		"myFederatedSystemIndex": {
			
		}
	}
}
4. Migrate the content of the existing Elasticsearch 6.x index
							.myFederatedSystemIndex to the
					new Elasticsearch 8.x
					index, by issuing an HTTP POST request to
							http[s]://new.es8.cluster/\_reindex
					with the following JSON payload:

{
  "source": {
    "remote": {
      "host": "http://existing.es6.cluster:9200"
    },
    "index": ".myFederatedSystemIndex"
  },
  "dest": {
    "index": "@myFederatedSystemIndex"
  },
  "script": {
    "source": "if (ctx.\_source['process.processappid.key'] != null) {ctx.\_source['process.processappid.key'] = \"2066.\" + ctx.\_source['process.processappid.key']} if (ctx.\_source['process.processappid.key'] != null && ctx.\_source['process.processtemplateid.key'] != null) {ctx.\_source['process.processtemplateuid.key'] = ctx.\_source['process.processappid.key'] + \"|\" + ctx.\_source['process.processtemplateid.key']}",
    "lang": "painless"
  }
}
For more information about the Elasticsearch reindex REST API, see
							Reindex API.
5. Update the index settings with their final values. Issue an HTTP PUT request to
							http[s]://new.es8.cluster:9200/@myFederatedSystemIndex/\_settings
					using the following JSON payload (replacing the
							number\_of\_replicas value by the
					actual value defined for the federated system property
						index.number\_of\_replicas in
					server.xml):{
  "index" : {
    "number\_of\_replicas" : 2,
    "refresh\_interval": null
  }
}
6. Start the Process Federation Server
servers.