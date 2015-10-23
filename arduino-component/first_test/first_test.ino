// initial setup , where you 'tell the board which pins belong to what'

int reedSensor01 = 6;
int reedSensor02 = 5;
int panicSwitch = 0;
int alarm = 13;

void setup() {
  // put your setup code here, to run once:

  pinMode(reedSensor01, INPUT);
  pinMode(reedSensor02, INPUT);
  pinMode(panicSwitch, INPUT);
  pinMode(alarm, OUTPUT);
  
  digitalWrite(reedSensor01, HIGH);
  digitalWrite(reedSensor02, HIGH);
  digitalWrite(panicSwitch, HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(reedSensor01) && digitalRead(reedSensor02) == LOW) {
    // Do Nothing
    digitalWrite(alarm, LOW);
  }
  else if(digitalRead(reedSensor01) || digitalRead(reedSensor02) == HIGH) {
    // Set off Alarm
    digitalWrite(alarm, HIGH);
  }
  else if(digitalRead(panicSwitch) == HIGH) {
    // Do Nothing
    digitalWrite(alarm,LOW);
  }
  else if (digitalRead(panicSwitch) == LOW) {
    // Set off Alarm
    digitalWrite(alarm, HIGH);
  }
}
