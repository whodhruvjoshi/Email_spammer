import pickle
import streamlit as st

# loading the saved model
sentiment_model = pickle.load(open('model.pkl','rb'))
# creating a function for Prediction


def spam_prediction(input_sms):
    prediction = sentiment_model.predict(input_sms)[0]
    if (prediction == 0):
        return 'Not a spam'
    else:
        return 'spam'


def main():
    # giving a title
    st.title('Devloper@Shubham Sharma')
    st.title("Email Spam Classifier")
    # getting the input data from the user
    # mean radius	mean texture	mean perimeter	mean area	perimeter error	area error	worst radius	worst texture	worst perimeter	worst area
    input_sms = st.text_area("Enter the message")
    
    
    
    # code for Prediction
    diagnosis = ''

    # creating a button for Prediction

    if st.button('Predict'):
        diagnosis = spam_prediction([input_sms])

    st.success(diagnosis)



if __name__ == '__main__':
    main()
