def answer_question(qa_pipeline, context, question):
    if not context.strip() or not question.strip():
        return "Please provide both study material and a question."
    result = qa_pipeline(question=question, context=context)
    return result['answer']

def create_tutor_interface(qa_pipeline):
    with gr.Tab("💬 AI Tutor"):
        gr.Markdown("### 🤖 Ask a Doubt from Your Study Notes")
        with gr.Row():
            context = gr.Textbox(lines=6, label="📘 Paste Study Material")
            question = gr.Textbox(lines=2, label="❓ Ask a Question")
        tutor_output = gr.Textbox(label="🧠 AI Answer")
        gr.Button("Get Answer").click(
            lambda c, q: answer_question(qa_pipeline, c, q), 
            inputs=[context, question], 
            outputs=tutor_output
        )