#include <WiFi.h>


const char* ssid = "MIT";
const char* password = "PCvPkbh1B}";


WiFiServer server(80);


String header;


const int pumpPin = 4;


unsigned long currentTime = millis();
unsigned long previousTime = 0;
const long timeoutTime = 2000;


void setup() {
  Serial.begin(115200);
  // Initialize the output variables as outputs
  pinMode(pumpPin, OUTPUT);
  digitalWrite(pumpPin, LOW);


  // Connect to Wi-Fi network with SSID and password
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  // Print local IP address and start web server
  Serial.println("");
  Serial.println("WiFi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  server.begin();
}


void loop(){
  WiFiClient client = server.available();   // Listen for incoming clients


  if (client) {                             // If a new client connects,
    currentTime = millis();
    previousTime = currentTime;
    Serial.println("New Client.");          // print a message out in the serial port
    String currentLine = "";                // make a String to hold incoming data from the client
    while (client.connected() && currentTime - previousTime <= timeoutTime) {  // loop while the client's connected
      currentTime = millis();
      if (client.available()) {             // if there's bytes to read from the client,
        char c = client.read();             // read a byte, then
        Serial.write(c);                    // print it out the serial monitor
        header += c;
        if (c == '\n') {                    // if the byte is a newline character
          // if the current line is blank, you got two newline characters in a row.
          // that's the end of the client HTTP request, so send a response:
          if (currentLine.length() == 0) {
            // HTTP headers always start with a response code (e.g. HTTP/1.1 200 OK)
            // and a content-type so the client knows what's coming, then a blank line:
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type:text/html");
            client.println("Connection: close");
            client.println();
           
            // turns the GPIOs on and off
            Serial.println(header);
            if (header.indexOf("GET /?time=") >= 0) {
              int start = header.indexOf("GET /?time=") + 11;
              int end = header.indexOf(" HTTP/1.1");
              header[end] = '\0';
              String t = &(header[start]);
              int time = t.toInt();
              digitalWrite(pumpPin, HIGH);
              Serial.println(time);
              delay(time);
              digitalWrite(pumpPin, LOW);
            }
           
           
            client.println();
            break;
          } else {
            currentLine = "";
          }
        } else if (c != '\r') {
          currentLine += c;
        }
      }
    }
    header = "";
    client.stop();
    Serial.println("Client disconnected.");
    Serial.println("");
  }
}


import numpy as np
import pandas as pd
from terra.base_client import Terra
from datetime import datetime, timedelta
import json
import requests
import time
from gpiozero import PWMLED
from time import sleep




"""
Initializations:
"""
global cnt, current_speed, last_update
cnt = 0
current_speed = 0.9
last_update = 0


"""
do a quick diagnostic - "how many cigs do u smoke a day" - if high, med, or low then do 21, 14, or 7 respectively


21 mg patch: Releases approximately 0.87 mg per hour.
Per minute:
0.87 mg ÷ 60 minutes ≈ 0.0145 mg/min




14 mg patch: Releases approximately 0.58 mg per hour.
Per minute:
0.58 mg ÷ 60 minutes ≈ 0.0097 mg/min




7 mg patch: Releases approximately 0.29 mg per hour.
Per minute:
0.29 mg ÷ 60 minutes ≈ 0.0048 mg/min
"""


MAX_RATE = 0.0145
# stress level: 0 - 100, craving: bool, rate: 0 - max rate
def compute(inp):
    return {
        "stress": inp[-1],
        "craving": inp[-1] > 1.5*inp[-2],
        "pwm_rate": np.mean(inp) / 100,
        "si_rate": np.mean(inp) / 100 * MAX_RATE
    }


# Set up the endpoint and headers
url = 'https://thubgzodxizmmtyvcfgp.supabase.co/rest/v1/terra_output'
current = 'https://thubgzodxizmmtyvcfgp.supabase.co/rest/v1/terra_current?id=eq.1'
headers = {
    'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRodWJnem9keGl6bW10eXZjZmdwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjYzNDQ0NjUsImV4cCI6MjA0MTkyMDQ2NX0.kOBtx9MYpeKu4FV4wcfjet0mDpqwJmTGDwkTa4oVmP8',
    'Content-Type': 'application/json',
    'Prefer': 'return=minimal'
}


# Initialize the Terra object
terra = Terra(api_key="e6LUApBzI7xNM3BhltjsPCnlzJ00WF1s", dev_id="4actk-smartpatch-testing-5ElA4qm5Ju", secret="3a8d426c89d67f671cfaef8f29ea2ac46f5def2af91f8c06")




# Create a user object
USER_ID = "98417876-7604-45a9-b657-465d1c801124"
terra_user = terra.from_user_id(USER_ID)




# Fetch the daily data
garmin = terra_user.get_daily(start_date=datetime.strptime('2024-09-13','%Y-%m-%d'), end_date=datetime.now(), to_webhook = False)
garmin_json = garmin.get_json()
# print(json.dumps(nutrition_resp_json, indent=4))
with open('garmin_data_pretty.json', 'w') as f:
    json.dump(garmin_json, f, indent=4)


stress_data = garmin_json["data"][0]["stress_data"]["body_battery_samples"]
lvls = [entry["level"] for entry in stress_data]


# PWM object for GPIO pin 12:
pwm = PWMLED(12)


# every 3 min
def update():
    global cnt, current_speed


    # "last 3 hours / 60 times stress data" but really next interval
    fs_data = lvls[cnt:cnt+60]
    cnt = (cnt + 1) % len(lvls)


    # Define the payload - nicotine pump rate
    payload = compute(fs_data)


    current_speed = payload["pwm_rate"]


    # Send the POST request
    response = requests.post(url, headers=headers, json=payload)


    # Check the response status
    if response.status_code == 201:
        print("Data inserted successfully!")
    else:
        print(f"Failed to append output data. Status code: {response.status_code}")
        print(f"Response: {response.text}")




    # Send the POST request
    response2 = requests.patch(current, headers=headers, json=payload)




    # Check the response status
    if response.status_code == 201:
        print("Data inserted successfully!")
    else:
        print(f"Failed to update current data. Status code: {response.status_code}")
        print(f"Response: {response.text}")


def run_motor(speed):
    if speed == 0:
        pwm.value = 1
    elif (1 >= speed > 0):
        speed = 1 - (.25 + (.75*speed))
        print("Speed: " + str(speed))
        pwm.value = speed
    else:
        print("error: speed out of bounds, rate unchanged")




if __name__ == "__main__":
    while True:
        run_motor(current_speed)
        # delay for 10 ms
        time.sleep(0.01)


        current_time = time.time()
        if current_time - last_update >= 15:
            # modify current_speed and update last update time
            update()
            last_update = current_time
