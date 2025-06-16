def predict_risk(model, att, avg_score, assignments):
    pred = model.predict([[att, avg_score, assignments]])[0]
    if pred == 1:
        return "⚠ Student is AT RISK!\n👉 Suggest extra tutoring or mentoring."
    else:
        return "✅ Student is NOT at risk.\n👍 Keep up the good performance!"

def create_risk_interface(model):
    with gr.Tab("🚨 Risk Prediction"):
        gr.Markdown("### 📉 Predict If a Student Is At Risk")
        att = gr.Slider(0, 100, step=1, value=75, label="📅 Attendance (%)")
        avg = gr.Slider(0, 100, step=1, value=60, label="🧮 Average Test Score")
        assign = gr.Slider(0, 10, step=1, value=5, label="📂 Assignments Completed")
        risk_output = gr.Textbox(label="🔎 Prediction Result")
        gr.Button("Predict").click(
            lambda a, avg, assign: predict_risk(model, a, avg, assign),
            inputs=[att, avg, assign],
            outputs=risk_output
        )