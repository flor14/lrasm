from lrasm.multicollinearity_tst import multicollinearity_test
import numpy as np
import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor
import pytest


def test_multicollinearity_test():
    """Test multicollinearity test outputs from dataset"""
    X_proper = pd.DataFrame({"head": [1,2,3,3,5,8,7],"Feet": [7,6,5,4,3,2,1], 'Random': [12,24,25,26,29,55,99]})
    X_str_df = pd.DataFrame({"head": ["str",2,3,4,5,6,7]})
    X_series = pd.Series([1,2,3,4,5,6,7])

    with pytest.raises(TypeError):
        multicollinearity_test(X_str_df, 10)
        multicollinearity_test(X_series, 10)
        
    assert round(multicollinearity_test(X_proper, 10)['VIF'][0], 2) == 9.04
    
    assert round(multicollinearity_test(X_proper, 10)['VIF'][2], 2) == 8.37
    
    assert isinstance(multicollinearity_test(X_proper, 10), pd.DataFrame)