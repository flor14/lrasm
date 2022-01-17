
def homoscedasticity_test(X, y):
    """This function recieves a linear regression model and outputs a
    scatter plot figure of residuals plotted against fitted values.

    Parameters
    ----------
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
    >>> homoscedasticity_test(X_train, y_train) 

    """