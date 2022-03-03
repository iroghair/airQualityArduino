void setup() {
  Serial.begin(9600);
}

void loop() {
  float dataRead = analogRead(A0);
  dataRead = (dataRead/1024)*5.0;
  // String dataToSend = String(dataRead);
  Serial.println(dataRead);
  delay(300);
}