# INSTALL

```
git clone git@github.com:wzyuliyang/ceph-request.git 
cd ceph-request
python setup.py install

or

pip install ceph-request
```

# HOW

## s3

```
[root@graphite ~]# ceph-request -h
CONFIGURE FILE EXP.:
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
-h                       show help
-c                       set configure file. the default configure file is ~/ceph-request.cfg.
--version                get the version of ceph-request tool.
-v                       show more info of request.
-m --method              the http method. one type of [GET PUT POST DETELE HEAD]
--headers                set request header.   exp. --headers '{"Range": "bytes=0-10"}'
-r --request             set http request url. exp. '/' '/bucket' '/admin' '/bucket/object'
--file                   set upload file
--content                set http request body content
--download               set loal file name for download
--type                   default type is s3, you can use --type swift to sent swift request to radosgw
```

create bucket named yuliyang
```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg -m put -r '/yuliyang' -v
```

delete bucket named yuliyang
```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg -m delete -r '/yuliyang2222' -v   
```

upload file

```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg -m put -r '/yuliyang6/object1' --file setup.py  -v    
```

upload file from content

```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg -m put -r '/yuliyang6/object2' --content 'sdadsa' -v
```

delete object

```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg -m delete -r '/yuliyang6/object2'  -v                     
```

get location of bucket named yuliyang
```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg -m get -r '/yuliyang6?location' -v
```

get acl of bucket yuliyang
```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg -m get -r '/yuliyang6?acl' -v        
```

set acl for bucket yuliyang
```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg -m put -r '/yuliyang6?acl' -v  --content '<?xml version="1.0" encoding="UTF-8"?><AccessControlPolicy xmlns="http://s3.amazonaws.com/doc/2006-03-01/"><Owner><ID>admin</ID><DisplayName>admin</DisplayName></Owner><AccessControlList><Grant><Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser"><ID>admin</ID><DisplayName>admin</DisplayName></Grantee><Permission>READ</Permission></Grant></AccessControlList></AccessControlPolicy>'
```

set header

```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg -m put -r '/yuliyang2/obj1'  --headers '{"x-amz-meta-cmcc":"onestgroup2"}'

#head it 
[root@joke ceph-request]# ceph-request -c ceph-request.cfg -m head -r '/yuliyang2/obj1' -v                                       
```

range download
```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg  -m get -r '/yuliyang6/object1' --headers '{"Range": "bytes=0-10"}'  -v --download rangedownload -v 
```

## swift

list buckets
```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg --type swift -m get -r '/swift/v1' -v
```

list bucket

```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg --type swift -m get -r '/swift/v1/yuliyang2' -v
```

download file
```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg --type swift -m get -r '/swift/v1/yuliyang/obj1'  --download swiftdownobj1 -v
```

create bucket
```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg --type swift -m put -r '/swift/v1/yuliyang7' -v
```
detele bucket
```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg --type swift -m delete -r '/swift/v1/yuliyang7' -v    
```
head bucket
```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg --type swift -m head -r '/swift/v1/yuliyang7' -v
```

copy object

```
#create object
[root@NFJD-PSC-oNest-Mst-SV1 ceph-request]# ceph-request -c yuliyang.cfg --type swift  -m put -r '/swift/v1/yuliyang-b1/obj2' -v  --content 'dassduadhkwkdkad'

#copy object
[root@NFJD-PSC-oNest-Mst-SV1 ceph-request]# ceph-request -c yuliyang.cfg --type swift   -m put -r '/swift/v1/yuliyang-b2/obj2copy' -v  --headers '{"X-Copy-From": "/yuliyang-b1/obj2"}'

# get object 
[root@NFJD-PSC-oNest-Mst-SV1 ceph-request]# ceph-request -c yuliyang.cfg --type swift   -m get -r '/swift/v1/yuliyang-b2/obj2copy' -v

```
# set bucket public read
```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg --type swift   -m post -r '/swift/v1/asdadas' -v --headers '{"x-container-read": ".r:*"}'
```

# set bucket public write

```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg --type swift   -m post -r '/swift/v1/asdadas' -v --headers '{"x-container-write": ".r:*"}'
```

# set bucket public read and write
```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg --type swift   -m post -r '/swift/v1/asdadas' -v --headers '{"x-container-read": ".r:*","x-container-write": ".r:*"}'
```

## admin rest api
show usage 
```
# add user cap
[root@graphite ~]# radosgw-admin caps add --uid=admin --caps="users=*;buckets=*;metadata=*;usage=*;zone=*"
# enable usage log
[root@graphite ~]# cat /etc/ceph/ceph.conf |grep rgw_enable_usage_log
rgw_enable_usage_log = True
# show usage
[root@graphite ~]# ceph-request -c ceph-request.cfg  -m get -r '/admin/usage?format=json' |python -c 'import sys, json; print json.dumps(json.load(sys.stdin),indent=4)'

```
## set user quota
```
[root@ceph03 yuliyang]# ceph-request -c ceph-request.cfg  -m put -r '/admin/user?quota&uid=admin&quota-type=user' -v --content='{"enabled":true,"max_size_kb":102400,"max_objects":10000}'
```

## get user quota
```
[root@ceph03 yuliyang]# ceph-request -c ceph-request.cfg  -m get -r '/admin/user?quota&uid=admin&quota-type=user' -v 
```

