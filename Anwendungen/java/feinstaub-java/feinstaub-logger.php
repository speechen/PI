<?php

$log = "feinstaub.log";
$schluessel = array("SDS_P1", "SDS_P2", "temperature", "humidity", "signal");

$json = file_get_contents("php://input");
$daten = json_decode($json, true);
$sensoren = $daten["sensordatavalues"];

$zeit = date("Y-m-d H:i:s");
$zeile = $zeit.",";

foreach ($schluessel as $key) {
 $index = array_search($key, array_column($sensoren, "value_type"));  # ab PHP 5.5.0
 $zeile .= $sensoren[$index]["value"].",";
}

$zeile = rtrim($zeile, ",") ."\n";
file_put_contents($log, $zeile, FILE_APPEND);

?>
ok