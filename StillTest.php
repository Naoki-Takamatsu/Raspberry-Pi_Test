<?php

$results = shell_exec('gpio -g mode 6 out');
echo "<pre>$results</pre>";

$results = shell_exec('gpio -g write 6 1');
echo "<pre>$results</pre>";

$results = shell_exec('/usr/bin/raspistill -o php_test.jpg');
echo "<pre>$results</pre>";

$results = shell_exec('gpio -g write 6 0');
echo "<pre>$results</pre>";

print("< [Still] End >");

?>
