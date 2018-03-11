# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish

publish.single("CoreElectronics/test", "1", hostname="test.mosquitto.org")
print("Done")
