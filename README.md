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
[root@joke ceph-request]# ceph-request -c ceph-request.cfg -m put -r '/yuliyang' -v
< PUT /yuliyang HTTP/1.1
< Host: 192.168.10.147:8081
< Connection: keep-alive
< Accept-Encoding: gzip, deflate
< Accept: */*
< User-Agent: python-requests/2.11.1
< Content-Length: 0
< date: Sun, 06 Nov 2016 07:09:10 GMT
< Authorization: AWS admin:blKkc0yX5gAJO3GggZyxABteewk=
< 

> HTTP/1.1 200 OK
> x-amz-request-id: tx0000000000000000004c6-00581ed716-857b-default
> Content-Length: 0
> Date: Sun, 06 Nov 2016 07:09:11 GMT
> Connection: Keep-Alive
> 

```

delete bucket named yuliyang
```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg -m delete -r '/yuliyang2222' -v   
< DELETE /yuliyang2222 HTTP/1.1
< Host: 192.168.10.147:8081
< Connection: keep-alive
< Accept-Encoding: gzip, deflate
< Accept: */*
< User-Agent: python-requests/2.11.1
< Content-Length: 0
< date: Sun, 06 Nov 2016 07:10:07 GMT
< Authorization: AWS admin:/a5MuVsJtU/R+OUWSAwpuFli6NM=
< 

> HTTP/1.1 204 No Content
> x-amz-request-id: tx0000000000000000004cc-00581ed74f-857b-default
> Date: Sun, 06 Nov 2016 07:10:07 GMT
> Connection: Keep-Alive
> 
```

upload file

```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg -m put -r '/yuliyang6/object1' --file setup.py  -v    
< PUT /yuliyang6/object1 HTTP/1.1
< Host: 192.168.10.147:8081
< Connection: keep-alive
< Accept-Encoding: gzip, deflate
< Accept: */*
< User-Agent: python-requests/2.11.1
< Content-Length: 847
< date: Sun, 06 Nov 2016 07:11:13 GMT
< Authorization: AWS admin:xEHdF0fMDP+1b2Vn/ghCeX4wm0M=
< 
< #encoding:utf-8
from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='ceph-request',
      version=version,
      description="ceph cmd tool to send rest http request to rgw",
      long_description="""ceph cmd tool to send rest http request to rgw""",
      classifiers=[],
      keywords='python ceph radosgw',
      author='wzyuliyang',
      author_email='wzyuliyang911@gmail.com',
      url='https://github.com/wzyuliyang/ceph-request',
      license='MIT License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'requests-toolbelt',
                    'requests',
      ],
      entry_points={
        'console_scripts':[
            'ceph-request = ceph_request.ceph_request:main'
        ]
      },
)

> HTTP/1.1 200 OK
> ETag: "320c1c0f22dc91d94afe36a042ebc89d"
> Content-Length: 0
> Accept-Ranges: bytes
> x-amz-request-id: tx0000000000000000004d0-00581ed791-857b-default
> Date: Sun, 06 Nov 2016 07:11:13 GMT
> Connection: Keep-Alive
> 
```

upload file from content

```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg -m put -r '/yuliyang6/object2' --content 'sdadsa' -v
< PUT /yuliyang6/object2 HTTP/1.1
< Host: 192.168.10.147:8081
< Connection: keep-alive
< Accept-Encoding: gzip, deflate
< Accept: */*
< User-Agent: python-requests/2.11.1
< Content-Length: 6
< date: Sun, 06 Nov 2016 07:11:48 GMT
< Authorization: AWS admin:l2gnOW20YTeqL2k1ow/EuMbsP3Y=
< 
< sdadsa
> HTTP/1.1 200 OK
> ETag: "efa66f9d2333cccff5f93e8043a6a0ce"
> Content-Length: 0
> Accept-Ranges: bytes
> x-amz-request-id: tx0000000000000000004d1-00581ed7b4-857b-default
> Date: Sun, 06 Nov 2016 07:11:48 GMT
> Connection: Keep-Alive
> 

