#update requests limit nginx
exec { 'fix--for-nginx':
  command => "sed -i 'worker_processes 1;' /etc/nginx/nginx.conf; sudo service nginx restart",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
exec { 'ngnx-reload':
  command => 'systemctl reload nginx',
  path    => '/lib/systemd/system'
}
