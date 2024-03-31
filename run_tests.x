#!/bin/bash

# Runs on Gradescope server
# CODE: student code

# student_code_with_answers is on my local system
export PYTHONPATH=student_code_with_answers:/autograder/MAKE-STUDENT-OUTPUT/CODE:.:pytest_utils:instructor_code_with_answers:tests

due_date="2024-04-02"

# Current date in YYYY-MM-DD format
current_date=$(date '+%Y-%m-%d')
echo "current_date" : $current_date
echo "due_date" : $due_date

if [[ "$current_date" < "$due_date" ]] || [[ "$current_date" == "$due_date" ]]; then
    echo "Current date is earlier than the due date."

#pytest -s tests/test_answers_preprocessed_hw4_expand.py
#pytest -s tests/test_structure_preprocessed_hw4_expand.py

pytest -s tests/test_structure_preprocessed_hw4_expand.py::test_structure_question1_a_explain_explain_string_lparen_rparen

#pytest -s tests/test_structure_preprocessed_hw4_expand.py::test_structure_question1_a_string_lparen_rparen
#pytest -s tests/test_answers_preprocessed_hw4_expand.py::test_answers_question2_a_string
#pytest --import-mode='prepend' -s tests/test_answers_preprocessed_hw4_expand.py::test_answers_question10_e_A_and_B_conditionally_independent_given_class_plus_comma_explain_explain_string
#pytest --import-mode='prepend' -s tests/test_structure_preprocessed_hw4_expand.py
#pytest --import-mode='prepend' -s tests/test_structure_preprocessed_hw4_expand.py::test_structure_question10_e_A_and_B_conditionally_independent_given_class_plus_comma_explain_explain_string_lparen_rparen

else 
    echo "Current date is later than the due date."

    pytest -s tests/test_answers_preprocessed_hw4_expand.py
fi
