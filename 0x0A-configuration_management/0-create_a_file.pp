# Create a file called holberton using Puppet, create a file in /tmp.

file { 'holberton':
  path    => '/tmp/holberton',
  group   => 'www-data',
  owner   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet'
}
