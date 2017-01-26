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
创建桶，-v显示请求详细信息
```
ceph-request -c ceph-request.cfg -m put -r \
'/{bucket}' \
-v
```
删除桶
```
ceph-request -c ceph-request.cfg -m delete -r \
'/{bucket}' \
-v   
```
上传对象到桶
```
ceph-request -c ceph-request.cfg -m put -r \
'/{bucket}/{object}' \
--file localfile.txt  -v    
```
上传对象，对象内容为--content字符串指定
```
ceph-request -c ceph-request.cfg -m put -r \
'/{bucket}/{object}' \
--content 'string' -v
```
删除对象
```
ceph-request -c ceph-request.cfg -m delete -r \
'/{bucket}/{object}'  \
-v                     
```
获取桶的location信息
```
ceph-request -c ceph-request.cfg -m get -r \
'/{bucket}?location' \
-v
```
获取桶的acl
```
ceph-request -c ceph-request.cfg -m get -r  \
'/{bucket}?acl' \
-v        
```
设置桶的acl
```
ceph-request -c ceph-request.cfg -m put -r \
'/{bucket}?acl' \
-v  --content '<?xml version="1.0" encoding="UTF-8"?><AccessControlPolicy xmlns="http://s3.amazonaws.com/doc/2006-03-01/"><Owner><ID>admin</ID><DisplayName>admin</DisplayName></Owner><AccessControlList><Grant><Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser"><ID>admin</ID><DisplayName>admin</DisplayName></Grantee><Permission>READ</Permission></Grant></AccessControlList></AccessControlPolicy>'
```
给对象设置自定义metadata属性
```
ceph-request -c ceph-request.cfg -m put -r \
'/{bucket}/{object}' \
--headers '{"x-amz-meta-cmcc":"onestgroup2"}'
#获取对象属性
ceph-request -c ceph-request.cfg -m head -r \
'/{bucket}/{object}' \
-v                                       
```
下载对象的一部分
```
ceph-request -c ceph-request.cfg  -m get -r \
'/{bucket}/{object}' \
--headers '{"Range": "bytes=0-10"}' -v --download rangedownload -v 
```
开启桶的多版本

```
ceph-request -c ceph-request.cfg -m put -r  \
'/{bucket}?versioning' \
-v --content '<?xml version="1.0" encoding="UTF-8"?><VersioningConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/"><Status>Enabled</Status></VersioningConfiguration>'
```
挂起（暂停）多版本
```
ceph-request -c ceph-request.cfg -m put -r \
'/{bucket}?versioning' \
-v --content '<?xml version="1.0" encoding="UTF-8"?><VersioningConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/"><Status>Suspended</Status></VersioningConfiguration>'
```
列出version桶内所有对象，包括多版本对象的其他版本
```
ceph-request -c ceph-request.cfg -m get -r \
'/{bucket}?versions' \
|xmllint  --format -
```
列出某个对象的所有版本
```
ceph-request -c ceph-request.cfg -m get -r \
'/{bucket}?versions&prefix={obj_prefix}' \
|xmllint  --format -
```

## swift功能例子
>使用tempauth

