#include <espduino.h>
#include <mqtt.h>

extern boolean wifiConnected;
extern ESP esp;
extern MQTT mqtt;

void setup()
{
 initMQTT();
 mqtt.subscribe("/topic/1");
}

void loop() {
  esp.process();
  if (wifiConnected) {

  }
}
