# Script that installs and configures an Nginx server using Puppet

exec { 'header':
  command  => 'sudo apt-get -y update;
  sudo apt-get -y upgrade;
  sudo apt-get -y install nginx;
  sudo service nginx start;
  sudo sed -i "/server_name _/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default
  sudo service nginx restart',
  provider => shell,
}
