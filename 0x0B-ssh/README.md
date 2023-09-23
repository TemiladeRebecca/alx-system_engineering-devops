# 0x0B-ssh
 
## Project description:
- What is a server
- Where servers usually live
- What is SSH
- How to create an SSH RSA key pair
- How to connect to a remote host using an SSH RSA key pair
- The advantage of using `#!/usr/bin/env` bash instead of `/bin/bash`

## Tasks description:

* [0-use_a_private_key](./0-use_a_private_key): Bash script that uses `ssh` to connect to my
server using the private key ~/.ssh/school with the user ubuntu

* [1-create_ssh_key_pair](./1-create_ssh_key_pair): Bash script that creates an RSA key pair.
	- Name of the created private key must be school
	- Number of bits in the rsa key pair to be generated: 4096
	- The created key must be protected by the passphrase betty

* [2-ssh_config](./2-ssh_config): SSH configuration file configured to use the private key
`~/.ssh/school` and to refuse authentication using a password.
- SSH client configuration must be configured to use the private key ~/.ssh/school
- SSH client configuration must be configured to refuse to authenticate using a password

* [100-puppet_ssh_config.pp](./100-puppet_ssh_config.pp): Puppet manifest that makes changes to our configuration file
- Your SSH client configuration must be configured to use the private key ~/.ssh/school
- Your SSH client configuration must be configured to refuse to authenticate using a password
