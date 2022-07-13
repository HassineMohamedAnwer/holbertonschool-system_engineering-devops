# fixing the web stack: Apache is returning a 200 not 500
# replacing phpp with php wp-settings.php


exec {'phpp php':
  command => 'sed -i "s/.phpp/.php/g"  /var/www/html/wp-settings.php',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => 'test -f /var/www/html/wp-settings.php'
}
