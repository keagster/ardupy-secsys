int door = 8;

void setup() {
  // put your setup code here, to run once:
  pinMode(door, OUTPUT);
}

void loop() {
  // 
  digitalWrite(door, HIGH);
  delay(10000);
  digitalWrite(door, LOW);
  delay(10000);
}
