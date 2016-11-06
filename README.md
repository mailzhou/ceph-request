# INSTALL

```
python setup.py install
```

# HOW

```
ceph-request --help
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
