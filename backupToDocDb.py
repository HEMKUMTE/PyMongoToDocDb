import json
import pydocumentdb.document_client as document_client
import sys
import os
from bson import json_util
import pymongo
from pymongo import MongoClient


client = MongoClient()
#database name
db = client[sys.argv[1]]
#collection name
collectionName= db[sys.argv[2]]
res=[]

#outfile name
open(sys.argv[3],'w').write('')

with open(sys.argv[3], 'a') as outfile:
    for i in collectionName.find():
	
	json.dump(i, outfile,default=json_util.default)
	outfile.write('\n')
    
print 'backup completed'
outfile = sys.argv[3]
client = document_client.DocumentClient('https://XXXXXXXX.documents.azure.com:443', {'masterKey': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX=='})

# Attempt to delete the database.  This allows this to be used to recreate as well as create
try:
    db = next((data for data in client.ReadDatabases() if data['id'] == db))
    client.DeleteDatabase(db['_self'])
    print 'test database deleted'
except:
    pass

# Create database
try:
    db = client.CreateDatabase({ 'id': db })
    print 'test database created'
except:
    pass

# Create collection
try:
    collection = client.CreateCollection(db['_self'],{ 'id': collectionName })
    print 'restaurants collection created'
except:
    pass

#read the file 
with open(outfile) as f:
    for line in f:
        #upload this json document to the given collection
        jsondoc = json.loads(line)
        document = client.CreateDocument(collection['_self'],jsondoc)
        print 'one document uploaded'

print 'done exporting'