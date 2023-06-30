from pydantic import BaseModel



class Prediction_Input(BaseModel):
    id : int
    EK : float
    Mean_DMSNR_Curve:float
    Skewness_DMSNR_Curve:float

class Prediction_Output(BaseModel):
    id : int
    data_input : dict
    pred : float



    
