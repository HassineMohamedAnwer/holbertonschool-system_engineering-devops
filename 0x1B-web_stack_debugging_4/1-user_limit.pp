#increase hard and soft limit fixToo Many Open Files Error

exec { 'soft-limit':
  command => 'sed -i "nginx\t\tsoft\tholberton\t 10000" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'hard-limit':
  command => 'sed -i "nginx\t\thard\tholberton\t30000" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
