import paho.mqtt.client as mqtt
import time
def on_connect (client, userdata, flags, rc):
	print("Connected with result code"+str(rc))
	client.publish("/topic/0", "hello World", 0, False)

def on_publish(client, userdata, msg):
	#print(msg.topic+" "+str(msg.payload))
	print("published")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


client= mqtt.Client()
client.on_message= on_message
client.on_connect= on_connect
client.on_publish= on_publish
client.connect("192.168.0.108", 1883)
client.subscribe("/topic/0");

client.loop_start()
while True:
	client.publish("/topic/0","HI")
	time.sleep(5)
client.loop_end()