列出所有容器
```
ceph-request -c ceph-request.cfg --type swift -m get -r \
'/swift/v1' \
-v
```
列出容器内对象
```
ceph-request -c ceph-request.cfg --type swift -m get -r \
'/swift/v1/{bucket}' \
-v
```
按对象前缀列出容器内对象
```
ceph-request -c ceph-request.cfg --type swift -m get -r \
'/swift/v1/{bucket}?prefix={prefix}' \
-v
```
限制列出对象请求返回的对象数 
```
# list only 4 object
ceph-request -c ceph-request.cfg --type swift -m get -r \
'/swift/v1/{bucket}?&limit=4' \
-v 
```
下载对象
```
ceph-request -c ceph-request.cfg --type swift -m get -r \
'/swift/v1/{bucket}/{object}'  -\
-download swiftdownobj1 -v
```
创建容器
```
ceph-request -c ceph-request.cfg --type swift -m put -r \
'/swift/v1/{bucket}' \
-v
```
删除容器
```
ceph-request -c ceph-request.cfg --type swift -m delete -r  \
'/swift/v1/{bucket}' \
-v    
```
获取容器属性
```
ceph-request -c ceph-request.cfg --type swift -m head -r \
'/swift/v1/{bucket}' \
-v
```
拷贝对象
```
#create object
ceph-request -c yuliyang.cfg --type swift -m put -r \
'/swift/v1/{bucket}/{object}' \
-v  --content 'string'

#copy object
ceph-request -c yuliyang.cfg --type swift -m put -r \
'/swift/v1/{bucket}/{object}' \
-v  --headers '{"X-Copy-From": "/{src_bucket}/{src_object}"}'

# get object 
ceph-request -c yuliyang.cfg --type swift -m get -r  \
'/swift/v1/{bucket}/{object}' -v
```
设置容器可读
```
ceph-request -c ceph-request.cfg --type swift -m post -r \
'/swift/v1/{bucket}' \
-v --headers '{"x-container-read": ".r:*"}'
```
设置容器可写
```
ceph-request -c ceph-request.cfg --type swift -m post -r \
'/swift/v1/{bucket}' \
-v --headers '{"x-container-write": ".r:*"}'
```
设置容器公开可读可写
```
ceph-request -c ceph-request.cfg --type swift -m post -r \
'/swift/v1/{bucket}' \
-v --headers '{"x-container-read": ".r:*","x-container-write": ".r:*"}'
```
tempurl分享
```
ceph-request -c ceph-request.cfg --type swift -m post -r \
'/swift/v1' \
-v --headers '{"X-Account-Meta-Temp-Url-Key": "1122"}'


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
ceph-request -c ceph-request.cfg  -m get -r \
'/admin/usage?format=json'\
|python -c 'import sys, json; print json.dumps(json.load(sys.stdin),indent=4)'
```

设置用户配额
```
ceph-request -c ceph-request.cfg  -m put -r  \
'/admin/user?quota&uid={uid}quota-type=user' \
-v --content='{"enabled":true,"max_size_kb":102400,"max_objects":10000}'
```
获取用户配额
```
ceph-request -c ceph-request.cfg  -m get -r '/admin/user?quota&uid={uid}&quota-type=user' -v 
```
创建父用户
```
ceph-request -c ceph-request.cfg -m put -r \
'/admin/user?format=json&uid={uid}&display-name={display-name}&email=test@test.com' \
-v
```
删除父用户
```
ceph-request -c ceph-request.cfg -m delete -r \
'/admin/user?format=json&uid={uid}&purge-data=True' \
-v
```
删除子用户(swift)
```
ceph-request -c ceph-request.cfg -m put -r \
'/admin/user?format=json&uid={uid}&subuser={subuser}&access=full&generate-secret=True' \
-v
```
获取用户信息 
```
ceph-request -c ceph-request.cfg -m get -r \
'/admin/user?format=json&uid={uid}' -v
```
列出所有用户
```
ceph-request -c ceph-request.cfg -m get -r \
'/admin/metadata/user?format=json' -v
```
列出某个用户的所有桶列表
```
ceph-request -c ceph-request.cfg -m get -r  \
'/admin/bucket?format=json&uid={uid}' -v
```
获取桶的index
```
ceph-request -c ceph-request.cfg -m get -r  \
'/admin/bucket?index&format=json&bucket={bucket}&check-object=True&fix=True' \
-v
```

创建s3密钥(子账户)
```
ceph-request -c admin  -m put -r \
'/admin/user?key&format=json&uid={uid}&subuser={subuser}&key-type=s3' \
|json
```

创建s3密钥(父账户)
```
ceph-request -c admin  -m put -r \
'/admin/user?key&format=json&uid={uid}&key-type=s3' \
|json
```
