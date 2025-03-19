from plyer import notification
import time

while True:
    notification.notify(
        title='class timing',
        message='it is a class timing',
        timeout=2  # Corrected typo here
    )
    time.sleep(30)  # Indented correctly
