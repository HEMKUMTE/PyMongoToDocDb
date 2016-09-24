# A Python tool to Migrate a given MongoDB database to Azure DocumentDB

PyMongoToDocDb is a python tool to help you migrate your MongoDB database to Azure DocumentDB.

This version can only copy a given collection, and it overwrites the given Azure DocumentDB, we are building more features to this, the tool was built in the dev-sprint session at PyCon India 2016.

### Tech
PyMongoToDocDb uses a number of basic python packages
* [json] - Python json package
* [pymongo] - Python PyMongo Package
* [pydocumentdb] - Azure Python sdk for DocumentDB* 

Replace the Azure DocumentDb Host and Master Key in backupToDocDb.py at line
```
client = document_client.DocumentClient('https://XXXXXXXX.documents.azure.com:443', {'masterKey': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX=='})
```

Calling the Python Program

```sh
$ python backupToDocDb.py DBNAME COLLECTION BACKUPFILENAME 
```

