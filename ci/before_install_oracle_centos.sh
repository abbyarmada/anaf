#!/usr/bin/env bash
# this was tested on centos, installing oracle and/or cx_Oracle on debian/ubuntu is theoretically possible, but I gave up on that
sudo yum install libaio bc flex
export DB=oracle

# fake free so we can install oracle
sudo mv /usr/bin/free /usr/bin/free.original
sudo tee /usr/bin/free <<EOF > /dev/null
#!/bin/sh
cat <<__eof
             total       used       free     shared    buffers     cached
Mem:       1048576     327264     721312          0          0          0
-/+ buffers/cache:     327264     721312
Swap:      2000000          0    2000000
__eof
exit
EOF

sudo chmod 755 /usr/bin/free

wget -q http://dl.nucleoos.com.br/oracle-instantclient11.2-basic-11.2.0.4.0-1.x86_64.rpm
wget -q http://dl.nucleoos.com.br/oracle-instantclient11.2-devel-11.2.0.4.0-1.x86_64.rpm
wget -q http://dl.nucleoos.com.br/oracle-instantclient11.2-sqlplus-11.2.0.4.0-1.x86_64.rpm
wget -q http://dl.nucleoos.com.br/oracle-xe-11.2.0-1.0.x86_64.rpm
sudo rpm -ivh oracle-instantclient11.2-basic-11.2.0.4.0-1.x86_64.rpm
sudo rpm -ivh oracle-instantclient11.2-devel-11.2.0.4.0-1.x86_64.rpm
sudo rpm -ivh oracle-instantclient11.2-sqlplus-11.2.0.4.0-1.x86_64.rpm
sudo rpm -ivh oracle-xe-11.2.0-1.0.x86_64.rpm

export ORACLE_VERSION="11.2"
export ORACLE_HOME="/usr/lib/oracle/$ORACLE_VERSION/client64"
export PATH=$PATH:"$ORACLE_HOME/bin"
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:"$ORACLE_HOME/lib"
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:"/u01/app/oracle/product/11.2.0/xe/sqlplus/mesg"
pip install cx_Oracle

sudo cp /usr/bin/free.original /usr/bin/free

# Configure the server; provide the answers for the following questions:
# The HTTP port for Oracle Application Express: 8080
# A port for the database listener: 1521
# The password for the SYS and SYSTEM database accounts: admin
# Start the server on boot: yes
sudo /etc/init.d/oracle-xe configure <<END
8080
1521
admin
admin
y
END