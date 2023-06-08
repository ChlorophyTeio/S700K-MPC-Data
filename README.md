# S700K-MPC-Data

## S700K Power Curve

This project analyzes the power curve data of S700K and visualizes it using matplotlib.

Record the power data of the S700K switch machine. According to the sampling frequency of 40 milliseconds, the action process is about 7 seconds, with a total of 175 sampling points. Use Python to draw power curves for personal contact.

## Prerequisites

- Python 3.7 or above
- Pandas library
- NumPy library
- Matplotlib library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ChlorophyTeio/S700K-MPC-Data.git

2. Install the required libraries:

   ```bash
   pip install pandas numpy matplotlib
   ```

## Usage

1. Place your data file (`run.xlsx`) in the project directory.

2. Run the `plot_power_curve.py` script:

   ```bash
   python run.py
   ```

3. The power curve plot will be displayed, showing the curves for different variables.

## Customization

- Modify the `data.xlsx` file to include your own data.

- Customize the plot settings in `run.py`, such as figure size, marker style, label names, etc.

## License

This project is licensed under the [MIT License](LICENSE).
