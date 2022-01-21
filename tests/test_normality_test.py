from lrasm.normality_tst import normality_test
import numpy as np
import pandas as pd
from sklearn import linear_model
from scipy import stats
import pytest 

def test_normality_test():
    """Test normality test outputs from dataset"""
    X_proper = pd.DataFrame({"head": [1,2,3,3,5,8,7],"Feet": [7,6,5,4,3,2,1]})
    X_str_df = pd.DataFrame({"head": ["str",2,3,4,5,6,7]})
    X_series = pd.Series([1,2,3,4,5,6,7])
    X_wrong_len = pd.DataFrame({"head": [2,3,4,5,6,7]})

    y_proper = pd.Series([1,2,3,4,5,6,7])
    y_str_df = pd.Series(["str",2,3,4,5,6,7])

    with pytest.raises(TypeError):
        normality_test(X_str_df, y_proper)
        normality_test(X_series, y_proper)
        normality_test(X_proper, y_str_df)
        normality_test(X_proper, "str")
    
    with pytest.raises(ValuesError):
        normality_test(X_wrong_len,y_proper)
    
    assert isinstance(normality_test(X_proper, y_proper)[0],float)

    assert normality_test(X_proper, y_proper,0.01)[1] == "Fail"



