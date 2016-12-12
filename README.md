# SUPPORT S3/SWIFT/ADMIN REST API

> WINDOWS PLATFORM NOT SUPPORT CURRENT VERSION 

# INSTALL

```
git clone git@github.com:wzyuliyang/ceph-request.git 
cd ceph-request
python setup.py install

or

pip install ceph-request
```

# HOW

## create configure file
```
vim ceph-request.cfg 
[s3]
host = 192.168.10.147
port = 8081
access_key = admin
secret_key = admin
[swift]
host = 192.168.10.147
port = 8081
subuser = admin:admin
secret_key = gA2BrFTKD3GyDd9b3FIOxDih0PRZBFda13f92GxP

```
## SHOW HELP
```
ceph-request -h
```

## s3
create bucket named yuliyang
```
ceph-request -c ceph-request.cfg -m put -r '/yuliyang' -v
```
delete bucket named yuliyang
```
ceph-request -c ceph-request.cfg -m delete -r '/yuliyang2222' -v   
```
upload file
```
ceph-request -c ceph-request.cfg -m put -r '/yuliyang6/object1' --file setup.py  -v    
```
upload file from content
```
ceph-request -c ceph-request.cfg -m put -r '/yuliyang6/object2' --content 'sdadsa' -v
```
delete object
```
ceph-request -c ceph-request.cfg -m delete -r '/yuliyang6/object2'  -v                     
```
get location of bucket named yuliyang
```
ceph-request -c ceph-request.cfg -m get -r '/yuliyang6?location' -v
```
get acl of bucket yuliyang
```
ceph-request -c ceph-request.cfg -m get -r '/yuliyang6?acl' -v        
```
set acl for bucket yuliyang
```
ceph-request -c ceph-request.cfg -m put -r '/yuliyang6?acl' -v  --content '<?xml version="1.0" encoding="UTF-8"?><AccessControlPolicy xmlns="http://s3.amazonaws.com/doc/2006-03-01/"><Owner><ID>admin</ID><DisplayName>admin</DisplayName></Owner><AccessControlList><Grant><Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser"><ID>admin</ID><DisplayName>admin</DisplayName></Grantee><Permission>READ</Permission></Grant></AccessControlList></AccessControlPolicy>'
```
set header
```
ceph-request -c ceph-request.cfg -m put -r '/yuliyang2/obj1'  --headers '{"x-amz-meta-cmcc":"onestgroup2"}'
#head it 
ceph-request -c ceph-request.cfg -m head -r '/yuliyang2/obj1' -v                                       
```
range download
```
ceph-request -c ceph-request.cfg  -m get -r '/yuliyang6/object1' --headers '{"Range": "bytes=0-10"}'  -v --download rangedownload -v 
```
enable bucket versioning
```
ceph-request -c ceph-request.cfg -m put -r '/version?versioning' -v --content '<?xml version="1.0" encoding="UTF-8"?><VersioningConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/"><Status>Enabled</Status></VersioningConfiguration>'
```
Suspended versioning
```
ceph-request -c ceph-request.cfg -m put -r '/version?versioning' -v --content '<?xml version="1.0" encoding="UTF-8"?><VersioningConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/"><Status>Suspended</Status></VersioningConfiguration>'
```
list all versioned object of named bucket
```
ceph-request -c ceph-request.cfg -m get -r '/version?versions' |xmllint  --format -
```
list all versioned object of named key
```
ceph-request -c ceph-request.cfg -m get -r '/version?versions&prefix=obj1' |xmllint  --format -
```

