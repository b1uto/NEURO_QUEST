import asyncio
import websockets
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

async def send_heart_rate(websocket, path):
    driver = webdriver.Chrome()  # or webdriver.Firefox() or another browser
    url = 'https://pulsoid.net/widget/view/3c69d127-9a7d-44c4-9a20-703d0daac61d'
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'heartRate'))
        )

        while True:
            heart_rate_element = driver.find_element(By.ID, 'heartRate')
            heart_rate = heart_rate_element.text
            print(f'Heart Rate: {heart_rate}')

            await websocket.send(json.dumps({'heart_rate': heart_rate}))
            await asyncio.sleep(1)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()

# Start the WebSocket server on port 5678
start_server = websockets.serve(send_heart_rate, "localhost", 5678)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
