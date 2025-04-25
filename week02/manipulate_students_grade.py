import numpy as np

scores = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [84, 76, 88],
    [90, 93, 94],
    [75, 80, 70]
])

# 1️⃣ 每个学生的平均分（按行计算）
student_avg = np.mean(scores, axis=1)
print("Average score per student:", student_avg)

# 2️⃣ 每门课的平均分（按列计算）
subject_avg = np.mean(scores, axis=0)
print("Average score per subject:", subject_avg)

# 3️⃣ 总分最高的学生（先求总分，再求最大索引）
student_total = np.sum(scores, axis=1)
top_student_index = np.argmax(student_total)
print("Student with highest total score: Row", top_student_index)

# 4️⃣ 给每个学生的第三门课加 5 分（第三列）
scores[:, 2] += 5
print("Scores after adding 5 bonus to subject 3:\n", scores)
