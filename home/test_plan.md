Name:   QILONG ZHONG
SID:    540238846
Unikey: qzho0669

**Test Cases**
Table 1. Summary of test cases for parse_pulse_sequence
| File Name             | Function Name   | Description                                            | Expected Error Message(s) (if any) | Pass/Fail |
| --------------------- | ----------------| ------------------------------------------------------ | ---------------------------------- | --------- |
| pulse_sequence.in | positive_test_1 | Positive Case - Configure the frequency for 3 emitters |  | Pass      |
| pulse_sequence_2.in | positive_test_2 | Positive Case - Configure the frequency for 3 emitters, the input is in strange format but valid |  | Pass |
| pulse_sequence_3.in | negative_test_1 | Negative Case - Parser Test, it should identify the error in the input file and print the error message to the console. | See Appendix A | Pass |
| pulse_sequence_4.in | negative_test_2 | Negative Case - This test focuses on strange and errorneous input file format, or it is valid at parsing stage but invalid at setting the pulse sequence. The function should identify the error in the input file and print the error message to the console. | See Appendix B | Pass |
| pulse_sequence_5.in | edge_test_1 | Edge Case - The input file is empty. | | Pass |
| pulse_sequence_6.in | edge_test_2 | Edge Case - The input file contains very large numbers and very strange input format, such as a large number of spaces, tabs, and newlines. The function should still be able to set the pulse sequence correctly. | | Pass |

**Appendix A**

*Error Message for pulse_sequence_3.in*
```
Error: <symbol> <frequency> <direction>         # 3 times
Error: symbol is not between A-J                # 3 times
Error: frequency is not an integer              # 4 times
Error: frequency must be greater than zero      # 3 times
Error: direction must be 'N', 'E', 'S' or 'W'   # 4 times
```

**Appendix B**

*Error Message for pulse_sequence_4.in*
```
Error: <symbol> <frequency> <direction>         # 5 times
Error: emitter 'A' already has its pulse sequence set
Error: emitter 'D' does not exist
```

