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