## swift
list buckets
```
ceph-request -c ceph-request.cfg --type swift -m get -r '/swift/v1' -v
```
list bucket
```
ceph-request -c ceph-request.cfg --type swift -m get -r '/swift/v1/yuliyang2' -v
```
list object with prefix
```
ceph-request -c ceph-request.cfg --type swift   -m get -r '/swift/v1/lyhbucket?prefix=prefix1' -v
```
list object with limits 
```
# list only 4 object
ceph-request -c ceph-request.cfg --type swift   -m get -r '/swift/v1/lyhbucket?&limit=4' -v 
```
download file
```
ceph-request -c ceph-request.cfg --type swift -m get -r '/swift/v1/yuliyang/obj1'  --download swiftdownobj1 -v
```
create bucket
```
ceph-request -c ceph-request.cfg --type swift -m put -r '/swift/v1/yuliyang7' -v
```
detele bucket
```
ceph-request -c ceph-request.cfg --type swift -m delete -r '/swift/v1/yuliyang7' -v    
```
head bucket
```
ceph-request -c ceph-request.cfg --type swift -m head -r '/swift/v1/yuliyang7' -v
```
copy object
```
#create object
ceph-request -c yuliyang.cfg --type swift  -m put -r '/swift/v1/yuliyang-b1/obj2' -v  --content 'dassduadhkwkdkad'

#copy object
ceph-request -c yuliyang.cfg --type swift   -m put -r '/swift/v1/yuliyang-b2/obj2copy' -v  --headers '{"X-Copy-From": "/yuliyang-b1/obj2"}'

# get object 
ceph-request -c yuliyang.cfg --type swift   -m get -r '/swift/v1/yuliyang-b2/obj2copy' -v
```
set bucket public read
```
ceph-request -c ceph-request.cfg --type swift   -m post -r '/swift/v1/asdadas' -v --headers '{"x-container-read": ".r:*"}'
```
set bucket public write
```
ceph-request -c ceph-request.cfg --type swift   -m post -r '/swift/v1/asdadas' -v --headers '{"x-container-write": ".r:*"}'
```
set bucket public read and write
```
ceph-request -c ceph-request.cfg --type swift   -m post -r '/swift/v1/asdadas' -v --headers '{"x-container-read": ".r:*","x-container-write": ".r:*"}'
```

tempurl
```
ceph-request -c ceph-request.cfg --type swift   -m post -r '/swift/v1' -v --headers '{"X-Account-Meta-Temp-Url-Key": "1122"}'


# -*- coding: utf-8 -*-
import hmac
from hashlib import sha1
from time import time
method = 'GET'
key = '1122'  # the value in X-Account-Meta-Temp-Url-Key header
duration_in_seconds = 60*60
expires = int(time() + duration_in_seconds)
path = '/swift/v1/test/swift_init.sh'
hmac_body = '%s\n%s\n%s' % (method, expires, path)
sig = hmac.new(key, hmac_body, sha1).hexdigest()
s = '{path}?temp_url_sig={sig}&temp_url_expires={expires}'
print s.format(path=path, sig=sig, expires=expires)

curl "http://192.168.10.201/swift/v1/test/swift_init.sh?temp_url_sig=263cdcf75900f2eb2028a8d807cd1a02fd458c5e&temp_url_expires=1481561977"
```

## admin rest api
show usage 
```
# add user cap
radosgw-admin caps add --uid=admin --caps="users=*;buckets=*;metadata=*;usage=*;zone=*"
# enable usage log
cat /etc/ceph/ceph.conf |grep rgw_enable_usage_log
rgw_enable_usage_log = True
# show usage
ceph-request -c ceph-request.cfg  -m get -r '/admin/usage?format=json' |python -c 'import sys, json; print json.dumps(json.load(sys.stdin),indent=4)'
```
set user quota
```
ceph-request -c ceph-request.cfg  -m put -r '/admin/user?quota&uid=admin&quota-type=user' -v --content='{"enabled":true,"max_size_kb":102400,"max_objects":10000}'
```
get user quota
```
ceph-request -c ceph-request.cfg  -m get -r '/admin/user?quota&uid=admin&quota-type=user' -v 
```
create user
```
ceph-request -c ceph-request.cfg -m put -r '/admin/user?format=json&uid=user2&display-name=user2&email=user2@test.com' -v
```
delete user
```
ceph-request -c ceph-request.cfg -m delete -r '/admin/user?format=json&uid=user2&purge-data=True' -v
```
create subuser (swift)
```
ceph-request -c ceph-request.cfg -m put -r '/admin/user?format=json&uid=admin&subuser=user2-sub1&access=full&generate-secret=True' -v
```
get user info 
```
ceph-request -c ceph-request.cfg -m get -r '/admin/user?format=json&uid=user1' -v
```
list all users
```
ceph-request -c ceph-request.cfg -m get -r '/admin/metadata/user?format=json' -v
```
list all bucket of yuliyang user
```
ceph-request -c ceph-request.cfg -m get -r '/admin/bucket?format=json&uid=yuliyang' -v
```
get bucket index
```
ceph-request -c ceph-request.cfg -m get -r '/admin/bucket?index&format=json&bucket=yuliyang-b1&check-object=True&fix=True' -v
```
