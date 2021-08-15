# Now that you have successfully connected to your server, we would also like to join the party.
# Add the SSH public key below to your server so that we can connect using the ubuntu user.
exec { 'ssh_config':
  path    => '/bin',
  command => 'echo "PasswordAuthentication no" >> /etc/ssh/ssh_config; echo "IdentityFile ~/.ssh/holberton" >> /etc/ssh/ssh_config',
}
