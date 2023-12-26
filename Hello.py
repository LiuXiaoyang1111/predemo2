# 导入包
import streamlit as st
import numpy as np

# 设定标题
st.title("认知程度变化预测📈")

# 子标题
st.subheader("请在下方完成信息填写，以获得你在未来的认知程度变化")

# 填写信息
AGE = st.text_input("1️⃣请输入AGE（50-100）", placeholder="例：59")
try:
    AGE = int(AGE)
    if AGE < 50 or AGE > 100:
        st.write("输入不在规定范围内，请重新输入！")
except ValueError:
    if AGE != "":
        st.write("输入不是一个数字，请重新输入！")
R3 = st.text_input("2️⃣请输入R3（0-1）", placeholder="例：0.3")
try:
    R3 = float(R3)
    if R3 < 0 or R3 > 1:
        st.write("输入不在规定范围内，请重新输入！")
except ValueError:
    if R3 != "":
        st.write("输入不是一个数字，请重新输入！")
GENDER = st.selectbox("3️⃣请选择性别", ("男", "女"), index=None, placeholder="点击下拉选择")
if GENDER == "男":
    GENDER = 1
else:
    GENDER = 2
PTHOME = st.selectbox("4️⃣请选择PTHOME", list(range(1, 9)), index=None, placeholder="点击下拉选择")
DXSUM1 = st.selectbox("5️⃣请选择DXSUM1", list(range(1, 4)), index=None, placeholder="点击下拉选择")
MONTH = st.selectbox("6️⃣请选择MONTH", (6, 12, 24, 36, 48), index=None, placeholder="点击下拉选择")
GDDROP = st.selectbox("7️⃣请选择GDDROP", (0, 1), index=None, placeholder="点击下拉选择")
Q13SCORE = st.selectbox("8️⃣请选择Q13SCORE", list(range(6)), index=None, placeholder="点击下拉选择")
MMYEAR = st.selectbox("9️⃣请选择MMYEAR", list(range(1, 3)), index=None, placeholder="点击下拉选择")
MMDAY = st.selectbox("1️⃣0️⃣请选择MMDAY", list(range(1, 3)), index=None, placeholder="点击下拉选择")
MMHOSPIT = st.selectbox("1️⃣1️⃣请选择MMHOSPIT", list(range(1, 3)), index=None, placeholder="点击下拉选择")
MMFLOOR = st.selectbox("1️⃣2️⃣请选择MMFLOOR", list(range(1, 3)), index=None, placeholder="点击下拉选择")
MMTREE = st.selectbox("1️⃣3️⃣请选择MMTREE", list(range(1, 3)), index=None, placeholder="点击下拉选择")
MMBALLDL = st.selectbox("1️⃣4️⃣请选择MMBALLDL", list(range(1, 3)), index=None, placeholder="点击下拉选择")
MMTREEDL = st.selectbox("1️⃣5️⃣请选择MMTREEDL", list(range(1, 3)), index=None, placeholder="点击下拉选择")
FAQFORM = st.selectbox("1️⃣6️⃣请选择FAQFORM", list(range(6)), index=None, placeholder="点击下拉选择")
FAQTRAVL = st.selectbox("1️⃣7️⃣请选择FAQTRAVL", list(range(6)), index=None, placeholder="点击下拉选择")
NPIG = st.selectbox("1️⃣8️⃣请选择NPIG", list(range(2)), index=None, placeholder="点击下拉选择")

# 相应系数
INTERCEPT_coef = 1.62944
AGE_coef = -0.03732
R3_coef = -2.98442
if GENDER == 2:
    GENDER_coef = -0.58493
else:
    GENDER_coef = 0
if PTHOME == 3:
    PTHOME_coef = 0.58431
else:
    PTHOME_coef = 0
if DXSUM1 == 3:
    DXSUM1_coef = -7.59428
else:
    DXSUM1_coef = 0
if MONTH == 48:
    MONTH_coef = 1.02476
