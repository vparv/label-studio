<?php  
	try
	{
		$db = new PDO("admin.sqlite3");

	$m_id = $_POST[m_id];
    
	$db->exec(update num_completed SET MTURKID = :&id);
	echo(&m_id);
	}

	echo "1 record added";


?> 