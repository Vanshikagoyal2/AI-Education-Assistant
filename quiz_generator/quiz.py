import random
from .questions import question_bank

def generate_quiz():
    selected = random.sample(question_bank, 10)
    correct = []
    updates = []
    for i, q in enumerate(selected):
        correct.append(q["answer"])
        updates.append(gr.update(choices=q["options"], label=f"Q{i+1}: {q['q']}", value=None))
    return (*updates, correct, "", "")

def grade_quiz(*answers_and_correct):
    answers = answers_and_correct[:-1]
    correct = answers_and_correct[-1]
    
    if any(ans is None for ans in answers):
        return "⚠ Please complete all questions before submitting.", ""
    
    score = sum(ans == correct[i] for i, ans in enumerate(answers))
    feedback = f"✅ You scored {score}/10.\n"
    if score == 10:
        feedback += "Excellent work! 🎉"
    elif score >= 7:
        feedback += "Great job, just a few to improve!"
    elif score >= 4:
        feedback += "Needs more focus, keep practicing!"
    else:
        feedback += "Let's review the material again together."
    return "", feedback

def create_quiz_interface():
    with gr.Tab("📝 Random Quiz"):
        gr.Markdown("### ✍ Dynamic 10-Question Quiz")

        radios = [gr.Radio(choices=[], label=f"Q{i+1}", interactive=True) for i in range(10)]
        warning_msg = gr.Markdown("", elem_id="warning_msg", visible=True)
        quiz_feedback = gr.Textbox(label="📊 Quiz Feedback", lines=3)
        correct_answers_state = gr.State([])

        btn_new_quiz = gr.Button("🔄 New Quiz")
        btn_submit_quiz = gr.Button("Submit Quiz")

        btn_new_quiz.click(
            generate_quiz,
            inputs=[],
            outputs=radios + [correct_answers_state, warning_msg, quiz_feedback]
        )

        btn_submit_quiz.click(
            grade_quiz,
            inputs=radios + [correct_answers_state],
            outputs=[warning_msg, quiz_feedback]
        )