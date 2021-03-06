# KB

## Description 
KB is a command line tool to manage Prism instances, services, and service properties.

Everything is managed on a per domain/environment basis. Domain refers to either lab or production. Lab is the default domain. Environment is the puppet environment.
KB tries to use tab completion as much as possible. For example when setting the environment, pressing TAB lists all environments. Or partially typing the environment
and pressing TAB will do an autocomplete.

Predefined variables exist in the .variables file. These variables can be used as short-cuts when using the ssh command. Variables are prefixed with @. There is a
common set of variables that apply to all instances and role-based variables which apply only to specific roles. Typing @ then TAB will list all variables available
for the given role.

Get general help

    > kb --help
    
Get help on a specific command
    
    > kb instances --help
    > kb properties --help

Set the environment

    > kb setenvironment jsabin
    
List all machines in the environment

    > kb instances
    
List machines with a given role

    > kb instances d4::event-indexer
    
List machines that start with a given IP address
    
    > kb instances 10.93.5
    
List machines whose JSON Tags contains specific words

    > kb instances JAB:
    
List machines based on a query where role contains cassadnra and name contains m0044036

    > kb instances -q roles~cassandra\&fqdn~m0054036
    
Execute command on the second machine that has role d4::event-indexer
    
    > kb ssh d4::event-indexer 2 "sudo /etc/runpuppet --fast"
    
Execute command on all machines that have the role d4::event-indexer

    > kb ssh d4::event-indexer all "sudo /etc/init.d/event-indexer start"
    
SSH to the first machine that has role d4::event-indexer

    > kb ssh d4::event-indexer 1
    
Leverage variables defined in .variables file as short-cuts for SSH. This command replace @puppet with "sudo /etc/runpuppet --fast".

    > kb ssh d4::event-indexer 1 @puppet
    
List services in the environment
    
    > kb services 
    
List properties for a given service

    > kb properties myservice
    
Set properties for a service given a JSON file of property name/value pairs

    > kb setproperties myservice mypropertiesfile   
    
Remove property from a service

    > kb rmproperty myservice myproperty
     
Copy a file to several hosts

    > kb scpto d4::event-indexer all myfile.txt /home/myhomedir
    
Create CentOS 6.6 VM instance in AWS

    > kb createinstance awslabcloud m2.xlarge centos6.6 "Test machine"
    
 
## Installation
 
1. Install Pip.
2. Install TextTable - "pip install -U git+http://github.com/bufordtaylor/python-texttable". See https://github.com/bufordtaylor/python-texttable for more information.
3. Install Requests - "pip install requests".
4. Install argcomplete on LINUX

    1. "pip install argcomplete"
    2. "sudo activate-global-python-argcomplete"
    
5. Install argcomplete on OS X
    
    1. Install Homebrew - see http://brew.sh/
    2. Install the latest version of BASH "brew install bash". Verify that BASH is 4.2 or greater "echo $BASH_VERSION".
    3. Change shell by running "csh" and add "/usr/local/bin/bash" to the end of /etc/shells.
    4. Run "activate-global-python-argcomplete --dest /usr/local/etc/bash_completion.d"
    5. Run "source /usr/local/etc/bash_completion.d/python-argcomplete.sh"
    6. Add "source /usr/local/etc/bash_completion.d/python-argcomplete.sh" to your ./bashrc.
    
6. Copy src/kb to a location on your machine
7. Add the directory where kb is to your PATH variable - "export PATH=%PATH:/[path to kb]
8. Since AWS instances are not directly accessible from corp, kb uses a jump host. Currenly this is hard coded to use labProxy.
    
    1. Modify /etc/hosts to add "labproxy	[jump host name or ip address]"
9. Install pssh found at https://code.google.com/archive/p/parallel-ssh. Follow instructions in the INSTALL file.
10. Set lab and production URLs and readonly username and password

    1. export KB_LAB_URL=[lab url]
    2. export KB_PRODUCTION_URL=[production url]
    3. export KB_READONLY_USER=[username]
    4. export KB_READONLY_PASSWORD=[password]
    
## Change Prompt 
This will change the prompt to show the current environment that is set. I put this in my .bashrc file.

function kb_environment {
  environment=`kb environment`
  if [ -n "${environment}" ]; then
        echo [${environment}]
  fi
}

PS1=$PS1'$(kb_environment)'"\$ "
 