```

delete object

```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg -m delete -r '/yuliyang6/object2'  -v                     
< DELETE /yuliyang6/object2 HTTP/1.1
< Host: 192.168.10.147:8081
< Connection: keep-alive
< Accept-Encoding: gzip, deflate
< Accept: */*
< User-Agent: python-requests/2.11.1
< Content-Length: 0
< date: Sun, 06 Nov 2016 07:12:20 GMT
< Authorization: AWS admin:mNoW2TNm6u0dUbWSSoQHhglq3xY=
< 

> HTTP/1.1 204 No Content
> x-amz-request-id: tx0000000000000000004d2-00581ed7d4-857b-default
> Date: Sun, 06 Nov 2016 07:12:20 GMT
> Connection: Keep-Alive
> 
```

get location of bucket named yuliyang
```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg -m get -r '/yuliyang6?location' -v
< GET /yuliyang6?location HTTP/1.1
< Host: 192.168.10.147:8081
< Connection: keep-alive
< Accept-Encoding: gzip, deflate
< Accept: */*
< User-Agent: python-requests/2.11.1
< date: Sun, 06 Nov 2016 07:12:43 GMT
< Authorization: AWS admin:VzkI7g5G9eCGVHq70hzrznte9bo=
< 

> HTTP/1.1 200 OK
> x-amz-request-id: tx0000000000000000004d4-00581ed7eb-857b-default
> Content-Length: 127
> Date: Sun, 06 Nov 2016 07:12:43 GMT
> Connection: Keep-Alive
> 
<?xml version="1.0" encoding="UTF-8"?><LocationConstraint xmlns="http://s3.amazonaws.com/doc/2006-03-01/"></LocationConstraint>
```

get acl of bucket yuliyang
```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg -m get -r '/yuliyang6?acl' -v        
< GET /yuliyang6?acl HTTP/1.1
< Host: 192.168.10.147:8081
< Connection: keep-alive
< Accept-Encoding: gzip, deflate
< Accept: */*
< User-Agent: python-requests/2.11.1
< date: Sun, 06 Nov 2016 07:13:01 GMT
< Authorization: AWS admin:IkgSb12ueYcZaehqLFOsbR4bEqU=
< 

> HTTP/1.1 200 OK
> x-amz-request-id: tx0000000000000000004d5-00581ed7fd-857b-default
> Content-Type: application/xml
> Content-Length: 425
> Date: Sun, 06 Nov 2016 07:13:01 GMT
> Connection: Keep-Alive
> 
<?xml version="1.0" encoding="UTF-8"?><AccessControlPolicy xmlns="http://s3.amazonaws.com/doc/2006-03-01/"><Owner><ID>admin</ID><DisplayName>admin</DisplayName></Owner><AccessControlList><Grant><Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser"><ID>admin</ID><DisplayName>admin</DisplayName></Grantee><Permission>FULL_CONTROL</Permission></Grant></AccessControlList></AccessControlPolicy>
```

set acl for bucket yuliyang
```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg -m put -r '/yuliyang6?acl' -v  --content '<?xml version="1.0" encoding="UTF-8"?><AccessControlPolicy xmlns="http://s3.amazonaws.com/doc/2006-03-01/"><Owner><ID>admin</ID><DisplayName>admin</DisplayName></Owner><AccessControlList><Grant><Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser"><ID>admin</ID><DisplayName>admin</DisplayName></Grantee><Permission>READ</Permission></Grant></AccessControlList></AccessControlPolicy>'
< PUT /yuliyang6?acl HTTP/1.1
< Host: 192.168.10.147:8081
< Connection: keep-alive
< Accept-Encoding: gzip, deflate
< Accept: */*
< User-Agent: python-requests/2.11.1
< Content-Length: 417
< date: Sun, 06 Nov 2016 07:13:44 GMT
< Authorization: AWS admin:m/5cZphTV2mGusLVpUXsWI+qkD0=
< 
< <?xml version="1.0" encoding="UTF-8"?><AccessControlPolicy xmlns="http://s3.amazonaws.com/doc/2006-03-01/"><Owner><ID>admin</ID><DisplayName>admin</DisplayName></Owner><AccessControlList><Grant><Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser"><ID>admin</ID><DisplayName>admin</DisplayName></Grantee><Permission>READ</Permission></Grant></AccessControlList></AccessControlPolicy>
> HTTP/1.1 200 OK
> x-amz-request-id: tx0000000000000000004d6-00581ed828-857b-default
> Content-Type: application/xml
> Content-Length: 0
> Date: Sun, 06 Nov 2016 07:13:44 GMT
> Connection: Keep-Alive
> 
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
[root@joke ceph-request]# ceph-request -c ceph-request.cfg  -m get -r '/yuliyang6/object1' --headers '{"Range": "bytes=0-10"}'  -v --download rangedownload -v 
< GET /yuliyang6/object1 HTTP/1.1
< Host: 192.168.10.147:8081
< Connection: keep-alive
< Accept-Encoding: gzip, deflate
< Accept: */*
< User-Agent: python-requests/2.11.1
< Range: bytes=0-10
< date: Sun, 06 Nov 2016 07:15:19 GMT
< Authorization: AWS admin:m9ARrvp8X0DT+cqFcynaJJ87ahY=
< 

> HTTP/1.1 206 Partial Content
> Content-Range: bytes 0-10/847
> Content-Length: 11
> Accept-Ranges: bytes
> Last-Modified: Sun, 06 Nov 2016 07:11:13 GMT
> ETag: "320c1c0f22dc91d94afe36a042ebc89d"
> x-amz-request-id: tx0000000000000000004da-00581ed887-857b-default
> Content-Type: binary/octet-stream
> Date: Sun, 06 Nov 2016 07:15:19 GMT
> Connection: Keep-Alive
> 
```

## swift

list buckets
```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg --type swift -m get -r '/swift/v1' -v
< GET /swift/v1 HTTP/1.1
< Host: 192.168.10.147:8081
< Connection: keep-alive
< Accept-Encoding: gzip, deflate
< Accept: */*
< User-Agent: python-requests/2.11.1
< x-auth-token: AUTH_rgwtk0b00000061646d696e3a61646d696e0dcfa6921a61c714382a20585e421a32843e0f66e22fa391d87c6c40ae28dd6add5bd33c
< 

