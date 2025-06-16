import gradio as gr
from ai_tutor.tutor import create_tutor_interface
from ai_tutor.qa_model import load_qa_model
from quiz_generator.quiz import create_quiz_interface
from risk_prediction.predictor import create_risk_interface
from risk_prediction.model_training import load_model

def main():
    # Load models
    qa_pipeline = load_qa_model()
    risk_model = load_model()

    # Create app
    with gr.Blocks(theme=gr.themes.Soft()) as demo:
        gr.Markdown(
            """
            <h1 style="text-align: center;">📚 AI Education Assistant</h1>
            <p style="text-align: center;">AI Tutor • Dynamic Quiz • Risk Prediction</p>
            <hr>
            """
        )
        
        # Add all components
        create_tutor_interface(qa_pipeline)
        create_quiz_interface()
        create_risk_interface(risk_model)

    demo.launch()

if __name__ == "__main__":
    main()