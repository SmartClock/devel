import paho.mqtt.client as mqtt
import time
def on_connect (client, userdata, flags, rc):
	print("Connected with result code"+str(rc))
	client.publish("/topic/0", "hello World", 0, False)

def on_publish(client, userdata, msg):
	#print(msg.topic+" "+str(msg.payload))
	print "hi"

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    return

def loop():
	f=open("../../data/rss","r")
	lines= f.readlines()
	f.close()
	f=open("../../data/rss","w")
	f.close()
	for line in lines:
		print line

client= mqtt.Client()

client.on_connect = on_connect
client.on_publish = on_publish
client.on_message = on_message

client.connect("192.168.0.108", 1883, 60)

client.loop_start()
while True:
	loop()
	time.sleep(10);
client.loop_end()
