# Research Meeting Agenda
## Spring 2021 
### Friday, March 26, 2021
- Feedback:
I like to way you suggested to morph the idea in CP clean to our setting of FD violations and decision trees.
But,  I am not sure that the repairs of different tuples are completely *independent.* 
For example, consider the table R(A,B)={(a1,b1),(a1,b2)} with FD A->B. If one constructs the conditional repair tuple-by-tuple, b1 and b2 will in the domain of repair for both tuples. But, this approach does not consider the fact that if B=b1 (b2) in the first tuple, we must have B=b1 (b2) in the second tuple. **Considering them completely independent of each other may induce invalid repair or ignore some valid repairs.** 
- In CP Clean, they do a tuple-by-tuple repair because domain of repairs for missing values in one tuple is independent from other tuples. Since the dependencies of repairs makes the problem hard in the case of FD, I suggest that **we first start with the case of NULL values** similar to CPClean paper. The domain of possible repairs in each tuple is independent from others. 
- Now, my question for you is: Can you extend or generalize the efficient algorithms proposed in the CPClean paper to answer questions Q1 and Q2 for learning a decision tree? I suggest that you work on this question the coming week.
