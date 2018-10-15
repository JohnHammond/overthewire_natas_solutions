<html>
	<head>
		<title></title>
	</head>
	<body>
		<code><span style="color: #000000"><html>
		<head>
		<!-- This stuff in the header has nothing to do with the level -->
		<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
		<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
		<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
		<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
		<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
		<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
		<script>var wechallinfo = { "level": "natas11", "pass": "<censored>" };</script></head>
		<?
		
		$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
		
		function xor_encrypt($in) {
		    $key = '<censored>';
		    $text = $in;
		    $outText = '';
		
		    // Iterate through each character
		    for($i=0;$i<strlen($text);$i++) {
		    $outText .= $text[$i] ^ $key[$i % strlen($key)];
		    }
		
		    return $outText;
		}
		
		function loadData($def) {
		    global $_COOKIE;
		    $mydata = $def;
		    if(array_key_exists("data", $_COOKIE)) {
		    $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
		    if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
		        if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
		        $mydata['showpassword'] = $tempdata['showpassword'];
		        $mydata['bgcolor'] = $tempdata['bgcolor'];
		        }
		    }
		    }
		    return $mydata;
		}
		
		function saveData($d) {
		    setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
		}
		
		$data = loadData($defaultdata);
		
		if(array_key_exists("bgcolor",$_REQUEST)) {
		    if (preg_match('/^#(?:[a-f\d]{6})$/i', $_REQUEST['bgcolor'])) {
		        $data['bgcolor'] = $_REQUEST['bgcolor'];
		    }
		}
		
		saveData($data);
		
		
		
		?>
		
		<h1>natas11</h1>
		<div id="content">
		<body style="background: <span style="color: #0000BB"><?=$data</span><span style="color: #007700">[</span><span style="color: #DD0000">'bgcolor'</span><span style="color: #007700">]</span><span style="color: #0000BB">?></span>;">
		Cookies are protected with XOR encryption<br/><br/>
		
		<?
		if($data["showpassword"] == "yes") {
		    print "The password for natas12 is <censored>";
		}
		
		?>
		
		<form>
		Background color: <input name=bgcolor value="<span style="color: #0000BB"><?=$data</span><span style="color: #007700">[</span><span style="color: #DD0000">'bgcolor'</span><span style="color: #007700">]</span><span style="color: #0000BB">?></span>">
		<input type=submit value="Set color">
		</form>
		
		<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
		</div>
		</body>
		</html></span></code> [Finished in 0.5s]
	</body>
</html>