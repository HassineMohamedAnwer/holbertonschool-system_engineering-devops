#update requests limit nginx
exec { 'fix--for-nginx':
  command => "sed -i 's/worker_processes 10' /etc/nginx/nginx.conf",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
exec { 'ngnx-reload':
  command => 'systemctl reload nginx',
  path    => '/lib/systemd/system'
}
