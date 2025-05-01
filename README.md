# 🐍 Python Utility Scripts

This repository contains four Python scripts designed for various practical tasks: desktop notifications, QR code generation, text-to-speech, and WhatsApp automation.

## 📂 Scripts Overview

```plaintext
| Script                | Description                                          |
|-----------------------|------------------------------------------------------|
| notification.py       | Sends periodic desktop notifications.               |
| QR.py                 | Generates a QR code from a given string.            |
| edith.py              | A text-to-speech virtual assistant using pyttsx3.   |
| whatsapp.py           | Sends scheduled WhatsApp messages using pywhatkit. |
```

---

## 🛎️ notification.py — Desktop Notification Script

### 📦 Requirements

To install the required library:
```bash
pip install plyer
```

---

## 🔲 QR.py — QR Code Generator


### 📦 Requirements

To install the required libraries:
```bash
pip install qrcode[pil]
```

---

## 🗣️ edith.py — Text-to-Speech Assistant


### 📦 Requirements

To install the required library:
```bash
pip install pyttsx3
```

---

## 📱 whatsapp.py — WhatsApp Message Sender

### 📦 Requirements

To install the required library:
```bash
pip install pywhatkit
```

### ⚠️ Notes:
- Ensure you’re logged into WhatsApp Web in your default browser.
- The script requires an internet connection and accurate system time.
- Schedule the message at least 1–2 minutes ahead of the current time to ensure it sends correctly.

---

## 🤝 Contributing

Feel free to fork the repository, open issues, and submit pull requests. Contributions are welcome!

---

## 🙏 Acknowledgments

- **Plyer**: For desktop notification support.
- **QRCode**: For generating QR codes.
- **Pillow**: For handling image files.
- **pyttsx3**: For offline text-to-speech conversion.
- **PyWhatKit**: For WhatsApp automation and other utilities.

---
