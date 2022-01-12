# lrasm

# Package for testing linear and multiple linear regression assumptions


This package is built to contain functions to be able to quickly and easily test the linearity assumptions befre preforming linear regression or multiple linear regression for a specified dataset. 

The package contains 3 functions one for checking multicolliniarity, one for checking constant variance and one for checking normality in the residuals.

Function 1: Multicolliniarity.

- Takes a data set and a VIF threshold and checks if any of the calculated vif values exceed the given threshold. If so, the function will advise the user that this assumtion is violated, and vice versa.

- Returns the Calculated VIF values and a statement telling the user whether or not the assumpton is violated.

Function 2: Constant Variance.

- Takes a data set and some sort of variability threshold and checks if the variabiliy of the residuals is contant by comparing it to the given threshold. If the threshold is exceeded the function will advise the user that this assumtion is violated, and vice versa.

- Returns a plot of the fitted values vs residuals, the calculated variability value  and a statement telling the user whether or not the assumpton is violated.

Function 3: Normality.

- Takes a data set and a P-value threshold and preforms a shapiro wilk test for normality. If the P-value of the test does not exceed the threshold, the function will advise the user that this assumtion is violated, and vice versa.

- Returns the Calculated P-value and a statement telling the user whether or not the assumpton is violated.

## Installation

```bash
pip install LR_assumption_test
```

## Usage

- TODO

## Contributing

Authors: Yair Guterman, Hatef Rahmani, Song Bo Andy Yang  
Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`LR_assumption_test` was created by Yair Guterman, Hatef Rahmani, Song Bo Andy Yang . It is licensed under the terms of the MIT license.

## Credits

`LR_assumption_test` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
