#include <Keyboard.h>

void setup() {
  delay(2000); // Wait for OS to detect USB HID device

  // Open Run (Win + R)
  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  delay(100);
  Keyboard.releaseAll();
  delay(500);

  // Type the URL
  Keyboard.print("https://www.youtube.com/watch?v=dQw4w9WgXcQ");
  Keyboard.press(KEY_RETURN);
  Keyboard.releaseAll();

  // Wait to prevent immediate unplug stop
  delay(180000); // 180 seconds = 3 minutes
}

void loop() {
  // Nothing to do here
}
