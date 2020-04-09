<?php
echo "hello Fuckworld!\n";
$servername = "localhost";
$username = "phpmyadmin";
$password = "forward";
$dbname = "Fuckworld";
$conn = mysqli_connect($servername, $username, $password, $dbname);
// 检测连接
if (!$conn){
die("连接失败:".mysqli_connect_errno());
}
echo "连接成功!\n";

mysqli_query($conn, "set names 'utf8'");
mysqli_query($conn, "set character_set_client=utf8");
mysqli_query($conn, "set character_set_results=utf8");

$sql = "SELECT id, name, title FROM PlayMYSQL";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
    // 输出数据
    while($row = mysqli_fetch_assoc($result)) {
        echo "|id:  ".$row["id"]."    |Name:   ".$row["name"]."    |title:  ".$row["title"]."\n";
    }
} else {
    echo " 查无结果";
}

$sql = "INSERT INTO PlayMYSQL(id,title,name,date) VALUES (11,'仙女', '嫦娥', '2020/04/08')";
mysqli_query($conn, $sql);


mysqli_close($conn);
?>

