from fastapi import APIRouter, HTTPException, status
from models import Prediction_Input
from models import Prediction_Output
from tensorflow import keras

MODEL_PATH = 'modelPulsar.h5'


router = APIRouter()

preds = []

@router.get("/mlpulsar")
def get_preds():
    return preds

@router.post('/mlpulsar', status_code=status.HTTP_201_CREATED)
def create_pred(pred_input : Prediction_Input):
    
    try:
        model = keras.models.load_model(MODEL_PATH)

        EK=pred_input.EK
        Mean_DMSNR_Curve=pred_input.Mean_DMSNR_Curve
        Skewness_DMSNR_Curve=pred_input.Mean_DMSNR_Curve

        prediction_f=model.predict([[EK,Mean_DMSNR_Curve,Skewness_DMSNR_Curve]])

        prediction_dict = {"id": str(pred_input.id), "data_input":{"EK":str(pred_input.EK),"Mean_DMSNR_Curve":str(pred_input.Mean_DMSNR_Curve),"Skewness_DMSNR_Curve":str(pred_input.Skewness_DMSNR_Curve)}, "pred" : float(prediction_f[0,0])}
        preds.append(prediction_dict)

        return {"message": "Dato procesado exitosamente"}
    
    except:
        raise HTTPException(status_code=200, detail='Error procesando su solicitud')


