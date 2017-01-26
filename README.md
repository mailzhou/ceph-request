# ceph radosgw 工具，支持 S3/SWIFT/ADMIN REST API

> 暂不支持window版本

# 安装
```
方式1：
git clone git@github.com:wzyuliyang/ceph-request.git 
cd ceph-request
python setup.py install
方式2：
pip install ceph-request
```

# 使用
## 创建配置文件，填写用户信息

```
vim ceph-request.cfg 
[s3]                   #s3账户配置
host = 192.168.10.147  #radosgw地址
port = 8081            #radosgw端口
access_key = admin     #s3 access key
secret_key = admin     #s3 secret key
[swift]                #swift账户配置
host = 192.168.10.147  #radosgw地址
port = 8081            #radosgw端口
subuser = admin:admin  #swift账户名字 
secret_key = gA2BrFTKD3GyDd9b3FIOxDih0PRZBFda13f92GxP #swift账户 secret key
```
## 帮助
```
ceph-request -h
```

## s3功能例子
创建名叫 yuliyang的桶，-v显示请求详细信息
```
ceph-request -c ceph-request.cfg -m put -r '/yuliyang' -v
```
删除名叫 yuliyang的桶
```
ceph-request -c ceph-request.cfg -m delete -r '/yuliyang2222' -v   
```
上传对象到yuliyang6 这个桶，上传后的对象名object1,本地的待上传文件名字setup.py
```
ceph-request -c ceph-request.cfg -m put -r '/yuliyang6/object1' --file setup.py  -v    
```
上传对象，对象内容为--content字符串指定
```
ceph-request -c ceph-request.cfg -m put -r '/yuliyang6/object2' --content 'sdadsa' -v
```
删除对象
```
ceph-request -c ceph-request.cfg -m delete -r '/yuliyang6/object2'  -v                     
```
获取桶的location信息
```
ceph-request -c ceph-request.cfg -m get -r '/yuliyang6?location' -v
```
获取桶的acl
```
ceph-request -c ceph-request.cfg -m get -r '/yuliyang6?acl' -v        
```
设置桶的acl
```
ceph-request -c ceph-request.cfg -m put -r '/yuliyang6?acl' -v  --content '<?xml version="1.0" encoding="UTF-8"?><AccessControlPolicy xmlns="http://s3.amazonaws.com/doc/2006-03-01/"><Owner><ID>admin</ID><DisplayName>admin</DisplayName></Owner><AccessControlList><Grant><Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser"><ID>admin</ID><DisplayName>admin</DisplayName></Grantee><Permission>READ</Permission></Grant></AccessControlList></AccessControlPolicy>'
```
给对象设置自定义metadata属性
```
ceph-request -c ceph-request.cfg -m put -r '/yuliyang2/obj1'  --headers '{"x-amz-meta-cmcc":"onestgroup2"}'
#获取对象属性
ceph-request -c ceph-request.cfg -m head -r '/yuliyang2/obj1' -v                                       
```
下载对象的一部分
```
ceph-request -c ceph-request.cfg  -m get -r '/yuliyang6/object1' --headers '{"Range": "bytes=0-10"}'  -v --download rangedownload -v 
```
开启桶的多版本

```
ceph-request -c ceph-request.cfg -m put -r '/version?versioning' -v --content '<?xml version="1.0" encoding="UTF-8"?><VersioningConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/"><Status>Enabled</Status></VersioningConfiguration>'
```
挂起（暂停）多版本
```
ceph-request -c ceph-request.cfg -m put -r '/version?versioning' -v --content '<?xml version="1.0" encoding="UTF-8"?><VersioningConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/"><Status>Suspended</Status></VersioningConfiguration>'
```
列出version桶内所有对象，包括多版本对象的其他版本
```
ceph-request -c ceph-request.cfg -m get -r '/version?versions' |xmllint  --format -
```
列出某个对象的所有版本
```
ceph-request -c ceph-request.cfg -m get -r '/version?versions&prefix=obj1' |xmllint  --format -
```

