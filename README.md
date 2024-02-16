# PageRank Algorithm Implementation

This is a Python implementation of the PageRank algorithm, which is used to rank web pages in search engine results. This implementation provides two methods for calculating PageRank: sampling and iteration.

## Usage

To use this implementation, follow these steps:

1. **Install Python**: Make sure you have Python installed on your system. This implementation is compatible with Python 3.

2. **Clone the Repository**: Clone this repository to your local machine using Git:

    ```bash
    git clone https://github.com/yourusername/pagerank.git
    ```

3. **Navigate to the Directory**: Go to the directory where you cloned the repository:

    ```bash
    cd pagerank
    ```

4. **Run the Script**: Execute the `pagerank.py` script with the path to your corpus directory as an argument:

    ```bash
    python pagerank.py corpus
    ```

    Replace `corpus` with the path to your corpus directory containing HTML files.

## Parameters

- `DAMPING`: The damping factor used in the PageRank calculation. Default value is 0.85.
- `SAMPLES`: The number of samples used in the sampling method. Default value is 10,000.

## Files

- `pagerank.py`: The main Python script containing the PageRank implementation.
- `readme.md`: This README file providing information about the implementation and usage.

## Sample Output

After running the script, you will see the PageRank results printed to the console, including results from sampling and iteration methods.

## Credits

This implementation is based on the PageRank algorithm developed by Larry Page and Sergey Brin at Google.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
