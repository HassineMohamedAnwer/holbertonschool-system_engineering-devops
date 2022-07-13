#increase hard and soft limit
exec { 'soft-limit':
  command => 'sed -i "/holberton soft/s/5/10000/" /etc/security/limits.conf,
  path    => '/usr/local/bin/:/bin/'
}
exec { 'hard-limit':
  command => 'sed -i "/holberton hard/s/4/30000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
