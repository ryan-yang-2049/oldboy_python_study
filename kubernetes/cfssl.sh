

curl -L https://pkg.cfssl.org/R1.2/cfssl_linux-amd64 -o /usr/local/bin/cfssl      # 生成证书
curl -L https://pkg.cfssl.org/R1.2/cfssljson_linux-amd64 -o /usr/local/bin/cfssljson       # 通过传入json数据格式生成证书
curl -L https://pkg.cfssl.org/r1.2/cfssl-certinfo_linux-amd64 -o /usr/local/bin/cfssl-certinfo # 查看证书信息
chmod +x /usr/local/bin/cfssl  /usr/local/bin/cfssljson /usr/local/bin/cfssl-certinfo







































