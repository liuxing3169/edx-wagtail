1. Clone repos
    ```
    cd /edx/app
    git clone https://github.com/liuxing3169/edx-wagtail.git
    ```
2. Create python virtual environment & Installation dependencies 
    ```
    cd edx-wagtail
    python3 -m venv env
    source env/bin/activate
    pip install -r cms/requirements.txt
    deactivate
    ```
3. Create a configuration file for wagtail application
    ```
    touch /edx/etc/wagtail.yml
    vi /edx/etc/wagtail.yml
    ```
    And its content is like this: (can copy from edx/etc/lms.yml)

    ```
    DATABASES:
        default:
            ATOMIC_REQUESTS: true
            CONN_MAX_AGE: 0
            ENGINE: django.db.backends.mysql
            HOST: localhost
            NAME: edxapp
            OPTIONS: {}
            PASSWORD: yourPASSWORD
            PORT: '3306'
            USER: edxapp001
        read_replica:
            CONN_MAX_AGE: 0
            ENGINE: django.db.backends.mysql
            HOST: localhost
            NAME: edxapp
            OPTIONS: {}
            PASSWORD: yourPASSWORD
            PORT: '3306'
            USER: edxapp001
        student_module_history:
            CONN_MAX_AGE: 0
            ENGINE: django.db.backends.mysql
            HOST: localhost
            NAME: edxapp_csmh
            OPTIONS: {}
            PASSWORD: yourPASSWORD
            PORT: '3306'
            USER: edxapp_cmsh001
    ```
4. Run database migrate
    ```
    cd /edx/app/edx-wagtail
    source env/bin/activate
    export WAGTAIL_CFG=/edx/etc/wagtail.yml
    python cms/manage.py help
    python cms/manage.py makemigrations
    python cms/manage.py migrate
    deactivate
    ```
5. Add wagtail to supervisor
    ```
    cd /edx/app/supervisor/conf.available.d
    touch wagtail.conf
    vi wagtail.conf
    ```
    And its content is like this: 
    ```
    [program:wagtail]

    command=/edx/app/edx-wagtail/wagtail.sh

    user=www-data
    directory=/edx/app/edx-wagtail/cms
    stdout_logfile=/edx/var/log/supervisor/%(program_name)s-stdout.log
    stderr_logfile=/edx/var/log/supervisor/%(program_name)s-stderr.log
    killasgroup=true
    stopasgroup=true
    ```
    Then change file's owner
    ```
    sudo chown supervisor:supervisor wagtail.conf
    ```
    Reload the supervisor service to add wagtail to the services
    ```
    # sudo /edx/bin/supervisorctl 
    analytics_api                    RUNNING   pid 1385, uptime 1 day, 0:38:03
    certs                            RUNNING   pid 1388, uptime 1 day, 0:38:03
    cms                              RUNNING   pid 1392, uptime 1 day, 0:38:03
    discovery                        RUNNING   pid 1395, uptime 1 day, 0:38:03
    ecommerce                        RUNNING   pid 1396, uptime 1 day, 0:38:03
    ecomworker                       RUNNING   pid 1397, uptime 1 day, 0:38:03
    edxapp_worker:cms_default_1      RUNNING   pid 1398, uptime 1 day, 0:38:03
    edxapp_worker:cms_high_1         RUNNING   pid 1399, uptime 1 day, 0:38:03
    edxapp_worker:lms_default_1      RUNNING   pid 1400, uptime 1 day, 0:38:03
    edxapp_worker:lms_high_1         RUNNING   pid 1401, uptime 1 day, 0:38:03
    edxapp_worker:lms_high_mem_1     RUNNING   pid 1402, uptime 1 day, 0:38:03
    forum                            RUNNING   pid 1404, uptime 1 day, 0:38:03
    insights                         RUNNING   pid 1405, uptime 1 day, 0:38:03
    lms                              RUNNING   pid 1407, uptime 1 day, 0:38:03
    xqueue                           RUNNING   pid 1410, uptime 1 day, 0:38:03
    xqueue_consumer                  RUNNING   pid 1411, uptime 1 day, 0:38:03
    supervisor> reload
    Really restart the remote supervisord process y/N? y
    Restarted supervisord
    supervisor> status
    analytics_api                    RUNNING   pid 27040, uptime 0:00:13
    certs                            RUNNING   pid 27041, uptime 0:00:13
    cms                              RUNNING   pid 27042, uptime 0:00:13
    discovery                        RUNNING   pid 27043, uptime 0:00:13
    ecommerce                        RUNNING   pid 27044, uptime 0:00:13
    ecomworker                       RUNNING   pid 27045, uptime 0:00:13
    edxapp_worker:cms_default_1      RUNNING   pid 27046, uptime 0:00:13
    edxapp_worker:cms_high_1         RUNNING   pid 27047, uptime 0:00:13
    edxapp_worker:lms_default_1      RUNNING   pid 27048, uptime 0:00:13
    edxapp_worker:lms_high_1         RUNNING   pid 27049, uptime 0:00:13
    edxapp_worker:lms_high_mem_1     RUNNING   pid 27050, uptime 0:00:13
    forum                            RUNNING   pid 27051, uptime 0:00:13
    insights                         RUNNING   pid 27052, uptime 0:00:13
    lms                              RUNNING   pid 27053, uptime 0:00:13
    wagtail                          RUNNING   pid 27055, uptime 0:00:13
    xqueue                           RUNNING   pid 27056, uptime 0:00:13
    xqueue_consumer                  RUNNING   pid 27057, uptime 0:00:13
    supervisor> help

    default commands (type help <topic>):
    =====================================
    add    exit      open  reload  restart   start   tail   
    avail  fg        pid   remove  shutdown  status  update 
    clear  maintail  quit  reread  signal    stop    version

    supervisor> exit
    ```
