# Gemini Trading Hint Generator

A Python script that leverages the Google Gemini API to analyze chart images and provide trading hints (Long, Short, or Wait) based on predefined technical chart patterns.

-----

## 🚀 Features

  * **Chart Analysis:** Analyzes a provided chart image (`chart.png`).
  * **Pattern Recognition:** Integrates knowledge of common trading chart patterns (Double Top, Double Bottom, Ascending Triangle, etc.) from a custom content source.
  * **Trading Hints:** Generates a trading hint (`Open Long`, `Open Short`, or `Wait`) with reasoning and suggested stop-loss/take-profit targets.
  * **Customizable Strategy Recommendations:** Easily modify the `website_content` variable in the script to provide your own trading strategy recommendations or preferred pattern descriptions.
  * **Secure API Key Handling:** Utilizes environment variables to keep your Google Gemini API key secure and out of public repositories.
  * Example Output:
![image](https://github.com/user-attachments/assets/89f3a372-25a1-4011-af92-4fa0b1a8e568)
-----

## 🛠️ Installation

To get this project up and running on your local machine, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/DrSavalan/GeminiChartAnalyzer
    cd GeminiChartAnalyzer
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required libraries:**

    ```bash
    pip install -r requirements.txt
    ```

      * **Note:** You'll need to create a `requirements.txt` file first if you don't have one. You can generate it by running `pip freeze > requirements.txt` in your activated virtual environment after installing the necessary packages (`google-generativeai` and `python-dotenv`).

4.  **Set up your Google Gemini API Key:**

      * Obtain your API key from the [Google AI Studio](https://aistudio.google.com/app/apikey).
      * Create a file named `.env` in the root directory of your project (the same place as `main.py`).
      * Add your API key to the `.env` file like this:
        ```
        GOOGLE_API_KEY="your_actual_api_key_here"
        ```
      * **Important:** The `.env` file is excluded from version control by `.gitignore` to keep your API key private. **Do not commit your `.env` file to GitHub\!**

-----

## 💡 Usage

1.  **Place your chart image:** Ensure your chart image is named `chart.png` and is located in the same directory as the `main.py` script. If your image has a different name or format, you'll need to update the `image_file_name` and `mime_type` variables in `main.py`.

2.  **Customize Trading Strategies (Optional):**
    The `website_content` variable within `main.py` contains the descriptions of chart patterns and their associated trading hints. You can modify this multi-line string to include your own trading strategies, preferred entry/exit rules, or any other textual information you want the Gemini model to consider when analyzing the chart.

3.  **Run the script:**

    ```bash
    python main.py
    ```

The script will analyze the image and print the generated trading hint to your console.

-----

## 📜 Technical Chart Patterns Used

The script, by default, incorporates trading hints for the following chart patterns:

  * Double Top Pattern
  * Double Bottom Pattern
  * Ascending Triangle Pattern
  * Triple Top Pattern
  * Triple Bottom Pattern
  * Bearish Pennant Pattern
  * Bullish Rectangle Pattern
  * Bearish Rectangle Pattern

*(Remember, you can customize these by modifying the `website_content` variable in `main.py`.)*

-----

## 🤝 Contributing

Contributions are welcome\! If you have suggestions for improvements or new features, feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

-----

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

-----

## 📞 Contact

Dr. Savalan - [mechsavalan@gmail.com]

Project Link: [https://github.com/DrSavalan/GeminiChartAnalyzer](https://github.com/DrSavalan/GeminiChartAnalyzer)
