#include <LiquidCrystal.h>

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // initialize the serial communications:
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {    
    lcd.clear();
    delay(1000);

    String serialInput = "";
    while (Serial.available() > 0) {
      serialInput = Serial.readString();
    }
    Serial.print(serialInput.length());
    if(serialInput.length() > 16){                  //Check if new line is needed
      lcd.print(serialInput.substring(0,16));       //Substring end of screen
      lcd.setCursor(0, 1);                          //Start new row
      lcd.print(serialInput.substring(16, 32));     //Take the last values that there is space for
    }else{
      lcd.print(serialInput);
    } 
  }
}
