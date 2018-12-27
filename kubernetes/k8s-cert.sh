# -------------1. 生成CA证书-------------
cat > ca-config.json << EOF
{
    "signing":{
        "default":{
            "expiry":"87600h"
        },
        "profiles":{
            "kubernetes":{
                "expiry":"87600h",
                "usages":[
                    "signing",
                    "key encipherment",
                    "server auth",
                    "client auth"
                ]
            }
        }
    }
}
EOF
# -------------2. CA证书签名请求-------------
#  O 表示：一个通用名称  k8s中的一个用户
# OU 表示：一个组织一个团体，k8s中的一个组
cat > ca-csr.json << EOF
{
    "CN":"kubernetes",
    "key":{
        "algo":"rsa",
        "size":2048
    },
    "names":[
        {
            "C":"CN",
            "L":"BeiJing",
            "ST":"BeiJing",
            "O":"k8s",
            "OU":"System"
        }
    ]
}
EOF
# 生成证书命令
cfssl gencert -initca ca-csr.json | cfssljson -bare ca - 

# -------------3. server证书创建-------------
# hosts包含:
#     "hosts":[
#         "10.0.0.1",         # apiserver在集群内部的一些地址，必须保留
#         "127.0.0.1",        # 必须的
#         "192.168.4.150",    # 负载均衡的VIP
#         "192.168.4.151",    # 负载均衡的IP
#         "192.168.4.157",    # 负载均衡的IP
#         "192.168.4.153",    # kubernetes 的master01  IP
#         "192.168.4.154",    # kubernetes 的master02  IP
#         "kubernetes",        # 有些服务通过这个名称访问这个server（以下都是）
#         "kubernetes.default",
#         "kubernetes.default.svc",
#         "kubernetes.default.svc.cluster",
#         "kubernetes.default.svc.cluster.local"
#     ]
cat > server-csr.json << EOF
{
    "CN":"kubernetes",
    "hosts":[
        "10.0.0.1",
        "127.0.0.1",
        "192.168.4.150",
        "192.168.4.151",
        "192.168.4.157",
        "192.168.4.153",
        "192.168.4.154",
        "kubernetes",
        "kubernetes.default",
        "kubernetes.default.svc",
        "kubernetes.default.svc.cluster",
        "kubernetes.default.svc.cluster.local"
    ],
    "key":{
        "algo":"rsa",
        "size":2048
    },
    "names":[
        {
            "C":"CN", 
            "L":"BeiJing",
            "ST":"BeiJing",
            "O":"k8s",
            "OU":"System"
        }
    ]
}
EOF

cfssl gencert -ca=ca.pem -ca-key=ca-key.pem -config=ca-config.json -profile=kubernetes server-csr.json | cfssljson -bare server

# ---4.admin证书是用于使用 kube-controller 来访问集群时的证书-----
cat > admin-csr.json << EOF
{
    "CN":"admin",
    "hosts":[],
    "key":{
        "algo":"rsa",
        "size":2048
    },
    "names":[
        {
            "C": "CN", 
            "L": "Beijing",
            "ST": "Beijing",
            "O": "system:masters",
            "OU":"System"
        }
    ]
}
EOF
cfssl gencert -ca=ca.pem -ca-key=ca-key.pem -config=ca-config.json -profile=kubernetes admin-csr.json | cfssljson -bare admin


# ---5. 通过这个证书可以访问ApiServer
cat > kube-proxy-csr.json << EOF
{
    "CN":"system:kube-proxy",
    "hosts":[],
    "key":{
        "algo":"rsa",
        "size":2048
    },
    "names":[
        {
            "C":"CN", 
            "L":"Beijing",
            "ST":"Beijing",
            "O":"k8s",
            "OU":"System"
        }
    ]
}
EOF
cfssl gencert -ca=ca.pem -ca-key=ca-key.pem -config=ca-config.json -profile=kubernetes kube-proxy-csr.json  | cfssljson -bare kube-proxy











