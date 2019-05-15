<?php
$rep = $_GET['repertoire'];
$passcode = $_GET['passcode'];

$structure = './gilo/'.$rep;
if (!is_dir($structure)){
	// Créer le répertoire
	if (!mkdir($structure, 0777, true)) {
		die('Failed to create folders...');
	}
	
	// Créer le index.html
	$index = fopen($structure.'/'.'index.html', "a");
	fwrite($index, '<!DOCTYPE html PUBLIC "-//IETF//DTD HTML 2.0//EN">');
	fwrite($index, '<HTML>');
	fwrite($index, '<HEAD>');
	fwrite($index, '<TITLE>');
	fwrite($index, 'A Small Hello');
	fwrite($index, '</TITLE>');
	fwrite($index, '</HEAD>');
	fwrite($index, '<BODY>');
	fwrite($index, 'Bonjour!');
	fwrite($index, '</BODY>');
	fwrite($index, '</HTML>');
	fclose($index);
	
	// Créer le .htaccess
	$htaccess = fopen($structure.'/'.'.htaccess', "w");
	fwrite($htaccess, "AuthType Basic\n");
	fwrite($htaccess, "AuthName \"restricted area\"\n");
	fwrite($htaccess, "AuthUserFile /home/content/60/11707360/html/gilo/".$rep."/.htpasswd\n");
	fwrite($htaccess, "require valid-user");
	fclose($htaccess);

	// Créer le .htpasswd
	$htpasswd = fopen($structure.'/'.'.htpasswd', "w");
	//fwrite($htpasswd, $rep.":".md5($passcode));
	fwrite($htpasswd, $rep.":".crypt($passcode, base64_encode($passcode)));
	fclose($htpasswd);
	//phpinfo();
}
?>