6. Add wagtail to Nginx service
    ```
    cd /edx/app/nginx/sites-available
    touch wagtail
    vi wagtail
    ```
    And its content is like this: 
    ```
    upstream wagtail-backend {
                server 127.0.0.1:8020 fail_timeout=0;

    }

    server {
    listen 80 default_server;
    server_name www.yourdomianname.com;
    rewrite ^(.*)$ https://$host$1;
    location / {
        index index.html index.htm;
      }
    }

    server {
    # wagtail configuration file for nginx, templated by ansible

    # error pages
    error_page 500 /server/server-error.html;
    error_page 502 /server/server-error.html;
    error_page 504 /server/server-error.html;

    location @empty_json {
        # This location will return an empty body with content-type application/json
        # If this location is referenced by the error_page directive the
        # response code will be the error response code (i.e. 502), not 200
        # despite the "return 200" directive
        default_type application/json;
        return 200;
    }

    listen 443 ssl;
    server_name www.yourdomianname.com;
    ssl_certificate /etc/nginx/certs/www_yourdomianname_com.pem;
    ssl_certificate_key /etc/nginx/certs/www_yourdomianname_com.key;
    ssl_session_timeout 5m;
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;

    access_log /edx/var/log/nginx/access.log p_combined;
    error_log /edx/var/log/nginx/error.log error;

    client_max_body_size 100M;
    server_tokens off;

    location @proxy_to_wagtail_app {
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Port $server_port;
        proxy_set_header X-Forwarded-For $remote_addr;

        # newrelic-specific header records the time when nginx handles a request.
        proxy_set_header X-Queue-Start "t=${msec}";

        proxy_set_header Host $http_host;

        proxy_redirect off;
        proxy_pass http://wagtail-backend;
    }

    location / {
        try_files $uri @proxy_to_wagtail_app;
    }

    location ~ ^/static/(?P<file>.*) {

        root /edx/app/edx-wagtail/cms/static;
        try_files /$file /$file =404;

        # return a 403 for static files that shouldn't be
        # in the staticfiles directory
        location ~ ^/static/(?:.*)(?:\.xml|\.json|README.TXT) {
        return 403;
        }
      }
    }
    ```
7. Reload the Nginx service
    ```
    cd /etc/nginx/sites-enabled
    sudo ln /edx/app/nginx/sites-available/wagtail wagtail
    sudo service nginx reload
    sudo service nginx restart
    ```
DONE