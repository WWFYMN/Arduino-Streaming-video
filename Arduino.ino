#include <LiquidCrystal_I2C.h>
#include "Wire.h"
int i, j,x=0;
long y=0;
unsigned long previousMillis = 0; 
const unsigned long interval = 1;
byte buff[64];
LiquidCrystal_I2C lcd(0x27,16,2);
byte a[8][8];


void setup() {
  lcd.init();
  lcd.setBacklight(HIGH);
  Serial.begin(921600);
  Serial.print(BUFFER_LENGTH);
}

void loop() {

  if(Serial.available()>=63){
  
  Serial.readBytes(buff,63);}
  
  for(i=0 ; i<8;i++){for(j=0 ; j<8;j++){a[i][j]=buff[x];x++;}lcd.createChar(i,a[i]);}
  x=0;
  while(millis()-previousMillis<=interval){}
  previousMillis=millis();
  //lcd.clear();
  lcd.setCursor(1, 0);
  
  
  for( i=0 ; i<4;i++){
    lcd.write(i); 
  }
  lcd.setCursor(1, 1);
  for( i=4 ; i<8;i++){
    lcd.write(i);
  }
  Serial.flush();
  
  
}