else:
    MONTH_coef = 0
if DXSUM1 != "" and MONTH != "":
    if DXSUM1 * MONTH == 12:
        DXSUM1_MONTH = -1.35489 * 12
    elif DXSUM1 * MONTH == 24:
        DXSUM1_MONTH = -0.55894 * 24
    elif DXSUM1 * MONTH == 48:
        DXSUM1_MONTH = 0.63992 * 48
    elif DXSUM1 * MONTH == 72:
        DXSUM1_MONTH = 0.69173 * 72
    else:
        DXSUM1_MONTH = 0
if GDDROP == 1:
    GDDROP_coef = 0.31347
else:
    GDDROP_coef = 0
if Q13SCORE == 4:
    Q13SCORE_coef = 1.91052
else:
    Q13SCORE_coef = 0
if MMYEAR == 2:
    MMYEAR_coef = 0.59745
else:
    MMYEAR_coef = 0
if MMDAY == 2:
    MMDAY_coef = 0.66709
else:
    MMDAY_coef = 0
if MMHOSPIT == 2:
    MMHOSPIT_coef = 0.57832
else:
    MMHOSPIT_coef = 0
if MMFLOOR == 2:
    MMFLOOR_coef = 0.45082
else:
    MMFLOOR_coef = 0
if MMTREE == 2:
    MMTREE_coef = 2.07704
else:
    MMTREE_coef = 0
if MMBALLDL == 2:
    MMBALLDL_coef = 0.402
else:
    MMBALLDL_coef = 0
if MMTREEDL == 2:
    MMTREEDL_coef = 0.56747
else:
    MMTREEDL_coef = 0
if FAQFORM == 2:
    FAQFORM_coef = 0.51532
elif FAQFORM == 4:
    FAQFORM_coef = 1.16516
elif FAQFORM == 5:
    FAQFORM_coef = 1.30348
else:
    FAQFORM_coef = 0
if FAQTRAVL == 2:
    FAQTRAVL_coef = 1.61397
elif FAQTRAVL == 3:
    FAQTRAVL_coef = 0.58889
elif FAQTRAVL == 4:
    FAQTRAVL_coef = 0.84413
elif FAQTRAVL == 5:
    FAQTRAVL_coef = 1.13439
else:
    FAQTRAVL_coef = 0
if NPIG == 1:
    NPIG_coef = 0.46014
else:
    NPIG_coef = 0

# 计算结果
if AGE != None and R3 != None and GENDER != None and PTHOME != None and DXSUM1 != None and MONTH != None and GDDROP != None and Q13SCORE != None and MMYEAR != None and MMDAY != None and MMHOSPIT != None and MMFLOOR != None and MMTREE != None and MMBALLDL != None and MMTREEDL != None and FAQFORM != None and FAQTRAVL != None and NPIG != None:
    st.subheader("结果输出🖨️")
    prob = INTERCEPT_coef + AGE_coef * AGE + R3_coef * R3 + GENDER_coef * GENDER + PTHOME_coef * PTHOME + DXSUM1_coef * DXSUM1 + MONTH_coef * MONTH + DXSUM1_MONTH + GDDROP_coef * GDDROP + Q13SCORE_coef * Q13SCORE + MMYEAR_coef * MMYEAR + MMDAY_coef * MMDAY + MMHOSPIT_coef * MMHOSPIT + MMFLOOR_coef * MMFLOOR + MMTREE_coef * MMTREE + MMBALLDL_coef * MMBALLDL + MMTREEDL_coef * MMTREEDL + FAQFORM_coef * FAQFORM + FAQTRAVL_coef * FAQTRAVL + NPIG_coef * NPIG
    prob = np.exp(prob) / np.exp(prob + 1)
    prob = prob*100
    if prob < 0 or prob > 1:
        st.write("无法预测认知程度的恶化概率")
    else:
        st.write("认知程度恶化的概率为"+str(prob)[:5]+"%")
