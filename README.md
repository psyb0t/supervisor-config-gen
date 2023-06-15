# supervisor-config-gen

supervisor-config-gen is a bash script that simplifies the process of creating generic configuration files for Supervisor, allowing developers to focus on building software.

## Prerequisites

- Bash shell: This tool is written in Bash, so ensure that you have Bash installed on your machine before using it.

## Installation

Execute the following command to download supervisor-config-gen:

```shell
wget -qO- https://raw.githubusercontent.com/psyb0t/supervisor-config-gen/master/supervisor-config-gen > supervisor-config-gen
chmod +x supervisor-config-gen
```

After the download is complete, you can use supervisor-config-gen from the current location by executing `./supervisor-config-gen` but a true installation allows you to use it from any directory.

### Installing for all users

If you have root privileges, you can make the script available to all users:

```shell
sudo mv supervisor-config-gen /usr/local/bin/
```

### Installing for the current user

If you don't have root privileges or want to limit the script to the current user:

```shell
mkdir -p ~/bin
mv supervisor-config-gen ~/bin/
```

In order to execute supervisor-config-gen from any directory, the `$HOME/bin` directory needs to be added to your system's `$PATH`. This is because the `$PATH` variable tells the system which directories to search for executable files when you type a command in the terminal. By adding `$HOME/bin` to the `$PATH`, you can run the supervisor-config-gen command from any directory without needing to specify the full path.

To check if `$HOME/bin` is already in the `$PATH`, you can execute the following command in your terminal:

```shell
echo $PATH | grep -q "$HOME/bin" && echo "The $HOME/bin directory is already in your PATH" || echo "The $HOME/bin directory is not in your PATH yet"
```

This command will output a message indicating whether `$HOME/bin` is already in your path.

If it is not, add it to your shell profile file:

For `bash`:

```shell
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

For `zsh`:

```shell
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

Now you should be able to run `supervisor-config-gen` from any directory.

## Usage

supervisor-config-gen is meant to be used within the directory where your application resides. Ensure that your application has a valid directory structure before using this tool.

Here is an example of a directory structure for "shitty-app", an application name:

```bash
shitty-app                            # Application Name/Directory
├── main.py                           # Main Application Code
└── run.sh                            # Executable Script That Starts the Application
```

To generate the Supervisor configuration file, navigate to the directory of your application and execute the following command:

```bash
% cd shitty-app
% supervisor-config-gen
Generated shitty-app-supervisor.conf
```

The generated configuration file will be stored in your application's directory:

```bash
% ls
main.py  run.sh  shitty-app-supervisor.conf
```

You can view the generated configuration file by executing the following command:

```bash
cat shitty-app-supervisor.conf
[program:shitty-app]
command=/home/not-root/shitty-app/run.sh
directory=/home/not-root/shitty-app
process_name=%(program_name)s
numprocs=1
user=not-root

stopsignal=TERM
stopwaitsecs=10
stopasgroup=true

killasgroup=true

autostart=true
autorestart=true

redirect_stderr=true
redirect_stdout=true

stdout_logfile=/home/not-root/logs/supervisord/%(program_name)s-out.log
stdout_logfile_maxbytes=50MB
stdout_logfile_backups=10
stderr_logfile=/home/not-root/logs/supervisord/%(program_name)s-err.log
stderr_logfile_maxbytes=50MB
```

With supervisor-config-gen, you can create standardized Supervisor configuration files quickly and easily - Good luck with your coding!
