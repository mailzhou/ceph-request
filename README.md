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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-c                       set configure file. the default configure file is ~/ceph-request.cfg.
--version                get the version of ceph-request tool.
-v                       show more info of request.
-m --method              the http method. one type of [GET PUT POST DETELE HEAD]
-h --headers             set request header.   exp. --headers '{"Range": "bytes=0-10"}'
-r --request             set http request url. exp. '/' '/bucket' '/admin' '/bucket/object'
--file                   set upload file
--content                set http request body content
--download               set loal file name for download
--type                   default type is s3, you can use --type swift to sent swift request to radosgw
```

create bucket named yuliyang
```
ceph-request -c ceph-request.cfg -m put -r '/yuliyang'
```

delete bucket named yuliyang
```
ceph-request -c ceph-request.cfg -m delete -r '/yuliyang'
```

upload file

```
ceph-request -c ceph-request.cfg -m put -r '/yuliyang/object1' --file 1.txt
```

upload file from content

```
ceph-request -c ceph-request.cfg -m put -r '/yuliyang/object1' --content "this is content for object1"
```

delete object

```
ceph-request -c ceph-request.cfg -m delete -r '/yuliyang/object1' 
```

get location of bucket named yuliyang
```
ceph-request -c ceph-request.cfg -m get -r '/yuliyang?location'
```

get acl of bucket yuliyang
```
ceph-request -c ceph-request.cfg -m get -r '/yuliyang?acl'
```

set acl for bucket yuliyang
```
ceph-request -c ceph-request.cfg -m put -r '/yuliyang?acl' --content '<?xml version="1.0" encoding="UTF-8"?><AccessControlPolicy xmlns="http://s3.amazonaws.com/doc/2006-03-01/"><Owner><ID>admin</ID><DisplayName>admin</DisplayName></Owner><AccessControlList><Grant><Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser"><ID>admin</ID><DisplayName>admin</DisplayName></Grantee><Permission>READ</Permission></Grant></AccessControlList></AccessControlPolicy>'
```

set header

```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg -m put -r '/yuliyang2/obj1'  --headers '{"x-amz-meta-cmcc":"onestgroup2"}'

#head it 
[root@joke ceph-request]# ceph-request -c ceph-request.cfg -m head -r '/yuliyang2/obj1' -v                                           
< HEAD /yuliyang2/obj1 HTTP/1.1
< Host: 192.168.10.147:8081
< Connection: keep-alive
< Accept-Encoding: gzip, deflate
< Accept: */*
< User-Agent: python-requests/2.11.1
< date: Sun, 06 Nov 2016 02:30:32 GMT
< Authorization: AWS admin:yx2q0vW4bh1/8pDpmqCXPBqUiFQ=
< 

> HTTP/1.1 200 OK
> Content-Length: 0
> Accept-Ranges: bytes
> Last-Modified: Sun, 06 Nov 2016 02:30:30 GMT
> ETag: "d41d8cd98f00b204e9800998ecf8427e"
> x-amz-meta-cmcc: onestgroup2
> x-amz-request-id: tx000000000000000000020-00581e95c8-857b-default
> Content-Type: binary/octet-stream
> Date: Sun, 06 Nov 2016 02:30:32 GMT
> Connection: Keep-Alive
> 
```

range download
```
ceph-request -c ceph-request.cfg  -m get -r '/yuliyang4/obj1' --headers '{"Range": "bytes=0-10"}'  -v --download rangedownload
```

## swift

list buckets
```
ceph-request -c ceph-request.cfg --type swift -m get -r '/swift/v1'
```

list bucket

```
ceph-request -c ceph-request.cfg --type swift -m get -r '/swift/v1/yuliyang2'
```

download file
```
ceph-request -c ceph-request.cfg --type swift -m get -r '/swift/v1/yuliyang/obj1'  --download swiftdownobj1
```

create bucket
```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg --type swift -m put -r '/swift/v1/yuliyang7' -v
< PUT /swift/v1/yuliyang7 HTTP/1.1
< Host: 192.168.10.147:8081
< Connection: keep-alive
< Accept-Encoding: gzip, deflate
< Accept: */*
< User-Agent: python-requests/2.11.1
< x-auth-token: AUTH_rgwtk0b00000061646d696e3a61646d696e41c33c216827b4c1341a20582da0f20b6aa54399651c2f2019ae5ec906daaa7514c04203
< Content-Length: 0
< 

> HTTP/1.1 201 Created
> X-Trans-Id: tx0000000000000000004b6-00581ec8b4-857b-default
> Content-Length: 0
> Accept-Ranges: bytes
> Content-Type: text/plain; charset=utf-8
> Date: Sun, 06 Nov 2016 06:07:48 GMT
> Connection: Keep-Alive
> 
```
detele bucket
```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg --type swift -m delete -r '/swift/v1/yuliyang7' -v    
< DELETE /swift/v1/yuliyang7 HTTP/1.1
< Host: 192.168.10.147:8081
< Connection: keep-alive
< Accept-Encoding: gzip, deflate
< Accept: */*
< User-Agent: python-requests/2.11.1
< x-auth-token: AUTH_rgwtk0b00000061646d696e3a61646d696ed5608bf6351a4b19511b2058318afd13fd76eb4638c4f2adceb10a1494f1e53fec2b7d04
< Content-Length: 0
< 

> HTTP/1.1 204 No Content
> X-Trans-Id: tx0000000000000000004bc-00581ec9d1-857b-default
> Content-Length: 0
> Accept-Ranges: bytes
> Content-Type: text/plain; charset=utf-8
> Date: Sun, 06 Nov 2016 06:12:33 GMT
> Connection: Keep-Alive
> 
```
head bucket
```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg --type swift -m head -r '/swift/v1/yuliyang7' -v
< HEAD /swift/v1/yuliyang7 HTTP/1.1
< Host: 192.168.10.147:8081
< Connection: keep-alive
< Accept-Encoding: gzip, deflate
< Accept: */*
< User-Agent: python-requests/2.11.1
< x-auth-token: AUTH_rgwtk0b00000061646d696e3a61646d696ed76ae2bde9a3afbe4a1b2058a9c52116f60814e969f07fe85e77a0ec812fec88752c31fe
< 

> HTTP/1.1 204 No Content
> X-Timestamp: 0.00000
> X-Container-Object-Count: 0
> X-Container-Bytes-Used: 0
> X-Container-Bytes-Used-Actual: 0
> X-Storage-Policy: default-placement
> X-Trans-Id: tx0000000000000000004ba-00581ec9ca-857b-default
> Content-Length: 0
> Accept-Ranges: bytes
> Content-Type: text/plain; charset=utf-8
> Date: Sun, 06 Nov 2016 06:12:26 GMT
> Connection: Keep-Alive
> 
```
