#include <ESP8266WiFI.h>
#include <ESP8266WebServer.h>

ESP8266WebServer server(80):

void setup() {
 Serial.begin("ESP gestartet");
 WiFI.begin("5GH","112330720040719440");
 server.begin();
}

void loop() {

 server.handleClient();
}
