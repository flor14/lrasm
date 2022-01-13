def multicollinearity_test(X, y, VIF_thresh):
    """This function recieves a data set and VIF thrreshold and outputs VIF for each explarotary 
    variable along with a stetement whether or not the multicollinearity assumption is violated.
    Parameters
    ----------
    X : pd.Dataframe
        Dataframe containing exploratory variable data
    y : pd.Dataframe
        Dataframe containing response variable data
    VIF_thresh: float
        The threshold user defines for VIF
        
    Returns
    -------
    VIF
        VIF for explarotary variables
    Print statement
        Whether the multicollinearity assumption is violated. 
    
    Examples
    --------
    >>> multicollinearity_test(X_train, y_train, VIF_thresh = 10.0) 
    """