## swift功能例子
>使用tempauth
列出所有容器
```
ceph-request -c ceph-request.cfg --type swift -m get -r '/swift/v1' -v
```
列出容器内对象
```
ceph-request -c ceph-request.cfg --type swift -m get -r '/swift/v1/yuliyang2' -v
```
按对象前缀列出容器内对象
```
ceph-request -c ceph-request.cfg --type swift   -m get -r '/swift/v1/lyhbucket?prefix=prefix1' -v
```
限制列出对象请求返回的对象数 
```
# list only 4 object
ceph-request -c ceph-request.cfg --type swift   -m get -r '/swift/v1/lyhbucket?&limit=4' -v 
```
下载对象
```
ceph-request -c ceph-request.cfg --type swift -m get -r '/swift/v1/yuliyang/obj1'  --download swiftdownobj1 -v
```
创建容器
```
ceph-request -c ceph-request.cfg --type swift -m put -r '/swift/v1/yuliyang7' -v
```
删除容器
```
ceph-request -c ceph-request.cfg --type swift -m delete -r '/swift/v1/yuliyang7' -v    
```
获取容器属性
```
ceph-request -c ceph-request.cfg --type swift -m head -r '/swift/v1/yuliyang7' -v
```
拷贝对象
```
#create object
ceph-request -c yuliyang.cfg --type swift  -m put -r '/swift/v1/yuliyang-b1/obj2' -v  --content 'dassduadhkwkdkad'

#copy object
ceph-request -c yuliyang.cfg --type swift   -m put -r '/swift/v1/yuliyang-b2/obj2copy' -v  --headers '{"X-Copy-From": "/yuliyang-b1/obj2"}'

# get object 
ceph-request -c yuliyang.cfg --type swift   -m get -r '/swift/v1/yuliyang-b2/obj2copy' -v
```
设置容器可读
```
ceph-request -c ceph-request.cfg --type swift   -m post -r '/swift/v1/asdadas' -v --headers '{"x-container-read": ".r:*"}'
```
设置容器可写
```
ceph-request -c ceph-request.cfg --type swift   -m post -r '/swift/v1/asdadas' -v --headers '{"x-container-write": ".r:*"}'
```
设置容器公开可读可写
```
ceph-request -c ceph-request.cfg --type swift   -m post -r '/swift/v1/asdadas' -v --headers '{"x-container-read": ".r:*","x-container-write": ".r:*"}'
```
tempurl分享
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


#s3
import hmac
import base64
from hashlib import sha1
from urllib import quote_plus
Host = "192.168.10.201"
access_key = "test"
Expires = "1483802998"
Bucket = "new-bucket-6ecf1981"
Object = "2016-12-13_153252.jpg"
print "http://"+Host+"/"+Bucket+"/"+Object+"?AWSAccessKeyId="+access_key+"&Expires="+Expires+"&Signature="+ \
      quote_plus(base64.encodestring(hmac.new("test","GET\n\n\n"+Expires+"\n/"+Bucket+"/"+Object, sha1).digest()).strip())
```

## admin rest api 管理员接口

显示统计信息
```
# add user cap
radosgw-admin caps add --uid=admin --caps="users=*;buckets=*;metadata=*;usage=*;zone=*"
# enable usage log
cat /etc/ceph/ceph.conf |grep rgw_enable_usage_log
rgw_enable_usage_log = True
# show usage
ceph-request -c ceph-request.cfg  -m get -r '/admin/usage?format=json' |python -c 'import sys, json; print json.dumps(json.load(sys.stdin),indent=4)'
```

设置用户配额
```
ceph-request -c ceph-request.cfg  -m put -r '/admin/user?quota&uid=admin&quota-type=user' -v --content='{"enabled":true,"max_size_kb":102400,"max_objects":10000}'
```
获取用户配额
```
ceph-request -c ceph-request.cfg  -m get -r '/admin/user?quota&uid=admin&quota-type=user' -v 
```
创建父用户
```
ceph-request -c ceph-request.cfg -m put -r '/admin/user?format=json&uid=user2&display-name=user2&email=user2@test.com' -v
```
删除父用户
```
ceph-request -c ceph-request.cfg -m delete -r '/admin/user?format=json&uid=user2&purge-data=True' -v
```
删除子用户(swift)
```
ceph-request -c ceph-request.cfg -m put -r '/admin/user?format=json&uid=admin&subuser=user2-sub1&access=full&generate-secret=True' -v
```
获取用户信息 
```
ceph-request -c ceph-request.cfg -m get -r '/admin/user?format=json&uid=user1' -v
```
列出所有用户
```
ceph-request -c ceph-request.cfg -m get -r '/admin/metadata/user?format=json' -v
```
列出某个用户的所有桶列表
```
ceph-request -c ceph-request.cfg -m get -r '/admin/bucket?format=json&uid=yuliyang' -v
```
获取桶的index
```
ceph-request -c ceph-request.cfg -m get -r '/admin/bucket?index&format=json&bucket=yuliyang-b1&check-object=True&fix=True' -v
```

创建s3密钥(子账户)
```
ceph-request -c admin  -m put -r '/admin/user?key&format=json&uid=user2&subuser=swift4&key-type=s3' |json
```

创建s3密钥(父账户)
```
ceph-request -c admin  -m put -r '/admin/user?key&format=json&uid=user2&key-type=s3' |json
```
