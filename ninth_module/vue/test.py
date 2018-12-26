# -*- coding: utf-8 -*-

# __title__ = 'test.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.12.25'




 /opt/etcd/bin/etcdctl --ca-file=ca.pem --cert-file=server.pem --key-file=server-key.pem --endpoints="https://192.168.4.153:2380,https://192.168.4.154:2380,https://192.168.4.155:2380" cluster-health

[root@k8s_master01 etcd-cert]#
/opt/etcd/bin/etcdctl \
--ca-file=ca.pem --cert-file=server.pem --key-file=server-key.pem \
--endpoints="https://192.168.4.153:2379,https://192.168.4.154:2379,https://192.168.4.155:2379" \
cluster-health





yum-config-manager \
    --add-repo \
    https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo  


/opt/etcd/bin/etcdctl \
--ca-file=ca.pem --cert-file=server.pem --key-file=server-key.pem \
--endpoints="https://192.168.4.153:2379,https://192.168.4.154:2379,https://192.168.4.155:2379" \
set /coreos.com/network/config '{"network":"172.17.0.0/16","Backend":{"Type":"vxlan"}}'




systemctl daemon-reload
systemctl start flanneld












