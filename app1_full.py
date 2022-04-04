# źródło danych [https://www.kaggle.com/c/titanic/](https://www.kaggle.com/c/titanic)

import streamlit as st
import pickle
from datetime import datetime
startTime = datetime.now()
# import znanych nam bibliotek

filename = "model_hw.sv"
model = pickle.load(open(filename,'rb'))
# otwieramy wcześniej wytrenowany model

sex_d = {0:"M",1:"F"}
ChestPainType_d = {0:"ATA",1:"NAP", 2:"ASY", 3:'TA'}
RestingECG_d = {0:"Normal", 1:"ST", 2:"LVH"}
ExerciseAngina_d = {0:"N", 1:"Y"}
ST_Slope_d = {0:"Up", 1:"Flat", 2:"Down"}

# o ile wcześniej kodowaliśmy nasze zmienne, to teraz wprowadzamy etykiety z ich nazewnictwem

def main():

	st.set_page_config(page_title="Heart Disease App")
	overview = st.container()
	left, right = st.columns(2)
	prediction = st.container()

	st.image("https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/article_thumbnails/slideshows/did_you_know_this_could_lead_to_heart_disease_slideshow/650x350_did_you_know_this_could_lead_to_heart_disease_slideshow.jpg")
	

	with overview:
		st.title("HeartDisease")

	with left:
		sex_radio = st.radio( "Gender", list(sex_d.keys()), format_func=lambda x : sex_d[x] )
		ChestPainType_radio = st.radio( "Class", list(ChestPainType_d.keys()), format_func=lambda x: ChestPainType_d[x])
		RestingECG_radio = st.radio( "Emarked", list(RestingECG_d.keys()),  format_func= lambda x: RestingECG_d[x] )
		ExerciseAngina_radio = st.radio( "ExerciseAngina_d", list(ExerciseAngina_d.keys()),  format_func= lambda x: ExerciseAngina_d[x] )
		ST_Slope_radio = st.radio( "ST_Slope", list(ST_Slope_d.keys()),  format_func= lambda x: ST_Slope_d[x] )
                # ExerciseAngina_radio = st.radio( "ExerciseAngina", list(ExerciseAngina_d.keys()), format_func= lambda x: ExerciseAngina_d[x] )
                #ST_Slope_radio = st.radio( "ST_Slope", list(ST_Slope_d.keys()),  format_func= lambda x: ST_Slope_d[x] )
                

	with right:
		age_slider = st.slider("Age", value=1, min_value=1, max_value=80)
		RestingBP_slider = st.slider("RestingBP", min_value=0, max_value=10)
		Cholesterol_slider = st.slider("Cholesterol", min_value=0, max_value=10)
		MaxHR_slider = st.slider("MaxHR", min_value=0, max_value=500, step=1)
		FastingBS_slider = st.slider("FastingBS", min_value=0, max_value=500, step=1)
		Oldpeak_slider = st.slider("Oldpeak", min_value=0, max_value=500, step=1)
               

	data = [[sex_radio, ChestPainType_radio,RestingECG_radio,ExerciseAngina_radio,ST_Slope_radio, age_slider,
            RestingBP_slider,Cholesterol_slider,MaxHR_slider,FastingBS_slider,Oldpeak_slider]]
	survival = model.predict(data)
	s_confidence = model.predict_proba(data)

	with prediction:
		st.subheader("Will I have HeartDisease?")
		st.subheader(("Yes" if survival[0] == 1 else "No"))
		st.write("Prob {0:.2f} %".format(s_confidence[0][survival][0] * 100))

if __name__ == "__main__":
    main()
