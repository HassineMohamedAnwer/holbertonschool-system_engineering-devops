#update requests limit nginx
exec { 'fix--for-nginx':
  command => "sed -i 's/worker_processes 4;/worker_processes 7;/g' /etc/nginx/nginx.conf; sudo service nginx restart",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}

exec { 'ngnx-reload':
  command => 'systemctl reload nginx',
  path    => '/lib/systemd/system'
}
