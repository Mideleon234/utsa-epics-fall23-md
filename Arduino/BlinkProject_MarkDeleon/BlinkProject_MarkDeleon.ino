int led_pin1 = 13;
int led_pin2 = 12;
int blink_duration1 = 500;
int blink_duration2 = 1000;

void setup() {

pinMode(led_pin1, OUTPUT);
pinMode(led_pin2, OUTPUT);
}
  // put your setup code here, to run once:


void loop() {

digitalWrite (led_pin1,HIGH);
  delay (blink_duration1);
  digitalWrite (led_pin1,LOW);
  delay (blink_duration1);

  digitalWrite (led_pin2,HIGH);
  delay (blink_duration2);
  digitalWrite (led_pin2,LOW);
  delay (blink_duration2); 
  }
  // put your main code here, to run repeatedly:


