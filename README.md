# Chat with Multiple PDF using Gemini 💁

Welcome to the "Chat with PDF using Gemini" project repository! This project aims to provide a streamlined interface for users to interactively ask questions based on the content of PDF documents using Gemini, a conversational AI model.

## Overview

In this project, we leverage the power of various technologies and libraries to create an interactive web application using Streamlit. The application allows users to upload PDF files, extract text content, and ask questions related to the content of these documents. The answers are generated using the Gemini-Pro conversational AI model, providing users with relevant responses.

## Features

- Upload PDF files: Users can upload one or multiple PDF documents to the application.
- Extract text content: The application extracts text content from the uploaded PDF files using PyPDF2.
- Interactive question-answering: Users can ask questions based on the content of the PDF documents using the Gemini-Pro conversational AI model.
- Real-time response: The application generates responses to user questions in real-time, providing an interactive experience.

## How to Use

To use the "Chat with Multiple PDF using Gemini" application, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Rafe2001/Chat-Multi-PDF-Gemini.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Google API key:
   
   - Obtain a Google API key and configure it in your environment variables or in a `.env` file.
   - You can obtain a Google API key by following the instructions provided [here](https://makersuite.google.com/app/apikey).

4. Run the Streamlit application:

   ```bash
   streamlit run chat.py
   ```

5. Access the application in your web browser:

   Open a web browser and navigate to the URL provided by Streamlit (typically `http://localhost:8501`).

6. Upload PDF files and ask questions:

   - Upload one or multiple PDF documents using the file uploader in the sidebar.
   - Enter your question in the text input box and click the "Submit & Process" button.
   - The application will process the uploaded PDF files, extract text content, and generate responses to your questions using the Gemini AI model.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
