#!/bin/bash
# name:apiserver.sh 
# example : bash  apiserver.sh 192.168.4.153 https://192.168.4.153:2379,https://192.168.4.154:2379,https://192.168.4.155:2379
MASTER_ADDRESS=$1
ETCD_SERVERS=$2

cat << EOF >/opt/kubernetes/cfg/kube-apiserver

KUBE_APISERVER_OPTS="--admission-control=NamespaceLifecycle,LimitRanger,ServiceAccount,DefaultStorageClass,ResourceQuota,NodeRestriction \
--advertise-address=${MASTER_ADDRESS} \\
--bind-address=${MASTER_ADDRESS} \\
--secure-port=6443 \\
--authorization-mode=Node,RBAC \\
# --runtime-config=rbac.authorization.k8s.io/v1beta1 \\
--kubelet-https=true \\
--token-auth-file=/opt/kubernetes/cfg/token.csv \\
--service-cluster-ip-range=10.0.0.0/24 \\
--service-node-port-range=10000-60000 \\
--tls-cert-file=/opt/kubernetes/ssl/server.pem \\
--tls-private-key-file=/opt/kubernetes/ssl/server-key.pem \\
--client-ca-file=/opt/kubernetes/ssl/ca.pem \\
--service-account-key-file=/opt/kubernetes/ssl/ca-key.pem \\
--etcd-cafile=/opt/etcd/ssl/ca.pem \\
--etcd-certfile=/opt/etcd/ssl/server.pem \\
--etcd-keyfile=/opt/etcd/ssl/server-key.pem \\
# --storage-backend=etcd3 \\
--etcd-servers=${ETCD_SERVERS}  \\
# --enable-swagger-ui=true \\
--allow-privileged=true \\ 
# --apiserver-count=3 \\
# --audit-log-maxage=30 \\
# --audit-log-maxbackup=3 \\
# --audit-log-maxsize=100 \\
# --audit-log-path=/var/lib/audit.log \\
# --event-ttl=1h \\
--logtostderr=true \\
#--log-dir=/var/log/kubernetes/apiserver \\
--v=4"
EOF

cat << EOF >/usr/lib/systemd/system/kube-apiserver.service
[Unit]
Description=Kubernetes API Server
Documentation=https://github.com/kubernetes/kubernetes
After=network.target

[Service]
Type=notify
EnvironmentFile=-/opt/kubernetes/cfg/kube-apiserver
ExecStart=/opt/kubernetes/bin/kube-apiserver \$KUBE_APISERVER_OPTS
Restart=on-failure
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable kube-apiserver
systemctl restart kube-apiserver








