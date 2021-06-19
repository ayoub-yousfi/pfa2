<?php
system("gpio -g mod 4 out");
if ($_POST['executer']=='on') {
	system("gpio -g mod 4 1");
	# code...
}
else
{
	system("gpio -g mod 4 0");
}
header('Location:index.php')
?>