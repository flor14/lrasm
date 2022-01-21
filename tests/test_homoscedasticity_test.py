from lrasm.homoscedasticity_tst import homoscedasticity_test
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from matplotlib.pyplot import figure
from scipy import stats

def test_homoscedasticity_test():
    """Test homoscedasticity test outputs from dataset"""
    X_proper = pd.DataFrame({"head": [1,2,3,3,5,8,7]})
    X_str_df = pd.DataFrame({"head": ["str",2,3,4,5,6,7]})
    X_series = pd.Series([1,2,3,4,5,6,7])

    y_proper = pd.Series([1,2,3,4,5,6,7])
    y_str_df = pd.Series(["str",2,3,4,5,6,7])

    df, plot = homoscedasticity_test(X_str_df, y_proper)
    assert df is None and plot is None

    df, plot = homoscedasticity_test(X_series, y_proper)
    assert df is None and plot is None

    df, plot = homoscedasticity_test(X_proper, y_str_df)
    assert df is None and plot is None

    df, plot = homoscedasticity_test(X_proper, "str")
    assert df is None and plot is None

    df, plot = homoscedasticity_test(X_proper, y_proper)
    assert df.correlation_coefficient[0] == 0.523 and df.p_value[0] == 0.229
    assert isinstance(plot, plt.Figure)