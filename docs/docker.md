# Docker

There are two docker compose files within this repository:

* ``docker-compose.yml`` contains the dev environment
* ``prod.yml`` contains the production environment

# Dev Environment

ToDo

# Production Environment

1. Create a new user called ``tickets`` and add it into the ``docker`` group:
```
useradd tickets
usermod -aG docker tickets
```
1. Run ``docker-compose -f prod.yml build``
1. Create a systemd startup file for this docker-compose image:
```
# /etc/systemd/system/docker-compose-tickets.service

[Unit]
Description=Docker Compose Tickets App Service
Requires=docker.service
After=docker.service

[Service]
User=tickets
Group=Tickets
WorkingDirectory=/home/tickets/django_upgrade_video/
ExecStart=/usr/local/bin/docker-compose -f prod.yml up
ExecStop=/usr/local/bin/docker-compose -f prod.yml stop
TimeoutStartSec=0
Restart=on-failure
StartLimitIntervalSec=60
StartLimitBurst=3

[Install]
```
1. Reload systemd: ``systemctl daemon-reload``
1. And enable the service: ``systemctl enable docker-compose-tickets``
1. Start the service (or reboot): ``systemctl start docker-compose-tickets``


