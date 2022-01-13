
def test_homoscedacity(model, X, y):
    """This function recieves a linear regression model and outputs a
    scatter plot figure of residuals plotted against fitted values.

    Parameters
    ----------
    model : sklearn.linear_model.base.LinearRegression
        Scikit-learn Linear regression model

    X : pd.Dataframe
        Dataframe containing exploratory variable data

    y : pd.Dataframe
        Dataframe containing response variable data
        
    Returns
    -------
    matplotlib.pyplot.scatter
        Scatter plot of residuals plotted against fitted values

    Examples
    --------
    >>> test_homoscedacity(LinearRegression(), X_train, y_train) 

    """