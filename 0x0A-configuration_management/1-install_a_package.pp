# Script that using Puppet, install puppet-lint.

package { 'puppet-lint':
  ensure   => '2.1.1',
  name     => 'puppet-lint',
  provider => 'gem'
}
