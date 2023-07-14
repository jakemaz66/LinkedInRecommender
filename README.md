# LinkedIn Recommender

A web-based application that utilizes the GPT 3.5 model from the OpenAI API, along with Proxycurl API and SerpAPI, to scrape LinkedIn for relevant information. The application takes an input 'name' and returns the LinkedIn profile picture, a summary of the person, two interesting facts about them, a list of their qualifications, and an argument for their job performance based on their education and qualifications.

## Table of Contents

- [Summary](#summary)
- [Required Tools and Skills](#required-tools-and-skills)
- [Usage](#usage)
- [Files](#files)
- [Contributing](#contributing)
- [License](#license)
- [Conclusion](#conclusion)

## Summary

This project combines the power of the GPT 3.5 model from the OpenAI API, Proxycurl API, and SerpAPI to create a web-based application that extracts valuable information from LinkedIn profiles. By entering a person's name, the application scrapes LinkedIn for relevant details and generates a summary, interesting facts, qualifications, and an argument for job performance based on the person's education and qualifications.

The application is built using the LangChain framework, which connects the GPT 3.5 model with other APIs and provides an interface to interact with the model. The application also incorporates Flask as the web server to handle HTTP requests and responses.

## Required Tools and Skills

To run this project, you will need the following:

- Python 
- Flask 
- OpenAI API key
- Proxycurl API key
- SerpAPI key

The following skills are required:

- Python programming
- Web development (HTML, CSS)
- API integration and usage
- Data scraping and parsing

## Usage
To use, personal API keys must be supplied in the .env file

1. Run the Flask web server:

   ```
   python app.py
   ```

2. Access the application in your web browser by navigating to `http://localhost:5000`.

3. Enter the name of the person you want to search for and submit the form.

4. The application will scrape LinkedIn for the person's information and display the results, including the profile picture, summary, interesting facts, qualifications, and job performance argument.

## Files

- `index.html`: HTML file responsible for formatting the web page.
- `style.css`: CSS file responsible for styling the web page.
- `linkedin_search.py`: Initializes the LangChain agent for connecting to the GPT 3.5 model.
- `linkedin.py`: Scrapes the LinkedIn API for data related to the entered name.
- `app.py`: Runs the Flask web server and handles the web application's functionality.
- `.env`: Houses environment variables like API keys.
- `output_parsers.py`: Parses data to usable formats like JSON.
- `quality_search.py`: Initializes LangChain chains and prompts for the LLM.



## Conclusion

This project demonstrates the integration of advanced AI models, APIs, and web development techniques to create a web-based application for extracting and presenting information from LinkedIn profiles. By leveraging the power of the GPT 3.5 model, Proxycurl API, and SerpAPI, the application provides valuable insights into a person's professional profile.

Feel free to customize and enhance the project to suit your specific needs. 
