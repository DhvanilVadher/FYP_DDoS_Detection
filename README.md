# FYP_DDoS_Detection
  Attack Scripts include httpflood,icmpflood,synattack, udpattack etc using Scapy.
  And ANN.py includes training ANN model with help of Keras and other machine learning libraries.
  ANN.py generates a Sequential objects with which can be used for testing.

Currently ANN.py is training on these 11 parameters which can be changed accordingly.
<pre>
Average packet size : Average size of packet
Active mean : Mean time a flow was active before becoming idle
Active min : Minimum time a flow was active before becoming idle
Flow Inter arrival time (IAT) mean : Mean time between two packets sent in the flow
Flow duration : Duration of the flow in Microsecond
Forward packet length mean : Mean size of packet in forward direction
Total length of forward packets : Total size of packet in forward direction
Sub-flow forward bytes : The average number of bytes in a sub flow in the forward direction
Backward IAT mean : Mean time between two packets sent in the backward direction
Backward packet length std : Standard deviation size of packet in backward direction
Backward packet length min : Minimum size of packet in backward direction
</pre>
Testing.py is for Testing purpose.

all necessary traffic CSV files can be obtained here: https://drive.google.com/drive/folders/1mpoHtOBhDMucoSaYGY2sXwbAKZzMGsv_?usp=sharing
