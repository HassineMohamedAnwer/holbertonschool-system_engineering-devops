#update requests limit nginx
exec{ 'fix--for-nginx':
    command => 'echo "ULIMIT=\"-n 2000\"" > /etc/default/nginx',
    path    => '/usr/local/bin/:/bin/',
}

exec { 'ngnx reload':
  command => 'systemctl reload nginx',
  path    => '/lib/systemd/system'
}