> HTTP/1.1 200 OK
> X-Timestamp: 1478416569.39780
> X-Account-Container-Count: 7
> X-Account-Object-Count: 1045
> X-Account-Bytes-Used: 314574689
> X-Account-Bytes-Used-Actual: 314601472
> X-Trans-Id: tx0000000000000000004dc-00581ed8b8-857b-default
> Content-Type: text/plain; charset=utf-8
> Content-Length: 77
> Date: Sun, 06 Nov 2016 07:16:09 GMT
> Connection: Keep-Alive
> 
bucket11
yuliyang
yuliyang2
yuliyang3
yuliyang4
yuliyang4_segments
yuliyang6
```

list bucket

```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg --type swift -m get -r '/swift/v1/yuliyang2' -v
< GET /swift/v1/yuliyang2 HTTP/1.1
< Host: 192.168.10.147:8081
< Connection: keep-alive
< Accept-Encoding: gzip, deflate
< Accept: */*
< User-Agent: python-requests/2.11.1
< x-auth-token: AUTH_rgwtk0b00000061646d696e3a61646d696eafa8ed7a23a72faf482a2058000ccb32b2464cc7b29614a781efcaaaaf9786ceb181b84a
< 

> HTTP/1.1 200 OK
> X-Timestamp: 0.00000
> X-Container-Object-Count: 3
> X-Container-Bytes-Used: 104857605
> X-Container-Bytes-Used-Actual: 104861696
> X-Storage-Policy: default-placement
> X-Trans-Id: tx0000000000000000004de-00581ed8c8-857b-default
> Content-Length: 13
> Accept-Ranges: bytes
> Content-Type: text/plain; charset=utf-8
> Date: Sun, 06 Nov 2016 07:16:25 GMT
> Connection: Keep-Alive
> 
100M
aaa
obj1
```

download file
```
[root@joke ceph-request]# ceph-request -c ceph-request.cfg --type swift -m get -r '/swift/v1/yuliyang/obj1'  --download swiftdownobj1 -v
< GET /swift/v1/yuliyang/obj1 HTTP/1.1
< Host: 192.168.10.147:8081
< Connection: keep-alive
< Accept-Encoding: gzip, deflate
< Accept: */*
< User-Agent: python-requests/2.11.1
< x-auth-token: AUTH_rgwtk0b00000061646d696e3a61646d696ebc5791c83d51c5875d2a2058bdfaeb2d99770937a98eab5687d5fdf349012b813ca44223
< 

> HTTP/1.1 200 OK
> Content-Length: 162
> Accept-Ranges: bytes
> Last-Modified: Sat, 05 Nov 2016 14:49:53 GMT
> X-Timestamp: 1478357393.34874
> etag: 0b1895e0e256eb9993fe72cbd4719a64
> X-Trans-Id: tx0000000000000000004e0-00581ed8dd-857b-default
> Content-Type: binary/octet-stream
> Date: Sun, 06 Nov 2016 07:16:45 GMT
> Connection: Keep-Alive
> 
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
