Network Speed Test
This Python script uses the speedtest-cli library to test your internet connection speed. It provides results for download speed, upload speed, and ping time (latency).

Features
Download Speed: Measures the speed at which your network can receive data (in Mbps).
Upload Speed: Measures the speed at which your network can send data (in Mbps).
Ping: Measures the latency between your machine and the server (in milliseconds).
Requirements
You need to have Python installed and the speedtest-cli module installed to run this script.

Installation
Clone this repository:

bash
Copy code
git clone https://github.com/willin-broad/network-speed-test.git
Navigate to the project directory:

bash
Copy code
cd network-speed-test
Install the required Python package:

Install speedtest-cli using pip:

bash
Copy code
pip install speedtest-cli
How to Use
Run the script using Python:

bash
Copy code
python speed_test.py
This will output the download speed, upload speed, and ping in the terminal.

Example Output
bash
Copy code
Download speed in mbps :: 50.23
Upload speed in mbps :: 12.45
Ping :: 34.5 ms
License
This project is licensed under the MIT License.

Contributions
Feel free to fork the repository and submit pull requests. Any enhancements or bug fixes are welcome!

