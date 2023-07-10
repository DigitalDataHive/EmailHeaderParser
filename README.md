This script presents an interface that allows users to browse and select an email file, extract its header information, and display the extracted contents in a user-friendly manner.

To access the script, you can download it from the following GitHub repository: Email Header.py

Below are the instructions to execute the program:
1. Execute the script.
2. The GUI window will appear, and you can proceed by clicking the "Browse" button.
3. Choose an email file in .eml format using the file dialog that opens.
4. The script will extract the header information from the selected email file.
5. A new GUI window will open, displaying the extracted header information.

By following these steps, you can run the program, select an email file, and view the extracted header information in the GUI window.

Note: This script assumes that the email file is in UTF-8 encoding. If your email files are encoded differently, you may need to adjust the encoding accordingly in the extract_header_info function.

To run this script, make sure you have the following prerequisites:
1. Python 3 installed, which should include the tkinter module by default for GUI functionality.
2. Ensure that the PIL (Python Imaging Library) module is installed. If it's not already installed, you can install it by running the following command: `pip3 install pillow`.


Email Parsing Details: 

The extract_header_info() function takes the filename as an argument. It opens the selected email file, reads its contents, and uses email.message_from_file() to parse the email message.

The function then creates an empty dictionary called header_info to store the header information. It iterates over the headers in the email message (msg._headers) and extracts the name and value of each header.

The function attempts to decode the header value using decode_header(). If the value is encoded, it decodes it using the appropriate encoding (typically UTF-8). The decoded value is then added to the header_info dictionary with the header name as the key.
