# Modify the OS configuration
exec { "/usr/bin/env sed -i 's/5/4000/' /etc/security/limits.conf": }
exec { "/usr/bin/env sed -i 's/4/2000/' /etc/security/limits.conf": }
