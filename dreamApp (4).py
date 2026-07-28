import streamlit as st
import pandas as pd
import numpy as np

# ==================== 1. PAGE CONFIGURATION ====================
st.set_page_config(
    page_title="لبيتك",
    page_icon="🏠✨",
    layout="centered"
)

# ==================== 2. CUSTOM THEME / CSS ====================
# تم تحويل الألوان إلى درجات البيج والأوف وايت الدافئة مع خطوط بني دافئ
st.markdown("""
<style>
    /* خلفية التطبيق بيج فاتح دافئ ومريح للعين */
    .stApp {
        background-color: #FDFBF7;
    }
    
    /* لون العنوان الرئيسي (بني دافئ فاخر) */
    .app-title {
        color: #3E2723; 
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0px;
    }
    
    /* لون العنوان الفرعي (بيج غامق ترابي) */
    .app-subtitle {
        color: #795548;
        font-size: 18px;
        text-align: center;
        margin-bottom: 25px;
    }
</style>
""", unsafe_allow_html=True)

# ==================== 3. APP HEADER ====================
st.markdown('<p class="app-title">لبيتك 🏠✨</p>', unsafe_allow_html=True)
st.markdown('<p class="app-subtitle">من عالم التصميم لباب بيتك</p>', unsafe_allow_html=True)

st.write("---")

# ==================== 4. SIDEBAR SETUP ====================
st.sidebar.header("🎨 إعدادات استشارة التصميم")
team_name = st.sidebar.text_input("اسم استوديو التصميم / المصمم", "استوديو حولك")
st.sidebar.write(f"تم التطوير بواسطة: **{team_name}**")

# ==================== 5. INPUT SECTION (3 INPUTS) ====================
st.header("📥 تفاصيل المشروع والمساحة")

col1, col2 = st.columns(2)

# INPUT 1: Slider (مساحة الغرفة بالمتر المربع)
with col1:
    room_area = st.slider(
        "📐 مساحة الغرفة (بالمتر المربع)", 
        min_value=10, 
        max_value=150, 
        value=35,
        step=5
    )

# INPUT 2: Selectbox / Dropdown (نمط التصميم الداخلي)
with col2:
    design_style = st.selectbox(
        "🎭 نمط التصميم المطلوب",
        options=[
            "مودرن حديث (Modern Minimalist)", 
            "كلاسيك فاخر (Classic / Neoclassic)", 
            "بوهيمي طبيعي (Boho / Japandi)",
            "صناعي (Industrial)"
        ]
    )

# INPUT 3: Text Input / Query (ملاحظات العميل)
client_notes = st.text_input(
    "📝 متطلبات خاصة أو متطلبات الإضاءة والألوان", 
    placeholder="مثال: أركز على درجات البيج والرمال مع إضاءة دافئة ومساحة مكتبية..."
)

st.write("---")

# ==================== 6. ACTION & OUTPUT SECTION ====================
st.header("📊 تحليل وتكلفة التصميم المتوقعة")

# Action Button to generate result
if st.button("✨ إنتاج التقرير المبدئي للتصميم"):
    
    # تحديد اسم النمط المختار بشكل أصفى
    selected_style = design_style.split(" (")[0]
    
    st.subheader(f"نتيجة التحليل لـ: '{client_notes if client_notes else 'مشروع تصميم جديد'}'")
    
    # حسابات تقريبية مخصصة للديكور (سعر المتر التقريبي x المساحة)
    estimated_cost = room_area * 450  # متوسط التكلفة 450 ريال/متر
    
    # Dynamic Alert box based on room area
    if room_area >= 80:
        st.success(f"🏰 **مساحة واسعة جداً!** نمط ({selected_style}) سيعطي فخامة عالية مع توزيع مريح للأثاث والإضاءة.")
        st.balloons() # احتفال للمساحات الكبيرة!
    elif room_area >= 30:
        st.info(f"🏡 **مساحة متوازنة ومثالية!** خيار ممتاز لنمط ({selected_style}) يسهل فيه دمج الألوان والخامات.")
    else:
        st.warning(f"📐 **مساحة ملمومة!** يُنصح باستخدام ألوان فاتحة مثل (Nude/Cream) والمرايا لزيادة الشعور بالاتساع.")

    # Output Metric Display
    m1, m2 = st.columns(2)
    m1.metric(label="التكلفة التقديرية للتنفيذ", value=f"{estimated_cost:,} ر.س", delta="تقريبي")
    m2.metric(label="النمط المعتمد", value=selected_style)

    # Dynamic Data Chart Output (توزيع الميزانية المقترحة على عناصر الديكور)
    st.subheader("📈 توزيع الميزانية التقديري (Budget Breakdown)")
    
    # جدول توزيع الميزانية بناءً على مساحة الغرفة
    budget_breakdown = pd.DataFrame({
        "الأثاث والديكور": np.random.normal(loc=room_area * 200, scale=100, size=10),
        "الإضاءة والدهانات": np.random.normal(loc=room_area * 120, scale=50, size=10),
        "أجور التركيب والعمالة": np.random.normal(loc=room_area * 130, scale=40, size=10)
    })
    
    st.line_chart(budget_breakdown)

else:
    st.info("👆 قم بتعديل المدخلات في الأعلى ثم اضغط على **إنتاج التقرير المبدئي للتصميم** لعرض التحليل!")
