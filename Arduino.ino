#include <LiquidCrystal_I2C.h>
#include "Wire.h"
int i, j,x=0;
long y=0;
byte buff[64];
LiquidCrystal_I2C lcd(0x27,16,2); 
byte a[8][8];


void setup() {
  lcd.init();
  lcd.setBacklight(HIGH);
  Serial.begin(921600);
  
}

void loop() {

  if(Serial.available()>=63){ //wait for the data
  
  Serial.readBytes(buff,63);} //read the data into a buffer list
  delay(1);
  for(i=0 ; i<8;i++){for(j=0 ; j<8;j++){a[i][j]=buff[x];x++;}lcd.createChar(i,a[i]);}//convert the data into an array of 8 variables and create custom characters
  x=0;
  delay(2);
  lcd.clear();
  lcd.setCursor(1, 0);
  
  for( i=0 ; i<4;i++){
    lcd.write(i); 
  }
  lcd.setCursor(1, 1);
  for( i=4 ; i<8;i++){
    lcd.write(i);
  }// write custom characters to the screen
  Serial.flush();
  
  //}
  
}
