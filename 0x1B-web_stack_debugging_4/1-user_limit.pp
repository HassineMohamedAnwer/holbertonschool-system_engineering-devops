#increase hard and soft limit fixToo Many Open Files Error

exec { 'soft-limit':
  command => 'sed -i "holberton soft/s/4/10000/" /etc/security/limits.conf,
  path    => '/usr/local/bin/:/bin/'
}

exec { 'hard-limit':
  command => 'sed -i "holberton hard/s/5/30000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
