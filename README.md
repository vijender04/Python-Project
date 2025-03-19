# Python-Project


This repository contains two simple Python scripts:
1. **Notification Script**: A script that sends periodic desktop notifications.
2. **QR Code Generator**: A script that generates a QR code from a given string.

## Notification Script (`notification.py`)

This script uses the `plyer` library to send desktop notifications at regular intervals. It is useful for reminders or alerts.

### Features
- Sends a desktop notification every 30 seconds.
- Customizable title and message.

### Requirements
- `plyer`

You can install the required library using pip:
```bash
pip install plyer
```
 

---

## QR Code Generator (`QR.py`)

This script uses the `qrcode` library to generate a QR code from a given string and saves it as an image file.

### Features
- Generates a QR code from a string.
- Saves the QR code as an image file.

### Requirements
- `qrcode`
- `Pillow` (for image handling)

You can install the required libraries using pip:
```bash
pip install qrcode[pil]
```


## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.


## Acknowledgments

- **Plyer**: For providing the notification functionality.
- **QRCode**: For the QR code generation library.
- **Pillow**: For image handling in the QR code script.
