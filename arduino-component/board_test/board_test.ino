// Board Test file
// We have killed a board while wiring the relays :(
// After replacing 328p this confirms functionality
// Once Brodie has his own board a test fixture will be created to test all GPIO's

int led = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  digitalWrite(led, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(led, HIGH);
  delay(1000);
  digitalWrite(led, LOW);
  delay(1000);
}
