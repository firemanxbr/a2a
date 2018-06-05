# a2a
Python Aggregator to Ansible Playbooks

The Python Aggregator to Ansible Playbooks was created to address a gap not provided by the Ansible project. When you need to clone two or more git repositories with your playbooks and run in a sequence you can use the A2A.


## Installation
The installation works quickly and simply, it only needs a few steps:

```
$ git clone https://github.com/firemanxbr/a2a.git
$ pip3 install -r a2a / requirements.txt --user
```


## Quick start
The configuration of A2A only requires that you edit the configure.yaml file by entering the structure as shown below:

```
1:
  repo: "https://github.com/firemanxbr/a2a-sample.git"
  branch: "master"
  force_clone: True
  command: "ansible-playbook -vv -i 'localhost,' repositories/a2a-sample/playbook.yml --private-key=~/.ssh/id_rsa"
```

In line **1**, the ID of the aggregator is left, allowing you to add as many IDs as you need. Variables:

* **repo:** link to clone the repository, if you already have your ansible-playbooks locally you will not need this item, you can change the value to **"None"** or **""**.

* **branch:** git branch that should be used. If you choose to use the clone feature, you must fill in some branch, usually **"master"**.

* **force_clone:** ​​will erase the destination directory of your repository and only after deleting will clone, if it is not necessary to delete the directory and it is empty, the value can be "False". If the directory already exists it will generate an error.

* **command:** In this parameter the value will be your ansible command or any other shell command that you want to run in this exact sequence. 

The a2a tool is simple to use as any other command you have in your system.

```
$ ./a2a --help
Usage: ./a2a [file]

Python Aggregator to Ansible Playbooks.

Arguments:
  file         parameter file, if 'None' will use the default (default: configure.yaml)

Other actions:
  -h, --help   Show the help
```

### Development
This project it's using Python3, Pipenv, and Fire. These requirements are included into [`requirements.txt`](requirements.txt)

[**Python3**](https://www.python.org/) - will permit to explore the new resources of the Python language.

[**Pipenv**](https://github.com/pypa/pipenv) - is providing the better dependence management and development environment.

[**Clize**](https://github.com/epsy/clize) - is a CLI library to permit develop awesome CLI commands, much easier than argparser. 