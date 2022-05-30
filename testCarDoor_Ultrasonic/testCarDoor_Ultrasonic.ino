// -------------------------------------------------------------------------------------------------------------------------------------
// ---------------------------------------- LIBRARIES, DECLARATIONS AND OBJECT CREATION ------------------------------------------------
// -------------------------------------------------------------------------------------------------------------------------------------

// INCLUDE LIBRARIES
#include <SPI.h>
#include <MFRC522.h>
#include <Servo.h>

// VARIABLE GLOBAL DECLARATION
#define SS_PIN 10
#define RST_PIN 9

  // HC-SR4
#define echoPin 2 
#define trigPin 3 

// KEY CLASS
MFRC522 rfid(SS_PIN, RST_PIN); 
MFRC522::MIFARE_Key key; 

// SERVO CLASS
Servo servoMotor;

// -------------------------------------------------------------------------------------------------------------------------------------
// -------------------------------------------------------- GLOBAL VARIABLES -----------------------------------------------------------
// -------------------------------------------------------------------------------------------------------------------------------------

// KEY NUID
byte nuidPICC[4] = {0x5A, 0xA7, 0xA6, 0x81};

// DEFAULT DOOR STATUS
int doorStatus = 0; // 0 close, 1 open
int doorButton;

// REVERSE SENSOR ON/OFF
int reverseSensor = LOW;

// BUZZER 
int buzzerPin = 4;

// DAY OR NIGHT
int dayORnight = 5;

// -------------------------------------------------------------------------------------------------------------------------------------
// ----------------------------------------------------------- FUNCTIONS ---------------------------------------------------------------
// -------------------------------------------------------------------------------------------------------------------------------------

int cardKey(){
  
  // CHEACK CARD PRESENT
  if ( ! rfid.PICC_IsNewCardPresent()){return 0;}
  else{
    
    // CHEACK NUID READ CORRECTLY
    if ( ! rfid.PICC_ReadCardSerial()){return 0;}
    else{
      MFRC522::PICC_Type piccType = rfid.PICC_GetType(rfid.uid.sak);
    
      // CHEACK KEY TYPE
      if (piccType != MFRC522::PICC_TYPE_MIFARE_MINI &&  
        piccType != MFRC522::PICC_TYPE_MIFARE_1K &&
        piccType != MFRC522::PICC_TYPE_MIFARE_4K) {
        Serial.println(F("Llave No Compatible con el Sistema"));
        return 0;
      }

      // CHEACK KEY INFORMATION
      if (rfid.uid.uidByte[0] == nuidPICC[0] && 
        rfid.uid.uidByte[1] == nuidPICC[1] && 
        rfid.uid.uidByte[2] == nuidPICC[2] && 
        rfid.uid.uidByte[3] == nuidPICC[3] ) {
          
        Serial.println(F("LLAVE ENCONTRADA"));
        return 1;
        }
    }
  }
}

// ----------------------------------------------------------
int openDoor(){
  servoMotor.write(40);
  return 1;
}

// ----------------------------------------------------------
int closeDoor(){
  servoMotor.write(0);
  return 0;
}

// ----------------------------------------------------------
int ultrasonic(){
  
  // HC-SR04 NORMAL OPERATION WAVEFORM GENERATION
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // RECIEVE ECHO AND CALCULATE DISTANCE
  long duration = pulseIn(echoPin, HIGH);
  int distance = duration * 0.034 / 2; 

  if (distance <= 25){
    digitalWrite(buzzerPin, HIGH);
    delay(1000);
    digitalWrite(buzzerPin, LOW);
    delay(1000);
  }

  else if (distance <= 15){
    digitalWrite(buzzerPin, HIGH);
    delay(100);
    digitalWrite(buzzerPin, LOW);
    delay(100);
  }
  return distance;
}

int autoLights(){ // AUTOMATIC LIGHTS -----------------------------------
  
  int l1 = analogRead(0);
  int l2 = analogRead(1);
  Serial.print("l1: ");
  Serial.println(l1);
  Serial.print("l2: ");
  Serial.println(l2);
  int lf = (l1 + l2) / 2;
  if (lf >150){return 0;} // LUCES APAGADAS
  else{return 1;} // LUCES PRENDIDAS
}
// -------------------------------------------------------------------------------------------------------------------------------------
// ----------------------------------------------------- START UP PARAMETERS -----------------------------------------------------------
// -------------------------------------------------------------------------------------------------------------------------------------

void setup() { 
  
  Serial.begin(9600);
  
  pinMode(trigPin, OUTPUT); // ULTRASONIC TRIGGER
  pinMode(echoPin, INPUT); //ULTRASONIC ECHO

  pinMode(buzzerPin, OUTPUT);
  
  servoMotor.attach(6); // SERVO ON PIN 9
  servoMotor.write(0);
  
  pinMode(doorButton, INPUT);
  pinMode(reverseSensor, INPUT);

  pinMode(dayORnight, OUTPUT);
  
  SPI.begin(); // SPI BUS
  rfid.PCD_Init(); // MFRC522 INIT
  
  for (byte i = 0; i < 6; i++) {
    key.keyByte[i] = 0xFF;
  }
}

// -------------------------------------------------------------------------------------------------------------------------------------
// ---------------------------------------------------------- MAIN PROGRAM  ------------------------------------------------------------
// -------------------------------------------------------------------------------------------------------------------------------------

void loop() {
  int keyCheck = cardKey();

  // TO OPEN THE DOOR
  if (keyCheck == 1 && doorStatus == 0){
   Serial.println("ABRIR LA PUERTA"); 
   doorStatus = openDoor(); // DOOR OPEN
  }

  // TO CLOSE THE DOOR
  doorButton = digitalRead(7);
  if(doorStatus == 1 && doorButton == HIGH){
    Serial.println("CERRAR LA PUERTA");
    doorStatus = closeDoor(); // DOOR CLOSE
  }

  reverseSensor = digitalRead(8);
  Serial.print("REVERSE SENSOR: ");
  Serial.println(reverseSensor);
  if (reverseSensor == HIGH){
    Serial.println(ultrasonic());
  }

  // TO CHECK ON LIGHT STATUS 
  int lights = autoLights();
  digitalWrite(dayORnight, lights);
  
  // KEY READER HALT
  rfid.PICC_HaltA();
  rfid.PCD_StopCrypto1();
}
