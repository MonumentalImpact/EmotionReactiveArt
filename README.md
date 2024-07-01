# EmotionReactiveArt
Using facial emotion recognition to send (MQTT) messages to works of art, which can then use those emotions to change their state.

## camera

Continuously displays camera view onscreen, with the currently determined facial expression ('neutral', 'angry', 'disgust', 'fear', 'happy', 'sad', 'surprise'). When the user decides they want to see what will happen with a given emotion/facial expression, they hit a button that freezes the image and sends the emotion out to the exhibits using MQTT.

post dominant emotion to art/emotion

post details to art/emotiondetails


## works of art

Monitor the art/emotion MQTT topic to get the current exhibit emotion. The art then changes to reflect the current emotion.
