#!/bin/bash
# name:scheduler.sh
# 
MASTER_ADDRESS=$1

cat << EOF >/opt/kubernetes/cfg/kube-scheduler
KUBE_SCHEDULER_OPTS="--master=${MASTER_ADDRESS}:8080 \\
--leader-elect \\
--logtostderr=true \\
--v=4"
EOF

cat << EOF >/usr/lib/systemd/system/kube-scheduler.service

[Unit]
Description=Kubernetes Scheduler
Documentation=https://github.com/kubernetes/kubernetes
After=network.target
After=kube-apiserver.service

[Service]
EnvironmentFile=-/opt/kubernetes/cfg/kube-scheduler
ExecStart=/opt/kubernetes/bin/kube-scheduler \$KUBE_SCHEDULER_OPTS
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl restart kube-scheduler