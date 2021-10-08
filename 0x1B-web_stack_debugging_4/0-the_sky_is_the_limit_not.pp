# Sky is the limit
exec { '/usr/bin/env sed -i s/15/2000/ /etc/default/nginx': }
exec { '/usr/bin/env service nginx restart': }
