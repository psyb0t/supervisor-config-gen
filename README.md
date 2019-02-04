# supervisor-config-gen

create generic supervisor config in the current directory.

## installation

```
% git clone https://github.com/psyb0t/supervisor-config-gen.git
% cp supervisor-config-gen/supervisor-config-gen /usr/local/bin/supervisor-config-gen
```

or

```
% curl https://raw.githubusercontent.com/psyb0t/supervisor-config-gen/master/supervisor-config-gen > /usr/local/bin/supervisor-config-gen
% chmod +x /usr/local/bin/supervisor-config-gen
```

...or...

```
% echo "alias supervisor-config-gen='curl --silent https://raw.githubusercontent.com/psyb0t/supervisor-config-gen/master/supervisor-config-gen | bash'" >> ~/.bashrc
% source ~/.bashrc
```

## example usage

```
shitty-app                            # app name/residing directory
├── main.py                           # main app code
└── run.sh                            # startup executable script that runs the main app code
```

```
% cd shitty-app
% supervisor-config-gen
Generated shitty-app-supervisor.conf
% ls
main.py  run.sh  shitty-app-supervisor.conf
% cat shitty-app-supervisor.conf
[program:shitty-app]
command=/home/not-root/supervisor-config-gen/shitty-app/run.sh
directory=/home/not-root/supervisor-config-gen/shitty-app
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
