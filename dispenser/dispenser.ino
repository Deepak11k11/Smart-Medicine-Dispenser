#define LED_ENO 9
#define LED_PCM 6
#define LED_ONDEM 10
#define LED_CROCIN 11

String inputString = "";        
bool stringComplete = false;   

void setup() {
  Serial.begin(9600);   
  pinMode(LED_ENO, OUTPUT);
  pinMode(LED_PCM, OUTPUT);
  pinMode(LED_ONDEM, OUTPUT);
  pinMode(LED_CROCIN, OUTPUT);
}

void loop() {
  
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if (inChar == ',') {
      stringComplete = true;
      break;
    }
    inputString += inChar;
  }

  
  if (stringComplete) {
   
    if (inputString == "eno") {
      //digitalWrite(LED_ENO, HIGH);
      analogWrite(LED_ENO,200);
      delay(2000);
     analogWrite(LED_ENO,LOW);

    } else if (inputString == "pcm") {
      //digitalWrite(LED_PCM, HIGH);
      analogWrite(LED_PCM,200);
      delay(2000);
      analogWrite(LED_PCM,LOW);

    } else if (inputString == "ondem") {
     // digitalWrite(LED_ONDEM, HIGH);
     analogWrite(LED_ONDEM,200);
     delay(2000);
      analogWrite(LED_ONDEM,LOW);
    } else if (inputString == "crocin") {
      //digitalWrite(LED_CROCIN, HIGH);
      analogWrite(LED_CROCIN,200);
      delay(2000);
      analogWrite(LED_CROCIN,LOW);
    } else {
      digitalWrite(LED_BUILTIN,HIGH);
      delay(2000);
      digitalWrite(LED_BUILTIN,LOW);
    }

   
    inputString = "";
    stringComplete = false;
  }
}
