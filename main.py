# Before your other imports
import os
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

import google.generativeai as genai
import os

# --- Configuration ---
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
#api_key = "" # Replace with your actual API key; if you dont like the os.getenv method!
#The Above API has expired and is shown for example
# --- Image Loading and Captioning ---
image_file_name = 'chart.png'
mime_type = 'image/png'
website_content = """
The article discusses 42 chart patterns used for effective intraday, swing, and F&O trading. Here's a summary of trading hints related to the patterns mentioned in the article:

* **Double Top Pattern:** Traders often use double tops to identify potential short-selling opportunities or to exit long positions. After the pattern is confirmed by a breakdown below the neckline, traders anticipate further price declines.
* **Double Bottom Pattern:** Risky traders often enter the long setup after the formation of the double bottom itself, whereas risk-averse traders will be patient for a break and retest of a neckline.
* **Ascending Triangle Pattern:** Traders often use the ascending triangle to time entries for long trades in the direction of the prevailing uptrend. Stop losses are placed below the entry setup or candlestick setup, while profit-taking targets are set using the measured move projection.
* **Triple Top Pattern:** A short position is usually initiated on a break below support with a stop-loss placed above the previous swing high (previous lower high) or above the broken neckline or candlestick setup used to take entry.
* **Triple Bottom Pattern:** Here, there is a neckline that is supposed to be broken for momentum towards resistance and turned support to invite buyers into another leg of trend continuation.
* **Bearish Pennant Pattern:** Conservative traders enter at this retest, where the proper bearish candlestick pattern acted as a confluence to ride this upcoming bearish leg. The target range is calculated by measuring the range of the flagpole.
* **Bullish Rectangle Pattern:** The range of the rectangle is taken as the target range at the time of entry.
* **Bearish Rectangle Pattern:** The range of the rectangle is taken as the target range at the time of entry.

The article does not contain information about risk to reward.
"""
prompt_text = f"""
    Based on the provided image of a chart and the following information about technical chart patterns from a website:

    ---
    Website Content on Chart Patterns:
    {website_content}
    ---

    Analyze the chart in the image and provide a trading hint.
    Your hint should be one of the following:
    -   **Open Long**: If you recommend opening a long position. Include details for stop-loss and take-profit targets.
    -   **Open Short**: If you recommend opening a short position. Include details for stop-loss and take-profit targets.
    -   **Wait**: If no clear trading opportunity is identified.

    For 'Open Long' or 'Open Short' hints, also explain the reasoning based on the chart patterns.
    Note: The provided website content does not contain information about "risk to reward" ratios, so you may state if that information cannot be determined.
    """
try:
    with open(image_file_name, 'rb') as f:
        image_bytes = f.read()

    model = genai.GenerativeModel('gemini-2.5-flash')

    # Directly pass the image data as a dictionary within the contents list
    response = model.generate_content(
        contents=[
            {
                'mime_type': mime_type,
                'data': image_bytes
            },
            prompt_text
        ]
    )

    print(response.text)

except FileNotFoundError:
    print(f"Error: The file '{image_file_name}' was not found. Please ensure the image is in the same directory as the script or provide the full path.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
