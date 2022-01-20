def normality_test(X, y, p_value_thresh):
    """This function recieves a data set and p-value threshold and outputs the p-value from a shapiro wilks test along with a stetement whether or not the multicollinearity assumption is violated.
    Parameters
    ----------
    X : pd.Dataframe
        Dataframe containing exploratory variable data
    y : pd.Dataframe
        Dataframe containing response variable data
    p_value_thresh: float
        The threshold user defines for the p-value 
        
    Returns
    -------
    p-value
        p-value of the shapiro wilk test
    Print statement
        Whether the normality assumption is violated. 
    
    Examples
    --------
    >>> normality_test(X_train, y_train, VIF_thresh = 10.0).
    """ 