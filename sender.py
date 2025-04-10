import pywhatkit as kit
import random
import time


image = "data/wspp_image.jpg"

def message_sender(numbers, messages):
    """Sends a WhatsApp image with a message to each number."""
    for number, message in zip(numbers, messages):
        wait_time = random.randint(7, 10)
        try:
            kit.sendwhats_image(number, image, message, wait_time)
            time.sleep(3)
            #kit.sendwhatmsg_instantly(number, message, 10)
        except Exception as e:
            print(f"Error sending to {number}: {e}")