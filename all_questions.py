# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "Some instances can trigger more than one rule, for example a person could be a home owner and have a low annual income, hence they are not mutually exclusive."
    answers["(b) explain"] = "The rule set is non-exhaustive, missing coverage for certain combinations like employment status, high income"
    answers["(c) explain"] = "The order of rules is crucial as it directly impacts classification results, particularly in scenarios where there are overlapping rules. For instance, situations where being both a homeowner and single could activate multiple rules highlight the significance of rule ordering.."
    answers["(d) explain"] = "The presence of a default class ensures that every instance can be classified, even if it doesn't meet the requirements of any specific rule."

    return answers


def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "yes"
    answers["(b)"] = "no"
    answers["(c)"] = "no"

    # explain-string: explanation in english prose
    answers["(a) example"] = "Each rule is designed to apply to a specific set of characteristics that do not overlap with others, making them mutually exclusive."
    answers["(b) example"] = "The rules fail to cover all potential combinations, like animals that give birth but aren't warm-blooded, revealing their lack of exhaustiveness."
    answers["(c) example"] = "Given that the rules are mutually exclusive and don't overlap, the order of their application has no impact on the outcome, rendering ordering unnecessary."

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = True
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = False

    # explain_string: explanation in english prose
    answers["(a) explain"] = "Gradients are propagated backward from the output to the input layer, which means that computations rely on subsequent layers. This backward propagation allows for adjustments to be made to the network's parameters based on the calculated errors, facilitating learning."
    answers["(b) explain"] = "The activations of nodes in any layer are influenced by the activations of the preceding layer due to the feedforward process. This sequential activation flow through the layers enables the network to progressively extract features and make predictions."
    answers["(c) explain"] = "The vanishing gradient problem occurs when gradients become extremely small as error is backpropagated through the layers. However, it is distinct from the issue of discrepancy between training and test errors, which involves differences in performance between the training and testing phases of the network."
    answers["(d) explain"] = "Achieving perfect classification does not necessarily imply that gradients are zero. Perfect classification indicates that there is no error in the classification task, but it doesn't guarantee that the network has reached the global minimum of the loss function. Gradients being zero would mean that the network has converged to a local minimum or saddle point, but perfect classification can occur without reaching such points."

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}
    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.41
    answers["(a) P(X_1=1,X_2=1)"] = 0.28
    
    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"
    
    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "yes"
    
    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.5
    answers["(c) P(X_2=1 | +)"] = 0.5
    answers["(c) P(X_2=1 | -)"] = 0.32
    answers["(c) P(X_3=1 | +)"] = 0.4
    answers["(c) P(X_3=1 | -)"] = 0.16
    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = "+"
    answers["(d) Row 2"] = "-"
    answers["(d) Row 3"] = "-"
    answers["(d) Row 4"] = "-"
    # float between 0 and 1
    answers["(d) Training error rate"] = 0.25
    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 1
    answers["(b) K"] = 5

    # explain_string
    answers["(a) explain"] = "Assuming well-separated classes, choosing a smaller value of K, such as K=1, minimizes bias while closely following the class boundaries. With smaller K values, the algorithm tends to capture the local structure of the data more precisely, allowing it to closely adhere to the boundaries between classes."
    answers["(b) explain"] = "Choosing K=5 provides a balance that reduces variance without noticeably raising bias, making it appropriate for datasets with some degree of overlap or noise. With a moderate K value like 5, the algorithm can generalize well while still considering the local neighborhood of each data point, thereby accommodating potential overlap or noise in the dataset."

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # Conditional probabilities calculated from the dataset
    answers["(a) P(A=1|+)"] = 0.6
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.8
    answers["(a) P(A=1|-)"] = 0.4
    answers["(a) P(B=1|-)"] = 0.4
    answers["(a) P(C=1|-)"] = 0.2

    # Explanation for conditional probabilities
    answers["(a) P(A=1|+) explain your answer"] = "Calculated by dividing the number of positive instances where the feature is 1 by the total number of positive instances."
  
    # Probabilities for the sample R = (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 0.857  
    answers["(b) P(R|+)"] = 0.192
    answers["(b) P(R|-)"] = 0.032

    # Predicted class label for the sample
    answers["(b) class label"] = "+"

    # Explanation for the prediction
    answers["(b) Explain your reasoning"] = "The class label '+' has a higher posterior probability for the sample than the class label '-'."
  
    # Marginal and joint probabilities for independence check
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.4
    answers["(c) P(A=1,B=1)"] = 0.2

    # Checking independence between A and B
    answers["(c) A independent of B?"] = "yes"
  
    # For part (d), repeating the analysis with B=0
    answers["(d) P(A=1)"] = 0.5
    answers["(d) P(B=0)"] = 0.6  
    answers["(d) P(A=1,B=0)"] = 0.3

    # Checking independence for part (d)
    answers["(d) A independent of B?"] = "yes"
  
    # Conditional independence given class "+"
    answers["(e) P(A=1,B=1|+)"] = 0.2
    answers["(e) P(A=1|+)"] = 0.6
    answers["(e) P(B=1|+)"] = 0.4

    # Checking conditional independence given class "+"
    answers["(e) A independent of B given class +?"] = "no"

    # Explanation for conditional independence
    answers["(e) A and B conditionally independent given class +, explain"] = "For class = +, 0.24(product of the probabilities) not equal to 0.2(joint probability) , proving that A and B are not conditionally independent. The equivalence must exist for variables to be conditionally independent given the class.."
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question3'] = question3()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
