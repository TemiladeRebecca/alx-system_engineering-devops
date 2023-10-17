# 0x14-mysql

## Task description

* Installing Mysql on both servers:
    - copy signature key for package verification at https://dev.mysql.com/doc/refman/5.7/en/checking-gpg-signature.html
    key is present in file 'signature.key'. Save key in a file 'signature.key' on server
    - add the key to the server's apt keyring:
    sudo apt-key add signature.key
    - add the apt repo to the server's sources list:
    sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'
    - update the package list:
    sudo apt-get update
    - Install the mysql server 5.7:
    sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*

    - Ensure that Alx public key is in the '/.ssh/authorized_keys' file of the ubuntu user on both servers to enable access to the servers for check

    - Create a Alx user on both servers with given username and password and host, to enable access to the Mysql servers for check:
    `CREATE USER ‘user’@‘localhost' IDENTIFIED WITH mysql_native_password BY 'password';`

    - Make sure Alx user has permission to check the primary/replica status of your databases:
    `GRANT REPLICATION SLAVE ON *.* TO 'user'@'localhost';`

* Create a database on the primary server, create a table and add data to it:
    - replicate the database on the replica server
    - Make sure Alx has SELECT priveleges on table to check table exists and has data:
    `GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';`

* Each replica in a MySQL replication environment connects to the source database with a username and password. 
Replicas can connect using any MySQL user profile that exists on the source database and has the appropriate privileges.
    - Create a user('replica_user') on the source database that the replica can use to connect to the source database, with prefered password and
    host = '%' to enable access to the source database from any host and not only from replica server.
    `CREATE USER ‘replica_user’@‘%’ IDENTIFIED WITH mysql_native_password BY 'password';`
    - Grant the user the privileges required for replication- The user must have the REPLICATION SLAVE privilege;
    `GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';`
    - Make sure Alx has SELECT priveleges on mysql.user to confirm the replica exist
'GRANT SELECT ON mysql.user to 'holberton_user'@'localhost';'
    - Flush privileges:
    `flush privileges;`
