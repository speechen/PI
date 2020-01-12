#include <ESP8266WiFi.h>
#include <WEMOS_SHT3X.h>
#include <EEPROM.h>

SHT3X sht30(0x45);

const char* ssid = “5GH”;  // SSID of local network
const char* password = “112330720040719”;  // Password on network
const char* host = “WEBSEITE”; //Webserver

WiFiClient client;
char servername[] = “WEBSEITE”; // remote server we will connect to
String result;
float temp;
float feucht;
int temp1;
int temphigh;
const int sleepSeconds = 600;

void setup() {
Serial.begin(115200);
Serial.println(“Connecting”);
WiFi.begin(ssid, password);

while (WiFi.status() != WL_CONNECTED) {
delay(100);
}
Serial.println(“Connected”);
delay(1000);
}

void loop() {
EEPROM.begin(512);
temp1 = EEPROM.read(1);
temphigh = EEPROM.read(2);

// EEPROM wird geprüft ob Daten vorhanden sind die nicht 1 oder 0 sind!
// Ist das der Fall wird tempghigh auf 1 gesetzt.
if (!(temphigh == 0 || temphigh == 1))
{
temphigh = 1;
EEPROM.write(2, temphigh);
}

// Daten aus dem Sensor lesen.
if (sht30.get() == 0)
{
temp = sht30.cTemp;
feucht = sht30.humidity;
temp1 = temp;
EEPROM.write(1, temp1);
}
String tempString = String(temp, 1);
String feuchtString = String(feucht, 1);

Serial.println(“\nStarting connection to server…”);
//Ausgabe ueber serielle Verbindung
WiFiClient client;

// Temperaturdaten werden über URL Link an die Datenbank übergeben.
if (client.connect(host, 80)) {
Serial.println(“connected to server”);
String url = “/ghaus/wm_t1.php”;
url += “?t1=”;
url += temp;
client.print(String(“GET “) + url + ” HTTP/1.1\r\n” +
“Host: ” + host + “\r\n” +
“Connection: close\r\n\r\n”);
client.println();  //Verbindungs mit Server aufbauen und HTTP Anfrage senden
}

// Luftfeuchtigkeitsdaten werden über URL Link an die Datenbank übergeben.
if (client.connect(host, 80)) {
Serial.println(“connected to server”);
String url = “/ghaus/wm_f1.php”;
url += “?f1=”;
url += feucht;
client.print(String(“GET “) + url + ” HTTP/1.1\r\n” +
“Host: ” + host + “\r\n” +
“Connection: close\r\n\r\n”);
client.println();  //Verbindungs mit Server aufbauen und HTTP Anfrage senden

}
client.stop();
//Beenden der Verbindung

//prüfen ob die Temperatur unter 20 Grad ist und Mail senden.
if (temp1 < 20 && temphigh == 1)
{
temphigh = 0;
EEPROM.write(2, temphigh);
sendAMail(tempString, feuchtString);
}

//prüfen ob die Temperatur über 35 Grad ist und Mail senden.
if (temp1 > 35 && temphigh == 0)
{
temphigh = 1;
EEPROM.write(2, temphigh);
sendAMail(tempString, feuchtString);
}
EEPROM.commit();
EEPROM.end();
ESP.deepSleep(sleepSeconds * 1000000);
}

void sendAMail(String temp, String feucht)
{
if (client.connect(servername, 80)) {  //starts client connection, checks for connection
Serial.println(“connected”);
client.println(“GET /send_email.php?temperature=” + temp + “&humidity=” + feucht + ” HTTP/1.1″); //Send data
client.println(“Host: bau-es-selbst.info”);
client.println(“Connection: close”);  //close 1.1 persistent connection
client.println(); //end of get request
}
else {
Serial.println(“connection failed”); //error message if no client connect
Serial.println();
}

while (client.connected() && !client.available()) delay(1); //waits for data
while (client.connected() || client.available()) { //connected or data available
char c = client.read(); //gets byte from ethernet buffer
result = result + c;
}

client.stop(); //stop client
Serial.println(result);

}
