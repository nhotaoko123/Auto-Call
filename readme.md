# Auto Call Using GSM 3G

This project provides an automated calling solution using Google Mobile Services (GMS) over a 3G network. It leverages Android APIs to initiate calls automatically based on specific triggers or conditions.

## Features

- Automated call initiation using GSM APIs
- Send/Get report via email
- Working all the time

## Prerequisites

- Android device with Google Mobile Services (GMS)
- 3G network connectivity/ Wifi connectivity
- Raspberry Pi 3/4
- OLED 128x128, ...
  
```
     +----------------------+       +-------------------------+
     | 5V               Vcc | <---> | 2 *                  5V |
     |                      |       |                         |
     |                  GND | <---> | 6                   GND |
     |                      |       |                         |
     |      SIM800C     TXD | <---> | 10       Pi GPIO     RX |
     |                      |       |                         |
     |                  RXD | <---> | 8                    TX |
     |                      |       |                         |
     |                  MCP | <---> | **                  AUX |
     |                      |       |                         |
     |                  MCN | <---> | **                  AUX |
     +----------------------+       +-------------------------+

     +----------------------+       +-------------------------+
     |                   Vcc| <---> | 1 *                3.3V |
     |                      |       |                         |
     |                   Gnd| <---> | 9  **            Ground |
     |    OLED              |       |         Pi GPIO         |
     |                   SCL| <---> | 5               I2C SCL |
     |                      |       |                         |
     |                   SDA| <---> | 3               I2C SCA |
     +----------------------+       +-------------------------+

                     +----------------------+
                     | Mail:                |
                     |                      |
                     | Send:                |
                     |                      |
                     | IP:                  |
                     |                      |
                     | File:                |
                     +----------------------+

```

## Example about the systems are working

![image](https://github.com/user-attachments/assets/819c8cf9-3464-48fa-b9f3-1d3766b49348)
![image](https://github.com/user-attachments/assets/4a306b1a-805f-4d3c-b37a-b72f926693f5)

