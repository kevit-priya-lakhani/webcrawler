
# Ranveer Brar Website Crawler

This project contains a Scrapy spider to crawl the `ranveerbrar.com` website and extract links while ensuring only the desired links are followed.

## Project Structure

- `crawl_rb.py`: The main spider file containing the Scrapy spider definition and rules.

## Installation

To run this project, you need to have Python and Scrapy installed. Follow these steps to get started:

1. **Install Scrapy**:
    ```bash
    pip install scrapy
    ```

2. **Clone the Repository** (if applicable):
    ```bash
    git clone https://github.com/kevit-priya-lakhani/webcrawler
    cd your-repo
    ```

3. **Save the spider code**:
    Save the provided spider code into a file named `crawl_rb.py`.

## Running the Spider

To run the spider and output the results to a JSON file, use the following command:

```bash
scrapy runspider crawl_rb.py -o file.json
```

## Spider Configuration

The spider is configured to extract and follow links only within the `ranveerbrar.com` domain while excluding any links containing the term `comment`. The extracted data will be stored in the specified JSON output file.


## Output

The output of the spider will be saved in the specified JSON file (`file.json`). This file will contain the crawled data in JSON format.

## Additional Notes

- Ensure that the `start_urls` list contains valid URLs from which the spider should begin crawling.
- Modify the `parse_url` method to include any additional parsing logic needed for your project.

## License

This project is licensed under the MIT License.
