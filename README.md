# InstaQuoteBot

## Overview
InstaQuoteBot is a Python script designed to automate the process of generating and posting quote images to Instagram. It utilizes the InstaBot Python module to handle Instagram interactions. The script prompts the user to log in, fetches quotes and authors from an API, generates images using two different templates in an alternating fashion, and finally posts them to Instagram with default captions and hashtags.

## Requirements
- Python 3.x
- InstaBot Python module
- Image Processing / Editing libraries (e.g., Pillow)

## Installation
1. Clone this repository:
    ```bash
    https://github.com/codeterrayt/InstaQuoteBot.git
    ```
2. Navigate to the project directory:
    ```bash
    cd InstaQuoteBot
    ```
3. Install dependencies:
To use the InstaQuoteBot script, you need to ensure that you have the following dependencies installed:
    ```bash
    pip install instabot requests pillow numpy
    ```

4. Run the Script 
    ```bash
    python main.py
    ```

## Configuration

- **Image Templates:** Replace the template files in the `templates` directory with your desired image templates. Ensure that the templates are appropriately sized and formatted. You can modify the templates directly from the code by editing the [GeneateImage.py](GeneateImage.py).

- **Default Caption and Hashtags:** Modify the default caption and hashtags in the script to suit your preferences. You can find these in the script and adjust them accordingly.


## Contributing
Contributions are welcome! If you'd like to add new features, improve existing ones, or fix any issues, feel free to submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
